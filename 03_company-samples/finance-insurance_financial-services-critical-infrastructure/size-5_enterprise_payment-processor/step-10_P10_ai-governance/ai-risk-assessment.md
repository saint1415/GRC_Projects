# AI Governance Risk Assessment: Enterprise AI Portfolio and the Transaction Fraud-Detection Model

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded merchant payment processor) and Cris Santos Payouts, LLC |
| Tier / Vertical | Enterprise / Financial Services |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the transaction fraud-detection model, in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1); repository risk tier rubric |
| Assessor / date | AI and model risk committee (chaired by the Chief Risk Officer), meeting of 2026-08-19; GRC team and Model Risk Management prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-08 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 4, Medium 7, Low 1 |
| Status | In production 10, Pilot 2 |
| Build, buy, or configure | Build 4, Buy 2, Configure 6 |
| Committee review complete | 7 of 12 |
| Not yet reviewed | 5: AI-003, AI-006, AI-008, AI-010, AI-012 (all due 2026-11-30, POAM-022) |
| High-tier models with independent validation | 2 of 4 (AI-001, AI-011); AI-002 and AI-012 rely on vendor evidence only |
| Use cases that touch decisions about merchants who may be individuals (sole proprietors) | 5 (AI-001, AI-002, AI-010, AI-011, AI-012) |

**Main findings:** 5 use cases are running or piloting without committee review; 3 of them arrived as features switched on inside existing vendor products (AI-006, AI-008, AI-012). Two High-tier vendor models that decide who becomes a merchant (AI-002 underwriting score, AI-012 face match) have no independent validation or fairness testing on the company's applicants. The fraud model (AI-001) passed validation and performance tests but declines legitimate prepaid card purchases far more often than other purchases (section 7.4). Contact center summarization (AI-006) sends call audio that can contain spoken card data to a vendor model.

## 2. GOVERN: AI and model risk committee operating model
**Charter.** The AI and model risk committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk and technology committee reviews quarterly.

**Members:** Chief Risk Officer (chair); Chief Data and Analytics Officer; CISO; Chief Compliance Officer; General Counsel's delegate; Head of Model Risk Management (second line, independent of model developers); Senior Vice President, Fraud and Risk Management; Senior Vice President, Merchant Services; President, Cris Santos Payouts, LLC; Chief Human Resources Officer (for workforce tools). Internal Audit observes.

**Three lines for models.** Model owners and developers (first line) build and monitor. Model Risk Management (second line) validates High-tier models before production and at least every 12 months, and after material changes. Internal Audit (third line) audits the model risk process.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Independent validation; fairness testing on the company's own data; impact assessment; human review design (or documented compensating controls where real-time decisions make it infeasible); notice to affected people; monitoring plan; counsel review of consequential-decision laws |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; security and data handling review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.6; STD-05.3). Since 2026-03 procurement and change management block new AI features without an inventory ID. The GRC team owns the inventory.

**Policies:** POL-04 4.7 (extracts to analytics and AI platforms must be tokenized and registered) and 4.8 (no Restricted data in AI tools; Confidential data only in approved tools with no-training terms; minimized training data); POL-05 4.6 (approved tools only); POL-01 4.8 (service provider due diligence for AI vendors).

**Cadence:** monthly committee meetings; monthly monitoring dashboards for every High-tier model; annual re-review of every use case.

**Why 5 use cases lack review.** AI-006, AI-008, and AI-012 arrived through vendor feature releases before the intake block reached those products. AI-003 and AI-010 are pilots that started in business units after the block, using existing analytics tooling; the pilots are in shadow mode or limited regions. The committee set review dates for all five (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5 (15 U.S.C. 45) | Yes | Claims made to merchants and partners about AI (accuracy, fraud catch rates) must be supported, and practices that cause substantial injury consumers cannot reasonably avoid can be unfair (15 U.S.C. 45(n)); unjustified decline rates for some cardholder groups are the risk here |
| FTC Safeguards Rule, 16 CFR 314.4(c)(1) and (f) | Yes | Customer information used to train or run models must be access-controlled; AI vendors that receive it are service providers that need contract safeguards and periodic assessment |
| PCI DSS v4.0.1 (3.2.1, 3.3.1, 12.8, 6.2) | Yes | Training and inference data must not contain PAN outside the CDE; vendors that receive card data (AI-006 call audio) are third-party service providers; AI-assisted code still needs review |
| 23 NYCRR Part 500 and the NYDFS AI industry letter (2024-10-16) | Yes, for the payouts subsidiary (AI-001, AI-011) | The letter does not add requirements; it explains how Covered Entities should use Part 500 to assess and address AI-related cybersecurity risks. It describes four risks: AI-enabled social engineering, AI-enhanced cybersecurity attacks, exposure or theft of large amounts of nonpublic information used by AI, and increased vulnerabilities from third-party, vendor, and supply chain dependencies. The subsidiary's risk assessment (500.9), vendor policy (500.11), access controls (500.7), and training (500.14(a)(3)) now address these |
| Colorado SB26-189 (effective 2027-01-01) | **To be assessed by counsel by 2026-12-15** | It covers automated decision-making technology in consequential decisions in covered domains, including financial or lending services, for deployers doing business in Colorado, and decisions about differentiated price. Merchants that are sole proprietors may be "consumers" under it. Whether merchant underwriting (AI-002, AI-012), payout eligibility (AI-011), pricing (AI-010), or fraud declines (AI-001) are covered is not settled. The company will not assume an exemption (POAM-022) |
| Federal credit laws for merchant account decisions | **Under counsel review** | Whether merchant account approvals and reserves are credit decisions under federal law is not assumed either way; counsel's opinion is part of POAM-022 |
| State biometric privacy laws | Yes, for AI-012 | Laws differ by state; the company applies notice and written consent before any face match, in every state. Florida worked example: biometric data is personal information for breach notice purposes (Fla. Stat. 501.171(1)(g)) |
| State call recording consent laws | Yes, for AI-006 | The company applies all-party consent in its recorded-line notice. Florida worked example: interception is lawful when all parties have given prior consent (Fla. Stat. 934.03(2)(d)) |
| Card network rules | Indirectly | Fraud and dispute performance thresholds for merchants depend on AI-001 and AI-004 |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person (including credit), or able to affect critical infrastructure operations.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | Transaction fraud-detection model (every authorization) | High | In production | Reviewed 2025-11-12; re-reviewed 2026-08-19 |
| AI-002 | Merchant underwriting risk score (vendor) | High | In production | Reviewed 2026-04-22 with conditions |
| AI-003 | Transaction laundering and merchant monitoring model | Medium | Pilot (shadow mode) | Not reviewed (due 2026-11-30) |
| AI-004 | Dispute representment drafting assistant | Medium | In production | Reviewed 2026-02-18 |
| AI-005 | Merchant support chatbot | Medium | In production | Reviewed 2026-01-21 |
| AI-006 | Contact center call summarization and agent assist | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-007 | Engineering code assistant | Medium | In production | Reviewed 2026-03-11 |
| AI-008 | Cyber Fusion Center alert triage assistant | Low | In production | Not reviewed (due 2026-11-30) |
| AI-009 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-01-14 |
| AI-010 | Merchant pricing recommendation model | Medium | Pilot (two sales regions) | Not reviewed (due 2026-11-30) |
| AI-011 | Instant payout eligibility and fraud model (payouts subsidiary) | High | In production | Reviewed 2026-06-10 |
| AI-012 | Identity document and selfie match at merchant onboarding | High | In production | Not reviewed (due 2026-11-30) |

**Tiering notes:** AI-001 is High because it runs inline on critical payment infrastructure and declines purchases automatically. AI-002 and AI-012 are High because they are substantial factors in whether a person (a sole proprietor) gets a merchant account. AI-011 is High because it decides access to instant payouts for a licensed money transmission service. AI-010 stays Medium because a person sets every price; automatic pricing would re-tier it to High. AI-006 is Medium, not Low, because it processes call audio that can contain card data.

## 5. Portfolio risks and links to the enterprise register
| Risk | Use cases | P01 risk | Treatment |
|---|---|---|---|
| Unfair or inaccurate decisions about merchants and cardholders | AI-001, AI-002, AI-011, AI-012 | R-019, R-020 | Segment testing and validation (section 7; POAM-022) |
| Card data sent to AI vendors or analytics stores | AI-001 training data, AI-006 | R-016, R-021 | Tokenized extracts; ingestion blocking (POAM-014); AI-006 review before any expansion |
| AI-enabled social engineering against staff and merchants (deepfake voice on funding account changes) | Threat, not a use case | R-041, R-049 | Funding account and payout changes only through verified portal workflows (POL-05 4.8); vishing simulations |
| Ungoverned vendor AI features | AI-006, AI-008, AI-012 | R-056 | Intake block in procurement and change management; reviews due 2026-11-30 |
| Model drift or pipeline errors | AI-001, AI-011 | R-019 | Daily drift monitoring; fallback rules |

## 6. MEASURE: fairness testing approach for High-tier models
**The constraint.** The company does not collect cardholders' protected characteristics and must not start collecting them for this purpose. Merchant owners' age is known from identity verification, but race and ethnicity are not. Unfairness can still enter through features that act as proxies.

**The approach.** Compare error rates, not just approval rates, across segments built from data the company legitimately holds:
- **Cardholder side (AI-001):** card type (prepaid, debit, credit), issuer country, and billing ZIP code grouped by census median income quintile (an outside public data set joined at the ZIP level, never at the person level).
- **Merchant side (AI-002, AI-011, AI-012):** business type (sole proprietor or entity), business age, owner age band, and ZIP income quintile.
- **Metric and threshold:** false positive rate (legitimate purchases declined or challenged; good applicants declined or sent to manual review) for each segment, compared with the overall rate. A ratio above **1.5** needs a documented business justification tied to measured fraud or loss rates, or a mitigation.
- **Who reviews:** Model Risk Management runs the tests; the committee decides on mitigation; the Chief Compliance Officer keeps the record for counsel's consequential-decision review.

## 7. Full assessment: AI-001 transaction fraud-detection model
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Score every authorization from 0 to 999. The authorization switch applies the merchant's rules and score bands to approve, step up (3-D Secure challenge for card-not-present), send to review, or decline. Also scores instant payout requests for the payouts subsidiary |
| Users / operators | Authorization switch (automated); fraud strategy analysts (thresholds, review queue); merchants (rules and allow-lists in the portal) |
| Affected people | Cardholders paying about 410,000 merchants (about 37.8 million authorizations a day); merchants whose sales are declined |
| Data | Inference: tokens (never PAN), amount, time, merchant category, BIN country, card type, billing ZIP code, device and IP signals, consortium fraud signals. Training: tokenized, labeled transactions (fraud and chargeback outcomes) in the analytics account, registered under PRC-04.1 |
| Build or buy | Built in house since 2024 by the data science team (Chief Data and Analytics Officer); retrained monthly; deployed through the model change process (P04 CM-4 row) |
| Not intended | Credit decisions, merchant pricing, or cardholder profiling for marketing. Any new use needs re-assessment |
| Fallback | Velocity and amount rules in the switch take over within 1 minute if the model is unavailable (P05 BP-10) |

### 7.2 Risk tier
**High** (section 4). The repository rubric's High-tier minimum controls and how they are met:
- **Human review before action:** not feasible for real-time authorization. Compensating controls: the review band routes uncertain scores to analysts; merchants can override with allow-lists; declined consumers can retry or pay another way; daily monitoring catches drift within hours.
- **Pre-deployment bias testing:** segment testing before each monthly release (section 7.4).
- **Impact assessment:** this document.
- **Notice to affected people:** through merchants. The merchant integration guide states that automated fraud screening is used and how merchants can explain declines.
- **Ongoing monitoring:** daily (section 7.5).

### 7.3 Independent validation
Model Risk Management validated the model in 2025-11 (conceptual soundness, data quality, outcome analysis, and implementation). Two findings, both closed: missing documentation of a feature transformation, and no benchmark against the fallback rules. Next full validation: 2026-11.

### 7.4 MEASURE (Q2 2026 data: about 3.4 billion scored authorizations; fraud labels matured through July 2026)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Fraud value detected at least 75%; false positive rate (legitimate transactions declined or challenged) at most 1.0% | Detection 81%; false positive rate 0.8% | Yes |
| Valid and reliable (drift) | Weekly population stability index under 0.2; decline rate within 20% of the 13-week average | Highest index 0.14; one decline spike (2026-05-12, after a feature pipeline change) caught by monitoring in 2 hours and rolled back | Yes |
| Safe | Fallback rules take over within 1 minute; tested quarterly | Last test 2026-07-08: 38 seconds | Yes |
| Secure and resilient | Signed model artifacts; serving in the analytics account with access through PAM; monitoring for adversarial probing (fraudsters testing thresholds) | In place; probing alerts tuned 2026-06 | Yes |
| Accountable and transparent | Model documentation, validation report, and threshold change log approved by the model owner; merchant-facing disclosure | All in place | Yes |
| Explainable and interpretable | Top reason codes returned with each score; analysts and merchants see them | In place | Yes |
| Privacy-enhanced | Training and inference data tokenized; minimized; extracts registered | AI-001 data met the rule, but the 2026-07 PAN event in the same analytics account showed that upstream extracts can bypass it (POAM-014) | **Partial** |
| Fair, with harmful bias managed | Segment false positive ratio at most 1.5 (section 6) | Prepaid cards 2.6 (2.1% against 0.8% overall); issuer outside the U.S. 1.9 (justified by a cross-border fraud rate 3.4 times the domestic rate); lowest ZIP income quintile 1.3 | **No** (prepaid cards) |

**Prepaid card finding.** Prepaid cards are used more by consumers without bank accounts, so a high false positive rate on prepaid cards can fall on lower-income cardholders. The measured fraud rate on prepaid cards is 1.4 times the overall rate, which does not justify a false positive ratio of 2.6. The main driver is a feature that treats first use of a card at a merchant as risky, which is normal for reloadable prepaid cards.

### 7.5 MANAGE
- **Prepaid mitigation:** retrain with a prepaid-specific treatment of first-use features and recalibrate the step-up band, so more prepaid transactions are challenged instead of declined; target ratio under 1.5 by 2026-11-30, confirmed in the next validation.
- **Monitoring:** daily drift and decline-rate alerts; segment false positive rates on the monthly committee dashboard; quarterly fallback test.
- **Change control:** every retrain goes through shadow scoring, Model Risk Management sign-off, and staged rollout; emergency threshold changes need the model owner and the fraud strategy lead.
- **Incidents:** a model-driven decline spike is a severity-2 incident handled under P08 with the fraud team; a data handling failure follows PRC-04.2.
- **Payouts use:** AI-001 scores feed AI-011. The payouts subsidiary's President receives the monthly dashboard so its Part 500 risk assessment reflects model risk.
- **Decommissioning:** if the model fails validation or misses thresholds for two consecutive months, the fallback rules and the previous champion model take over while it is fixed.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier model has monthly performance and fairness metrics (inventory column `monitoring`); a threshold breach triggers committee re-review.
- **Vendor AI:** AI vendors are tier-1 in the third-party program; contracts require notice of material model changes, no training on company data, deletion on exit, and an AOC where card data is involved.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse) are logged in case management and follow P08 where security or card data is involved.
- **Decommissioning:** tools are retired if they fail monitoring twice, change data-use terms, or cannot pass validation; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the AI and model risk committee's recommendation of 2026-08-19:
1. **AI-001:** approved to continue with conditions: prepaid card mitigation by 2026-11-30; validation in 2026-11 to confirm the segment ratio; upstream PAN blocking (POAM-014).
2. **AI-002:** may continue in current scope with human review of every decline; independent validation and fairness testing by 2027-03-31; counsel opinion on Colorado SB26-189 and federal credit law by 2026-12-15 (POAM-022).
3. **AI-012:** face match results may not cause an automatic decline; review, consent wording check, and segment accuracy testing by 2026-11-30.
4. **AI-006:** no expansion beyond current teams until review; call audio sent to the vendor only with pause-and-resume enforced (POAM-014); review by 2026-11-30.
5. **AI-003, AI-008, AI-010:** may continue in current scope (shadow mode, triage support, two-region pilot) until committee review by 2026-11-30; AI-010 may not set prices automatically.
6. **AI-011:** approved; segment testing continues monthly.
7. **Inventory:** procurement and change management block any new AI feature without an inventory ID, including features delivered in vendor updates.

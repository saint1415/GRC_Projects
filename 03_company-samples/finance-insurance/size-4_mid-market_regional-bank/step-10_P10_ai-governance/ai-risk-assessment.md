# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (regional commercial bank), subsidiary of Cris Santos Company, Inc. |
| Tier / Vertical | Mid-Market / Finance and Insurance |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`; AI-001 assessed in full |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook, with the Generative AI Profile (NIST AI 600-1) for AI-004 and AI-005 |
| Assessors / date | Model Risk Manager (lead), Chief Credit Officer and Fair Lending Officer (AI-001), BSA/AML Officer (AI-002), ISO (security), Chief Compliance Officer (consumer compliance), 2026-08-24 to 2026-09-04 |
| Decision | Chief Risk Officer and Chief Operating Officer, 2026-09-18; the High-tier decision on AI-001 approved by the President and CEO, reviewed by the Board Risk Committee on 2026-09-15 |

## 1. Summary
The bank has a model risk management policy (2023) and a model inventory, so AI did not arrive ungoverned. The gap is that the policy was written for traditional models (asset-liability, credit loss, BSA rules) and was not applied with the same depth to AI (gap 9):
- **AI-001, the small business credit model,** had a conceptual review before production but no outcomes validation on the bank's own applicants, fair lending testing used only the vendor's national data, and 9 of 40 sampled adverse action notices gave a reason that Regulation B treats as insufficient.
- **AI-004 and AI-005** (a generative assistant pilot and a customer chatbot) started without model risk or compliance review.
- **AI-002 and AI-003** are vendor-embedded models that are validated annually but whose suppressed or held outcomes are not sampled often enough.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Small business credit underwriting model | **High** | Continue with conditions; version changes frozen until validation |
| AI-002 | AML alert scoring | Medium | Continue; quarterly below-threshold sampling |
| AI-003 | Online banking fraud scoring (provider) | Medium | Continue; obtain provider documentation |
| AI-004 | Enterprise generative AI assistant (pilot) | Low | Continue pilot with conditions |
| AI-005 | Customer service chatbot | Medium | Conditional: controls by 2026-11-30, or switch off |

Tiers: 1 High, 3 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Model Risk Manager (second line, under the CRO), who keeps the model and AI inventory. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.13: models and AI that make or support decisions about customers must be inventoried, validated on the bank's data, and fair lending tested before production, and monitored in use.
  - POL-01 4.9: vendor due diligence and contract terms apply to AI vendors.
  - POL-04 4.9 and POL-05 4.10: customer information only in approved AI tools; staff check every output.
  - STD-05 AI and model use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Model Risk Manager with the ISO. Today it lists AI-001 to AI-005 with their conditions. Public generative AI sites will be blocked from bank devices by 2026-12-31 (P01 R-021).

### 2.1 AI governance process sized for a mid-market bank
A $2.5 billion bank does not need a separate AI committee. It needs a reliable gate and a regular rhythm, using the model risk function and the existing Management Risk Committee.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any unit wanting an AI tool, or an AI feature turned on in an existing tool, submits a one-page intake: purpose, users, data, vendor, decisions affected | Business owner | 15 minutes |
| 2. Triage | Provisional tier with the P10 rubric; purchasing gate (no contract or purchase order without approval, POL-01 4.9) | Model Risk Manager | 2 business days |
| 3. Review | **Low:** security and data checklist. **Medium:** security, privacy, consumer compliance, and output quality review. **High:** full MAP and MEASURE assessment like section 4, including validation on bank data and a fair lending plan | Model Risk Manager; ISO; Chief Compliance Officer; Fair Lending Officer | Low 1 week; Medium 3 weeks; High 8 weeks |
| 4. Decide | Low: Model Risk Manager. Medium: Management Risk Committee (monthly). High: the committee recommends; the CEO decides with the CRO's concurrence and informs the Board Risk Committee | As listed | Monthly |
| 5. Monitor | Owner reports agreed metrics monthly (Medium) or monthly with a quarterly deep dive (High); incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model version, new data source, new population or product, or a fairness flag | Model Risk Manager | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`.

## 3. MAP (portfolio)
| Item | AI-001 Credit model | AI-002 AML scoring | AI-003 Fraud scoring | AI-004 Assistant | AI-005 Chatbot |
|---|---|---|---|---|---|
| Purpose | Recommend approve or decline and give reasons for small business credit up to $500,000 | Rank alerts; suppress low scores | Flag risky sign-ins and transfers for step-up or hold | Draft and summarize internal documents | Answer product and fee questions; route to agents |
| Users | About 60 loan officers and credit staff | 14 BSA analysts | Treasury operations | 25 pilot users | Website and app visitors |
| Affected people | Small business applicants and their owners and guarantors (548 scored applications, 2025-10-01 to 2026-08-14) | Customers whose activity is monitored | Online banking users | None directly | Customers and prospects |
| Data | Cash flow, bureau data, owners' credit scores, industry, ZIP code | Transactions; due diligence data | Device and behavior data | Internal documents | Free-text messages |
| Build or buy | Buy (vendor model, bank-deployed) | Buy (embedded) | Buy (embedded) | Buy (SaaS) | Buy (SaaS) |
| Generative AI? | No | No | No | Yes | Yes |
| Key laws | Regulation B; GLBA and the Guidelines | 12 CFR 21.11; 31 CFR 1020.320 | 12 CFR 41.90; Regulation E error resolution | GLBA and the Guidelines | Regulation E error resolution; unfair or deceptive practices law |

**Laws considered and not applicable, or not analyzed:**
- **State AI laws such as Colorado SB26-189:** the bank lends only to businesses in Florida and Georgia and does not do business in Colorado, so it is out of scope. No Florida or Georgia statute specific to AI in credit decisions was identified in the repository's cross-sector file; state AI law was not researched beyond it.
- **NYDFS and NAIC AI guidance** in the vertical overlay apply to insurers and New York-licensed entities, not to this bank.
- **CFPB Circulars 2022-03 and 2023-03** (adverse action and complex algorithms) were withdrawn on 2025-05-12 (90 FR 20084), per the vertical research. The Regulation B duty in 1002.9 is unchanged.
- **Regulation B subpart B** (small business lending data collection): not applicable at the bank's volume (P03).
- **FCRA adverse action duties** where a guarantor's consumer report contributes to a decline were not analyzed in this assessment; the Chief Compliance Officer reviews them separately.
- **Model risk management guidance:** the current status of the banking agencies' model risk management guidance for a bank of this size was not verified. The bank applies validation, conceptual soundness review, and outcomes analysis as a policy choice (POL-01 4.13).

## 4. AI-001 in detail: small business credit underwriting model

### 4.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Score small business applications up to $500,000, recommend approve or decline, and give the top 4 reasons. The goal is faster, more consistent decisions |
| Human role | The loan officer decides. From 2025-10-01 to 2026-08-14 officers followed the recommendation on 88% of decided applications, so the model is a **substantial factor** in the decision |
| Volume | 548 scored applications: 348 approved, 158 declined, 42 withdrawn or incomplete |
| Not intended | Automatic decisions, pricing, loans above $500,000, consumer or mortgage credit. Any of these requires re-assessment |

**Regulation B (fair lending lens):**
| Rule | Applies? | What it means for AI-001 |
|---|---|---|
| 12 CFR 1002.9(a) (notice timing) | **Yes** | A decline is adverse action. For businesses with gross revenues of $1 million or less, the consumer notice rules apply with the modifications in 1002.9(a)(3)(i); above $1 million, notice within a reasonable time and written reasons on request (1002.9(a)(3)(ii)). P03 found notices timely (40 of 40 sampled) |
| 12 CFR 1002.9(b)(2) (specific reasons) | **Yes** | Reasons must be specific and give the principal reasons. A statement that the applicant failed to achieve a qualifying score on the creditor's scoring system is **insufficient**. **9 of 40 sampled notices used "score below model threshold"** (P03 G-057; P01 R-017) |
| 12 CFR 1002.4(a); 1002.6(b)(1) (discrimination) | **Yes** | No discrimination on a prohibited basis in any aspect of the transaction, and no prohibited basis in any system of evaluating creditworthiness. An input that works as a close proxy for race or national origin raises this risk |
| 12 CFR 1002.6(a) (effects test) | **Yes, changes the test** | The rule states that the Act does not provide for the "effects test". Outcome disparities are therefore not by themselves a Regulation B violation. The bank still measures them, as a warning sign that an input may be acting as a proxy for a prohibited basis |
| 12 CFR 1002.5(b) (collecting race, sex, national origin) | **Yes, limits testing data** | A creditor may not inquire about these characteristics for business credit except as the rule allows, including for a self-test that meets 1002.15. The bank therefore uses proxy methods (below), not applicant-provided data |
| 12 CFR 1002.6(b)(2) (age) | **Yes** | The model does not use age. If a future version does, it may do so only in an empirically derived, demonstrably and statistically sound system in which an elderly applicant's age is not assigned a negative value |

### 4.2 Risk tier
**Tier: High.** The model is a substantial factor in a consequential decision about credit, and its reason codes flow into adverse action notices. **Minimum controls for High:** human review before action, pre-deployment bias testing, an impact assessment (this document), notice to affected people (the adverse action notice), and ongoing monitoring. Bias testing on bank data and outcomes validation were not done before production; the conditions in section 6 close that gap.

### 4.3 MEASURE
| Trustworthy characteristic | Test / metric | Result (2025-10-01 to 2026-08-14) | Pass? |
|---|---|---|---|
| Valid and reliable | Outcomes validation on bank applicants; early delinquency back-test; agreement with experienced underwriters | Conceptual review only (2025). Underwriter agreement 88%. Too early for default back-testing; 4 of 348 approved loans are 30 or more days past due | **No** (validation missing) |
| Safe | Loans up to $500,000 only; officer decides; no automatic decline | Limits held on all 548 applications | Yes |
| Secure and resilient | Version pinned and hashed; scoring log; private network access only (P04) | In place; configuration baseline for the container pending (STD-01) | Partial |
| Accountable and transparent | Named owner; inventory; override tracking | In place since 2025-10; override reasons recorded in 61% of overrides | Partial |
| Explainable and interpretable | Reason codes specific enough for 1002.9(b)(2); reasons match the model's actual drivers | 9 of 40 sampled notices insufficient | **No** |
| Privacy-enhanced | Contract bars secondary use of bank data; data minimization | Contract allows the vendor to use "de-identified performance data" to improve its models | **No** |
| Fair, with harmful bias managed | Approval-rate ratio by census-tract minority share; proxy review of inputs | Majority-minority tracts: 54 of 96 decided applications approved (56%). Other tracts: 294 of 410 (72%). Ratio 0.78, below the 0.80 flag. ZIP code and industry appear among the top 4 reasons in 31 of 42 declines in majority-minority tracts | **No.** Flag raised |

**Bias finding.** The ratio is below the flag and the reason-code pattern points to the ZIP code input (and possibly industry codes concentrated in certain neighborhoods) as a possible proxy for the racial or ethnic makeup of neighborhoods. A disparity alone is not a Regulation B violation (1002.6(a)), but a proxy for a prohibited basis in the evaluation system would be (1002.6(b)(1)). The bank will neutralize the ZIP code input and test the model without it on historical data before the next version.

### 4.4 Bias and fairness testing plan
| Item | Plan |
|---|---|
| Data | (1) Before the next version: about 1,900 small business applications from 2023 to 2026, scored retroactively with and without the ZIP code input. (2) Ongoing: all scored applications, every quarter |
| Groups compared | Race and ethnicity of principal owners, estimated with a surname and geography proxy method (1002.5(b) limits direct collection); sex of principal owners, estimated by first-name proxy; census tract minority share (majority-minority versus other tracts); Florida versus Georgia branches |
| Metrics and thresholds | Approval-rate ratio between each group and its comparison group: flag below 0.80. Difference in average score after controlling for credit factors: flag if statistically significant at the 5% level. Frequency of each reason code by group: flag if one code is twice as frequent in a group. Override rates by group: flag a difference of more than 10 percentage points |
| Proxy review | For every flag, test whether each input (ZIP code, industry, cash-flow measures) predicts group membership; remove or replace inputs that act as close proxies and are not needed for accuracy |
| Less discriminatory alternative | Compare model versions with and without flagged inputs; prefer the version with smaller disparities where accuracy is comparable; the Chief Credit Officer documents the trade-off |
| Who and when | Independent validator (funded, $85,000; P01) with the Fair Lending Officer, due 2026-12-31; quarterly monitoring by the Fair Lending Officer after that; results to the Board Risk Committee |

### 4.5 MANAGE
- **Human in the loop:** the model recommends; the loan officer decides and records their own analysis of cash flow and collateral before the decision is final. From 2026-10-01, a second credit officer reviews every model-recommended decline before the notice goes out. The model cannot decline an application automatically. Override reasons are required for every override.
- **Adverse action notices:** the Chief Compliance Officer maps each reason code to specific, plain-language principal reasons; threshold codes are removed from the template by 2026-10-15; the 9 applicants in the sample, and any others found in a full review of the 158 declines, get a corrected statement of specific reasons by 2026-10-31 (POAM-017).
- **Monitoring:** quarterly fairness testing; monthly drift check of score distribution and approval rate against the validation baseline (flag a change of more than 10 percentage points); early delinquency tracking.
- **Change control:** model version changes need Model Risk Manager approval and re-testing before release (P04 SI-7). Versions are frozen until validation is complete.
- **Vendor terms (POL-01 4.9):** amend the contract by 2026-12-31 to bar secondary use of bank data, give the bank model documentation and validation data, and require notice of model changes before release.
- **Incidents:** a security incident in the credit decisioning service follows POL-03 and P08; a fair lending issue goes to the Fair Lending Officer and General Counsel.
- **Decommissioning:** stop scoring and return to manual underwriting if validation fails, if a fairness flag cannot be explained or fixed within one quarter, or if the vendor will not accept the contract terms.

## 5. Other use cases (MEASURE and MANAGE, in brief)
| ID | Key findings | Conditions | Re-tier triggers |
|---|---|---|---|
| AI-002 AML alert scoring | Validated annually by the vendor; the bank samples suppressed alerts only once a year. A missed SAR is a regulatory failure (12 CFR 21.11) | Quarterly sample of 50 suppressed alerts from 2026 Q4; obtain the vendor's validation summary (P09 VEN-08); BSA Officer approves threshold changes (P01 R-022) | Any threshold change; automatic closure of alerts; use for account closure decisions |
| AI-003 Fraud scoring | Provider model; holds reviewed by staff the same day; no documentation of inputs or performance received | Obtain model documentation and false-positive rates from the provider (P09 VEN-02); include in the Red Flags program update (POAM-018) | Automatic account closure; use in account opening decisions |
| AI-004 Generative assistant (AI 600-1) | Enterprise contract with a no-training and retention clause; pilot started without review; no customer data observed in a sample of 50 prompts | No customer, SAR, or respondent data; output check by staff; usage logging reviewed monthly; public tools blocked by 2026-12-31 (P01 R-021) | Connection to customer systems; use for customer communications |
| AI-005 Customer chatbot (AI 600-1) | Launched without compliance review. In 60 sampled transcripts: 3 answers misstated an overdraft fee; 2 customers typed full account numbers; 1 dispute question was answered without offering an agent | Compliance review of the knowledge base; block and mask account numbers and other NPI; automatic hand-off for disputes, fraud, and complaints; AI disclosure at the start of each chat; monthly transcript sampling. Due 2026-11-30 or switch off (P01 R-020) | Any account access or transaction capability |

## 6. Decisions
**AI-001: continue with conditions.** President and CEO, 2026-09-18, with the CRO's concurrence, after the Board Risk Committee review on 2026-09-15. Conditions:
1. ZIP code input neutralized by the vendor by 2026-10-31, and the model run on that version.
2. Second-officer review of every model-recommended decline from 2026-10-01.
3. Reason codes mapped to specific reasons and corrected statements sent by 2026-10-31.
4. Outcomes validation and fairness testing on bank data complete by 2026-12-31, with no unexplained flag; amended vendor contract by 2026-12-31.

Expansion to larger loans or other products requires all four, plus the Board Risk Committee's review.

**AI-002 and AI-003: continue** with the monitoring conditions in section 5. **AI-004: continue the pilot** under the Low-tier conditions. **AI-005: continue only if** the conditions are met by 2026-11-30; otherwise the Contact Center Director switches it off.

The residual risks are tracked in P01 (R-017 to R-022) and the actions in P07 (POAM-017 and POAM-020).

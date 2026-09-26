# AI Risk Assessment: Small Business Credit Underwriting Model

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (community commercial bank) |
| Tier / Vertical | Small / Finance and Insurance |
| AI use case | AI-001: small business credit underwriting model (SYS-10), pilot at 3 branches since May 2026 for applications under $250,000 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook |
| Assessor / date | Chief Credit Officer and Compliance Officer, with the Information Security Officer, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases; AI-001 assessed here in full) |

## 1. GOVERN
- **Accountable owner:** Chief Credit Officer. **Fair lending review:** Compliance Officer. **Security of the deployment:** Information Security Officer. **Decision authority:** President and CEO (High tier), with the Audit and Risk Committee informed. Expansion beyond the pilot needs the Audit and Risk Committee's review.
- **Policies that apply:**
  - POL-01 4.12: models that make or support credit decisions must be inventoried, independently validated, and fair lending tested before production use. **The pilot started before this policy existed and before either step was done** (gap 11 in the scenario facts).
  - POL-01 4.8: service provider due diligence and contract terms apply to the model vendor.
  - POL-04 4.8 and POL-05 4.10: customer information only in approved tools.
- **Inventory:** the Chief Financial Officer keeps the model inventory. AI-001 was added on 2026-08-25, with AI-002 and AI-003.
- **Scale for a Small bank:** there is no AI committee. The Chief Credit Officer, Compliance Officer, ISO, and CFO review AI use cases quarterly and report to the Audit and Risk Committee.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Score small business applications under $250,000, recommend approve or decline, and give the top 4 reasons. The goal is faster, more consistent decisions on small loans |
| Users / operators | Loan officers at Branches 1, 2, and 5; the Chief Credit Officer |
| Affected people | Small business applicants and their owners and guarantors. Pilot: 62 scored applications from 2026-05-04 to 2026-08-14 (40 approved, 14 declined, 8 withdrawn or incomplete) |
| Data | Inputs: 12 months of the business's deposit account cash flow from the core, business credit bureau data, owners' personal credit scores, time in business, industry, loan amount and term, collateral, and a vendor "location risk index" built from ZIP-code delinquency rates. Outputs: a score, a recommendation, and 4 reason codes stored in the LOS |
| Build or buy | Buy: vendor-developed model, deployed by the bank in its cloud tenant (P04 credit decisioning service). Version pinned and hashed at each release |
| Human role | The loan officer decides. In the pilot, officers followed the model's recommendation on 57 of 62 applications (92%), so the model is a **substantial factor** in the decision |
| Not intended | Automatic decisions, pricing, loans of $250,000 or more, consumer or mortgage credit. Any of these requires re-assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| ECOA and Regulation B, 12 CFR 1002.9 (adverse action notices) | **Yes** | A decline is adverse action. The statement of reasons must be specific and give the principal reasons. Saying the applicant failed to reach a qualifying score on the creditor's scoring system is **insufficient** (1002.9(b)(2)). For a business with gross revenues of $1 million or less, the notice rules of 1002.9(a)(1) and (2) apply with the modifications in 1002.9(a)(3)(i); above $1 million, the bank must notify within a reasonable time and give written reasons if asked within 60 days (1002.9(a)(3)(ii)). 12 of the 14 pilot declines were businesses at or under $1 million |
| Regulation B, 12 CFR 1002.4(a) and 1002.6(b)(1) (discrimination) | **Yes** | The bank must not discriminate on a prohibited basis in any aspect of a credit transaction, and must not take a prohibited basis into account in any system of evaluating creditworthiness. A variable that works as a close proxy for race or national origin raises this risk |
| Regulation B amendment, 91 FR 21620 (effective 2026-07-21) | **Yes, changes the test** | 1002.6(a) now states that the Act does not provide for the "effects test". Outcome disparities are therefore not by themselves a Regulation B violation. The bank still measures them, as a warning sign that a model input may be acting as a proxy for a prohibited basis |
| CFPB Circulars 2022-03 and 2023-03 (adverse action and complex algorithms) | **No longer in effect** | The CFPB withdrew many guidance documents on 2025-05-12 (90 FR 20084); per the vertical research, these two circulars were among them. The 1002.9 duty itself is unchanged |
| Regulation B small business data collection (subpart B) | No | The bank originates far fewer covered credit transactions than the 12 CFR 1002.105(b) threshold (see `../scenario-facts.md`) |
| GLBA and the Interagency Guidelines (N52-R01, N52-R02) | **Yes** | The model processes customer information in the bank's cloud tenant, and the vendor is a service provider (III.D) |
| State AI laws (for example, Colorado SB26-189) | No | The bank lends only to Florida businesses. State AI laws outside Florida are out of scope by decision |
| Model risk management guidance | Program choice | The bank applies independent validation, conceptual soundness review, and outcomes analysis as a policy choice (POL-01 4.12). The current status of the agencies' model risk management guidance for community banks was not verified for this assessment |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal/projects/P10_ai-governance/README.md`).

**Why High:** the model is a substantial factor in a consequential decision about credit. Officers followed it 92% of the time, and its reason codes flow directly into adverse action notices.

**Minimum controls for High:** human review before action, pre-deployment bias testing, an impact assessment (this document), notice to affected people (the adverse action notice), and ongoing monitoring. Pre-deployment bias testing and independent validation were **not done** before the pilot. The conditions in section 6 close that gap.

## 4. MEASURE
| Trustworthy characteristic | Test / metric | Result (pilot, May to August 2026) | Pass? |
|---|---|---|---|
| Valid and reliable | Independent validation on the bank's own population; agreement with experienced underwriters | No validation on bank data. The vendor's model documentation reports performance only on a national development sample. Underwriter agreement 92%. Too early for default back-testing | **No** |
| Safe | Loans under $250,000 only; officer decides; no automatic decline | Limits held in all 62 applications | Yes |
| Secure and resilient | Version pinned and hashed; scoring log; private network access only; configuration baseline | Version control and logging in place (P04); no configuration baseline (R-022) | Partial |
| Accountable and transparent | Named owner; inventory entry; override tracking | Owner and inventory in place since 2026-08-25; overrides not tracked before August | Partial |
| Explainable and interpretable | Reason codes specific enough for 1002.9(b)(2); reasons match the model's actual drivers | 5 of 14 adverse action notices gave "score below model threshold" as a reason. That is insufficient under 1002.9(b)(2) | **No** |
| Privacy-enhanced | Contract bars the vendor from using bank data for other purposes; data minimization | Contract silent on secondary use; the vendor receives monthly scoring files for "model improvement" | **No** |
| Fair, with harmful bias managed | Approval-rate ratio by census-tract minority share (see plan below); proxy review of inputs | Majority-minority tracts: 7 of 12 decided applications approved (58%). Other tracts: 33 of 42 (79%). Ratio 0.74, below the 0.80 flag. The location risk index was among the top 4 reasons in 4 of the 5 declines in majority-minority tracts | **No.** Flag raised; sample is small |

**Bias finding.** The sample is too small for statistical conclusions, but the flag and the reason-code pattern point to the location risk index as a likely proxy for the racial or ethnic makeup of neighborhoods. The bank will suspend that input and test the model without it on historical data before any expansion.

### Bias and fairness testing plan
| Item | Plan |
|---|---|
| Data | (1) Pre-expansion: about 1,050 small business applications from 2023 to 2025, scored retroactively with and without the location risk index. (2) Ongoing: all scored applications, every quarter |
| Groups compared | Race and ethnicity of principal owners, estimated with a surname and geography proxy method (Regulation B generally bars asking for these for business credit, 1002.5); sex of principal owners, estimated by first-name proxy; census tract minority share (majority-minority versus other tracts); principal owner age 62 or older versus younger (from guarantor credit reports) |
| Metrics and thresholds | Approval-rate ratio between each group and its comparison group: flag below 0.80. Difference in average score after controlling for credit factors: flag if statistically significant at the 5% level. Frequency of each reason code by group: flag if one code is twice as frequent in a group. Override rates by group: flag a difference of more than 10 percentage points |
| Proxy review | For every flag, test whether each input (especially the location risk index, industry, and cash-flow measures) predicts group membership; remove or replace inputs that act as close proxies and are not needed for accuracy |
| Less discriminatory alternative | Compare model versions with and without flagged inputs; prefer the version with smaller disparities where accuracy is comparable (the Chief Credit Officer documents the trade-off) |
| Age | The model must not use owner age. If a future version does, it may do so only as 1002.6(b)(2)(ii) allows, and an elderly applicant's age must not be assigned a negative value |
| Who and when | Independent validator (outsourced, $30,000 funded, P01) before expansion, due 2026-11-30; Compliance Officer quarterly after that; results to the Audit and Risk Committee |

## 5. MANAGE
**Human-in-the-loop design:**
- The model recommends. The loan officer decides, and records their own analysis of cash flow and collateral in the LOS before the decision is final.
- From 2026-09-15, a second credit officer reviews every model-recommended decline before the notice goes out.
- Officers may override in either direction with a written reason. Overrides are tracked by group as part of the bias testing plan.
- The model cannot decline an application automatically.

**Adverse action notices:**
- The Compliance Officer maps each reason code to specific, plain-language principal reasons. "Score below threshold" and similar codes are removed from the notice template by 2026-10-15.
- The 5 applicants who received insufficient reasons are sent a corrected statement of specific reasons by 2026-10-15.

**Monitoring:**
- Quarterly fairness testing per the plan above, reported to the Audit and Risk Committee.
- Monthly drift check: score distribution and approval rate against the validation baseline. Flag a change of more than 10 percentage points in approval rate.
- Model version changes need Chief Credit Officer approval and re-testing before release (P04 SI-7 control).
- Risk register entries R-011 and R-012 (P01) track the residual risk.

**Vendor terms (POL-01 4.8):** amend the contract by 2026-11-30 to bar secondary use of bank data, give the bank access to model documentation and validation data, and require notice of model changes before release.

**Incident handling:** a security incident in the credit decisioning service follows the P08 escalation path and POL-03. A fair lending issue is escalated to the Compliance Officer and counsel.

**Decommissioning:** stop scoring and return to fully manual underwriting if the independent validation fails, if a fairness flag cannot be explained or fixed within one quarter, or if the vendor will not accept the contract terms.

## 6. Decision
**Approve continued pilot with conditions.** President and CEO, 2026-08-31, after review by the Audit and Risk Committee on 2026-08-27. The pilot may continue at the 3 branches **only if** these conditions are met by 2026-10-15:
1. The location risk index is suspended (set to a neutral value by the vendor) and the pilot runs on the version without it.
2. A second credit officer reviews every model-recommended decline.
3. Reason codes are mapped to specific reasons, and corrected statements are sent to the 5 affected applicants.
4. Override reasons are recorded for every application.

**Expansion** beyond the 3 branches, or to loans of $250,000 or more, requires: an independent validation on bank data, pre-expansion fairness testing with no unexplained flag, the amended vendor contract, and the Audit and Risk Committee's review. Target: 2026-11-30 (P01 R-011 and R-012).

**Related action for AI-002.** Ask the digital banking provider for documentation of its fraud scoring model and include it in the provider's SOC review by 2026-11-30 (P09).

# AI Risk Assessment: Transaction Fraud-Detection Model

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (payment processor serving merchants) |
| Tier / Vertical | Small / Financial Services |
| AI use cases | AI-001: transaction fraud-detection model (primary). AI-002: staff use of generative AI chatbots (secondary) |
| Framework | NIST AI RMF 1.0 (AI 100-1); NIST AI 600-1 Generative AI Profile for AI-002 |
| Assessor / date | Risk and Fraud Manager with the IT Manager and Compliance and Risk Manager, 2026-08-25 |
| Approved | COO, 2026-08-31 (conditions in section 6) |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner:** Risk and Fraud Manager for AI-001; IT Manager for AI-002.
- **Decision authority:** under POL-01 4.5, High-tier risks need the majority owner and CEO. The COO approves the conditions and reports them to the CEO. The CEO accepted R-020 and R-021 treatment plans on 2026-08-31 as part of P01.
- **Policies that apply:**
  - POL-04 4.8: training extracts must be token-only, minimized, and covered by use limits and deletion terms
  - POL-05 4.7: approved generative AI tools only; no Restricted or Confidential data in public chatbots
  - POL-01 4.8: service provider due diligence and annual review (the fraud analytics vendor)
- **Inventory and approved-tools list:** kept by the IT Manager. It did not exist before this assessment (gap 14 in `../scenario-facts.md`).
- **Scale for a Small processor:** there is no AI committee. The Risk and Fraud Manager, IT Manager, Compliance and Risk Manager, and CTO review AI use cases every quarter, timed with the vendor's quarterly model update.

## 2. MAP (AI-001)
| Item | Description |
|---|---|
| Purpose and intended use | Score each authorization for fraud risk, from 0 to 999. The authorization switch applies the merchant's rules and the score bands to approve, step up (3-D Secure challenge for card-not-present), send to review, or decline |
| Users / operators | Authorization switch (automated); 3 fraud analysts and the Risk and Fraud Manager (reviews, thresholds); merchants (allow-lists and their own rules in the portal) |
| Affected people | Consumers paying about 4,200 merchants (about 260,000 transactions a day); merchants whose sales are declined |
| Data | Inputs: tokens (never PAN), amount, time, merchant category, BIN country, card type, billing ZIP code, and device and IP signals for card-not-present. Training: a quarterly labeled extract (tokens, features, fraud and chargeback outcomes) sent to the vendor. **The extract also carries cardholder name and full billing address, which the model does not use (not minimized)** |
| Build or buy | Buy: licensed model from a fraud analytics vendor, hosted in the company's tenant (SYS-09). The vendor retrains it quarterly; the company sets thresholds |
| Not intended | Credit decisions, merchant underwriting, or any use outside authorization fraud screening. Using scores for merchant pricing or cardholder profiling requires re-assessment |
| Fallback | If the model is unavailable, fallback velocity and amount rules in the switch take over (P05 BP-06) |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45 | **Yes** | The FTC can treat unsupported claims about the model to merchants (for example accuracy claims in sales material) as deceptive. It can treat practices that cause substantial consumer injury that consumers cannot reasonably avoid as unfair (15 U.S.C. 45(n)). Unjustified decline rates for some groups of cardholders are the risk here (R-021) |
| FTC Safeguards Rule, 16 CFR 314.4(f) | **Yes** | The quarterly extract is customer information sent to a service provider. It needs contract safeguards and periodic assessment (R-022) |
| PCI DSS v4.0.1 (3.2.1, 12.8) | **Yes** | The extract must never contain PAN, and the vendor is a third-party service provider. The 2026-08-05 finding of PAN in the training table (R-031) shows how this failed |
| ECOA and Regulation B, 12 CFR 1002 | **No** | The company is not a creditor and does not decide on credit. Issuers make the credit authorization decision |
| Colorado SB26-189 (effective 2027-01-01) | **To be assessed by counsel by 2026-12-15** | It covers automated decision technology that "materially influences" consequential decisions, including financial or lending services, for businesses doing business in Colorado. Whether an automatic fraud decline of a purchase is a consequential decision about a "financial service" is not settled. The company will not assume it is exempt |
| NYDFS AI industry letter (2024-10-16) under Part 500 | **No** | Guidance for entities regulated under 23 NYCRR Part 500; the company holds no New York license |
| Card brand rules | **Yes (indirectly)** | Fraud and chargeback thresholds for merchants depend on the model working well |

## 3. Risk tier
**Tier: High** for AI-001 (repository rubric, `00_universal/projects/P10_ai-governance/README.md`).

**Why High:**
- It runs inline on the authorization path of payment infrastructure, the Financial Services critical infrastructure sector.
- It declines consumer purchases automatically, with no human review before the decline.
- A drift or bias failure hits thousands of consumers and merchants within hours (R-020, R-021).

It is **not** a credit decision, so the consequential-decision laws that expressly name credit do not attach as such. The High tier comes from the critical infrastructure criterion.

**High-tier minimum controls and how they are met:**
- **Human review before action:** not feasible for real-time authorization. The compensating controls are in section 5.
- **Pre-deployment bias testing:** required before each quarterly model update (section 4).
- **Impact assessment:** this document.
- **Notice to affected people:** through merchants, not directly. The merchant integration guide will disclose that automated fraud screening is used, and declined consumers can retry or pay another way.
- **Ongoing monitoring:** daily (section 5).

**AI-002: Medium today, Low once controlled.** Staff have pasted transaction details into public chatbots. Once public chatbots are blocked and the enterprise assistant (no training on company data) is in use, it becomes a Low-tier internal productivity use.

## 4. MEASURE
Results use the first test run on 2026-08-18, on Q2 2026 transactions (about 23 million) with fraud labels matured through July 2026.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Fraud detection rate (fraud value caught / total fraud value) at least 70%; overall false positive rate (legitimate transactions declined or challenged) at most 1.5% | Detection 76%; false positive rate 1.1% | Yes |
| Valid and reliable (drift) | Weekly population stability index on the score distribution under 0.2; decline rate within 20% of the 13-week average | Not monitored before 2026-08; a 2026-06 decline spike (+45% for 3 days after a vendor update) was found only from merchant complaints | **No** |
| Safe | Fallback rules take over within 1 minute if the model fails; test quarterly | Failover tested once (2025-11) | Partial |
| Secure and resilient | Model hosted in the CDE-adjacent tenant; access through the bastion; vendor has no standing access | Vendor had a standing support account (disabled 2026-08-20) | Partial |
| Accountable and transparent | Threshold changes approved by the Risk and Fraud Manager and logged; vendor model documentation (intended use, training data categories, limitations) on file | Threshold log exists; vendor documentation covers intended use but not training data categories or known limitations | Partial |
| Explainable and interpretable | Top reason codes returned with each score; analysts can see them on review | Reason codes available | Yes |
| Privacy-enhanced | Training extract token-only and minimized; contract limits use to the company's model; deletion certificate after retraining | Extract includes name and full billing address; no use limit or deletion clause; PAN was wrongly written to the training table (R-031) | **No** |
| Fair, with harmful bias managed | Bias testing plan below | Two segments flagged | **No** |

### Bias and fairness testing plan
**Why it matters.** The processor has no data on cardholders' protected characteristics and must not collect it for this purpose. Unfairness can still enter through features that act as proxies: card type (prepaid cards are used more by consumers without bank accounts), BIN country, and billing ZIP code. The test looks for **unjustified differences in false positive rates**: legitimate purchases declined or challenged.

| Element | Plan |
|---|---|
| Groups compared | (1) Card type: prepaid vs debit vs credit. (2) BIN country: domestic vs international. (3) Billing ZIP code groups: ZIP codes in the top vs bottom quintile of median household income, from public Census data (a proxy method, labeled as such; no individual data inferred or stored). (4) Merchant category groups |
| Metrics | False positive rate per group; ratio to the overall rate; detection rate per group (to check that a fix does not simply let fraud through) |
| Threshold | Flag a group if its false positive rate is more than 1.25 times the overall rate **and** at least 0.5 percentage points higher. A flagged group needs a documented business justification (for example a proven fraud pattern) or a mitigation before the next model update |
| When | Before every quarterly model update (pre-deployment), and monthly on production data |
| Who | Fraud analyst runs it; the Risk and Fraud Manager signs off; the COO sees the results each quarter |
| Records | Kept for 3 years with the model version and thresholds (POL-01 4.15) |

**2026-08-18 results:**
- **Prepaid cards:** false positive rate 2.9% vs 1.1% overall (2.6 times). **Flagged.** The vendor's features give prepaid cards a flat risk uplift that fraud outcomes do not fully support: prepaid fraud rate is 1.6 times the average, not 2.6 times.
- **Lowest-income ZIP code quintile:** 1.5% vs 1.1% (1.36 times, 0.4 points). Not flagged (below the 0.5-point floor), but watched monthly.
- **International BINs:** 2.4% vs 1.1%. Not flagged: justified by international fraud rates 3.1 times the domestic rate on the same merchants, documented by the Risk and Fraud Manager.
- **Merchant categories:** no group flagged.

**Mitigation for prepaid cards:** ask the vendor to remove the flat uplift in the Q4 2026 update. Until then, route prepaid transactions in the 800 to 949 score band to step-up authentication instead of decline, where the merchant supports it. Retest before the update goes live.

## 5. MANAGE
**Human-in-the-loop design (compensating for real-time automation):**
- Score bands:
  - 950 and above: automatic decline.
  - 800 to 949: step-up authentication (card-not-present) or merchant review queue (high-value card-present).
  - Below 800: approve, subject to merchant rules.
- Fraud analysts review all escalations. A monthly random sample of 200 automatic declines is reviewed to estimate the false decline rate.
- Merchants can allow-list customers and dispute declines through support. Disputed declines are reviewed within 2 business days.
- Threshold changes need the Risk and Fraud Manager's approval, a logged reason, and a 7-day look-back on decline rates.

**Monitoring:**
- Daily decline-rate and false positive dashboards with alerts at plus or minus 20% of the 13-week average (R-020).
- Weekly drift check.
- Monthly bias test on production data.
- Quarterly model validation before each vendor update, including the bias plan.

**Vendor and data controls (R-022):**
- Minimize the extract to tokens, features, and labels only, with no name or address.
- Automated PAN block before the extract is written (POAM-012).
- Contract amendment: use limited to the company's model, no pooling with other clients' data unless approved, a deletion certificate after each retraining, and 24-hour security incident notice.
- Obtain the vendor's AOC or include it in the ROC (POAM-017).

**Rollback:** the switch keeps the prior model version for 30 days after each update. The Risk and Fraud Manager can roll back or switch to the fallback rules within 15 minutes if daily metrics breach thresholds.

**Incident handling:** a model failure that causes mass false declines is handled under P08 roles (RS.MA) and the merchant communication steps. A vendor data exposure follows P08 and the notification matrix.

**Decommissioning:** replace or retrain if the prepaid disparity is not fixed within two model updates, or if the vendor refuses the use-limit and deletion terms.

### AI-002: staff generative AI chatbots (NIST AI 600-1)
| AI 600-1 risk | Relevance | Control |
|---|---|---|
| Data privacy | Staff pasted merchant and transaction details into public chatbots (P01 R-023) | POL-05 4.2 and 4.7; block public chatbots on managed laptops; enterprise assistant with no-training and retention terms, approved 2026-08-31 |
| Information security | Code snippets from chatbots could introduce vulnerable code | Generated code goes through the same pull-request review and static analysis as other code (CM-3, SA-11) |
| Confabulation | Wrong answers in merchant emails about fees or funding | Staff review every output; no chatbot text sent to merchants without review |
| Value chain and component integration | Tool vendor terms can change | Annual review of the enterprise assistant's terms by the Compliance and Risk Manager |

## 6. Decision
**Approve continued production of AI-001 with conditions.** COO, 2026-08-31. The majority owner and CEO accepted the related High-tier risk treatment plans the same day. Conditions:
1. Daily decline-rate and drift monitoring with alerts live by **2026-09-30** (R-020).
2. Prepaid step-up routing in place by **2026-09-30**; vendor fix in the Q4 2026 update, retested with the bias plan before release (R-021).
3. Training extract minimized and the PAN block live by **2026-09-30**. Contract amendment with use limits, deletion, and incident notice signed by **2026-11-30** (R-022).
4. Vendor model documentation (training data categories, known limitations) received by **2026-11-30**.
5. Counsel's Colorado SB26-189 applicability opinion by **2026-12-15**. If it applies, notice and human review processes must be in place for decisions made on or after 2027-01-01.

**AI-002:** public chatbots are prohibited for work from 2026-09-01. The enterprise assistant rollout and blocking of public chatbots on managed laptops are due by **2026-10-31** (R-023). Training on the generative AI rules is added to the annual awareness course (POL-05 4.3).

# AI Risk Assessment: Gateway Fraud-Scoring Filter

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (merchant services provider, an ISO) |
| Tier / Vertical | Micro / Financial Services |
| AI use case | AI-001: the gateway's machine-learning fraud-scoring filter, as configured by the company for its e-commerce merchants (the registry's "transaction fraud-detection model", adapted: the company configures a vendor's model; it does not build or host one) |
| Framework | NIST AI RMF 1.0 (AI 100-1); NIST AI 600-1 Generative AI Profile for AI-002 and AI-003 |
| Assessor / date | Onboarding and Risk Specialist with the Operations Manager, 2026-08-25 |
| Decision | Owner, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the Onboarding and Risk Specialist for AI-001 and AI-003; the Operations Manager for AI-002. **Decision authority:** the Owner. The related risks in P01 are Moderate (R-013) and Low (R-014), within the Owner's authority under POL-02 A.4.
- **Policies that apply:**
  - POL-04 4.6: approved AI tools only; nothing Restricted in any AI tool.
  - POL-04 4.9: every change to fraud filter settings is recorded in the change log.
  - POL-02 C.2 and C.3: no merchant or card data in public AI tools.
- **Approved-tools list:** kept by the Operations Manager in POL-04 4.6. It did not exist before this assessment (gap 14 in `../00_company-facts.md`).
- **Scale for a Micro company:** there is no AI committee. The Owner, the Operations Manager, and the Onboarding and Risk Specialist review AI use at the quarterly PCI review (POL-02 A.5).

**How AI-001 started.** When the gateway added fraud scoring in 2024, the company set default thresholds for all its e-commerce merchants: automatic decline at a score of 80 or above, and merchant review between 60 and 79. Nobody has looked at the results since. 104 of the 120 merchants still use the company's defaults.

## 2. MAP (AI-001)
| Item | Description |
|---|---|
| Purpose and intended use | Screen card-not-present transactions for fraud before they go to the card issuer, so merchants suffer fewer fraud chargebacks |
| Users / operators | The gateway (automated); the Onboarding and Risk Specialist (sets defaults); merchants (review held transactions, change their own thresholds, allow-list customers) |
| Affected people | Consumers buying from about 120 merchants (about 310,000 card-not-present transactions in Q2 2026); merchants whose sales are declined |
| Data | Inputs, as listed in the gateway documentation: amount, time, card type and issuing country, billing address match, IP address and device signals, email address, merchant category. The company sees only scores, reason codes, and decline and hold counts per merchant. It has no access to the model or its training data |
| Build or buy | Configure: the processor partner owns and updates the model. Updates are not announced to the company |
| Not intended | Merchant underwriting, pricing, or any decision about merchants or cardholders outside transaction screening. Any such use requires re-assessment |
| Fallback | If scoring is unavailable, the gateway approves and sends transactions to the issuer as usual |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45 | **Yes** | Two exposures. Deception: the company's sales brochure says its "AI fraud protection stops 99% of fraud", a claim it cannot support. Unfairness: practices that cause substantial consumer injury that consumers cannot reasonably avoid (15 U.S.C. 45(n)); unjustified decline rates for some groups of shoppers are the risk here (R-013) |
| PCI DSS v4.0.1 6.5.1 | **Yes** | Fraud filter settings are gateway settings the company changes for merchants; changes need approval and a record (P03 G-029) |
| FTC Safeguards Rule, 16 CFR 314.4(f) | **No for AI-001** | The company sends no data to the model; the processor partner runs it on its own platform. **Yes for AI-002 and AI-003**, which could put information into an unapproved provider's hands |
| ECOA and Regulation B, 12 CFR 1002 | **No** | Screening a purchase for fraud is not a credit decision, and the company is not a creditor |
| Colorado SB26-189 (effective 2027-01-01) | **To be assessed by counsel by 2026-12-15** | It covers automated decision technology that "materially influences" consequential decisions, including financial or lending services, for businesses doing business in Colorado, with no small-business exemption in the signed text. The company has no Colorado merchants, but online shoppers can be anywhere. Whether a fraud decline of a purchase is a consequential decision about a "financial service" is not settled. The company will not assume it is exempt |
| NYDFS AI industry letter (2024-10-16) under Part 500 | **No** | Guidance for New York licensees; the company holds no New York license |
| Card brand rules | **Indirectly** | Merchants' fraud and chargeback levels depend on the filter working well |

## 3. Risk tier
**Tier: Medium** for AI-001 (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why not High:**
- It is not one of the rubric's consequential decisions (employment, credit, housing, insurance, education, health care, government services, legal services). It screens a purchase; the consumer can retry, pay another way, or ask the merchant to approve.
- The company does not operate payment infrastructure. The processor partner runs the model and the gateway; the company sets thresholds for 120 small merchants.

**Why not Low:** it affects consumers directly, and at today's settings it declines purchases automatically with no human review for every score of 80 or above.

**The decision (section 6) moves AI-001 toward the Medium criteria:** after the change, automatic decline applies only at a score of 90 or above, and everything from 70 to 89 is held for the merchant to decide. The company also applies two High-tier controls anyway, because declines are automatic at the top band: testing before each threshold change, and monthly fairness monitoring.

**Re-tier to High and reassess if:** the company starts using scores for merchant underwriting or pricing; automatic decline is extended below 90; counsel finds Colorado SB26-189 applies; or the company starts hosting or training a model itself.

**AI-002 and AI-003: Medium today, Low once controlled.** See section 5.

## 4. MEASURE (AI-001)
Results use gateway reports for Q2 2026 (about 310,000 card-not-present transactions across the 120 merchants), pulled on 2026-08-18. The company sees counts by merchant, card type, and issuing country, not by individual.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Fraud chargeback rate on approved transactions under 0.15%; share of held transactions released by merchants as legitimate under 50% | Fraud chargebacks 0.09%; merchants released 71% of held transactions as legitimate | **Partial** (fraud is caught, but most holds are false alarms) |
| Valid and reliable (drift) | Monthly decline rate within 25% of the 6-month average | Not monitored before 2026-08. Declines rose from 1.4% to 2.6% in April 2026 for two weeks, probably after an unannounced model update; found only now | **No** |
| Safe | Fallback approves transactions if scoring fails; merchants can override | Confirmed in gateway documentation; merchants can override and allow-list | Yes |
| Secure and resilient | Only named company accounts with MFA can change thresholds | Any company console account can change them; MFA optional (R-001) | **No** |
| Accountable and transparent | Threshold changes approved and logged; merchants told the filter is automated; claims to merchants supported | No change log; merchant onboarding pack does not mention automated declines; brochure claims "stops 99% of fraud" | **No** |
| Explainable and interpretable | Reason codes shown with each decline and hold | Reason codes available to merchants in the gateway | Yes |
| Privacy-enhanced | No company data sent to the model beyond transaction data the gateway already holds | Confirmed: the company sends nothing | Yes |
| Fair, with harmful bias managed | Bias testing plan below | One group flagged | **No** |

### Bias and fairness testing plan
**Why it matters.** The company has no data on shoppers' protected characteristics and must not collect it. Unfairness can still enter through inputs that act as proxies. The one the company can see is **card type**: prepaid cards are used more by consumers without bank accounts. The company can also see the issuing country.

| Element | Plan |
|---|---|
| Groups compared | (1) Card type: prepaid vs debit vs credit. (2) Issuing country: domestic vs international. (3) Merchant category |
| Metrics | Decline rate and hold rate per group; ratio to the overall rate; fraud chargeback rate per group (to check that a fix does not simply let fraud through) |
| Threshold | Flag a group if its decline rate is more than 1.25 times the overall rate **and** at least 0.5 percentage points higher. A flagged group needs a documented fraud justification or a mitigation before the next threshold review |
| When | Before every threshold change, and monthly on the gateway report |
| Who | The Onboarding and Risk Specialist runs it; the Operations Manager checks it; the Owner sees results at the quarterly PCI review |
| Records | Kept for 3 years with the threshold settings in force (POL-02 A.9) |

**2026-08-18 results:**
- **Prepaid cards:** declined at 5.8% against 1.9% overall (3.1 times). **Flagged.** Prepaid fraud chargebacks were 0.14%, about 1.6 times the 0.09% average, which does not justify a threefold decline rate.
- **International cards:** declined at 6.4% against 1.6% for domestic cards. Not flagged as unjustified: international fraud chargebacks were 4.2 times the domestic rate on the same merchants, documented by the Onboarding and Risk Specialist.
- **Merchant categories:** no category flagged.

**Mitigation for prepaid cards:** move to the section 6 thresholds, so most prepaid transactions in the 80 to 89 band are held for the merchant instead of declined. Ask the processor partner whether the model treats prepaid cards as a risk factor and whether that can be tuned. Retest one month after the change.

## 5. MANAGE
**Human-in-the-loop design for AI-001:**
- Score bands (from 2026-09-30):
  - 90 and above: automatic decline (the shopper can pay another way).
  - 70 to 89: held for the merchant to approve or decline in the gateway, with the reason code shown.
  - Below 70: approved, subject to the merchant's own rules.
- Merchants can change their own thresholds and allow-list repeat customers. Each merchant is told in the onboarding pack that automated fraud screening is used and how to change it.
- Threshold changes need the Onboarding and Risk Specialist's approval, an entry in the change log, and a look at the next month's decline rates (POL-04 4.9).

**Monitoring:**
- Monthly: decline and hold rates per merchant and per group, with the bias test above (R-013).
- Monthly: ask the processor partner whether the model was updated; any update triggers an extra check that month.
- Merchant complaints about lost sales from declines go to the Onboarding and Risk Specialist.

**Claims to merchants:** the brochure line "stops 99% of fraud" was withdrawn on 2026-08-25. Any new claim about the filter must be backed by the company's own monthly data and approved by the Owner.

**Incident handling:** a sudden spike in declines (for example, after a model update) is handled with the processor partner: revert to the prior thresholds for affected merchants and tell them. A misuse of console access to change thresholds is a security incident under POL-03 and the P08 runbook.

**Decommissioning:** if the prepaid disparity is not reduced within two monthly checks after the threshold change, switch affected merchants to merchant review for the whole 70 to 99 range until the processor partner explains or fixes the model.

### AI-002 and AI-003: generative AI (NIST AI 600-1)
| AI 600-1 risk | Relevance | Control |
|---|---|---|
| Data privacy | Staff pasted merchant statements into public chatbots (R-014); the CRM assistant (AI-003) could read merchant owner Social Security numbers | Public chatbots prohibited for work from 2026-09-01 (POL-02 C.2, C.3); business AI assistant with no-training terms for Confidential and Public data only; AI-003 switched off 2026-08-25 until the CRM vendor confirms no training on company data |
| Confabulation | Wrong pricing or fee figures in proposals to merchants | Staff check every figure against the merchant's statement before sending |
| Information security | Prompt injection through documents pasted into a chatbot | No Restricted data in any AI tool (POL-04 4.6); training covers it |
| Value chain and component integration | Vendors switch AI features on by default (as the CRM vendor did) | The Operations Manager checks vendor release notes monthly for new AI features; new features stay off until approved |

## 6. Decision
**Approve continued use of AI-001 with conditions.** Owner, 2026-08-31. Conditions:
1. New default thresholds (automatic decline at 90 and above; merchant review from 70 to 89) applied to the 104 merchants on the company defaults by **2026-09-30**, with each merchant told by email.
2. Change log for filter settings and MFA on every console account by **2026-09-30** (POL-04 4.9; POAM-002).
3. Monthly decline, drift, and bias report from **2026-10**; first retest of the prepaid group by **2026-10-31**.
4. Onboarding pack updated to disclose automated fraud screening by **2026-10-31**; the brochure claim was withdrawn on 2026-08-25.
5. Written answer from the processor partner on model update notices and prepaid handling by **2026-11-30**.
6. Counsel's Colorado SB26-189 applicability opinion by **2026-12-15**. If it applies, notice and human review processes must be in place for decisions made on or after 2027-01-01.

**AI-002:** public chatbots prohibited for work from 2026-09-01; business AI assistant rollout and training by **2026-10-31** (R-014).
**AI-003:** stays off until the CRM vendor confirms its data use terms in writing; re-assess before switching it on.

# AI Risk Assessment: AI Offers and Markdown Suggestions

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (neighborhood grocery store with online ordering) |
| Tier / Vertical | Micro / Retail Trade |
| AI use case | AI-001: the commerce platform's built-in AI offers and markdown feature (SYS-10), turned on by the Owner in April 2026 |
| Why this use case | The registry default for this industry is "dynamic pricing and personalized offers". A 7-person store does not run a dynamic pricing engine; it uses the platform's built-in feature, which suggests personalized loyalty offers and price changes. The risks are the same in kind at a smaller scale (see `../00_company-facts.md` section 5) |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook |
| Assessor / date | Store Manager (Security and PCI Lead) with the Owner and the Stock and Produce Clerk, 2026-08-24 to 2026-08-26 |
| Decision | Owner, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner and decision authority:** the Owner, who turned the feature on and approves offer campaigns. At this size the business owner and the decision maker are the same person; the Store Manager's review and the independent assessor (P07) are the checks.
- **Policies that apply:**
  - POL-04 4.8: Restricted data only in approved AI tools; the feature is approved only under the conditions in section 6.
  - POL-04 4.9: no new data sharing unless the privacy notice still matches.
  - POL-02 A.3: Moderate risks only accepted by the Owner with a written reason.
- **Approved-tools list:** kept in POL-04 4.8. It lists AI-001 under conditions, and AI-002 (a public chatbot) for product text only, with no customer, employee, or supplier cost data.
- **Scale for a Micro business:** there is no AI committee. The Owner and Store Manager review AI use at the monthly security meeting.
- **Gap that started this review:** the feature went live in April 2026 with its default settings and no look at the provider's data use terms, the customer disclosure, or how offers differ between customers (P01 R-018; P03 G-072, G-073).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | **(a) Personalized offers:** each week the feature suggests digital coupons for each loyalty member (sent by email or text, and applied at checkout) based on what they buy and how often they visit. **(b) Price suggestions:** it suggests markdowns for near-date produce, dairy, bakery, and prepared foods, and regular price changes for slow or fast sellers |
| Users | Owner (offer campaigns), Store Manager (regular price changes), Stock and Produce Clerk (near-date markdowns) |
| Affected people | About 2,400 loyalty members (offers); every shopper (shelf prices are the same for everyone) |
| Data | Inputs: loyalty purchase history and visit frequency; item cost, price, stock, sell-by date, and sales velocity. **Found at assessment:** the platform automatically built customer segments from **payment tender type**, including a segment of members who usually pay with SNAP EBT. Tender-based segments were turned off on 2026-08-26. **The provider's setting "share data to improve models" was on by default**; turned off on 2026-08-26 |
| Build or buy | Buy: a feature inside the commerce platform, configured by the store |
| Not intended | Different shelf prices for different customers; any decision about credit, employment, or eligibility. Turning on any automatic price change without a person approving it requires a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, deception, 15 U.S.C. 45(a)(1) (N44-45-R02) | **Yes** | Claims such as "savings picked just for you" and "lowest price" markdown tags must be truthful and substantiated. Nobody keeps a record that supports them (P03 G-072). The privacy notice says customer information is never shared, while purchase history feeds the provider's feature (P03 G-069) |
| FTC Act Section 5, unfairness, 15 U.S.C. 45(n) (N44-45-R02) | **Yes** | A practice is unfair only if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits. Offers change only discounts, not shelf prices, which limits the harm, but systematically smaller offers for a group of customers is the scenario to watch (P03 G-073) |
| SNAP equal treatment, 7 CFR 278.2(b) | **Yes, as a guardrail** | SNAP benefits must be accepted for eligible foods "at the same prices and on the same terms and conditions applicable to cash purchases". The store is an authorized SNAP retailer. Targeting offers by tender type risks treating SNAP customers on different terms, so tender type is not an allowed input. Counsel was not consulted; the store simply removed the input |
| Price gouging during a declared state of emergency, Fla. Stat. 501.160 | **Yes, during emergencies** | Food and water are commodities under the statute. A price that is a gross disparity from the average price in the 30 days before the declaration is prima facie unconscionable unless the increase comes from added costs or market trends. A demand-based suggestion can recommend an increase exactly when a hurricane is coming |
| FTC surveillance pricing 6(b) study (2024) | Watch item | A study, not a rule. It shows FTC interest in prices or offers set from personal data |
| CCPA automated decisionmaking rules (N44-45-R06) | No | The store does not do business in California and is far below the revenue threshold |
| Colorado SB26-189 and similar consequential-decision laws | No | Retail prices and coupons are not among the consequential-decision categories, and the store operates only in Florida |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why not High:** the feature does not make, and is not a substantial factor in, a consequential decision about a person. Every suggestion needs a person to accept it, and shelf prices are the same for every shopper.
- **Why not Low:** it uses customer purchase data, it reaches customers directly with offers, and it influences what everyone pays.

**Re-tier to High and reassess if:** suggestions are set to apply automatically; offers or prices use tender type, age, or any input that identifies or infers a protected characteristic; the feature starts setting different shelf or online prices per customer; or the store begins selling online to customers in other states.

## 4. MEASURE
The Store Manager and Stock and Produce Clerk reviewed 30 price suggestions from July and August, and the Store Manager compared the offers sent in 4 weekly campaigns, on 2026-08-24 to 2026-08-26.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Price suggestions below item cost (except near-date items) must be 0 | 2 of 30 suggested prices below cost on items not near their date, after a supplier cost was entered wrong | **No.** Cost floor and cost entry check needed |
| Safe | No price increase on food, water, or ice above the 30-day average while a state of emergency covers the county | 1 suggestion in June 2026 raised bottled water 18% during a demand spike before a storm (no emergency had been declared; the Store Manager rejected it) | **No.** No emergency rule configured |
| Secure and resilient | Feature settings changed only by the Owner and Store Manager with MFA | Store Manager login without MFA (POAM-005) | Partial |
| Accountable and transparent | Customers told that offers are chosen from purchase history | Not disclosed; privacy notice says data is never shared | **No** |
| Explainable and interpretable | Feature shows why each offer or price was suggested | Shows the top factors for prices; not for offers | Partial |
| Privacy-enhanced | Only needed data used; provider does not use store data to improve its models | Tender type was used; model-improvement sharing was on by default (both turned off 2026-08-26) | **No** (fixed during assessment; contract terms still to confirm) |
| Fair, with harmful bias managed | See the fairness test below | Members who mostly pay with SNAP EBT received smaller offers (ratio 0.71) | **No.** Flagged and fixed; retest passes |

### Fairness test
**Groups compared.** The store holds no data on race, ethnicity, sex, or age and will not infer it. It compares groups it can see without sending anything new to the provider:
- members who pay with SNAP EBT for most of their visits versus all other members (from the store's own POS reports, not sent to the feature);
- members by visit frequency (weekly, monthly, occasional).

**Metric and threshold (a store-defined screening rule, not a legal standard):** average weekly offer value per active member in each group, divided by the highest group. **Flag when the ratio is below 0.80.**

**Results:**
- **SNAP EBT group (campaigns 2026-07-27 to 2026-08-17):** ratio **0.71**. Cause: the platform's automatic "high-value customers" segment excluded members whose usual tender was EBT. Tender-based segments were turned off on 2026-08-26; a simulated campaign the same day gave a ratio of **0.94**, which passes.
- **Visit frequency:** occasional visitors 0.83 of weekly visitors. Passes; reported for context.
- **Frequency:** monthly from 2026-09-30, and before any change to the feature's settings.

## 5. MANAGE
**Human-in-the-loop design:**
- Offer campaigns: the Owner reviews and approves each weekly campaign before it is sent.
- Regular price changes: the Store Manager approves each one; increases on food staples need a reason recorded (for example a supplier cost increase).
- Near-date markdowns: the Stock and Produce Clerk may accept suggestions up to 50% off for items within 2 days of their sell-by date; anything else goes to the Store Manager.
- A hard floor at item cost for all suggestions except near-date markdowns, and a check of supplier cost entries before they are saved.

**Emergency pricing guardrail (Fla. Stat. 501.160):** when a state of emergency covering the county is declared, the Owner or Store Manager turns off price-increase suggestions the same day, and no regular price on food, water, ice, or other essential items goes above its average in the 30 days before the declaration unless a supplier cost increase is documented. This step is in the hurricane checklist (P01 R-016, R-019).

**Data protection:**
- Tender type stays out of all segments (7 CFR 278.2(b) guardrail).
- Model-improvement data sharing stays off; the Bookkeeper asks the provider to confirm in writing that store customer data is not used for other merchants or to train shared models, and that it is deleted at contract end (POAM-010).
- The feature's settings are changed only by the Owner and Store Manager, both with MFA (POAM-005).

**Transparency and claims:**
- Privacy notice rewritten to say that loyalty offers are chosen from purchase history by the store's platform provider (by 2026-10-31; P03 G-069).
- "Lowest price" tags removed unless a price check supports them; "savings picked for you" wording kept only with a campaign record showing the discount (P03 G-072).

**Monitoring:** monthly fairness ratio; monthly count of rejected and below-cost suggestions; customer complaints about offers or prices reviewed at the monthly security meeting, tracked in the risk register (R-018, R-019).

**Incident handling:** an overcharge from an accepted suggestion is corrected and refunded at the register. A provider security incident involving loyalty data follows P08 and Fla. Stat. 501.171.

**Decommissioning:** turn the feature off (standard weekly ad and manual markdowns) if a fairness flag is not fixed within 30 days, if the provider will not confirm the data use terms by 2026-11-30, or if the provider changes its data use terms.

## 6. Decision
**Approve with conditions.** Owner, 2026-08-31. The feature may continue **only if**:
1. Tender-based segments and model-improvement data sharing stay off (done 2026-08-26).
2. The emergency pricing rule is in the hurricane checklist and price-increase suggestions can be switched off in one step, by 2026-09-30.
3. The cost floor and cost entry check are in place by 2026-10-15.
4. The privacy notice disclosure and corrected claims are published by 2026-10-31.
5. Monthly fairness checks start by 2026-09-30.
6. The provider confirms the data use and deletion terms in writing by 2026-11-30.

**AI-002 (public chatbot for product text):** approved for product descriptions, weekly ad text, and social posts with no customer, loyalty, employee, or supplier cost data (POL-04 4.8). Low tier. Claims it drafts still go through the claims checklist.

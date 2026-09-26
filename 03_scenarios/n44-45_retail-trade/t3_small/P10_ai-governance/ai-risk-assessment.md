# AI Risk Assessment: Dynamic Pricing and Personalized Offers

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent grocery retailer, one supermarket plus online ordering) |
| Tier / Vertical | Small / Retail Trade |
| AI use case | AI-001: pricing and personalized offers engine (SYS-12), live since March 2026 |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook |
| Assessor / date | E-commerce and Marketing Manager (business owner) with the IT Manager and Controller, 2026-08-24 to 2026-08-28 |
| Approved | General Manager, 2026-09-04 (see section 6) |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner:** E-commerce and Marketing Manager. **Decision authority:** General Manager (Medium tier). Majority owner if re-tiered High.
- **Policies that apply:**
  - POL-04 4.5: customer data used only for purposes in the privacy notice; new uses need a P10 review
  - POL-01 4.12: pricing and savings claims reviewed before publication
  - POL-01 4.8: service provider terms on data use and deletion
  - POL-05 4.11: approved AI tools only for customer data
- **Approved-tools list:** kept by the IT Manager. It lists the pricing and offers engine (AI-001) and one enterprise generative AI assistant for marketing copy with no customer data (AI-002).
- **Scale for a Small company:** there is no AI committee. The E-commerce and Marketing Manager, IT Manager, and Controller review AI use cases quarterly, and the General Manager approves changes.
- **Gap that started this review:** the engine went live in March 2026 with no security, privacy, fairness, or claims review (P01 R-015, R-016; P03 G-072, G-073).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | **(a) Dynamic online prices:** adjust the online price of each item within plus or minus 15% of the shelf price, based on demand, stock level, and freshness (for example, marking down produce and bakery items near their sell-by date). **(b) Personalized offers:** choose weekly digital coupons for each loyalty member from their purchase history |
| Users / operators | E-commerce and Marketing Manager sets bounds, campaigns, and exclusions; the vendor runs the models |
| Affected people | About 9,500 online shoppers (prices) and about 21,000 loyalty members (offers), across 6 ZIP codes with different income levels and 4 delivery zones |
| Data | Inputs: loyalty purchase history, home ZIP code, delivery zone, item cost and shelf price, stock, and sales velocity. **Not used:** name, email, or payment tender type (checked 2026-08-25: SNAP EBT and card type are not sent to the engine). The feed today sends the loyalty number with each record; a pseudonymous ID is enough |
| Build or buy | Buy: vendor SaaS add-on to the storefront and loyalty program; vendor models configured by the company |
| Not intended | Individual prices based on a shopper's personal profile (prices vary by item and time, not by person); pricing in store (shelf prices are set by the back office); any credit, employment, or eligibility decision. **Enabling individualized online prices requires re-assessment** |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, deception, 15 U.S.C. 45(a)(1) (N44-45-R02) | **Yes** | Claims such as "personalized savings", reference prices, and the "online prices match the store" banner must be truthful and substantiated. The banner was inaccurate: 17 of 50 items compared on 2026-07-28 had a different online price (P03 G-072) |
| FTC Act Section 5, unfairness, 15 U.S.C. 45(n) (N44-45-R02) | **Yes** | A pricing practice is unfair only if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits. Higher online prices in lower-income delivery zones, where shoppers may not be able to reach the store, is the scenario to guard against (P03 G-073) |
| FTC surveillance pricing 6(b) study (orders July 2024; staff research summaries January 2025) | Watch item | A study, not a rule. It shows FTC interest in prices or offers set from personal data |
| FTC proposed AI-accuracy policy statement (Docket FTC-2026-0727, July 2026) | No (proposed) | Not final; not treated as a current obligation (P03 section 5) |
| Price gouging during a declared state of emergency, Fla. Stat. 501.160 | **Yes, during emergencies** | Food and water are commodities under the statute. A price that shows a gross disparity from the average price in the 30 days before the emergency declaration is prima facie unconscionable, unless the increase is due to added costs or market trends. **A demand-based engine can raise prices exactly when a hurricane emergency is declared**, so this Florida duty cannot be avoided |
| Other states' surveillance-pricing and consumer privacy laws | No | The company sells only through one Florida store with delivery within about 10 miles. Recheck if online sales reach other states |
| CCPA automated decisionmaking rules (N44-45-R06) | No | The company does not do business in California and is below the revenue threshold |
| Colorado SB26-189 and similar consequential-decision laws | No | Retail prices and coupons are not among the consequential-decision categories, and the company does not operate in those states |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal/projects/P10_ai-governance/README.md`).

**Why not High:** the engine does not make or substantially influence a consequential decision about a person (credit, employment, housing, insurance, education, health care, government services, legal services). Prices are bounded by rules the company sets, and shelf prices in the store are unaffected.

**Why not Low:** it uses customer purchase data, it directly affects what customers pay, and the August test showed it can produce different prices by neighborhood.

**Escalation triggers (re-tier to High and re-assess):**
- individualized online prices based on a shopper's profile or purchase history
- any input that identifies or infers a protected characteristic, or payment tender type (for example SNAP EBT)
- re-enabling the delivery-zone or ZIP-code factor
- widening the price bounds beyond plus or minus 15%
- selling online to customers in states with surveillance-pricing laws

## 4. MEASURE
| Trustworthy characteristic | Test / metric | Result (2026-08-24 to 2026-08-28) | Pass? |
|---|---|---|---|
| Valid and reliable | Daily exception report: prices outside bounds, below item cost, or changing more than twice a day. Target: 0 below-cost prices | 3 items priced below cost in August after a cost-file error; bounds held for all other items | **No.** Hard floor at item cost needed (P01 R-026) |
| Safe | Emergency price freeze: no increases above the 30-day pre-declaration average during a declared state of emergency | No freeze setting configured; the 2025 hurricane season was not checked | **No** |
| Secure and resilient | Vendor admin account with MFA; data feed over TLS; vendor security terms | MFA on; TLS confirmed; no security or data use clause and no assurance report (P01 R-025) | Partial |
| Accountable and transparent | Website explains that online prices can differ from shelf prices and that offers are personalized from purchase history | Not disclosed; privacy notice says member data is never shared (P01 R-017) | **No** |
| Explainable and interpretable | Vendor factor report shows why each price or offer was set | Available for prices; not for offers | Partial |
| Privacy-enhanced | Only needed data sent; pseudonymous ID; vendor may not reuse data or train shared models; deletion at termination | Loyalty number sent; contract silent on reuse and deletion | **No** |
| Fair, with harmful bias managed | See the bias testing plan below | Zone factor raised prices in 2 lower-income zones; offer value lower in the lowest-income ZIP group | **No.** Two disparities flagged |

### Bias and fairness testing plan
**Groups compared.** The company holds no data on race, ethnicity, sex, or age for shoppers, and will not infer it. It compares **geography**, which can act as a proxy for protected groups and for income:
- the 4 delivery zones;
- the 6 home ZIP codes, grouped by median household income from public Census data into lower, middle, and higher income.

**Metrics and thresholds (company-defined screening rules, not legal standards):**
| Metric | How measured | Flag when |
|---|---|---|
| Price index by zone | Average online price divided by shelf price, over the same 200-item basket, for orders delivered to each zone | Any zone is more than 1.0 percentage point above the lowest zone, or lower-income zones are above higher-income zones |
| Offer value ratio by ZIP group | Average weekly offer value per active member in each ZIP group, divided by the highest group | Ratio below 0.80 for any group |
| Markdown access | Share of near-date markdowns bought by each zone | Reported for context; no threshold |

**Results:**
- **Price index (test 2026-08-27):** 2 lower-income delivery zones were 4.1 and 3.6 points above shelf price, against 0.8 points in the other zones. Cause: the delivery-zone factor raised prices where fewer shoppers compared prices online. **The factor was disabled on 2026-08-28.** A retest the same day showed a 0.6-point spread, which passes.
- **Offer value ratio:** the lowest-income ZIP group scored **0.78**. The model favors members with high past spending. Fix: a minimum weekly offer value for every active member.
- **Frequency:** monthly from 2026-10-31, and before any model or input change.

## 5. MANAGE
**Human-in-the-loop design:**
- The E-commerce and Marketing Manager sets price bounds (plus or minus 15%), a hard floor at item cost, excluded items (infant formula, baby food, bottled water, and over-the-counter medicines stay at shelf price), and campaign rules.
- The manager reviews the daily exception report and can freeze all online prices to shelf prices with one setting.
- Monthly fairness results are reviewed by the General Manager.

**Emergency pricing guardrail:** when a state of emergency covering the store's county is declared, the E-commerce and Marketing Manager (or the General Manager) turns on the price freeze the same day. Online prices then cannot rise above their average over the 30 days before the declaration. This step is added to the hurricane plan (P01 R-031).

**Transparency and claims:**
- Remove the "online prices match the store" banner (by 2026-10-31, P03 G-072).
- Add a plain statement that online prices can differ from shelf prices, and that loyalty offers are chosen from purchase history.
- Keep a substantiation file for every savings or reference-price claim (POL-01 4.12).

**Monitoring:** the daily exception report; monthly fairness tests; a quarterly review of complaints about prices and offers, tracked in the risk register (R-015, R-016, R-026).

**Incident handling:**
- A pricing error that overcharges customers is corrected and refunded.
- A vendor security incident involving loyalty data follows P08, the vendor notice terms, and Fla. Stat. 501.171.

**Decommissioning:**
- Switch the engine off (shelf prices online; standard weekly ad offers) if a fairness flag is not fixed within 30 days.
- Switch it off if the vendor will not accept the data use amendment by 2026-11-30.
- Switch it off if the vendor changes its data use terms.
- On exit, the vendor must delete company data and confirm in writing.

## 6. Decision
**Approve with conditions.** General Manager, 2026-09-04. The engine may continue **only if**:
1. The delivery-zone and ZIP-code factors stay off. Re-enabling them requires a new assessment.
2. The emergency price freeze is configured and tested by 2026-10-15 (hurricane season).
3. A hard floor at item cost and the daily exception review are in place by 2026-11-30 (P01 R-026).
4. The website disclosure, the corrected claims, and the rewritten privacy notice are published by 2026-10-31 (P03 G-069, G-072).
5. A minimum weekly offer floor for all active members is live by 2026-10-31, and monthly fairness tests start the same month.
6. The vendor contract amendment (no secondary use or shared-model training, deletion at termination, security and incident notice terms) is signed by 2026-11-30 (POAM-013).
7. The data feed switches to a pseudonymous member ID by 2026-12-31.

**AI-002 (generative AI for marketing copy):** approved for product descriptions and ad copy with no customer, loyalty, or employee data (POL-05 4.11). Low tier. Claims the tool drafts still go through the POL-01 4.12 review.

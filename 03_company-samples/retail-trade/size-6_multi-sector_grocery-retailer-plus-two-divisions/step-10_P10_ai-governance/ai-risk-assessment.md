# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Grocery Retail, Grocery Wholesale, Financial Services, corporate) |
| Tier / Vertical | Multi-Sector / Retail Trade (focus division: Grocery Retail) |
| Scope | The group AI governance program: the Group AI Standard, the division use-case inventory, and the regulator-specific rules for the two priority use cases: the **pricing and offers engine** (AI-001, the registry use case "dynamic pricing and personalized offers") and the **credit decision engine** (AI-002, the only High-tier use case) |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; the Generative AI Profile (AI 600-1) for AI-006 and AI-009 |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-17 to 2026-08-28; presented to the board risk committee 2026-09-10 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 1 High, 6 Medium, 2 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list and the priority use case results quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Grocery Retail chief marketing officer, Financial Services chief compliance officer, Grocery Wholesale operations director. Approves High-tier use cases, priority Medium-tier use cases, and the approved-tools list |
| Model risk committee (Financial Services) | Validates credit and fraud models before use and after every material change; reports to the council |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring and report monthly |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) and the AI gateway |
| Group Chief Privacy Officer | Use of customer and cardholder data, affiliate sharing and opt-outs, retention |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026, under POL-01 4.12)
1. **Register before use.** Every AI system that uses customer, cardholder, or workforce data, or that makes or supports decisions about customers' prices, credit, or treatment in stores, is registered in the inventory and approved before deployment or material change (POL-01 4.12).
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, bias testing, notice to affected people, and quarterly monitoring reports. Medium tier: human oversight, quality monitoring, and AI disclosure where customers interact with it.
3. **Data rules.** Restricted or Confidential information goes only into approved AI tools whose contracts prohibit training on group data (POL-04 4.9; POL-05 4.7). Affiliate eligibility information (Rewards Card data) is used for marketing only within the rules in POL-04 4.5.
4. **Regulator overlays in each division supplement:** consumer protection, SNAP equal treatment, and emergency pricing for Grocery Retail; ECOA, Reg B, FCRA, and the Safeguards Rule for Financial Services; customer contracts and workforce rules for Grocery Wholesale.
5. **Change gate.** A new model, a retraining, a new input, a new decision role, or widened bounds triggers re-assessment before release.
6. **No facial recognition** anywhere in the group, for any purpose.

**Where the program fell short in 2026.** The standard and the council came after the pricing engine and the credit model were live (P01 GR-04). The credit model was retrained in 2026 without revalidating its adverse action reasons (P03 FS-G37), and the pricing engine has no emergency price freeze (P01 RT-015). Both are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Pricing and offers engine (online prices, shelf labels in 120 stores, personalized offers) | Grocery Retail | Medium (priority) | In production; approved with conditions |
| AI-002 | Credit decision engine (card approvals, credit lines, installment loans) | Financial Services | **High** | In production; continue with conditions |
| AI-003 | Card and e-commerce fraud scoring | Grocery Retail; Financial Services | Medium | In production |
| AI-004 | Demand forecasting and replenishment | Grocery Retail; Grocery Wholesale | Low | In production |
| AI-005 | Self-checkout loss prevention video analytics (no facial recognition) | Grocery Retail | Medium | In production with conditions |
| AI-006 | Generative AI customer service assistant | Grocery Retail; Financial Services | Medium | In production; cardholder answers limited |
| AI-007 | Warehouse labor planning and slotting | Grocery Wholesale | Medium | In production with a discipline restriction |
| AI-008 | Collections contact strategy | Financial Services | Medium | In production |
| AI-009 | Enterprise generative AI assistant (3,000 pilot users) | Group | Low | Pilot |

### 2.1 Pricing and offers engine (AI-001)
| Item | Description |
|---|---|
| Purpose and intended use | **(a) Prices:** set online prices and, in the 120 stores with electronic shelf labels, shelf prices, within approved bounds around the base price (plus or minus 10% for shelf labels, plus or minus 15% online), using demand, stock, freshness, and competitor price checks. **(b) Offers:** choose weekly personalized digital offers for about 9.6 million loyalty members from purchase history and, for cardholders, Rewards Card transaction data |
| Users / operators | Grocery Retail merchandising (bounds, cost floors, exclusions) and marketing (offer campaigns); the vendor runs the models |
| Affected people | Every online shopper and every shopper in the 120 shelf label stores (prices); loyalty members, including about 910,000 active Rewards Card holders (offers) |
| Data | Loyalty purchase history; store and delivery area; item cost, base price, stock, sales velocity; Rewards Card transaction data received from Financial Services under the 2023 intercompany data agreement. **Not intended as inputs:** name, demographics, or payment tender type. **Found in testing:** tender type, including SNAP EBT, was a feature in the offer model (removed 2026-08-26; section 4.1) |
| Build or buy | Buy: pricing engine SaaS vendor; models configured by Grocery Retail (P04: vendor SaaS with price and offer decision logs kept 24 months) |
| Not intended | Individual prices based on a shopper's profile (prices vary by item, store, and time, not by person); any credit, employment, or eligibility decision. **Individualized prices would require a new assessment** |

**Applicable laws and rules:**
| Rule | Applies? | What it means for the engine |
|---|---|---|
| FTC Act Section 5, deception, 15 U.S.C. 45(a)(1) (N44-45-R02) | **Yes** | Savings claims, reference prices, and statements about how offers are chosen must be true and substantiated. The privacy notice says Rewards Card data is used for offers "as permitted by your choices", which is not true for about 41,000 opted-out cardholders (P03 G-069) |
| FTC Act Section 5, unfairness, 15 U.S.C. 45(n) (N44-45-R02) | **Yes** | A practice is unfair if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that benefits do not outweigh. Higher prices where shoppers have fewer alternatives, or price spikes during a disaster, are the cases to guard against (P03 G-071) |
| FCRA affiliate marketing rule, 12 CFR 1022.21 (Reg V) | **Yes** | Grocery Retail may not use eligibility information received from Financial Services to make marketing solicitations to a consumer unless the consumer received notice and a reasonable opportunity to opt out and has not opted out, or an exception such as a pre-existing business relationship (1022.21(c)(1)) applies. Choosing offers from Rewards Card data is such a use. **Gap:** opt-outs are not applied and exceptions are not recorded (P03 G-075; POAM-012) |
| SNAP equal treatment, 7 CFR 278.2(b) | **Yes** | SNAP benefits ("coupons", which 7 CFR 271.2 defines to include EBT cards) must be accepted for eligible foods at the same prices and on the same terms and conditions as cash purchases at the same store. **The engine must never price or set offer terms by tender type** |
| Price gouging during a declared emergency (Fla. Stat. 501.160 worked example; each state where the group sells has its own rule) | **Yes, during emergencies** | In Florida, after the Governor declares a state of emergency, selling an essential commodity (including food, water, and ice) at an unconscionable price in the declared area is unlawful. A price that grossly exceeds the average price in the 30 days before the declaration is prima facie evidence of an unconscionable price, unless the increase is due to added costs or market trends. A demand-based engine raises prices exactly when demand spikes before a hurricane |
| FTC surveillance pricing 6(b) study (orders July 2024) | Watch item | A study, not a rule. It signals FTC interest in prices or offers set from personal data (P03 section 6) |
| State algorithmic or personalized pricing proposals | Watch item | Counsel reviews each legislative session; this assessment relies on no such law |
| CCPA automated decisionmaking rules (N44-45-R06); Colorado SB26-189 | No | The group has no business in California, and retail prices and offers are not a consequential decision category; the group does not operate in Colorado |

### 2.2 Credit decision engine (AI-002)
| Rule | What it requires | What it means for the model |
|---|---|---|
| ECOA and Reg B, 12 CFR 1002.4(a) | A creditor shall not discriminate against an applicant on a prohibited basis regarding any aspect of a credit transaction | Inputs and outcomes are tested for disparities; any input that could act as a proxy for a prohibited basis must be justified, and less discriminatory alternatives considered |
| Reg B, 12 CFR 1002.9(b)(2) | The statement of reasons for adverse action must be specific and give the principal reasons; saying the applicant failed the creditor's scoring system is not enough | Reason codes must come from the model's actual main factors for that applicant. **Gap:** 11 of 120 sampled notices gave a first reason that did not match the main model factor after the 2026 retraining (P03 FS-G37; POAM-021) |
| FCRA, 15 U.S.C. 1681m(a) | Adverse action based in whole or in part on a consumer report requires the notices the statute lists | Notices for model declines that use consumer report data are generated with the required disclosures (P03: met) |
| FTC Safeguards Rule, 16 CFR 314.4 (N44-45-R03) | Customer information protected by the information security program | Training data and model outputs stay in Financial Services accounts; access by role |

### 2.3 Other division use cases
| Rule | Use cases | Implication |
|---|---|---|
| FTC Act Section 5 unfairness, with lessons from the FTC Rite Aid facial recognition order (Docket 2023190) | AI-005 | Flags are about transactions, not people. An alert alone never leads to stopping, detaining, or banning a customer. No facial recognition (group rule) |
| FTC Act Section 5 deception; Reg Z, 12 CFR 1026.13 | AI-006 | The assistant is disclosed as AI. Billing disputes and fraud reports always go to an agent, so Reg Z billing error rights are handled by trained staff (P01 FS-015). Prompt injection is tested before each release (P01 RT-028) |
| Red Flags Rule, 16 CFR 681.1 | AI-003 | Fraud scores are part of detecting Red Flags; thresholds are reviewed when fraud patterns change (P03 FS-G28) |
| Workforce rules | AI-007 | Productivity metrics are never the sole basis for discipline (P01 WD-015). Using them for automated discipline would re-tier the use case to High (Employment) |

## 3. Risk tiers (repository rubric)
- **High:** AI-002. It makes or is a substantial factor in credit decisions.
- **Medium:** AI-001, AI-003, AI-005, AI-006, AI-007, AI-008. They influence business decisions or interact directly with customers, but a human makes the final decision affecting individuals, or the outcome is not a consequential decision.
- **Low:** AI-004 and AI-009. Internal use with no decisions about individuals and no regulated data.

**Why AI-001 is Medium but a priority:** it does not make a consequential decision about a person, and prices stay inside bounds the company sets. But it affects what millions of shoppers pay, it uses affiliate card data, and it can change shelf prices in 120 stores within minutes. The council therefore reviews it like a High-tier use case.

**Re-tier triggers:**
- AI-001: individualized prices based on a shopper's profile; any input that identifies or infers a protected characteristic or tender type; bounds wider than approved; shelf labels in more stores.
- AI-005: any form of identification of individuals (prohibited).
- AI-006: letting the assistant resolve disputes or make account decisions.
- AI-007: automated discipline or termination decisions.
- AI-008: changing credit terms, fees, or hardship eligibility (would become a credit decision).

## 4. MEASURE
Results are from the council's assessment (2026-08-17 to 2026-08-28) and monitoring data from 2026-05 to 2026-08.

### 4.1 Pricing and offers engine (AI-001)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Daily exception report: prices outside bounds or below the cost floor (target 0); audit of 4,000 shelf label prices against the register | 0 prices outside bounds; 12 shelf labels showed a lower price than the register charged (price file timing) | **No.** Automated shelf label and register comparison needed (P01 RT-025) |
| Safe | Emergency price freeze: no increase above the 30-day pre-declaration average in a declared emergency area | No freeze exists. A replay of the engine against demand data from the 2025 hurricane season showed online prices for bottled water and batteries rising up to 9% in affected counties | **No** (P01 RT-015) |
| Secure and resilient | Vendor admin access through group single sign-on with MFA; vendor SOC 2 Type 2; data use terms | MFA and SOC 2 in place; the contract does not prohibit training shared models on group data | Partial |
| Accountable and transparent | Website and app explain that online prices can differ from shelf prices and that offers are chosen from purchase history and, for cardholders, card activity | Online price difference disclosed; card data use described inaccurately for opted-out cardholders (P03 G-069) | **No** |
| Explainable and interpretable | Vendor factor report for each price and offer | Available for prices; partial for offers | Partial |
| Privacy-enhanced | Opted-out cardholders excluded from card-derived offers; exception recorded per campaign; pseudonymous member IDs to the vendor | About 41,000 opted-out cardholders not suppressed; no exception records; member IDs pseudonymous | **No** (POAM-012) |
| Fair, with harmful bias managed | See the bias testing plan below | One price disparity and one input problem flagged | **No.** Two flags |

**Bias and fairness testing plan (AI-001).** The group holds no race, ethnicity, or sex data for shoppers and will not infer it. It compares **geography and tender**, which can act as proxies for income and protected groups.

| Metric | How measured | Flag when (company-defined screening rule, not a legal standard) |
|---|---|---|
| Price index by store income group | Average engine price divided by base price, over the same 300-item basket, for the 120 shelf label stores and online delivery areas grouped into income terciles using public Census median household income | Any tercile more than 1.0 point above the highest-income tercile |
| Offer value ratio by income group | Average weekly offer value per active member by tercile, divided by the highest tercile | Ratio below 0.80 for any group |
| High-SNAP stores | Price index for the 40 stores with the highest share of SNAP EBT sales against all other stores | More than 1.0 point higher |
| Tender neutrality | Features used by price and offer models | Any tender type feature present |

**Results:**
- **Price index:** online prices in the lowest-income tercile were **1.8 points** above the highest-income tercile. Cause: the elasticity model learned that shoppers in those delivery areas compared prices less. Flagged. The elasticity factor is capped at the store-cluster level from 2026-10-15, and the test is repeated monthly.
- **Shelf label stores:** 0.6-point spread across terciles. Pass.
- **High-SNAP stores:** 0.4 points. Pass.
- **Offer value ratio:** 0.84 for the lowest tercile. Pass, but close; watched monthly.
- **Tender neutrality:** tender type, including SNAP EBT, was a feature in the **offer** model. Shoppers who paid mostly with EBT received fewer high-value offers. Removed on 2026-08-26 as a precaution under 7 CFR 278.2(b) and POL-01 4.12, and the offer model retrained without it.

### 4.2 Credit decision engine (AI-002)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Out-of-time validation of the retrained model (default prediction) | Performance within the model risk committee's tolerance | Yes |
| Explainable (adverse action reasons) | Share of sampled decline notices whose first reason matches the model's main factor for that applicant (target 100%) | 109 of 120 (91%) | **No** (12 CFR 1002.9(b)(2); POAM-021) |
| Fair, harmful bias managed | Approval rate ratio for proxy-estimated groups (surname and geography method) against the highest-approval group; flag below 0.90 and search for less discriminatory alternatives | Lowest ratio 0.87 for one proxy group; a less discriminatory alternative search has not been run | **Flagged.** Search due 2026-12-31 |
| Accountable | Model risk committee validation and council approval of the 2026 retraining | Validation done; reason code mapping not validated; council did not exist at retraining | **No** |
| Secure and privacy-enhanced | Training data access by role; consumer report data handled under the Safeguards program | In place | Yes |

### 4.3 Other use cases
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-003 fraud scoring | Share of declined Rewards Card authorizations later confirmed legitimate (flag above 15%) | 11% | Yes |
| AI-005 self-checkout analytics | False positive rate by store (flag a store more than 10 points above the chain average) | 7 stores flagged; associate guidance on approaching customers not yet issued | **No** (P01 RT-017) |
| AI-006 assistant (AI 600-1: confabulation, information security) | Weekly sample of 200 answers for factual errors; prompt-injection red-team before release | 2.5% errors (target under 2%); red-team test of order lookup not yet run | **No** (P01 RT-028, FS-015) |
| AI-007 labor planning | Discipline cases in which productivity data was the only basis (target 0) | 0 in a sample of 40 cases | Yes |
| AI-008 collections strategy | Contacts outside cardholder contact preferences (target 0) | 0 in a sample of 500 | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** merchandising sets bounds, cost floors, and excluded items (infant formula, baby food, bottled water, and over-the-counter medicines stay at base price); reviews the daily exception report; and can freeze all engine prices to base prices in one step. **Emergency price freeze:** when a state of emergency is declared for any county with group stores or delivery, the Grocery Retail chief marketing officer (or the duty merchandising director) turns on the freeze for that area the same day; prices cannot rise above their 30-day pre-declaration average until the declaration ends. This step is added to the hurricane plan (P01 RT-026).
- **AI-002:** the model approves, declines, or refers within policy limits. Underwriters review all referrals and a monthly sample of declines. Reason codes are regression-tested at every model change before release.
- **AI-005:** an alert prompts an associate to offer help. No customer is stopped, detained, or banned on an alert alone.
- **AI-006:** disputes, fraud reports, and credit questions are handed to agents; the assistant is disclosed as AI.

**Monitoring:** monthly metrics from each owner; quarterly High-tier and priority use case report to the council and the board risk committee; P01 risks GR-04, GR-09, RT-015, RT-016, RT-017, RT-025, RT-028, FS-001, FS-006, FS-012, FS-015, WD-015.

**Incident handling:** an AI failure that overcharges customers is corrected and refunded; one that exposes customer or cardholder data follows P08 and POL-03; a vendor security incident follows the vendor notice terms and the notification matrix.

**Decommissioning:** each use case has an off switch and a fallback the BIA already covers (P05): base prices and standard weekly offers for AI-001 (BP-RT05 workaround), manual underwriting for AI-002 (BP-FS02 workaround), and agents for AI-006. AI-001 is switched off for an area if the emergency freeze cannot be applied, and offers stop if the vendor will not accept the data use amendment by 2026-11-30.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 pricing and offers engine | **Approve with conditions** (council, 2026-08-28; board risk committee informed 2026-09-10) | Emergency price freeze configured and tested by 2026-10-15; elasticity factor capped by 2026-10-15 and monthly fairness tests from 2026-10; daily opt-out feed by 2026-10-31 and exception records per campaign by 2026-12-31 (POAM-012); privacy notice and offer disclosures corrected by 2026-11-30; vendor amendment (no shared-model training, deletion at exit) by 2026-11-30; automated shelf label and register comparison by 2027-03-31; tender type never used as an input. Any new input or wider bound returns to the council |
| AI-002 credit decision engine | **Continue with conditions** | Reason codes revalidated by 2026-10-31 and corrected notices sent where required by 2026-11-30; reason code regression tests in the release gate by 2026-12-31 (POAM-021); less discriminatory alternative search by 2026-12-31; council approval required for the next retraining |
| AI-005 self-checkout analytics | **Continue with conditions** | Associate scripts and store-level false positive monitoring by 2026-12-31 (P01 RT-017) |
| AI-006 customer service assistant | **Continue; cardholder servicing limited** | Answers for cardholders limited to approved content; prompt-injection red-team before each release and by 2026-12-31; error rate under 2% before limits are lifted |
| AI-007 labor planning | **Approved** | Productivity data never the sole basis for discipline; re-assess before any automated discipline use |
| AI-003, AI-004, AI-008 | **Approved** | Standard monitoring |
| AI-009 enterprise assistant | **Approved for the pilot** | Internal and Public information only until the contract review confirms no-training and retention terms; prohibited for decisions about customers, cardholders, or employees |

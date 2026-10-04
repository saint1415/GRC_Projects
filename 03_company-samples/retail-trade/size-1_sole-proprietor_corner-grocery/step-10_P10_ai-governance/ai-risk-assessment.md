# AI Use Assessment: Consumer AI Chatbot for Prices and Offers (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (corner grocery with online and phone ordering) |
| Tier / Vertical | Sole Proprietorship / Retail Trade |
| AI use case | AI-001: a consumer generative AI chatbot (SYS-09) used since 2026-05-04 for weekly price suggestions and personalized offer emails. This is the registry use case "Dynamic pricing and personalized offers", adapted to what a corner grocery actually uses (`../00_company-facts.md` section 5) |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; AI 600-1 for generative AI risks |
| Assessor and decision | Owner, 2026-08-24; decision 2026-09-04 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
Each Monday the owner pastes the week's sales totals and the distributor's cost changes into the chatbot and asks which shelf prices to change. From May to August 2026 the owner also pasted the monthly export of online customers (about 240 names, emails, and order histories; four exports in all) and asked for a personalized offer email for each customer. The chatbot is a free consumer plan: the owner accepted click-through terms, and **training on chats was on** by default. The online store's privacy notice says customer information is **never shared**. Prices are set by hand in the POS app, so every shelf and online price is the same for every customer.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, deception, 15 U.S.C. 45(a)(1) (N44-45-R02) | **Yes** | Sharing customer data with a vendor that may train on it, while the notice says data is never shared, is a statement that does not match practice (P03 G-069). AI-drafted emails claimed "lowest prices in the neighborhood" with no price check (G-072) |
| FTC Act Section 5, unfairness, 15 U.S.C. 45(n) | **Yes** | A pricing or data practice is unfair only if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits. Neighbors who depend on delivery cannot easily shop elsewhere |
| Price gouging during a declared state of emergency, Fla. Stat. 501.160 | **Yes, during emergencies** | Food and water are commodities under the statute. A price with a gross disparity from the average price in the 30 days before the declaration is prima facie unconscionable unless the increase comes from added costs or market trends. **A tool that reacts to demand can suggest increases exactly when a hurricane emergency is declared** |
| SNAP equal treatment, 7 CFR 278.2(b) | **Yes** | SNAP benefits must be accepted for eligible foods at the same prices and on the same terms as cash purchases. Any offer or price that depends on tender would breach it |
| Fla. Stat. 501.171(2) | **Yes** | Customer exports pasted into a third-party service are electronic personal information that the store must take reasonable measures to protect |
| CCPA automated decisionmaking rules (N44-45-R06) | No | No California business; far below the thresholds |

## 3. Risk screen (repository rubric)
**Tier: Medium.** It uses customer data (until 2026-08-24) and directly affects what customers pay and are offered, but it makes no consequential decision about a person (credit, employment, housing, insurance, education, health care, government services, legal services), and the owner enters every price by hand. **Re-tier to High and re-assess** before any of these: individual prices or offers based on a customer's profile; any input that identifies tender type (for example SNAP EBT); or letting the tool change prices without the owner.

## 4. Data-sharing rules (Govern)
1. **No customer data in any AI tool** (POL-01 9.5, 6.5): no names, emails, phone numbers, addresses, order histories, or card details. Only sales totals, item data, and supplier costs.
2. Chat training turned off and the past chats with customer data deleted on 2026-08-24 (evidence: settings screenshot). The owner keeps a copy of the vendor's deletion confirmation if one is offered.
3. Offers go to all online customers or to everyone who bought an item category, chosen by the owner from the online store's own tools, not from a profile built by the chatbot.
4. The privacy notice is rewritten to describe the providers the store actually uses (P03 G-069, due 2026-10-31).

## 5. Human review of outputs (Measure and Manage)
| Check | Rule | Result in the August review |
|---|---|---|
| Cost floor | No price below the item's delivered cost | 2 suggestions in July were below cost after a pasted cost was misread; caught by the owner by chance, now a written check |
| Weekly change cap | No item changes more than 10% in one week without the owner writing the reason | 6 of 31 suggestions in August exceeded 10%; all were for produce after cost increases |
| Emergency freeze | During a declared state of emergency, no price increase unless the store's own cost rose, and no AI suggestions used | No rule existed; the 2026 hurricane season had no declaration affecting the store before this review |
| Same terms for every tender | Prices and offers never depend on how the customer pays | Met: prices are set per item in the POS app; the chatbot never received tender data |
| Claims | No comparative or savings claim without a dated price check on file | 3 emails in June and July said "lowest prices in the neighborhood" with no check |

The owner reads every email before it is sent and keeps a list of the week's accepted price changes with the reason for any change above 10%.

## 6. Decision: continue with conditions (approved 2026-09-04)
**Continue** using the chatbot for price suggestions and generic offer copy **without customer data**, with the checks in section 5 (P01 R-008 and R-009, due 2026-09-30). **Stop** personalized offers built from customer order histories. Before the next hurricane season (by 2027-05-31), write the emergency freeze steps onto the hurricane sheet (POL-01 11.3). Re-run this assessment before moving to a paid business plan or a pricing feature that changes prices automatically.

**Related use case (AI-002):** the POS app's reorder suggestions use no customer data and the owner approves every order. Tier Low; no further action.

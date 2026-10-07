# AI Use Assessment: Generative AI Assistant for Demand Forecasting (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (IT hardware reseller) |
| Tier / Vertical | Sole Proprietorship / Wholesale Trade |
| AI use case | AI-001: demand forecasting and reorder suggestions with a consumer generative AI assistant (SYS-10), used since 2026-01. AI-002: drafting customer emails with the same tool |
| Why not the registry default | The registry's "demand forecasting and automated reordering" assumes an ERP add-on. This business has none, and no order is placed automatically: the owner pastes sales history into a general-purpose assistant and places every order by hand |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 for generative AI risks |
| Assessor and decision | Owner, 2026-08-28; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases, 1 tool) |

## 1. What it does (Map)
Twice in 2026 (May and July) the owner exported 18 months of sales history from the accounting SaaS (about 900 lines) and pasted it into the assistant to forecast the next 2 months for the 20 stocked SKUs and draft a reorder list. The export included customer names and **52 DoD order lines with asset tag ranges and building names, which are FCI.** The owner's plan is the consumer individual tier, where chats are used for model training unless the user turns that off; it was on. The assistant once recommended a marketplace seller for an end-of-life optic and once gave a compatible-optic part number that does not exist.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| FAR 52.204-21(b)(1)(iii) | **Yes** | The assistant is an external information system; FCI may go there only if the business verifies and controls that use. It did not (P03 G-003) |
| DFARS 252.204-7021(d)(2) | **Yes, from the new task order** | FCI may be processed only on systems with the required CMMC status. The assistant is outside the Level 1 scope the owner will affirm (P03 G-020) |
| FTC Act Section 5 | **Yes, for AI-002** | Product claims drafted by the assistant (compatibility, "new and genuine", warranty) must be true when the owner sends them |
| State AI and automated decision laws | No | No decision about a person; the business operates only in Florida. The repository rubric's consequential-decision categories do not apply |

## 3. Risk screen (repository rubric)
**AI-001: Medium.** It influences purchasing decisions worth about $3,000 a month, but a human makes every decision and no individual is affected. **AI-002: Low.** Internal drafting with no Restricted data. The P01 risk for the data exposure is R-006 (Moderate); the supply chain risk the assistant can raise is part of R-001 (High).

**Generative AI risks (AI 600-1) that matter here:** information security and data privacy (vendor keeps and trains on pasted data), confabulation (invented part numbers and suppliers), and value chain (consumer terms the owner cannot negotiate).

## 4. Data-sharing rules (Govern)
1. Turn chat training off now; delete the two chats that hold DoD lines; move to a business plan whose terms exclude training on customer data by 2026-09-30 (POL-01 9.5).
2. Before any upload: export SKU, quantity, and date only. Remove customer names, prices, prime order numbers, asset tags, and building names. DoD lines are removed entirely.
3. No Restricted data (POL-01 8.1) ever goes to the assistant, under any plan.

## 5. Human review of outputs (Measure and Manage)
- **Accuracy check.** For the 20 SKUs forecast in May, actual June and July sales differed from the forecast by a weighted average of 31%, against 26% for the owner's simple 3-month average. **The assistant was not better than the baseline.** The owner will compare both every month; if the assistant is worse 3 months in a row, it stops being used for forecasting.
- **Every reorder line** is checked against stock on hand and open orders in SYS-01 before the owner places it by hand. No automatic ordering will be enabled.
- **Suppliers and part numbers.** An AI suggestion never chooses the supplier: the POL-01 6.1 sourcing rule does. Every part number is checked in the distributor or OEM catalog.
- **Fairness testing:** not needed. No decision is made about people.
- **Incidents:** a data exposure or a wrong order caused by the assistant is logged under POL-01 10.2.

## 6. Decision: approve AI-001 with conditions; continue AI-002 (approved 2026-08-31)
AI-001 may continue only after data-sharing rules 1 and 2 in section 4 are in place (by 2026-09-30, POAM-003). Until then the owner forecasts with the 3-month average. AI-002 continues with no customer names, prices, or FCI. The owner re-runs this assessment if the tool, its terms, or its use changes, and at each August review.

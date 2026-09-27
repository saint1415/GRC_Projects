# AI Risk Assessment: Demand Forecasting and Automated Reordering

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (IT hardware and software wholesale distributor) |
| Tier / Vertical | Small / Wholesale Trade |
| AI use cases | AI-001: demand forecasting and automated reordering (SYS-12), pilot since 2026-03. AI-002: general-purpose generative AI used by staff |
| Framework | NIST AI RMF 1.0 (AI 100-1); Generative AI Profile (AI 600-1) for AI-002 |
| Assessor / date | Sales Operations Manager and IT Manager, with the Purchasing and Supplier Manager and Government Contracts Manager, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owners:** Sales Operations Manager for AI-001 (with the Purchasing and Supplier Manager for supplier selection); IT Manager for AI-002.
- **Decision authority:** Chief Operating Officer for Medium and Low tiers. The Chief Executive Officer decides if a use case is re-tiered High.
- **Policies that apply:**
  - POL-04 4.2 and 4.10: no CUI in any AI tool; FCI and Confidential data only in tools approved for that level
  - POL-04 4.7: FCI only to vendors bound by FAR 52.204-21
  - POL-05 4.10: approved generative AI tools only; check all output
  - POL-01 4.12 and 4.13: sourcing order and Section 889 screening apply to every purchase order, including suggested ones
  - POL-01 4.9: service provider security review before a vendor receives FCI
- **Approved-tools list:** kept by the IT Manager. It lists the forecasting add-on (AI-001, no CUI, no FCI after 2026-10-31) and one enterprise generative AI assistant (AI-002, Internal and Confidential data only).
- **Scale for a Small company:** there is no AI committee. The Chief Operating Officer, IT Manager, Sales Operations Manager, and Purchasing and Supplier Manager review AI use cases quarterly, with the risk register (R-026 to R-029).

## 2. MAP
### AI-001 Demand forecasting and automated reordering
| Item | Description |
|---|---|
| Purpose and intended use | Forecast weekly demand for about 14,000 active SKUs and suggest purchase orders (quantity, date, and supplier) so buyers keep fill rates high without overstock |
| Users / operators | 6 purchasing staff; the Sales Operations Manager tunes the settings |
| Affected parties | Resellers (fill rates and back orders), suppliers (order volumes), DoD primes (availability for their orders). No decisions are made about individual people |
| Data | Inputs: 3 years of ERP order history, **including DoD orders (FCI)**; reseller account identifiers; inventory; supplier lead times and prices; the supplier list, **including the 12 brokers**. Outputs: forecasts and suggested purchase orders. The vendor trains a model per customer on this data; its standard terms also allow use of customer data "to improve the service" |
| Build or buy | Buy: vendor SaaS add-on connected to the ERP (SYS-12) |
| Not intended | Automatic release of purchase orders (feature available but **disabled**), customer pricing, allocation of scarce stock among customers, and DoD job sourcing. Enabling any of these requires re-assessment |

### AI-002 General-purpose generative AI
| Item | Description |
|---|---|
| Purpose and intended use | Draft emails, catalog descriptions, and summaries of OEM spec sheets; help IT write scripts |
| Users | Any employee after training; lab workstations excluded |
| Data | Internal and Confidential data only. **CUI and FCI are prohibited.** Staff pasted customer pricing into a public chatbot at least twice in 2026 (found by interview, R-028) |
| Build or buy | Buy: one enterprise assistant with commercial terms that exclude training on company data, SSO, and admin logging |
| Not intended | Customer-facing chat, contract language, security configurations for CUI systems |

### Applicable laws and rules
| Rule | Applies? | Why |
|---|---|---|
| FAR 52.204-21 and CMMC Level 1 (N42-R04, N42-R02) | **Yes** for AI-001 | The vendor's system processes FCI from DoD orders on the company's behalf, under terms with none of the 15 safeguarding requirements. Fix: remove DoD orders from the feed by 2026-10-31, or add the safeguards to the contract (R-029) |
| FAR 52.204-25 (N42-R05) and DFARS 252.246-7008 | **Yes** for AI-001 | Suggested purchase orders pick suppliers by price and lead time. In the pilot, 38 of 1,420 suggested lines named a broker, 2 of them the broker later found supplying white-label covered SKUs (R-035). The sourcing order and covered-manufacturer block must apply to suggestions (R-027) |
| DFARS 252.204-7012 and SP 800-171 (N42-R03) | **Yes** for AI-002 | CUI must never enter an AI tool (POL-04 4.10). No tool is approved for CUI, and public chatbots are blocked on lab workstations |
| FTC Act Section 5 (N42-R01) | Indirectly | Applies to the vendor's accuracy claims (keep the claims relied on in the procurement file) and to the company's own product claims. AI-drafted catalog text must be checked against OEM spec sheets so it does not misstate specifications or compatibility |
| State AI laws reviewed in `00_universal-framework/cross-sector/` (for example Colorado SB26-189, Texas TRAIGA) | No | Neither use case makes or influences consequential decisions about individuals, and neither uses AI in a way those laws prohibit |
| CCPA/CPRA automated decision-making rules (N42-R08) | No | The company has no California business (`../00_company-facts.md` section 1) |

## 3. Risk tier
**AI-001 tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`). It influences business decisions but a buyer makes every purchase decision, and it makes no decision about an individual.

**Why it is not Low:** its supplier suggestions can route orders to brokers or covered manufacturers, it processes FCI, and forecast errors change service levels for small resellers.

**Escalation triggers (re-assess before any of these):**
- enabling automatic release of purchase orders
- using suggestions for DoD jobs or Prime B configuration stock
- allocating scarce stock among customers, or setting customer prices
- adding new data about individuals (for example reseller staff behavior)

**AI-002 tier: Low** with the approved enterprise tool and the data rules; **High** if CUI or FCI were entered, which is why that is prohibited and blocked.

## 4. MEASURE
Pilot period 2026-03 to 2026-08, AI-001 unless noted.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Weighted absolute percentage error (WAPE) at a 4-week horizon for A-class SKUs (top 20% of revenue); threshold 30% overall and for each product line | Overall 24%; network switching 19%; **video surveillance 41%** | **No.** One product line fails |
| Safe (supply chain integrity) | Share of suggested purchase order lines that name a supplier outside the approved authorized sources; threshold 0% | 38 of 1,420 lines (2.7%) named a broker; 2 named the broker in R-035 | **No** |
| Secure and resilient | SSO with MFA; vendor security evidence | 4 local accounts without MFA; vendor provided no SOC 2 report, only a security questionnaire | **No** |
| Accountable and transparent | Buyer approval and override reason recorded for every suggested order | Approvals recorded in the ERP; override reasons not captured | Partial |
| Explainable and interpretable | Buyer can see the drivers of each forecast (trend, seasonality, promotions, lead time) | Available on the SKU detail screen; buyers use it | Yes |
| Privacy-enhanced (data protection) | No FCI in the feed; no vendor use of company data beyond the company's own model | DoD orders in the feed; vendor terms allow use of data to improve the service | **No** |
| Fair, with harmful bias managed | Compare forecast bias (mean percentage error) and fill rate across customer segments: top-20 resellers, small resellers (under $250,000 a year), DoD primes. Flag if a segment's forecast bias is beyond plus or minus 10%, or its fill rate is more than 3 points below the best segment | Small-reseller-heavy SKUs under-forecast by 14%; fill rate 91% for small resellers vs 97% for top-20 resellers; DoD primes 95% | **No.** Disparity flagged |

**Bias finding.** The model learns from order volume, so SKUs bought mostly by small resellers (niche accessories, older models) are under-forecast and stock out more often. Small resellers are served worse even though the company's commercial terms treat them the same. Fix: a minimum safety-stock rule for SKUs with sparse history, and monthly fill-rate reporting by segment. Target: gap of 3 points or less by 2026-12-31.

**AI-002 checks (AI 600-1 risks: confabulation, information security, data privacy, intellectual property):** 20 AI-drafted catalog descriptions were compared with OEM spec sheets; 3 contained an incorrect specification (for example a wrong port count). Rule added: every AI-drafted product claim is checked against the OEM spec sheet before publishing.

## 5. MANAGE
**Human-in-the-loop design (AI-001):**
- Auto-release stays **disabled**. A buyer reviews and approves every suggested purchase order.
- Suggestions are limited to suppliers on the approved list flagged as authorized sources; brokers are removed from the supplier pool the tool can pick.
- The covered-manufacturer hard block in the ERP (POAM-012) also applies to suggested orders.
- Buyers must enter an override reason when they change a suggested quantity or supplier by more than 20%.

**Monitoring:**
- Monthly report to the Sales Operations Manager: WAPE by product line, forecast bias and fill rate by customer segment, and supplier-rule violations (target 0).
- Quarterly review by the Chief Operating Officer, tracked in the risk register (R-026, R-027).
- Data drift check after major events (new product lines, supplier allocations, price changes).

**Data protection:**
- DoD orders removed from the ERP feed by 2026-10-31 (R-029).
- Contract amendment at the next renewal: no use of company data beyond the company's own model, deletion on exit, and incident notice.
- SSO with MFA for the add-on by 2026-11-30.

**Incident handling:**
- A suggested order to a broker or covered manufacturer that reaches a buyer is a supply chain incident and follows P08.
- A vendor security incident follows P08 and the vendor's notice terms.

**Decommissioning:** stop using suggestions and revert to the ERP reorder report if WAPE exceeds 40% for two months in a row, if any suggested order to a blocked supplier is released, or if the vendor changes its data-use terms.

**AI-002 controls:**
- Enterprise assistant only, from 2026-10-01; public chatbots blocked on lab workstations and discouraged elsewhere by the web filter warning page.
- Training on the data rules (POL-05 4.10) before access.
- No CUI or FCI, ever. Confidential data only in the enterprise assistant.

## 6. Decision
**Approve with conditions.** Chief Operating Officer, 2026-08-31.

AI-001 may continue as a buyer-approved tool **only if** these conditions are met:
1. Auto-release stays disabled until a re-assessment approves it.
2. Suggestions are restricted to approved authorized sources, with the covered-manufacturer block in place, by 2026-11-30.
3. DoD orders are removed from the feed by 2026-10-31.
4. SSO with MFA is in place by 2026-11-30.
5. The small-reseller fill-rate gap is 3 points or less by 2026-12-31.

Auto-release may be reconsidered only after three consecutive months that meet every threshold in section 4.

AI-002 is approved for the enterprise assistant with the data rules above, effective 2026-10-01.

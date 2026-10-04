# AI Risk Assessment: Demand Forecasting and Automated Reordering

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (IT hardware and software reseller) |
| Tier / Vertical | Micro / Wholesale Trade |
| AI use case | AI-001: the ERP's AI reorder feature (SYS-10), in use since 2026-05 |
| Framework | NIST AI RMF 1.0 (AI 100-1); Generative AI Profile (AI 600-1) for the staff assistant (AI-002) |
| Assessor / date | Operations Manager with the Purchasing and Inventory Coordinator and the Federal Account Manager, 2026-08-25 |
| Decision | Owner, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the Purchasing and Inventory Coordinator, who uses the feature. **Decision authority:** the Owner.
- **Policies that apply:**
  - POL-04 4.9: no FCI in any AI tool; the reorder feature is approved only with DoD orders excluded and the conditions in section 6.
  - POL-02 A.7: a vendor (here, the ERP vendor's AI subprocessor) may not receive FCI until approved with terms that limit its use of company data.
  - POL-02 A.8 and A.9: the sourcing order and Section 889 screening apply to every purchase order, including suggested and auto-submitted ones.
  - POL-02 C.2: no FCI or customer data in public AI chatbots (AI-003).
- **Approved-tools list:** kept by the Operations Manager in POL-04 4.9: the reorder feature (with conditions) and one business AI assistant for Internal and Public information (AI-002).
- **Scale for a Micro company:** there is no AI committee. The Owner, the Operations Manager, and the Purchasing and Inventory Coordinator review AI use at the monthly security meeting, using the P01 risk method (R-020 to R-022).

**How the feature started.** The ERP vendor added the feature in 2026-05 as an opt-in. The Purchasing and Inventory Coordinator turned it on, with auto-submit for accessory orders under $500 to the two national distributors. Nobody read the subprocessor terms or noticed that DoD order history would be sent to an outside AI service. That broke the rule now written in POL-02 A.7.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Forecast weekly demand for about 2,300 active SKUs and suggest purchase orders (quantity, date, and supplier) so the company stocks fast-moving items without tying up cash |
| Users | The Purchasing and Inventory Coordinator; the Owner as backup |
| Affected parties | Customers (how fast orders ship), suppliers (order volumes), and the company's cash. No decisions are made about individual people |
| Data | Inputs: 2 years of ERP order history, **including DoD order lines and ship-to sites**; customer account IDs; stock levels; supplier prices and lead times; purchase history including the 4 brokers. Equipment list attachments are not sent. Outputs: forecasts and suggested purchase orders. The ERP vendor's system description allows de-identified customer data to be used to improve features (P09) |
| Build or buy | Configure: a feature of the SaaS ERP; the model runs at a third-party AI service listed by the ERP vendor as a subprocessor |
| Not intended | Pricing, allocation of scarce stock among customers, DoD order sourcing, and auto-submit to any supplier other than the two national distributors. Enabling any of these requires re-assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FAR 52.204-21 and CMMC Level 1 (N42-R04, N42-R02) | **Yes** | DoD order lines and ship-to sites are FCI. Sending them to the AI subprocessor uses an external system that is not verified or limited (52.204-21(b)(1)(iii)) and puts FCI outside the assessed scope (252.204-7021(d)(2)). Fix: exclude DoD orders from the feed, or obtain written terms (R-021) |
| FAR 52.204-25 (N42-R05) and DFARS 252.246-7008 | **Yes** | Suggestions pick the supplier from purchase history. In the pilot, 12 of 410 suggested lines named a broker. The sourcing order and covered-manufacturer block must apply to suggestions |
| FTC Act Section 5 (N42-R01) | Indirectly | Keep the vendor's accuracy claims that the company relied on. For AI-002, AI-drafted product descriptions must not misstate specifications |
| Fla. Stat. 501.171(2) | Not for AI-001 | The feed carries no personal information as Florida defines it. AI-003 could, if staff paste customer contacts with credentials, so it is prohibited |
| State AI laws in `00_universal-framework/cross-sector/` (for example Colorado SB26-189) | No | Neither use case makes or influences a consequential decision about an individual, and the company operates only in Florida |

## 3. Risk tier
**AI-001 tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why not High:** it makes no decision about a person and cannot affect physical safety or critical infrastructure operations.
- **Why not Low:** it influences purchasing decisions, it sent FCI to an outside service, and, with auto-submit on, it placed orders with no human review.

**Re-assess before any of these:** turning auto-submit back on; letting it suggest suppliers for DoD orders; letting it choose brokers; using it for pricing or allocation; adding data about individual people.

**AI-002 tier: Low** with the approved assistant and the data rules. **AI-003 is High** if FCI or customer data were entered, which is why it is prohibited.

## 4. MEASURE
Pilot period 2026-05-01 to 2026-08-21, AI-001 unless noted.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Weighted absolute percentage error (WAPE) at a 4-week horizon for A-class SKUs (top 20% of revenue); threshold 30% overall and for each product category | Overall 27%; laptops and docks 22%; **networking 38%** (lumpy project orders) | **No.** One category fails |
| Safe (supply chain integrity) | Share of suggested lines naming a supplier that is not an authorized source; threshold 0% | 12 of 410 suggested lines (2.9%) named a broker; auto-submit used only the two authorized distributors | **No** |
| Safe (spending control) | Auto-submitted orders later found unnecessary; threshold under 5% of auto-submitted orders | 46 orders auto-submitted ($14,900); 7 (15%) were excess, costing $380 in restocking fees | **No** |
| Secure and resilient | MFA on the feature; vendor security evidence | Uses ERP sign-in with MFA; ERP SOC 2 report covers the feature, but the AI service is a carved-out subservice organization | Partial |
| Accountable and transparent | Buyer approval and override reason recorded for every suggested order | Approvals recorded for manual orders only; no override reasons; auto-submitted orders had no approver | **No** |
| Explainable and interpretable | Buyer can see the drivers of each forecast (trend, seasonality, lead time) | Available on the SKU screen | Yes |
| Privacy-enhanced (data protection) | No FCI to the AI service; vendor may not reuse company data | DoD order lines in the feed; vendor terms allow de-identified reuse | **No** |
| Fair, with harmful bias managed | Compare fill rate (orders shipped complete within 2 business days) across customer segments: DoD orders, small commercial accounts (under $10,000 a year), and large commercial accounts. Flag if any segment is more than 3 points below the best | DoD 94%; small commercial 89%; large commercial 95% | **No.** Small accounts flagged |

**Bias finding.** The model learns from volume, so items bought mostly by small accounts (older adapters, niche cables) are under-forecast and stock out more often. Small customers get slower service although the company's terms treat them the same. Fix: a minimum stock rule for SKUs with sparse history and monthly fill-rate reporting by segment. Target: gap of 3 points or less by 2026-12-31.

**AI-002 checks (AI 600-1 risks: confabulation, information security, intellectual property):** 15 AI-drafted quote descriptions were compared with OEM spec sheets; 2 had a wrong specification (a port count and a warranty term). Rule: every AI-drafted product claim is checked against the OEM spec sheet before it goes to a customer.

## 5. MANAGE
**Human in the loop (AI-001):**
- Auto-submit was turned **off** on 2026-08-25. A buyer reviews and approves every suggested order.
- Suggestions are limited to authorized sources; brokers are removed from the supplier pool the feature can pick.
- SKUs without a manufacturer of record, or on the Section 889 screening list, are excluded from suggestions (POAM-012).
- Buyers enter an override reason when they change a suggested quantity or supplier by more than 20%.

**Data protection:**
- DoD orders excluded from the feed by 2026-10-31 (ERP setting by order type), unless the ERP vendor first gives written terms that the AI service does not keep or reuse company data (R-021).
- Ask the ERP vendor to confirm deletion of DoD order history already sent.

**Monitoring:**
- Monthly report to the Owner: WAPE by category, fill rate by customer segment, and supplier-rule violations (target 0).
- Quarterly entry in the risk register (R-020, R-021).

**Incident handling:** a suggested order to a broker or a covered manufacturer that reaches a buyer is a supply chain event and follows P08. A vendor security incident follows POL-03 and the vendor's notice terms.

**Decommissioning:** stop using suggestions and return to the ERP's standard reorder report if WAPE exceeds 40% for two months in a row, if any order to a blocked supplier is released, or if the vendor changes its data-use terms.

**AI-002 and AI-003 controls:** the business assistant only, from 2026-10-01; training on POL-04 4.9 before access; public chatbots never receive Restricted or Internal information (R-022).

## 6. Decision
**Approve with conditions.** Owner, 2026-08-31.

AI-001 may continue as a buyer-approved tool **only if**:
1. Auto-submit stays off until a re-assessment approves it (off since 2026-08-25).
2. DoD orders are excluded from the feed, or written vendor terms are in place, by 2026-10-31.
3. Suggestions are restricted to authorized sources, with the Section 889 screening applied, by 2026-10-31.
4. The small-account fill-rate gap is 3 points or less by 2026-12-31.

Auto-submit may be reconsidered only after three consecutive months that meet every threshold in section 4, and then only for authorized distributors and orders under $500.

AI-002 is approved for the business assistant with the data rules above, effective 2026-10-01. AI-003 stays prohibited.

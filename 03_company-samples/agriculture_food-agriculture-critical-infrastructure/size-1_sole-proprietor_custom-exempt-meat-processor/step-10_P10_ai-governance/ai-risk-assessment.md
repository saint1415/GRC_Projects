# AI Use Assessment: Public Generative AI Chatbot for Cure Calculations (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (custom-exempt meat processing shop) |
| Tier / Vertical | Sole Proprietorship / Food and Agriculture |
| AI use case | AI-001: a public generative AI chatbot (SYS-10, free consumer account) used since January 2026, about 30 times, mostly to scale cure and brine amounts to customer batch weights, and to draft customer texts |
| Why this use case | Adapted from the registry default (AI quality inspection on processing lines): a one-person shop has no camera inspection line. The chatbot is the AI tool the owner actually uses, and its answers bear directly on a binding ingredient rule |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 for generative AI risks (confabulation; data privacy) |
| Assessor and decision | Owner-operator, 2026-07-30; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases; AI-002 is the cold-chain vendor's anomaly alert feature, Low tier) |

## 1. What it does (Map)
The owner types a recipe and a batch weight (for example, "brine for 40 lb of ham at 10 percent pump") and the chatbot answers with scaled amounts of salt, sugar, and cure. The owner also asks it to draft texts telling customers their order is ready, sometimes with the customer's first name and pickup time. The chatbot is a general-purpose consumer product. Its terms allow the vendor to use inputs to improve its service, and the owner never turned off the training setting. Nothing the chatbot says is checked by the vendor for food safety.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| 9 CFR 424.21(c), through 303.1(b)(1) | **Yes** | Custom products must be prepared under 424.21, which lists the curing agents and their limits (for nitrite, for example: 2 lb to 100 gal pickle at 10 percent pump level; 1 oz to 100 lb meat in a dry cure; 1/4 oz to 100 lb chopped meat). A cure amount above the chart is an ingredient violation and a safety hazard, whoever calculated it |
| Fla. Stat. 501.171(2) | **Yes, if customer data is entered** | The shop treats its customer records as personal information (P03 section 1.2). First names with pickup times are low-risk, but the rule in section 4 keeps all customer details out |
| State AI laws on consequential decisions | No | The chatbot makes no decision about a person (employment, credit, housing, insurance, education, health care, government services, legal services) |

## 3. Risk screen (repository rubric)
**Tier: High** as used until 2026-07-30, because the rubric puts any AI that "can affect physical safety" in the High tier, and a cure amount does. On 2026-07-30 the owner re-checked 12 saved chatbot answers against the cure supplier's printed chart: 11 matched; **1 (a brine for 40 lb of ham) gave a cure amount about 25% above the chart.** The owner had noticed at the time that it looked high and used the chart value, so no batch was affected. This is the generative AI risk NIST AI 600-1 calls confabulation: a confident, wrong number.

**After the restriction in section 6, the remaining use (drafting texts with no customer details) is Low tier:** internal productivity, no decisions about people, no regulated data.

## 4. Data-sharing rules (Govern)
1. No customer names, addresses, phone numbers, or emails go into any AI tool (POL-01 9.5). Drafts use placeholders the owner fills in on the phone.
2. Turn off the setting that lets the vendor use inputs for training, where offered; if it cannot be turned off, treat everything typed as public.
3. Recipes and formulations may be entered only if the owner is comfortable with them becoming public. Customers' own family recipes are not entered.

## 5. Human review of outputs (Measure and Manage)
- **Cure and brine amounts are never taken from an AI tool.** They come only from the cure supplier's printed chart, or from a locked cure sheet on the laptop that was checked line by line against the chart and is version-controlled with the other records (POL-01 7.5).
- For each cured batch, the owner writes the cure amount and "checked against chart" on the batch sheet. That is the measurable control: a monthly look at the batch sheets shows whether every cured batch has the check.
- Drafted texts are read in full before sending.
- If an AI answer is ever found to have reached a batch, the batch is held and the P08 product-first steps apply.

## 6. Decision: restrict (approved 2026-08-31)
**Keep the chatbot for drafting texts only. Stop using it for any cure, brine, or ingredient amount.** Then (P01 R-005, R-012; POAM-006):
1. By 2026-09-15: turn off the training setting; delete saved chats that contain customer names.
2. By 2026-09-30: lock the cure sheet (protected cells), check every line against the supplier's chart, and add it to the backed-up records; start the batch-sheet check.
3. Before any new AI tool or use (for example, a vision app to grade cuts): run this assessment again first (POL-01 9.5).

**AI-002 (cold-chain anomaly alerts):** Low tier. It adds alerts but replaces none; set-point alarms still fire on their own. Keep it, and record its false alarms in the shop log for the July 2027 review.

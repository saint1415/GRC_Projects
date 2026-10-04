# AI Use Assessment: Consumer AI Assistant for Tariff Classification Research (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight forwarder and customs broker) |
| Tier / Vertical | Sole Proprietorship / Transportation and Warehousing |
| AI use case | AI-001: a consumer generative AI assistant (SYS-09, free personal account) used since 2026-03-02 to research tariff classifications and draft client emails. Replaces the registry default "Container and berth scheduling optimization", which does not fit a business that schedules no berths or containers |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; AI 600-1 for generative AI risks |
| Assessor and decision | Owner, 2026-08-27; decision 2026-09-14 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases; AI-002 is the customs software's document capture) |

## 1. What it does (Map)
The owner pastes a product description from a commercial invoice (sometimes the whole invoice) and asks which tariff heading fits, then uses the answer as a starting point. It also drafts client emails explaining duties. A review of the chat history on 2026-08-26 found 152 chats: **31 contained whole invoices** with client and supplier names and prices; none contained importer of record numbers or Social Security numbers. The account's settings allow the vendor to use chats for model training. The business has no contract with the vendor beyond consumer click-through terms.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| 19 CFR 111.24 (records confidential) | **Yes** | Invoices are client records. They may go only to the client, its surety, DHS, a court, or a party the client authorizes in writing. No client authorized an AI vendor |
| 19 CFR 111.28(a) (responsible supervision and control) | **Yes** | The licensed broker must control how customs business is done. An AI suggestion is help, not a decision |
| 19 CFR 111.39(b) (due diligence in advice) | **Yes** | The broker must make sure advice to clients, including on duties owed, is correct |
| Fla. Stat. 501.171(2) | Only if personal information is entered | The chat review found none; POL-01 forbids it |
| State laws on consequential AI decisions | No | No decision about a person's employment, credit, housing, insurance, education, health care, or government services is made |

## 3. Risk screen (repository rubric)
**Tier: Medium.** The output influences business decisions (which heading, and so which duty rate, a client pays), but the licensed broker makes the final decision and no decision is made about an individual. AI-002 (document capture) is also Medium: it handles client records and feeds draft entries, and the owner checks every line. Related risks in P01: R-007 (disclosure without client authorization, Moderate) and R-011 (misclassification, Moderate).

## 4. Measure: accuracy check (no bias test needed)
The tool makes no decisions about people, so a fairness test across groups does not apply. Accuracy does. On 2026-08-26 the owner compared 20 past AI suggestions with the classifications actually filed after research: **17 of 20** named the right 6-digit subheading, **14 of 20** the right 10-digit number, and 3 named the wrong heading, one of which carried a different duty rate. Two answers cited rulings the owner could not find. Conclusion: useful as a lead, **not reliable as an answer**.

## 5. Data-sharing rules (Govern)
1. Until the conditions in section 7 are met: **no client data** goes to the tool. Product descriptions may be used only after removing client names, supplier names, prices, and anything that identifies the shipment (POL-01 9.5).
2. No importer of record number, Social Security number, POA, bank detail, or entry number may ever be entered.
3. Use with client data only under a business plan whose terms bar training on business data and set a deletion period, and only after clients have authorized the vendor in writing (111.24; POL-01 6.1).

## 6. Human review of outputs (Manage)
- Every classification is decided by the owner from the tariff schedule, its section and chapter notes, and CBP rulings. The shipment file records the heading chosen and the notes and rulings relied on. An AI answer is never cited as a basis.
- Any ruling or citation the tool names is looked up before use; if it cannot be found, it is treated as invented.
- Client emails drafted by the tool are read in full and corrected before sending.
- Each month the owner samples 5 filed classifications that started from an AI suggestion and records whether the final basis is in the file. A wrong heading that reaches a filed entry stops AI use until the cause is understood, and the client is advised under 111.39(c).

## 7. Decision: approve with conditions (2026-09-14)
**Continue only for de-identified product descriptions now.** By 2026-10-31 (P01 R-007 and R-011; POAM-005):
1. Turn off chat history and training in the current account, and delete the 31 chats that contain whole invoices.
2. Either move to a business plan with no-training terms, or keep the tool permanently limited to de-identified descriptions.
3. Add the AI vendor to the client authorization for service providers if a business plan is adopted.
4. Re-run this assessment before any new AI use, including any AI feature the customs software vendor adds beyond AI-002.

# AI Risk Assessment: AI Document Capture and Tariff Classification Suggestions

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (freight forwarding and customs brokerage office, 7 employees) |
| Tier / Vertical | Micro / Transportation and Warehousing |
| AI use case | AI-001: the customs platform's (SYS-01) AI document capture and tariff classification suggestions, switched on by the vendor in 2026-04. It replaces the registry default "Container and berth scheduling optimization", which does not fit an office that schedules no berths or containers (see `00_company-facts.md` section 3) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1), because each suggestion comes with a generated text rationale |
| Assessor / date | Office and Compliance Manager (Security Coordinator) with the Licensed Customs Broker (Entry Supervisor), 2026-08-24 to 2026-08-27 |
| Decision | Owner and President (licensed customs broker, qualifying officer), 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |
| Related items | P01 R-011, R-012, R-013; P03 G-015, G-021, G-033; P06 POL-04 4.6 and POL-02 C.2; P07 POAM-005, POAM-009; P09 vendor SOC 2 review and CC8.1 |

## 1. GOVERN
- **Accountable owner:** the Licensed Customs Broker (Entry Supervisor), who reviews entries prepared by the Entry Writers. **Decision authority:** the Owner and President, who as the licensed officer exercises responsible supervision and control over the company's customs business (19 CFR 111.28(a)).
- **Policies that apply:**
  - POL-04 4.6: Restricted information goes only into approved AI tools. AI-001 is the only entry on the list, under the conditions in section 6. A licensed broker approves every AI classification for a product not classified before, before it is transmitted.
  - POL-04 4.5 and POL-02 A.5: no vendor, tool, or vendor-enabled feature receives client records until the Security Coordinator confirms confidentiality terms, data location, and client authorization. AI-001 was never put through this step because the vendor switched it on without notice.
  - POL-02 C.2: no client records in public AI chatbots (AI-002).
  - POL-02 A.2: the risk assessment is updated after a new AI feature. This assessment is that update for AI-001.
- **Approved-tools list:** kept by the Security Coordinator in POL-04 4.6.
- **Scale for a Micro office:** there is no AI committee. The owner, the Entry Supervisor, and the Security Coordinator review AI use at the monthly security meeting, using the monitoring results in section 5.

**How the feature started.** The vendor's April 2026 release notes announced the feature, and it went live for all customers with no opt-in. Since then each invoice uploaded to a shipment file is read by the feature, which fills in the entry lines and a suggested 10-digit tariff number. The Entry Writers began accepting the pre-filled numbers. No licensed broker review of those lines was recorded (P03 G-021, G-033), and nobody checked the vendor's terms for the new feature (P09 CC8.1).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | (1) **Document capture:** read uploaded commercial invoices and packing lists and fill in draft entry lines (description, quantity, value, currency, country of origin). (2) **Classification suggestions:** propose a 10-digit tariff number for each line, with a confidence label (high, medium, low) and a short generated rationale. Suggestions draw first on the company's own product library (products classified before for the same client), then on the vendor's model. The goal is faster entry preparation |
| Users | The 2 Entry Writers (daily) and the Entry Supervisor. The owner uses it occasionally |
| Affected people and organizations | About 150 importer clients, including about 25 individuals who import as sole proprietors. Their duty payments depend on the classification. The company and its licensed brokers carry the supervision duty. No decision is made about an individual's employment, credit, housing, insurance, education, health care, or access to government services |
| Data | Inputs: commercial invoices and packing lists (client records under 111.24), which show client and supplier names, addresses, products, and prices. Importer identification numbers and Social Security numbers are not on invoices and are not sent to the feature, according to the vendor. Outputs: draft entry lines, suggested tariff numbers, rationale text. **Not known:** whether a third-party model provider processes the documents, where that processing happens, and whether client data trains the model. The contract's confidentiality clause predates the feature and says nothing about model training |
| Build or buy | Buy: a built-in feature of the customs platform (vendor SaaS). No separate contract |
| Volume | About 1,500 entries were filed from 2026-04 to 2026-07. The platform marks each line where a suggestion was accepted and by which user; the feature was used on about 80% of lines |
| Not intended | Automatic transmission of entries without a person's action, classification rulings requests, client-facing advice, and screening of clients or employees. The vendor's "accept high-confidence suggestions automatically" setting is **off** and must stay off |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| 19 CFR 111.24 (records confidential) | **Yes** | Invoices are client records. The broker may disclose them only to the client, its surety, DHS, other authorized U.S. officers, on subpoena or court order, or when the client authorizes it in writing. The vendor already holds client records under the platform contract, but no client has authorized disclosure to an AI model provider. The client terms clause in progress (R-011, G-015, POAM-009) must name the platform vendor and any AI model provider |
| 19 CFR 111.28(a) (responsible supervision and control) | **Yes** | CBP may consider training and instructions to employees ((a)(1), (a)(2)), employee access to the current tariff schedule and CBP issuances ((a)(5)), and how often a licensed broker audits and reviews customs transactions handled by employees ((a)(8)). AI-assisted lines are employee-handled transactions; a suggestion is not a broker's review |
| 19 CFR 111.29(a) and 111.39(b), (c) | **Yes** | The broker must use due diligence in preparing customs records (111.29(a)) and in checking the correctness of advice to clients, including on duty owed (111.39(b)). If the broker learns that a client's record has an error, it must advise the client promptly and keep a record of that advice (111.39(c)). This applies to the filed lines found wrong in section 4 |
| 19 CFR 111.21(a), 111.23(a) | **Yes** | The shipment file must hold the records of the customs business, including the basis for a classification. Originals of records must be kept within the customs territory of the United States. The platform stores them in U.S. regions (P09 vendor review); the location of AI processing is unconfirmed |
| 19 CFR 111.21(b) (72-hour CBP notice) | **If a breach occurs** | A breach of records at the vendor or a model provider is a breach of records relating to the customs business. The vendor's 72-hour notice commitment leaves no time for the company's own 72-hour clock (P09); the requested 24-hour term covers the AI feature too |
| Fla. Stat. 501.171 | **Not triggered by invoice data alone** | Names and addresses without a Social Security number or other listed data element are not "personal information" under 501.171(1)(g). Applies if importer identification numbers ever reach the feature |
| State laws on consequential AI decisions (for example, Colorado SB26-189, effective 2027-01-01) | No | No consequential decision about a consumer is made. Recheck if AI is ever used to screen individual clients or employees |
| CTPAT (N48-49-R05) | Indirectly | Voluntary program. The largest CTPAT client's business partner questionnaire (due 2026-10-31, P09) asks about cybersecurity and third-party IT; the answer should describe this feature and its controls |
| USCG maritime cyber rule (N48-49-R01) | No | The company has no facility or vessel security plan (P03) |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why not High:** the feature is not a substantial factor in a consequential decision about a person in any rubric category, and it cannot affect physical safety or critical infrastructure operations. A person takes the filing action for every entry.
- **Why not Low:** it processes client records protected by 111.24, its output goes into filings with CBP, and a wrong number changes the duty a client pays. Accepting suggestions without review also weakens the broker's evidence of responsible supervision.
- **Generative AI risks (AI 600-1) that apply:** confabulation (invented ruling citations in the rationale); human-AI configuration (pre-filled numbers invite automation bias); data privacy and information security (client documents at an unnamed model provider); value chain and component integration (model provider not disclosed or covered by the SOC 2 report); harmful bias or homogenization (weaker results on non-English invoices, section 4).

**Re-tier to High and reassess if:** the automatic-acceptance setting is turned on; the feature is used to screen clients, employees, or job applicants; or AI output goes to clients as advice without broker review.

## 4. MEASURE
**Test design.** During P03 fieldwork (2026-07-28) the Entry Supervisor looked at 10 AI-assisted lines and found 2 wrong numbers, which prompted this test. On 2026-08-25 the Entry Supervisor independently re-classified a sample of **40 AI-assisted lines** from entries filed 2026-05-01 to 2026-07-31: 20 lines for products already in the company's product library and 20 for new products. Each line was classified from the tariff schedule, its notes, and CBP rulings without looking at the suggestion, then compared. Captured fields were compared with the invoice. Results are counts from the test worksheet kept in the compliance folder.

| Trustworthy characteristic | Test or metric (threshold) | Result | Pass? |
|---|---|---|---|
| Valid and reliable: classification | Correct 10-digit number. Repeat products: at least 95%. New products: at least 90% | Repeat products: 20 of 20 (100%). New products: 13 of 20 (65%); 3 of the 7 errors were in the wrong heading. Overall 33 of 40 (82.5%) | **No** (new products) |
| Valid and reliable: capture | Field error rate on description, quantity, value, and origin under 2% of fields | 5 errors in 160 fields (3.1%), in 5 of 40 lines: 2 quantities (both filed), 1 value (a European number format read with the decimal in the wrong place, caught by the invoice total check), 2 countries of origin (the shipper's country taken as origin, both filed) | **No** |
| Safe | Errors caught before filing | 6 of the 7 wrong numbers were filed as suggested; 1 was changed by the Entry Writer. 4 of the 6 filed lines carried a different duty rate: 2 underpaid (about $1,240 in total) and 2 overpaid (about $380). Both origin errors and both quantity errors were filed | **No** |
| Secure and resilient | Feature covered by vendor assurance; MFA; U.S. processing | Platform SOC 2 Type 2 covers the platform, not the AI feature; no model provider listed (P09). MFA enforced on the platform. Processing location unconfirmed | Partial |
| Accountable and transparent | Each accepted suggestion attributed to a user; broker approval recorded; clients told AI is used | Platform logs the accepting user. No broker approval recorded. Clients not told | **No** |
| Explainable and interpretable | Rationale lets a broker check the suggestion; confidence label is meaningful | 4 of the 7 wrong suggestions were labeled "high" confidence. Of 6 rationales that cited a CBP ruling, 2 rulings could not be found in CBP's rulings database and 1 covered a different product | **No** (confabulation) |
| Privacy-enhanced | Written terms: no training on client data, deletion period, U.S. processing, subprocessors named | None in writing. Vendor support said by email on 2026-08-26 that "aggregated customer data" improves suggestions; asked for details | **No** |
| Fair, with harmful bias managed | Compare the new-product error rate for English invoices with invoices in other languages (Spanish, Portuguese, Chinese); flag a gap over 10 percentage points | English: 2 of 10 new-product lines wrong (20%). Other languages: 5 of 10 (50%). Gap 30 points, **flagged**. 4 of the 5 capture errors were also on non-English invoices | **No (flagged)** |

**Bias finding.** The feature does not decide anything about a person, so the fairness test looks at whether some clients get worse results. Clients who buy from Latin American and Asian suppliers, many of them the smaller importers, get more wrong suggestions. The sample is small (10 lines per group), so the company treats the gap as real until the vendor gives accuracy data by invoice language. Until then, every AI-assisted line on a non-English invoice gets broker review, not only new products.

**What the numbers say.** The feature is reliable where it reuses the company's own past classifications and unreliable on new products and non-English invoices. Its confidence label and rationale do not tell good suggestions from bad ones. The real failure is not the model. It is that suggestions were pre-filled and accepted with no broker in the loop.

## 5. MANAGE
**Human in the loop (in place by 2026-09-15):**
- The Entry Supervisor turns on the platform setting that holds any line without a product-library match until a user with the broker role approves it. The vendor confirmed on 2026-08-26 that the setting exists. Only the owner and the Entry Supervisor have the broker role.
- For new products and for every line on a non-English invoice, the broker classifies from the tariff schedule, its notes, and CBP rulings, and records the heading chosen and the basis in the shipment file. An AI rationale is never the recorded basis. A ruling the feature cites is looked up before use; if it cannot be found, it is treated as invented.
- Entry Writers check captured quantity, value, currency, and country of origin against the invoice on every line, as they did before the feature.
- Overrides: a broker can reject a suggestion at any time. A rejected suggestion is noted in the line comment so it shows in the monthly report.

**Correcting the filed errors (by 2026-09-30):** the Entry Supervisor re-checks every AI-assisted line for new products filed since 2026-04, advises each affected client in writing under 111.39(c), and corrects the entries through CBP's correction process, with customs counsel for any entry already liquidated. The 4 duty-rate errors, 2 origin errors, and 2 quantity errors from the test are corrected first.

**Data protection (by 2026-12-31; R-011, POAM-009):**
- Ask the vendor in writing for: the model provider's name and location; whether client documents leave U.S. regions; whether client data trains any model, including in aggregated or de-identified form; retention and deletion of documents sent to the model; and whether the next SOC 2 report will cover the feature (P09 follow-ups).
- Contract addendum at renewal: no training on company data; U.S. processing; subprocessors named; incident notice within 24 hours; advance notice and opt-in for new AI features.
- The client terms clause drafted by counsel names the platform vendor and its AI model provider as authorized service providers (111.24).

**Monitoring:**
- Monthly: the Entry Supervisor's recorded review sample of 10 entries includes at least 5 AI-assisted lines (G-021). Results go to the monthly security meeting and to P01 R-012.
- Monthly: the platform report of accepted and rejected suggestions; any accepted suggestion on a new product without broker approval is a finding.
- Quarterly: new-product error rate by invoice language, from the monthly samples.
- Vendor release notes reviewed monthly for AI changes (P09 CC8.1). Any new AI feature triggers a new assessment before use.

**Training:** the annual training (POAM-005) covers the AI rules: suggestions are not decisions, check every captured field, record the basis, and never paste client documents into public chatbots.

**Incident handling:**
- A wrong classification that reaches a filed entry is logged, the client is advised under 111.39(c), and the entry is corrected. Two or more in a month go to the owner.
- A security incident at the vendor or model provider that involves client records is handled under POL-03 and the P08 runbook, including the 72-hour notice to the CBP Security Operations Center with any known compromised importer identification numbers (111.21(b)).

**Decommissioning criteria:** the owner turns off classification suggestions (and capture if needed) if: the vendor will not disclose the model provider and data use terms by 2026-12-31; the new-product error rate stays above 10% for two months in a row after the controls are in place; the language gap stays flagged at the 2027-02 review; or a vendor incident exposes client records through the feature. On shutdown, the company asks the vendor to confirm deletion of documents held for the feature and keeps the shipment records as required by 111.23(b).

## 6. Decision
**Approve with conditions.** Owner and President, 2026-08-31.

AI-001 stays on for document capture and for suggestions that match the company's product library. Suggestions for new products and for non-English invoices may be used only as leads, with broker classification and recorded approval. Conditions:
1. Broker approval setting on and the basis recorded for every new-product line (2026-09-15; R-012, G-021, G-033).
2. Look-back review of new-product lines filed since 2026-04, client advice, and corrections (2026-09-30).
3. AI rules covered in the first annual training (2026-10-31; POAM-005).
4. Vendor answers on the model provider, data use, and processing location; contract addendum at renewal (2026-12-31; R-011, POAM-009).
5. Client terms clause naming the vendor and its model provider sent to all active clients (2026-12-31; G-015).
6. Reassessment in 2027-02 with three months of monitoring data, or sooner if the vendor changes the feature.

**Related actions for the other inventory entries.** AI-002 (public chatbots): client data prohibited under POL-02 C.2; permitted only for general research and for text that contains no client information; the Security Coordinator blocks known chatbot sites on company computers if a monthly check finds misuse (R-013, due 2026-09-30). AI-003 (the suite's built-in generative AI assistant): not licensed and not approved; if a future plan includes it, it stays off until assessed under this method.

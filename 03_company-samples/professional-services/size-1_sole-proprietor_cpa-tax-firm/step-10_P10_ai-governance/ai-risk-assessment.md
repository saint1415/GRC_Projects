# AI Use Assessment: Generative AI Assistant for Tax and Document Preparation (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (CPA and tax preparation practice) |
| Tier / Vertical | Sole Proprietorship / Professional, Scientific, and Technical Services |
| AI use case | AI-001: a general-purpose generative AI assistant on an individual paid plan (SYS-08), used from 2026-02-02 to summarize client tax documents and draft IRS notice responses. Client data stopped 2026-07-27. The registry's "generative AI for tax and document preparation" is narrowed to this one tool, the only AI tool the owner uses |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; AI 600-1 for generative AI risks |
| Assessor and decision | CPA-owner, 2026-08-24; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases; AI-002, the tax software's extraction feature, is not turned on) |

## 1. What it does (Map)
The owner uploaded brokerage composite 1099s, K-1s, and three new clients' prior-year returns and asked for summaries to key into the tax software, and pasted IRS notice text to get draft responses. From February to July 2026 this covered about 70 clients (about 95 individual consumers). Full SSNs appeared on 12 documents. The individual plan's terms let the vendor use chats to improve its models unless the user turns that off, and they make no commitment about where data is processed. The owner turned the setting off, stopped all client data, and deleted those chats on 2026-07-27. The tool still helps with generic tax questions and letter templates.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| IRC 7216; 26 CFR 301.7216 (N54-R02) | **Yes** | Everything in the uploads is tax return information (301.7216-1(b)(3)). A disclosure needs a permission in 301.7216-2 or the client's prior written consent (301.7216-3(a)(1)). See section 2.1 |
| FTC Safeguards Rule (N54-R01) | **Yes** | The vendor received customer information, so it is a service provider the firm must select, bind by contract, and assess (314.4(f)); a new application must be evaluated before use (314.4(c)(4)) |
| Circular 230, 31 CFR 10.22 | **Yes** | A practitioner must use due diligence in preparing returns and in what it tells clients and the IRS. Relying on another's work product counts as diligent only with reasonable care in supervising and evaluating it. The owner applies that standard to AI output |
| Fla. Stat. 501.171(2) | Indirectly | Reasonable measures to protect personal information include where it is sent |
| Colorado SB26-189 and similar state AI laws | **No** | The tool makes no decision about a person in a consequential category (employment, lending, housing, insurance, and others). Tax preparation support is not one |

### 2.1 IRC 7216 analysis (for counsel to confirm)
1. **The preparer-to-preparer permission probably does not fit.** 301.7216-2(d)(1) allows disclosure to another *tax return preparer* located in the United States for preparing or auxiliary services, but not for "substantive determinations" (an "analysis, interpretation, or application of the law"). A general-purpose AI vendor does not hold itself out as providing tax preparation services, its terms do not commit to U.S. processing, and drafting a notice response is analysis of the law.
2. **The contractor permission does not fit.** 301.7216-2(d)(2) requires every individual who receives the information to get a written notice of sections 6713 and 7216. That cannot be done with a consumer AI service.
3. **No consent was obtained.** Under 301.7216-3 consent must be written, signed before the disclosure, knowing and voluntary, and not a condition of service. And for Form 1040 filers, no consent can authorize sending an SSN to a preparer outside the United States except under the IRS's safeguards (301.7216-3(b)(4)).
4. **Conclusion.** The past uploads had no confirmed basis. Counsel will advise by 2026-10-31 on the uploads (a section 7216 question, not a breach notice question: about 95 consumers is below the 500-consumer FTC threshold in 314.4(j)) and on any future consent route.

## 3. Risk screen (repository rubric)
**Tier: Medium.** The tool influences work that reaches clients and the IRS, and it touched regulated data, but the owner makes and signs every decision. Not High: no consequential decision about a person. Not Low: Low requires no regulated data, which was not true before 2026-07-27. The tier does not change the core rule: **no tier allows client tax return information into a tool without a confirmed IRC 7216 basis** (POL-01 8.10 and 9.5).

## 4. Data-sharing rules (Govern)
1. **Allowed:** generic tax questions, de-identified fact patterns, and letter templates with placeholders.
2. **Prohibited:** client names, SSNs, account numbers, addresses, employers, uploaded documents, and images of notices (POL-01 9.5).
3. The model-improvement setting stays off; the owner checks the vendor's terms each July and records any change (POL-01 6.3, 6.4).
4. Client data may enter an AI tool only after a new assessment shows business terms with no training on firm data and U.S. processing, a counsel-approved IRC 7216 basis, and the pre-adoption checklist. AI-002 (the tax software's extraction feature) stays off until then; it is also outside the vendor's SOC 2 report (P09).

## 5. Human review of outputs (Measure and Manage)
**Errors found in the July review of the chat history:** one draft notice response cited a Code subsection that does not exist (the AI 600-1 "confabulation" risk), and one 1099 summary left out the wash sale loss disallowed amount. Both were caught before anything was filed or sent, because the owner reconciles to the form totals. Rules from 2026-08-31:
- Check every cited authority against the primary source (Code, regulation, or IRS publication) before it goes to a client or the IRS.
- Reconcile every AI-produced figure to the source document; never key a figure from an AI summary alone.
- Log each AI-assisted item sent out and, once a month, recheck five of them; a wrong figure or citation that reaches a client or the IRS stops use until the owner records the cause.
- Fairness: the tool makes no decision about people, so no group bias test applies. The accuracy check above is the measure.

## 6. Decision: approve with conditions (2026-08-31)
**AI-001 may continue for generic, de-identified work only.** Conditions:
1. No client data (in force since 2026-07-27; POL-01 9.5).
2. Counsel's written advice on the past uploads and on any consent route by 2026-10-31 (P01 R-006; POAM-010; P03 G-036, G-039, G-041).
3. The review rules in section 5 apply to every output (P01 R-007, closed 2026-08-31).

Stop using the tool if the vendor changes its terms to train on paid-plan chats without an opt-out, or if a review rule is skipped. **AI-002 stays off.**

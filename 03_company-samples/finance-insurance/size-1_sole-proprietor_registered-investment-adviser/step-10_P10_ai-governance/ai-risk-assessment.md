# AI Use Assessment: Consumer Generative AI Assistant (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (state-registered investment adviser) |
| Tier / Vertical | Sole Proprietorship / Finance and Insurance |
| AI use case | AI-001: a consumer generative AI assistant (SYS-09) used to summarize client statements and draft quarterly review letters. Used about 3 times a week from 2026-05-04; paused 2026-07-15 |
| Why not the brief's use case | The generated brief names an "AI credit underwriting model". A one-person adviser makes no credit decisions; the Sole Proprietorship scope is "one third-party AI tool the owner uses", which is this assistant |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 for generative AI risks |
| Assessor and decision | Owner-adviser, 2026-08-24; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
The owner pasted or uploaded custodian statements and meeting notes into the assistant and asked for a plain-language summary of performance and changes, then edited the draft into a review letter. Statements for about 25 client households went in, some with full account numbers; no SSNs were found in the chat history on review. It is a consumer plan: the owner accepted click-through terms, and those terms **allow the vendor to use chats to improve its models** unless the user turns that off. Nothing drafted by the assistant makes a decision about a client; the owner decides what to send.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| FTC Safeguards Rule, service provider oversight (16 CFR 314.4(f)) | **Yes** | The vendor "receives, maintains, processes, or otherwise is permitted access to customer information" through a service to the adviser, so it is a service provider (314.2(r)). The adviser must select providers capable of safeguards and require them by contract (314.4(f)(1)-(2)). Consumer terms that allow training do neither |
| Fla. Stat. 501.171 | **To assess with counsel** | Florida's definition counts a financial account number as personal information only with a required security code, access code, or password. The statements had names and account numbers but no codes or SSNs, so notice is **probably not** triggered. Counsel confirms before 2026-09-30 |
| GLBA privacy (N52-R01) | **To assess with counsel** | Sharing client information with a nonaffiliated company is limited by the GLBA privacy rules and the adviser's own privacy notice. Counsel confirms whether this use fits the notice |
| Colorado SB26-189 (effective 2027-01-01) | No | No Colorado clients, and the tool drafts text; it does not make or materially influence a consequential decision about a person |
| Fla. Stat. 934.03 | Not for AI-001 | Applies to AI-002 (meeting recording): recording requires every party's prior consent |

## 3. Risk screen (repository rubric)
**Tier: Medium.** It uses regulated data (customer information), so it cannot be Low, and its output goes to clients, but the owner makes every decision and reviews every letter. It is not High: it makes no consequential decision about credit, insurance, or any other listed category. The tier does not matter yet, because **no tier allows customer information to go to a provider without contractual safeguards** (POL-01 6.1).

**Generative AI risks (AI 600-1) that matter here:** confabulation (invented or wrong figures in a letter that looks right, P01 R-015); data privacy (client data kept or used for training, R-006); information integrity (a fluent summary that hides a fee or a loss).

## 4. Data-sharing rules (Govern)
1. No customer information goes to any AI tool without a written P10 assessment, a business plan whose contract bars model training and sets retention, and the owner's written approval (POL-01 9.4).
2. Even on an approved plan, **never** enter account numbers, SSNs, dates of birth, or ID images. Use household initials and round figures where possible.
3. The approved tool is listed in POL-01 Appendix A; everything else is prohibited for client work.

## 5. Human review of outputs (Measure and Manage)
For any approved tool: the owner checks **every figure** in an AI-assisted letter against the custodian statement before it is sent, reads the whole letter for statements the owner would not make, and keeps the source statement with the letter. Each quarter the owner re-checks 3 sent letters against the statements and records the result. One material error (wrong return, wrong fee, wrong holding) stops use until the cause is understood. **No accuracy testing was done during the consumer use**; the owner re-checked 5 letters sent in June and found one rounded return shown as 6.4% instead of 6.1%, corrected in a follow-up note to that client.

**Bias and fairness plan:** not needed for AI-001, which makes no decision about people. If a future tool suggests client portfolios or suitability, re-run this assessment and compare suggestions across age and account size before use.

## 6. Decision: stop the consumer plan (approved 2026-08-31)
**Do not resume the consumer assistant.** By 2026-09-30 (P01 R-006, R-015):
1. Turn off model training in the account settings, delete the chat history and uploaded files, then close the account; keep a screenshot of each step.
2. Ask counsel to confirm the Florida and GLBA privacy analysis in section 2 and record the answer.
3. Evaluate one business-plan assistant against the POL-01 6.2 checklist (no-training contract terms, retention limits, MFA, assurance report). Use it only after that check, under the rules in sections 4 and 5.

**Related use case (AI-002):** the video meeting service's AI summary feature stays **off**. Before it is turned on, run this assessment for it, confirm the vendor's terms, and get every participant's prior consent to recording (Fla. Stat. 934.03), noted in the CRM.

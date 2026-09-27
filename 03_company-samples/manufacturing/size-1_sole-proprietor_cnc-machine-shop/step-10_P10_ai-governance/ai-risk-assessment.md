# AI Use Assessment: Consumer Generative AI Assistant (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated CNC machine shop) |
| Tier / Vertical | Sole Proprietorship / Manufacturing (NAICS 332710) |
| AI tool | SYS-08: a general-purpose generative AI assistant on a free consumer plan, used since 2026-03 (about 40 chats) |
| Use cases | AI-001 drafting quotes and customer emails and explaining GD&T callouts; AI-002 writing and editing G-code snippets (same tool) |
| Why this tool | The vertical's scenario (an AI-enabled device software function) fits a device maker, not a parts supplier. This is the one third-party AI tool the owner uses |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 for generative AI risks |
| Assessor and decision | Owner-machinist, 2026-08-19; decision 2026-09-04 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. What it does (Map)
The owner types or pastes text, or uploads a file, and the assistant returns text: a draft quote or email, an explanation of a tolerance callout, or a block of G-code. It is a consumer product. The owner accepted click-through terms. Those terms promise no confidentiality to business users, and the default setting lets the vendor use chats to improve its models. A review of the chat history on 2026-08-19 found:
- **one OEM drawing PDF uploaded** (2026-05) to ask about a callout;
- **notes pasted from two aerospace drawings** (FCI) to help with a quote;
- **about 12 G-code snippets** generated or edited, 3 of which were used on the machines after the owner edited them.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| FAR 52.204-21(b)(1)(iii) (N31-33-R02; C-DIB-R04) | **Yes** | The assistant is an external information system. Putting FCI into it was a use the shop did not verify or limit |
| OEM NDAs and SQAs | **Yes** | The uploaded drawing went to a party outside the NDA, and AI-written G-code in a released OEM program would be a process change needing OEM approval |
| ITAR and EAR (N31-33-R03, R04) | **Not today** | The shop takes no controlled technical data (POL-01 8.3). Controlled data in a cloud AI service could raise export questions, which is one more reason the rule is absolute |
| State AI laws (for example Colorado SB26-189) | **No** | The shop makes no consequential decisions about people with AI |
| FTC Act Section 5 | **Low relevance** | The shop makes no AI claims to customers |

## 3. Risk screen (repository rubric)
- **AI-001 (writing and GD&T): Low**, but only with public or generic content. It supports internal work and makes no decisions about people. With customer drawing content in it, it is not allowed at any tier under consumer terms.
- **AI-002 (G-code): High.** The rubric makes any AI that "can affect physical safety" High. A wrong move in AI-written G-code (a rapid move into a clamp, a wrong Z depth, a missing coolant or spindle command) can crash a machine and throw a tool or part near the operator, and a wrong feature on an OEM part could reach a medical device. Bias testing does not apply, because no people are being assessed. What High requires here is **human review before action** and monitoring.

**AI 600-1 risks that matter:** confabulation (plausible but wrong G-code or tolerance explanations), information security and intellectual property (customer drawings in a vendor's service), value chain (consumer terms the shop cannot negotiate), and human-AI configuration (trusting fluent output).

## 4. Data-sharing rules (Govern)
1. No customer information (drawings, models, part numbers, notes, customer names with job details) goes into any AI tool unless the tool is approved in writing after this assessment and its terms protect confidentiality and bar training on shop data (POL-01 9.6). The consumer plan is not approved for customer information.
2. Generic questions (how to read a GD&T symbol, a standard thread-milling cycle, email wording with no customer details) are allowed.
3. Model training is switched off in the account settings, and chat history is reviewed every quarter.

## 5. Human review of outputs (Measure and Manage)
For **G-code (AI-002)**, before any cut:
1. Read every line and check work offsets, tool numbers, spindle and coolant commands, and safe Z retracts.
2. Run it in the CAM software's simulation with the actual stock, fixture, and tools.
3. Dry-run on the machine with the Z offset raised, then single-block the first part.
4. Never put AI-written code into a released OEM program without the OEM's written approval (POL-01 8.5).
5. Record on the traveler that AI-written code was used. A crash or near miss stops AI-002 use until the owner reviews what went wrong.

For **writing (AI-001)**: the owner reads every draft before sending and checks every number (prices, quantities, dates, tolerances) against the source.

No accuracy testing was done before 2026-08-19. From 2026-09 the owner logs each AI-002 snippet used and whether it needed correction; if more than 1 in 5 needs a safety-relevant fix, AI-002 stops.

## 6. Decision (approved 2026-09-04)
**AI-001 continues for generic content only. AI-002 continues only under the section 5 steps.** Actions (P01 R-008; P07 POAM-006):
1. Training opt-out set and the chats with customer content deleted on 2026-08-19.
2. The owner told the affected OEM and the aerospace customer in writing on 2026-08-20 what had been shared and that it was deleted. Neither asked for more.
3. Quarterly check of chat history, starting 2026-11.
4. Before any paid business AI tool is used with customer information: a new P10 assessment, contract terms with confidentiality and no training on shop data, and each customer's consent where its contract requires it.

# AI Use Assessment: Consumer Generative AI Chatbot (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent insurance agency) |
| Tier / Vertical | Sole Proprietorship / Financial Services |
| AI use case | AI-001: consumer generative AI chatbot (SYS-08), used 2026-04-06 to 2026-08-04 for about 40 client accounts; paused 2026-08-05. AI-002 (the AMS's built-in assistant) is screened in section 7 |
| Why not the vertical default | The registry's "transaction fraud-detection model" does not fit: the agency processes no transactions; insurers and banks run fraud scoring |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 for generative AI risks (data privacy, confabulation, information security) |
| Assessor and decision | Owner-agent, 2026-08-21; decision 2026-09-14 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
The owner pasted declarations pages, applications, and quote printouts into a general-purpose chatbot and asked it to compare coverages, deductibles, and exclusions between insurers, and to draft coverage summaries and renewal emails. Inputs included client names, addresses, vehicle identification numbers, prior claims, and, for 7 clients, driver license numbers. No Social Security numbers were found in the chat history. The owner accepted consumer click-through terms, which **let the vendor use chats to improve its models unless the user opts out**; the owner had not opted out. The outputs shaped advice the licensed agent gives clients.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| Rule 69O-128, F.A.C. (Fla. Stat. 626.9651) | **Yes** | The agency relies on the agent exception from privacy notices (69O-128.002(16)(b)), which holds only if it discloses nonpublic personal information as the rule permits. Sending client data to a chatbot vendor that may train on it is not a disclosure to place or service the client's insurance. Counsel reviews (P03 G-018) |
| Fla. Stat. 501.171 | **Yes, to assess** | Driver license numbers with names are personal information (501.171(1)(g)1.a.(II)). The pastes were made by the owner, not taken by an outsider, so counsel decides whether this is a "breach of security" (unauthorized access) at all, and documents the conclusion (501.171(4)(c) if notice is not given) |
| Insurer data security addenda | **Yes** | Policyholder information of the lead insurer was pasted. Counsel decides whether the 72-hour incident notice applies |
| State AI laws on consequential decisions | Not for AI-001 | The agency does not decide eligibility, price, or claims; the insurers do. The repository rubric still treats coverage advice to consumers as "influences decisions" |

## 3. Risk screen (repository rubric)
**Tier: Medium.** The tool influenced advice to consumers about insurance, but the licensed agent made every recommendation. The tier does not change the decision below, because **no tier allows client information to go to a vendor without written terms** (POL-01 6.1, 10.4).

Generative AI risks from NIST AI 600-1 that showed up here: **data privacy** (client data retained and possibly trained on), **confabulation** (one coverage comparison sent in July 2026 stated the wrong windstorm deductible; caught before binding), and **information security** (chats kept in a consumer account protected only by a password).

## 4. Data-sharing rules (Govern)
1. No Restricted or Confidential data (POL-01 9.1) goes into any AI tool without a written P10 assessment, contract terms that bar training on agency data and set a deletion period, and the owner's approval.
2. Even in an approved tool, remove driver license numbers, Social Security numbers, and bank details before pasting; use policy numbers or initials instead of names where the task allows.
3. AI tools are listed on the vendor list (POL-01 6.2) and reviewed each August.

## 5. Human review of outputs (Measure and Manage)
For any AI-drafted coverage comparison or summary: the agent checks every limit, deductible (including windstorm and hurricane deductibles), and exclusion against the insurer's policy forms or declarations before it reaches a client; the agent signs off as the person giving the advice; once a month the owner re-checks 3 sent summaries against the forms and logs the result. A material error stops use of the tool until the cause is understood.

## 6. Decision: stop the consumer chatbot (approved 2026-09-14)
**Do not resume AI-001.** By 2026-09-30 (P01 R-004, POAM-006):
1. Turn off model training in the account, delete the chat history, close the consumer account, and keep screenshots of each step.
2. With counsel, decide under Rule 69O-128, 501.171, and the addenda whether any notice is owed, and keep the written conclusion for 5 years.
3. Re-check the other AI-drafted comparisons sent from April to August 2026 against the policy forms (the one known error was corrected before binding), and record the result.
4. Any future standalone AI tool needs a new assessment under section 4 before first use; until then AI-002 is the only approved AI tool.

## 7. AI-002: AMS built-in assistant (screened, approved with conditions)
The AMS vendor added an assistant in its 2026-06 release, on by default. It drafts emails and summarizes notes inside the AMS. The vendor's AI terms say customer data is not used to train shared models and prompts are kept 30 days, and the data stays under the existing AMS contract. **Tier: Medium; approved 2026-09-14** on three conditions: Restricted data is never typed into prompts; the owner edits and sends every draft; and the owner asks whether the next SOC 2 report covers the assistant (P09 vendor review).

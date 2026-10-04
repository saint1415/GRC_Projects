# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed B2B SaaS publisher of a multi-tenant customer service platform) |
| Tier / Vertical | Mid-Market / Information |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. The registry use case, the generative AI feature embedded in the product, is AI-001 and AI-002 |
| Company role | **Developer and provider** of AI-001, AI-002, and AI-003, which customers (the deployers) turn on for their own agents and end consumers. **Deployer** of AI-004 and AI-005 for its own staff |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-001, AI-002, AI-004, and AI-005 |
| Assessors / date | VP Product and the Director of Machine Learning (product), Director of Security (security), Associate General Counsel, Privacy (privacy and legal), VP Customer Support (support operations), 2026-09-08 to 2026-09-18 |
| Decision | Chief Technology Officer, 2026-09-29; the High-tier decision noted by the CEO |
| Related items | P01 R-019 to R-023, R-045, R-046; P03 G-019, G-033, G-045; P07 POAM-015, POAM-016, POAM-019, POAM-021; P09 V-06 |

## 1. Summary
AI Assist (AI-001) and Answer Bot (AI-002) shipped after a product security review only (gap 7). Neither had an AI risk assessment, an evaluation suite, or adversarial testing. The portfolio is not out of control, but three problems need fixing before the features grow:
- **AI-002, Answer Bot:** answers end consumers with no human in the loop, sometimes from outside the customer's knowledge base. That contradicts the product page claim.
- **AI-001 and AI-002:** the model provider keeps Standard tenants' prompts for 30 days, which contradicts the trust center.
- **AI-005, the call summarizer:** joins calls automatically and does not reliably get consent from everyone on the call.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | AI Assist reply drafting for agents | Medium | Approve with conditions |
| AI-002 | Answer Bot (customer-facing chatbot) | High | Beta continues in grounded-only mode; no new customers until thresholds are met |
| AI-003 | Ticket triage and priority classifier | Medium | Approve with conditions |
| AI-004 | Engineering AI coding assistant | Low | Approve |
| AI-005 | Sales and support call summarizer | Medium | Approve with conditions |

Tiers: 1 High, 3 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** VP Product, supported by the Director of Security. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.15: AI features and tools must be approved before release or use. 4.11: AI statements must be true and reviewed each quarter. 4.12: no training on customer data.
  - POL-04 4.6: customer content only to approved AI providers, with no-training and zero-retention terms, minimum data in prompts.
  - POL-05 4.8 and 4.9: approved tools only; all-party consent before recording calls.
  - STD-05 AI development and use standard: due 2026-12-15.
- **Approved tools list:** kept by the Director of IT. Today it lists AI-004 and AI-005 for staff.

### 2.1 Lightweight AI governance process
A mid-market company does not need a standing AI committee with a large charter. It needs a short, reliable gate and a monthly rhythm, using existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any team that wants to ship an AI feature, change a model, or adopt an AI tool submits a one-page intake: purpose, users, affected people, data, provider, decisions affected | Requesting owner | 15 minutes |
| 2. Triage | Provisional tier with the rubric below; check that the provider is an approved sub-processor with no-training and zero-retention terms | Director of Security | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy, and an evaluation plan with thresholds. **High:** full MAP and MEASURE assessment like this one, including adversarial and subgroup testing | Director of Security; Associate General Counsel, Privacy; Director of Machine Learning | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Director of Security. Medium: the **AI review group** (VP Product, Director of Security, Associate General Counsel, Privacy, Director of Machine Learning, VP Customer Support), monthly for 45 minutes. High: the review group recommends, the CTO decides, and the CEO is informed | As listed | Monthly |
| 5. Monitor | Owners report agreed metrics monthly; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: model or provider change, new data type, new customer segment (for example healthcare or banks), new autonomy (actions instead of answers) | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`, plus one **company rule**: any AI that sends content to end consumers without per-message human review is High until it has met its evaluation thresholds for 2 consecutive months. That is why AI-002 is High even though it makes no consequential decision.

## 3. MAP
| Item | AI-001 AI Assist | AI-002 Answer Bot | AI-003 Triage classifier | AI-004 Coding assistant | AI-005 Call summarizer |
|---|---|---|---|---|---|
| Purpose | Draft replies and summaries for agents | Answer end consumers from the customer's help center; hand off to agents | Predict priority, topic, sentiment for routing | Code completion and chat for engineers | Summarize sales and support calls into the CRM |
| Users | Agents at about 1,100 customers | End consumers of 85 beta customers | All tenants (opt-out available) | 190 engineers | About 200 sales and support staff |
| Affected people | End consumers who receive the replies | End consumers who get answers (about 18,000 conversations a day) | End consumers whose tickets wait longer or shorter | Customers, if insecure code ships | Customers and prospects on recorded calls |
| Data | Ticket text, history, knowledge base, first names; PHI in the healthcare cell | Questions, history, knowledge base | Ticket text and metadata | Source code | Call audio and transcripts |
| Build or buy | Build on a bought model | Build on a bought model | Build (own model) | Buy | Buy |
| Generative AI? | Yes | Yes | No (classifier) | Yes | Yes |
| Not intended | Sending without an agent; medical, legal, or financial advice | Account actions (refunds, cancellations), advice on health, legal, or financial matters, use in the healthcare cell | Automatic closure or denial of service | Generating secrets or handling customer data | Recording without consent |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5 (N51-R01) | **Yes, all** | Deception: the trust center says AI providers do not retain data (false for Standard tenants, P03 G-033), and the product page says Answer Bot answers only from the help center (false in 7% of sampled replies, G-045). Unfairness: unreasonable handling of customer data in prompts |
| FTC proposed policy statement on suppression of accuracy in AI systems (91 FR 41638, 2026-07-07) | **Watch item** | Proposed, not final; comments closed 2026-07-31. Relevant to how AI-002 is marketed |
| Customer DPA and CCPA service-provider terms (N51-R03) | **Yes, AI-001 to AI-003** | Customer data may be used only to provide the service and never to train models. AI-003 is trained only on the company's own support tickets and synthetic data |
| HIPAA as a business associate | **Yes, AI-001 in the healthcare cell** | The cell uses the model provider's zero-retention endpoint under a subcontractor BAA. AI-002 is not enabled in the cell |
| CPPA ADMT regulations (N51-R03) | **Considered; not triggered today** | The rules cover ADMT used for significant decisions. None of the features makes decisions about consumers. If customers connect AI-002 to account actions, re-assess |
| Colorado SB26-189 (effective 2027-01-01) | **Considered; not triggered today** | Developer documentation duties apply to AI that materially influences consequential decisions (for example lending or insurance). The 9 bank customers use AI-002 only for general questions. Counsel to reconfirm before any bank enables account features |
| State chatbot disclosure laws | **Not researched in depth** | Some states require telling consumers they are talking to a bot. AI-002 always shows an "AI assistant" label and a "talk to a person" option, so the company does not depend on the answer |
| Fla. Stat. 934.03(2)(d) and other states' recording laws | **Yes, AI-005** | Interception is lawful in Florida only when all parties have given prior consent. The company applies that rule to every call |

## 4. MEASURE (by use case)
Tests ran 2026-09-08 to 2026-09-18 on production samples (with customer data viewed only by the assessors under POL-02) and on synthetic test tenants.

| Use case | Trustworthy characteristic | Test or metric | Threshold | Result | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | 500 sampled drafts checked against the ticket and knowledge base for invented policies, prices, or promises | Under 1% | 12 of 500 (2.4%) | **No** |
| AI-001 | Secure and resilient | Cross-tenant probes: retrieval asked for content of other tenants | 0 leaks | 0 of 200 | Yes |
| AI-001 | Secure and resilient | Prompt injection in inbound emails (40 cases) | 0 drafts carrying attacker text unflagged | 6 of 40 | **No** |
| AI-001 | Privacy-enhanced | No training; no retention by the provider | Both in contract | No training: yes. Retention: 30 days on the standard endpoint | **No** |
| AI-001 | Accountable and transparent | Agents can see sources for each draft | Available | Available | Yes |
| AI-002 | Valid and reliable | 400 sampled replies grounded in the customer's knowledge base | 99% or more grounded | 372 of 400 (93%) | **No** |
| AI-002 | Safe | 60 scripted sensitive prompts (self-harm, medical symptoms, legal threats, fraud reports, account closure) handed to an agent | 100% handoff | 51 of 60 (85%) | **No** |
| AI-002 | Secure and resilient | Prompt injection (50 cases) changing the answer or revealing configuration | 0 | 7 of 50 changed the answer; 0 revealed configuration or other tenants' data | **No** |
| AI-002 | Fair, harmful bias managed | Answer accuracy for Spanish versus English questions on the same knowledge base (300 each) | Gap of 5 points or less | 88% versus 94% (6 points) | **No** |
| AI-002 | Accountable and transparent | "AI assistant" label and "talk to a person" option on every conversation | 100% | 100% | Yes |
| AI-003 | Valid and reliable | Overall accuracy on 2,000 human-labeled tickets | 85% or more | 89% | Yes |
| AI-003 | Fair, harmful bias managed | Recall of urgent tickets by language (English, Spanish, other) | Each group within 5 points of English | English 91%, Spanish 78%, other 74% | **No** |
| AI-004 | Secure and resilient | 50 sampled AI-assisted pull requests reviewed for insecure patterns and secrets | Caught in review before merge | 2 insecure patterns, both caught in review; 0 secrets | Yes |
| AI-005 | Accountable and transparent | 40 sampled recorded calls with a consent statement from all parties at the start | 100% | 26 of 40 (65%) | **No** |
| AI-005 | Privacy-enhanced | Summaries stored only in the CRM with the account; audio deleted in 30 days | Both | Both | Yes |

### 4.1 Bias and fairness testing plan
| Use case | Groups compared | Metric | Threshold | Frequency |
|---|---|---|---|---|
| AI-002 | Question language (English, Spanish, and the next 3 languages by volume) | Answer accuracy on matched question sets | Gap of 5 points or less | Before any release that changes prompts or model; quarterly |
| AI-002 | Reading level of questions (plain versus complex wording) | Handoff rate and accuracy | Gap of 5 points or less | Quarterly |
| AI-003 | Ticket language | Recall of urgent tickets | Within 5 points of English | Quarterly; after retraining |
| AI-001 | Ticket language | Rate of invented content in drafts | Within 1 point of English | Quarterly |

The platform holds no race, sex, age, or disability data, so tests use language and wording as the available proxies. Results are shared with customers on request.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the agent reviews and sends every reply; there is no auto-send. Drafts with possible injected instructions are flagged in the workspace.
- **AI-002:** no per-message review, so the safeguards are built in: grounded-only mode (refuse when retrieval is weak), a sensitive-topic classifier that hands off to an agent, a visible "talk to a person" option, and a customer-set daily cap on bot-only conversations.
- **AI-003:** agents and customer administrators can change priority; customers can turn the classifier off.
- **AI-004:** normal code review and CI tests apply to every change.
- **AI-005:** auto-join off; the host must start the summarizer after reading the consent script; recording stops if anyone objects.

**Monitoring:** owners report the section 4 metrics monthly to the AI review group. AI-002 also gets a weekly report until it passes all thresholds for 2 months. Results feed the risk register (P01 R-019 to R-023, R-045, R-046).

**Incident handling:**
- A harmful or false AI output that reaches end consumers is an incident under POL-03. The feature flag is turned off first for the affected tenant or all tenants.
- A model provider security incident follows P08 and the DPA and BAA terms.
- A customer complaint about an AI answer goes to the VP Customer Support and is logged.

**Decommissioning criteria:**
- AI-002: switch off for all tenants if grounded-only mode does not reach 99% by 2026-12-15, or if a sensitive-topic failure causes harm.
- AI-001 and AI-002: stop calls to the standard endpoint on 2026-11-30, whether or not the migration is complete.
- AI-005: remove the tool if consent reaches less than 100% in 2 consecutive monthly samples after 2026-11-30.
- Any feature: stop if the provider changes data-use terms or the model changes without notice.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | All tenants on the zero-retention endpoint (2026-11-30); injection flagging in the workspace and invented-content rate under 1% (2026-12-15); trust center statement corrected now (2026-10-15) | CTO, 2026-09-29 |
| AI-002 | **Beta continues in grounded-only mode; no new customers** | Product page claim withdrawn (2026-10-15); grounding 99% or more, 100% sensitive-topic handoff, injection fixes, and language gap within 5 points (2026-12-15); not available in the healthcare cell; re-assess before any account actions | CTO, 2026-09-29; noted by the CEO |
| AI-003 | **Approve with conditions** | Retrain with balanced language samples and meet the recall threshold (2027-03-31); quarterly subgroup tests | CTO, 2026-09-29 |
| AI-004 | **Approve** | Secret scanning in the IDE (2027-03-31); quarterly sample review | Director of Security, 2026-09-29 |
| AI-005 | **Approve with conditions** | Auto-join off and consent script (2026-11-30); monthly sample of 20 calls until 2 months at 100% | CTO, 2026-09-29 |

The conditions are tracked as POAM-021 in P07, with the statement fixes in POAM-019 and the provider retention fix in POAM-015. The AI review group holds its first monthly meeting on 2026-10-07.

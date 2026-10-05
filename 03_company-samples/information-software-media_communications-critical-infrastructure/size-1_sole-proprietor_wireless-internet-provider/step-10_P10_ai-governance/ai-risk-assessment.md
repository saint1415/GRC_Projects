# AI Use Assessment: AI Support Assistant with Account Access (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated wireless internet service provider) |
| Tier / Vertical | Sole Proprietorship / Communications |
| AI use case | AI-001: the billing platform's AI support assistant add-on (SYS-08) on the customer portal chat and the text-message support line, with read access to the customer's account and the ability to open repair tickets. Turned on 2026-05-04. This is the registry's "customer-service chatbot with account access", adapted to the one AI tool a one-person ISP actually uses |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 for generative AI risks |
| Assessor and decision | Owner-operator, 2026-08-20; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner and approver:** the owner-operator (no committee at this size).
- **Policies that apply:** POL-01 7.8 (CPNI online only after compliant sign-in; account change notices), POL-01 8.3 (no marketing use of CPNI), POL-01 6.1 (vendor terms before CPNI access), POL-01 9.6 (AI tools).
- **How it started:** the owner switched the add-on on in the billing platform without a review. It was never in the billing vendor's SOC 2 report (P09). This is the first assessment.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Answer outage, billing, and plan questions at any hour so customers are not waiting for the owner, who is often on a tower |
| Users / operators | Customers on the portal chat (signed in) and the text line (not signed in); the owner reviews escalations |
| Affected people | About 310 account holders and anyone who texts the support number. About 620 sessions from 2026-05-04 to 2026-08-14 (380 chat, 240 text) |
| Data | Inputs: customer messages; account data read through the platform (balance, plan, invoices, outage status, tickets, and for the 52 home phone accounts, recent call history, which is CPNI). Outputs: answers and repair tickets. The add-on terms say customer data is not used to train models; the model provider keeps transcripts 30 days for abuse monitoring (owner asked the vendor to confirm both in writing) |
| Build or buy | Buy: vendor add-on built on a third-party large language model |
| Actions allowed | Read the account; open a repair ticket. No payments, plan changes, credits, address or password changes, or disconnections |

**What went wrong (found 2026-07-22, P03).** On the text line the assistant accepted an account number and service ZIP code, both printed on every bill, and then listed the account's recent home phone calls. The CPNI rules forbid authenticating with account information before online access to CPNI (47 CFR 64.2010(c)). The owner turned off the call history skill on the text line that day. A review of all text sessions since launch found 14 that showed call history; the owner called each account holder back at the telephone number of record, all 14 confirmed they had asked, and no breach was determined (incident log, 2026-07-22).

**Rules that apply:**
| Rule | Applies? | Why |
|---|---|---|
| FCC CPNI rules (C-COMMUNICATIONS-R01) | **Yes** | The assistant is an online channel that can show call history, so 64.2010(a), (c), and (f) apply; an unauthorized disclosure through it is handled under 64.2011. The vendor's handling of CPNI is the company's responsibility |
| FTC Act Section 5 | Yes, for broadband statements | Broadband is an information service (P03 section 1.2); the assistant's claims about plans, speeds, and prices must be accurate and match the broadband labels |
| Fla. Stat. 501.171 | Only if credentials are exposed | For example, a portal user name with a password |
| State AI laws | Not identified | All customers are in Florida, and the assistant makes no consequential decision. It still says it is an AI assistant (section 5) |

## 3. Risk tier
**Tier: Medium** (repository rubric). It talks directly to customers and reads CPNI, but it makes no decision about a person, cannot change the account, and hands everything else to the owner. **Re-tier to High and reassess** if it is ever allowed to change authentication details, decide credits or disconnections, or use CPNI for marketing.

## 4. MEASURE
Tests on 2026-07-22 (text line) and 2026-08-14 (transcript sample and prompts).

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 50 transcripts graded against invoices and the knowledge base; incorrect answers must be under 5% | 4 of 50 incorrect (8%): outage restoration times and the late fee rule | **No** |
| Safe | 10 prompts about calling 911 when the home phone or internet is down | 10 of 10 told the customer to use a mobile phone and call 911 | Yes |
| Secure and resilient | 20 prompt injection and data extraction prompts; no other customer's data; no action outside the allow-list | No cross-account data (the platform limits the assistant to the session's account); 1 prompt revealed internal knowledge article text, no customer data | **Partial** |
| Accountable and transparent | AI disclosure; hand-off to the owner on request; transcripts exportable | Disclosure shown on chat but not in the first text message; hand-off works; transcripts exportable | **Partial** |
| Explainable and interpretable | Billing answers cite the invoice line | Cited in 31 of 40 billing answers | **Partial** |
| Privacy-enhanced | CPNI only after compliant sign-in; no training on customer data; transcript retention known | Text-line CPNI gap (fixed 2026-07-22); no-training and 30-day retention in the add-on terms, written confirmation pending | **No** until conditions 1 and 4 are met |
| Fair, with harmful bias managed | Compare incorrect-answer and escalation rates by language (English, Spanish), channel (chat, text), and customer type (year-round, seasonal, farm and business). Flag any group more than 3 percentage points worse on incorrect answers or 10 points worse on escalation | Spanish: 2 of 12 graded sessions incorrect (17%) vs 7% English, a sample too small to conclude. Other groups within thresholds | **Inconclusive.** Spanish billing questions go to the owner until 30 Spanish sessions can be graded |

## 5. MANAGE
- **Human-in-the-loop:** the owner handles every escalation, dispute, credit, payment arrangement, and account change; the assistant only reads and opens tickets. Customers can ask for the owner at any time.
- **Monitoring:** 20 transcripts a month graded for accuracy, by language and channel; complaints that mention the assistant counted, and any about release of CPNI added to the CPNI certification complaint summary (64.2009(e)).
- **Incident handling:** any sign that the assistant showed CPNI to someone other than the account holder is logged the same day and handled under P08 and the 64.2011 sequence.
- **Decommissioning criteria:** turn the add-on off if it discloses CPNI to the wrong person, if accuracy stays above 5% incorrect for two months, or if the vendor will not confirm the no-training term in writing.

## 6. Decision
**Approve with conditions**, by the owner-operator on 2026-08-31:
1. CPNI (call history, home phone invoice lines) is shown only inside a signed-in portal session. The text line answers outages and general questions only (POL-01 7.8). Due 2026-10-31 (POAM-004).
2. The first text message in every session says the customer is talking to an AI assistant. Due 2026-09-30.
3. Account change notices are turned on for new online accounts, email of record, and service address. Due 2026-10-31.
4. The vendor confirms in writing that customer data is not used for training and states transcript retention; the add-on is added to the vendor list (POL-01 6.2). Due 2026-10-31.
5. Any new skill or action needs a reassessment first (POL-01 9.6).

**AI-002** (general-purpose AI chat assistant for drafting) is Low tier and approved for drafting only, with no customer data, CPNI, credentials, or full configurations (POL-01 9.6).

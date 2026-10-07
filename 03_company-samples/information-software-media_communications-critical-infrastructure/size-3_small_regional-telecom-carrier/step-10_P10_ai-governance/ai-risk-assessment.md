# AI Risk Assessment: Customer-Service Chatbot with Account Access

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (regional broadband and wired telecommunications carrier) |
| Tier / Vertical | Small / Communications |
| AI use case | AI-001: customer-service chatbot on the web portal and app, with read and update access to customer accounts through an API to the BSS. Pilot since 2026-04-06 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | IT Manager with the Director of Customer Operations and the Regulatory Affairs Manager, 2026-08-24 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner:** Director of Customer Operations (business owner). **Decision authority:** COO (Medium tier). The Chief Executive Officer decides if the use case is re-tiered High.
- **Policies that apply:**
  - POL-02 4.10: customer authentication for online CPNI access (47 CFR 64.2010(c), (e))
  - POL-04 4.3: CPNI used for marketing only with approval, checked at the time of use
  - POL-01 4.9: no CPNI to a vendor without CPNI and security terms and a security review
  - POL-05 4.9: approved generative AI tools only
- **Approved-tools list:** kept by the IT Manager. Today it lists only the chatbot (customer-facing, under the conditions in section 6). No staff generative AI tool is approved for CPNI.
- **Scale for a Small company:** there is no AI committee. The Director of Customer Operations, IT Manager, and Regulatory Affairs Manager review AI use cases quarterly and report to the COO.
- **How the pilot started:** customer operations bought the chatbot in early 2026 without a security or CPNI review. This assessment is the first. The gap is tracked as SOC 2 criterion CC3.4 and P01 R-022.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Answer common questions (outages, bills, plans, payments) and handle simple account tasks without a phone call, to cut care call volume during outages |
| Users / operators | Customers using web or app chat; care agents who receive escalated chats; the vendor's support staff (configuration only) |
| Affected people | About 64,000 account holders, including people who are not the account holder but try to use the chat. About 14,000 chat sessions per month in the pilot |
| Data | Inputs: customer messages; account data from the BSS API (balance, plan, bill lines, call detail, CPNI approval flag not yet available). Outputs: answers, bill explanations, payment arrangement offers, plan suggestions. Transcripts are kept by the vendor for 90 days. **Vendor training on company data is not contractually excluded** |
| Build or buy | Buy: vendor SaaS built on a large language model platform, configured with company knowledge articles and an API connector to the BSS |
| Account actions allowed today | Read balance, bills, plan, and recent call detail; set paperless billing; take a payment arrangement from the BSS rules; open a repair ticket |
| Not intended | Password, address of record, or authentication changes; service disconnection; credits or adjustments; number porting; any decision about credit or deposits. None of these is enabled. Enabling any requires re-assessment |

**What went wrong in the pilot (found 2026-07-24, P03):**
1. **Quick help mode** showed balance, plan, and the last 3 calls after only an account number and service ZIP code. That is account information the CPNI rules forbid as an authenticator for online access (64.2010(c)). It was disabled on 2026-07-31. The Regulatory Affairs Manager reviewed the 1,140 quick help sessions with counsel. No complaint or sign of use by someone other than the account holder was found, so no breach determination was made. The review is recorded in the incident register (64.2011(d) record practice).
2. **Plan upsell** suggested broadband plans to voice-only customers based on their calling patterns without checking CPNI approval (64.2007(b); P03 G-007). Disabled by 2026-10-15 (POAM-019).

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FCC CPNI rules, 47 CFR 64.2001-64.2011 (C-COMMUNICATIONS-R01) | **Yes** | The chatbot is an online channel that shows CPNI (call detail, voice plan, voice bill lines), so 64.2010(c) and (e) authentication applies, and upsell use of CPNI needs approval (64.2007). An unauthorized disclosure through the chatbot would be handled under 64.2011. The vendor's handling of CPNI is the company's responsibility |
| FTC Act Section 5 | Possibly, for broadband-related statements | Section 5 excludes common carriers subject to the Communications Act (15 U.S.C. 45(a)(2)); counsel reads that as limited to common carrier services (P03 section 1.2). Chatbot claims about broadband plans, prices, or privacy must be accurate |
| Florida breach law, Fla. Stat. 501.171 | Yes, if the chatbot exposes Florida-defined personal information | For example, a user name with a password or security answer |
| State AI laws (for example, Utah, Colorado, Texas) | Not identified as applicable | The company serves only Florida addresses, and the chatbot makes no consequential decision in the categories those laws list. The chatbot still discloses that it is AI at the start of every chat |
| Sector AI rules | None identified | The vertical overlay lists no Communications-specific AI rule |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why not High:** the chatbot does not make, and is not a substantial factor in, a consequential decision about a person (credit, housing, employment, and so on). Payment arrangement offers come from fixed BSS rules, and the chatbot only relays them. Credits, deposits, and disconnections stay with human agents.

**Why not Low:** it talks directly to customers, it reads CPNI, and it can take account actions. Errors can expose call detail or mislead customers about bills.

**Escalation triggers (re-tier to High and re-assess):**
- any authentication, password, or address-of-record change through chat
- deciding credits, deposits, payment arrangement eligibility, or disconnections
- a voice (spoken) channel for the chatbot
- use of CPNI for marketing through the chatbot at scale

## 4. MEASURE
Pilot data: 2026-04-06 to 2026-08-14 (about 58,000 sessions). Tests run 2026-07-24 and 2026-08-11.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Monthly sample of 50 transcripts graded against the knowledge base and BSS data. Incorrect billing or policy answers must be under 3% | 200 transcripts: 6% incorrect (mostly late fee and payment arrangement rules) | **No** |
| Safe | Outage and 911 questions route to published guidance; no advice to unplug equipment during 911 outages | 40 of 40 outage prompts answered correctly; 911 prompts routed to the recorded guidance | Yes |
| Secure and resilient | Red-team set of 50 prompt injection and data extraction prompts; no access to another customer's data; no action outside the allowed list | No cross-account access (the API enforces the session's account). 3 of 50 prompts made the bot change paperless billing without the customer asking | **Partial** |
| Accountable and transparent | AI disclosure at chat start; hand-off to a human on request; transcripts retained and reviewable | Disclosure shown; hand-off works; the company cannot export vendor transcripts on demand | **Partial** |
| Explainable and interpretable | Answers about bills cite the bill line or knowledge article used | Citations shown for 70% of billing answers | **Partial** |
| Privacy-enhanced | Online CPNI shown only after portal sign-in (64.2010(c)); CPNI approval checked before any upsell; no vendor training on company data; transcripts deleted within 90 days | Quick help disabled; approval not checked (upsell being disabled); training exclusion not in contract | **No** |
| Fair, with harmful bias managed | Compare, by chat language (English and Spanish) and by customer type (year-round and seasonal residential, business): task completion, incorrect-answer rate, and escalation rate. Flag any group whose incorrect-answer rate exceeds the baseline by more than 3 percentage points, or whose task completion is more than 10 points lower | Spanish (11% of sessions): incorrect answers 11% vs 5% English; task completion 28% vs 44%. Seasonal and business customers within thresholds | **No.** Language disparity flagged |

**Bias finding.** Spanish-language customers get wrong billing answers more than twice as often and finish tasks less often. In a Florida service area, that means one group of customers is more likely to be misled about what they owe. Until the vendor shows parity, Spanish billing and payment questions go straight to a bilingual agent, and Spanish knowledge articles are being rewritten (the CPNI notice is also only partly translated; P02 PT-5).

**Why these groups.** The chatbot does not collect race, age, or disability data, and the company is removing dates of birth from account records (POL-04 4.8). Language is recorded for every session, and customer type is in the BSS, so these comparisons are possible without collecting new sensitive data.

## 5. MANAGE
**Human-in-the-loop design:**
- The chatbot can only take actions on an allow-list enforced at the API gateway, not only in the prompt: read billing and outage data, set paperless billing (with confirmation), create a repair ticket, and relay a BSS payment arrangement offer for the customer to accept.
- Every account change needs an explicit customer confirmation step.
- Credits, adjustments, disputes, disconnections, and any authentication change go to a human agent.
- Customers can ask for a person at any time. The chat hands off with the transcript so the customer does not repeat themselves.

**Monitoring:**
- Monthly 50-transcript accuracy sample, reported by language, to the Director of Customer Operations (P01 R-034).
- Weekly review of API calls by the chatbot client for actions outside the allow-list (part of POAM-006 until managed detection is live).
- Complaints mentioning the chatbot are tagged in the BSS and reviewed monthly, and any complaint about unauthorized release of CPNI is counted for the annual certification (64.2009(e)).

**Incident handling:**
- Any chatbot disclosure of CPNI to someone other than the account holder is a suspected incident under POL-03 and follows the P08 notification matrix (64.2011).
- A vendor security incident must be reported to the company within 24 hours once the contract is amended (POAM-015).
- The chatbot can be switched to "outage messages only" mode by the NOC or customer operations in minutes.

**Decommissioning:**
- Stop, export transcripts, and fall back to phone and portal if the vendor contract is not amended by 2026-12-31.
- Stop if incorrect answers stay above 3% for three months in a row after 2026-12-31.
- Stop if a prompt injection leads to disclosure of another customer's data.

## 6. Decision
**Approve with conditions.** COO, 2026-09-04. The pilot may continue **only if** these conditions are met by 2026-10-15:
1. Quick help mode stays disabled. Account data is shown only after portal or app sign-in.
2. The plan upsell is disabled until it checks the CPNI approval flag (POAM-019).
3. A dedicated API client is limited to the allow-list in section 5, enforced at the gateway (P04 finding 4).
4. Spanish billing and payment questions route to bilingual agents until the fairness thresholds are met.
5. The accuracy threshold (under 3% incorrect) is met in the October sample, or billing answers are limited to quoting the bill.

**By 2026-12-31:** vendor contract amended with CPNI confidentiality, no training or secondary use of company data, 90-day transcript deletion, transcript export on request, and 24-hour incident notice (POAM-015).

General launch beyond the pilot needs two consecutive monthly samples under 3% incorrect, no open fairness flag, and a completed vendor security review.

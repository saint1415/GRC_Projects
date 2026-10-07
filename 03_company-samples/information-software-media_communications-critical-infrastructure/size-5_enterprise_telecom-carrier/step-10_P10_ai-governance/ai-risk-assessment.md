# AI Governance Risk Assessment: Enterprise AI Portfolio and Customer-Service Chatbot

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded regional broadband and wired telecommunications carrier; FL, GA, SC, NC) |
| Tier / Vertical | Enterprise / Communications |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the customer-service chatbot with account access, in section 6 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1); repository risk tier rubric |
| Assessor / date | AI council (chaired by the Chief Data Officer), meeting of 2026-08-19; GRC team prepared the portfolio review; data science lead ran the fairness tests |
| Decision | Executive risk committee, 2026-09-10 (section 8) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 4, Medium 7, Low 1 |
| Status | In production 9, Pilot 2, Suspended 1 |
| Council review complete | 8 of 12 |
| Not yet reviewed | 4: AI-005, AI-008, AI-011, AI-012 (all due 2026-11-30, POAM-023) |
| Use cases that read CPNI | 3 (AI-001, AI-002, AI-006); AI-009 allows it only in the approved tenant |
| High-tier use cases without bias testing | 2 (AI-005, AI-012), both unreviewed; AI-012 is suspended |

**Main findings:** four use cases entered without council review, including a High-tier fraud and deposit model (AI-005) and an AI transcription feature offered to SL-2 customers (AI-011). The chatbot (AI-001), the company's largest customer-facing AI use, gives wrong billing answers more than twice as often in Spanish as in English and misses the 3% accuracy threshold overall.

## 2. GOVERN: AI council operating model
**Charter.** The AI council was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk and technology committee reviews quarterly.

**Members:** Chief Data Officer (chair); CISO; Chief Privacy Officer; Chief Compliance Officer (CPNI compliance officer); General Counsel's delegate; Chief Customer Officer; Chief Network Officer's delegate (network automation); Chief Human Resources Officer (workforce and HR tools); Vice President, Regulatory Affairs; and the data science lead. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Council vote, then the executive risk committee | Local validation and bias testing on the company's data; impact assessment; human review design; notice to affected people; monitoring plan; for network automation, a rollback and outage-reporting plan |
| Medium | Council vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy, CPNI, and security review |
| Low | Council chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products and systems inherited through acquisitions, must be registered before use (POL-05 4.6; STD-05.3). Since 2026-03, procurement and change management block AI features without an inventory ID. The GRC team owns the inventory.

**Policies:** POL-04 4.10 (no Restricted data, including CPNI, in AI tools without council approval and no-training terms); POL-04 4.3 (CPNI used only with approval checked at time of use); POL-02 4.9 (customer authentication before CPNI disclosure); POL-05 4.6 (approved tools only); POL-01 4.8 (vendor CPNI terms); STD-05.3 (approved AI tools list).

**Cadence:** monthly council meetings; quarterly monitoring review for every High-tier use case and for AI-001; annual re-review of every use case.

**Why 4 use cases lack review.** AI-005 and AI-011 arrived as vendor features enabled by business teams in 2026; AI-008 and AI-012 came with the AQ-02 and AQ-03 systems. AI-012's ranking was switched off on 2026-08-20 when the inventory sweep found it.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FCC CPNI rules, 47 CFR 64.2001-64.2011 (C-COMMUNICATIONS-R01) | Yes, for AI-001, AI-002, AI-006, and AI-009 | Online CPNI access requires authentication without readily available biographical or account information (64.2010(c), (e)); CPNI-based marketing needs approval checked before use (64.2007, 64.2009(a)); unauthorized disclosure through an AI tool is a breach under 64.2011. A vendor's handling of CPNI is the company's responsibility (64.2010(a)) |
| FTC Act Section 5 | Possibly, for broadband-related statements | Section 5 excludes common carriers subject to the Communications Act (15 U.S.C. 45(a)(2)); counsel reads that as limited to common carrier services. Chatbot statements about broadband plans and prices must be accurate |
| State breach laws (Florida worked example, Fla. Stat. 501.171) | Yes, if an AI tool exposes state-defined personal information | For example, portal credentials |
| Recording consent laws | Yes, for AI-002 and AI-011 | Care calls start with an all-party recording announcement; SL-2 customers are responsible for their own callers under the service agreement. Florida worked example: Fla. Stat. 934.03(2)(d) |
| FCRA | Possibly, for AI-005 | Adverse action duties where consumer report data is an input (15 U.S.C. 1681m); counsel confirms at review |
| Federal equal employment opportunity laws | Yes, for AI-012 | Counsel reviews adverse impact before any re-enable |
| FCC outage reporting (47 CFR Part 4) | Yes, for AI-004 | An automated action that causes a reportable outage must be reported like any other outage |
| State AI statutes | None identified for the four operating states | The repository's cross-sector file (verified 2026-09-25) lists no AI statute for Florida, Georgia, South Carolina, or North Carolina. Colorado SB26-189 does not apply (no Colorado operations). The chatbot still discloses that it is AI at the start of every chat |
| Sector AI rules | None identified | The vertical overlay lists no Communications-specific AI rule |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person, or able to affect physical safety or critical infrastructure operations.

| ID | Use case | Tier | Status | Council review |
|---|---|---|---|---|
| AI-001 | Customer-service chatbot with account access | Medium | In production | Reviewed 2026-01-21; re-reviewed 2026-08-19 |
| AI-002 | Agent assist (transcription, summary, next steps) | Medium | In production | Reviewed 2026-03-18 |
| AI-003 | Network anomaly detection and predictive maintenance alerts | Medium | In production | Reviewed 2025-11-12 |
| AI-004 | Closed-loop remediation for broadband gateways and OLT ports | High | Pilot (one region) | Reviewed 2026-06-17 |
| AI-005 | Identity and fraud risk scoring at account opening (deposits, manual review) | High | In production | Not reviewed (due 2026-11-30) |
| AI-006 | Churn prediction and retention offers | Medium | In production | Reviewed 2025-12-10 |
| AI-007 | Collections prioritization and payment arrangement eligibility | High | In production | Reviewed 2026-04-15 |
| AI-008 | Field technician route and schedule optimization (AQ-02) | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-009 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-04-08 |
| AI-010 | SOC alert triage assistant | Low | In production | Reviewed 2026-02-25 |
| AI-011 | Call transcription and summarization for SL-2 customers | Medium | Pilot (14 customers) | Not reviewed (due 2026-11-30) |
| AI-012 | Applicant resume screening and ranking (AQ-03 HR system) | High | Suspended | Not reviewed (due 2026-11-30) |

**Tiering notes:** AI-004 is High because automated actions on network elements can affect critical infrastructure operations, including 911 calling over VoIP; it stays in recommend mode outside one test region. AI-005 is High because it can require deposits or route orders to manual review, which affects access to an essential service. AI-007 is High because it orders the suspension work queue, even though a person approves every suspension. AI-001 stays Medium because it makes no consequential decision; the triggers in section 6.3 would re-tier it.

## 5. MEASURE and MANAGE: portfolio controls
- **Bias testing:** done for AI-001 (section 6) and AI-007 (by service area and language, 2026-04, no flag). Not done for AI-005 or AI-012; both must be tested before council approval. AI-005 testing will compare deposit and decline rates by service area and preferred language, because the vendor model uses address and device signals that can act as proxies.
- **Monitoring:** each High-tier use case and AI-001 report quarterly performance and fairness metrics (inventory column `monitoring`) to the council; threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, CPNI disclosure, bias finding, unexpected network action) are logged as SOC cases and follow P08 where security, CPNI, or service is involved. AI-004 actions that cause an outage follow the NORS and PSAP steps in P08 section 7.1.
- **Third parties:** AI vendors that receive CPNI are tier-1 vendors; contracts must bar training on company data and require 24-hour incident notice (POAM-014).
- **Decommissioning:** use cases are retired if they fail monitoring thresholds twice, change data-use terms, or are superseded at an AQ migration; the inventory records retirement.

## 6. Full assessment: AI-001 customer-service chatbot with account access
### 6.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Answer billing, outage, and plan questions and handle simple account tasks without a phone call, especially during outage call surges |
| Users / operators | Customers in web and app chat; care agents who receive escalated chats; the vendor's support staff (configuration only) |
| Affected people | About 3 million account holders and anyone who tries to use the chat; about 410,000 sessions a month; about 14% of sessions in Spanish |
| Data | Inputs: customer messages; account data from the BSS API after portal or app sign-in (balance, plan, bill lines, recent call detail, CPNI approval flag). Outputs: answers, bill explanations, payment arrangement offers from fixed BSS rules, plan suggestions. Transcripts kept by the vendor 90 days; the contract bars training on company data |
| Build or buy | Buy: vendor SaaS on a large language model platform, configured with company knowledge articles and a dedicated API client |
| Account actions allowed | Read balance, bills, plan, and recent call detail; set paperless billing (with confirmation); relay a BSS payment arrangement offer; open a repair ticket |
| Not intended | Password, address of record, or authentication changes; disconnection or suspension; credits or adjustments; number porting; deposits. None is enabled; enabling any requires re-assessment |

### 6.2 What changed since the first review
- **Authentication:** the chatbot shows account data only after portal or app sign-in, which meets 64.2010(c) and (e) for the main company. AQ-02 customers cannot use account features in chat until the AQ-02 reset is fixed (POAM-006).
- **CPNI-based suggestions:** plan suggestions for voice customers use call detail only when the BSS approval flag allows it (64.2007(b)); otherwise suggestions use non-CPNI data only. Verified in 50 test sessions on 2026-08-11.
- **API allow-list:** on 2026-08-04 the red team found that 2 of 60 prompts led the chatbot to call a service feature endpoint outside the intended action list. The gateway now enforces the allow-list for the chatbot's API client (since 2026-08-11); a retest of the same 60 prompts on 2026-08-12 produced no action outside the list.

### 6.3 Risk tier
Medium (section 4). Escalation triggers (re-tier to High and re-assess): any authentication or address-of-record change through chat; deciding credits, deposits, payment arrangement eligibility, or suspensions; a spoken voice channel; CPNI-based marketing through the chatbot at scale.

### 6.4 MEASURE (2026-05 to 2026-07; tests 2026-08-04 to 2026-08-12)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Monthly sample of 200 transcripts graded against the knowledge base and BSS data; incorrect billing or policy answers under 3% | 600 transcripts: 4.9% incorrect overall (mostly late fee and payment arrangement rules) | **No** |
| Safe | Outage and 911 questions route to published guidance; no advice to unplug equipment during 911 outages | 40 of 40 outage prompts correct; 911 prompts routed to recorded guidance | Yes |
| Secure and resilient | Red-team set of 60 prompt injection and data extraction prompts; no access to another customer's data; no action outside the allow-list | No cross-account access (the API enforces the session's account). 2 of 60 out-of-list actions before gateway enforcement; 0 of 60 after | Yes (after fix) |
| Accountable and transparent | AI disclosure at chat start; hand-off to a person on request; transcripts exportable | Disclosure shown; hand-off works; export on request works | Yes |
| Explainable and interpretable | Billing answers cite the bill line or knowledge article used | Citations shown for 78% of billing answers | **Partial** |
| Privacy-enhanced | Online CPNI only after sign-in (64.2010(c)); approval checked before CPNI-based suggestions; no vendor training on company data; 90-day transcript deletion; 24-hour incident notice | All met except incident notice, which the contract sets at 72 hours (POAM-014) | **Partial** |
| Fair, with harmful bias managed | Compare by chat language (English, Spanish) and customer type (year-round residential, seasonal residential, business): incorrect-answer rate, task completion, escalation rate. Flag a group whose incorrect-answer rate exceeds the baseline by more than 3 points or whose task completion is more than 10 points lower | Spanish: 9.8% incorrect vs 4.1% English; task completion 31% vs 46%. Seasonal and business customers within thresholds | **No** (language disparity) |

**Bias finding.** Spanish-speaking customers get wrong billing answers more than twice as often and finish tasks less often. In the company's service area, that means one group of customers is more likely to be misled about what they owe. Until the vendor shows parity, Spanish billing and payment questions route straight to a bilingual agent (live 2026-10-15), and the Spanish knowledge articles are being rewritten. The CPNI notice is already fully translated (64.2008(c) requires all portions be translated if any are).

**Why these groups.** The chatbot does not collect race, age, or disability data, and the company does not want to collect it for this purpose. Language is recorded for every session and customer type is in the BSS, so these comparisons need no new sensitive data.

### 6.5 MANAGE
**Human-in-the-loop design:**
- Actions are limited to an allow-list enforced at the API gateway, not only in the prompt.
- Every account change needs an explicit customer confirmation.
- Credits, adjustments, disputes, suspensions, deposits, and any authentication change go to a person.
- Customers can ask for a person at any time; the hand-off carries the transcript.

**Monitoring:**
- Monthly 200-transcript accuracy sample, reported by language, to the Chief Customer Officer and the council (P01 R-027).
- Weekly report of API calls rejected by the allow-list, reviewed by the SOC (P01 R-026).
- Quarterly red-team of 60 prompts.
- Complaints that mention the chatbot are tagged and reviewed monthly; any complaint about unauthorized release of CPNI is counted for the annual certification (64.2009(e)).

**Incident handling:**
- A chatbot disclosure of CPNI to someone other than the account holder is a suspected incident under POL-03 and follows the P08 notification matrix (64.2011).
- The NOC or customer operations can switch the chatbot to "outage messages only" mode in minutes.

**Decommissioning:**
- Stop account features and fall back to phone and portal if the vendor contract is not amended for 24-hour notice by 2026-12-31.
- Stop billing answers if incorrect answers stay above 3% for three months in a row after 2026-12-31.
- Stop immediately if a prompt injection leads to disclosure of another customer's data.

## 7. Link to the risk register and POA&M
AI-001 risks are P01 R-026 (CPNI disclosure through the chatbot) and R-027 (language accuracy gap); portfolio governance is R-030; unapproved public tools are R-029 (treatment Avoid). The review backlog and the Spanish routing are tracked as POAM-023; vendor terms as POAM-014.

## 8. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the council's recommendation of 2026-08-19:
1. **AI-001:** approved to continue with conditions: Spanish billing and payment questions routed to bilingual agents by 2026-10-15; the accuracy threshold met in two consecutive monthly samples, or billing answers limited to quoting the bill, by 2026-12-31; contract amended for 24-hour incident notice by 2026-12-31 (POAM-014).
2. **AI-004:** stays in recommend mode outside the test region until rollback tests and outage-reporting integration are complete.
3. **AI-005:** may continue in its current scope until council review by 2026-11-30; deposits above $200 and all declines stay with analysts; bias testing required before approval.
4. **AI-008 and AI-011:** may continue in current scope until review by 2026-11-30; no expansion to new SL-2 customers.
5. **AI-012:** ranking stays disabled until council review and an adverse impact analysis are complete.

# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional broadband and wired telecommunications carrier) |
| Tier / Vertical | Mid-Market / Communications |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv` |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-001, AI-002, and AI-005 |
| Assessors / date | Vice President of Regulatory Affairs (CPNI and legal), vCISO and Security Manager (security), NOC Director (AI-003), Data Analytics Manager (AI-004 technical review), 2026-08-24 to 2026-09-04 |
| Decision | Chief Operating Officer, 2026-09-17; the High-tier decision (AI-003) taken jointly with the CTO and noted by the CEO |

## 1. Summary
Four of the five tools reached production before any security or CPNI review (gap 13 in `../00_company-facts.md`): the chatbot had a limited review, and agent assist, the churn model, and the NOC tool were adopted by departments. Staff were also using public generative AI tools. None is out of control, but each needs conditions:
- **AI-001, the chatbot with account access:** its "verify me" fallback accepted SSN4 and service address, which the CPNI rules forbid for online access (47 CFR 64.2010(c)). Disabled 2026-07-24.
- **AI-002, agent assist:** transcribes every care call through a subprocessor the CCaaS vendor's SOC 2 report carves out; the recording notice does not mention AI transcription.
- **AI-003, NOC alarm correlation:** can group or down-rank an alarm on a 911-tagged circuit, which could delay the 30-minute PSAP notice. It is the only High-tier use case.
- **AI-004, churn model:** used a CPNI feature that tracked calls to competitors' sales lines (prohibited by 64.2005(b)(2); removed 2026-08-28) and does not check CPNI approval before offers.
- **AI-005, enterprise assistant:** replaces risky public tools; Low tier with data rules.

| ID | Use case | Risk tier | Main rule | Decision |
|---|---|---|---|---|
| AI-001 | Customer-service chatbot with account access | Medium | 47 CFR 64.2010(c), (e); 64.2007 | Approve with conditions |
| AI-002 | Contact center agent assist | Medium | Fla. Stat. 934.03; 64.2010(b) | Approve with conditions; expansion paused |
| AI-003 | NOC alarm correlation and predictive maintenance | **High** | 47 CFR 4.9(h); 9.19(b) | Approve with conditions |
| AI-004 | Churn prediction and next-best-offer model | Medium | 47 CFR 64.2005(b)(2); 64.2007(b); 64.2009 | Approve with conditions |
| AI-005 | Enterprise generative AI assistant | Low | POL-05 4.10 | Approve pilot with conditions |

Tiers: 1 High, 3 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Vice President of Regulatory Affairs (chair of the AI review group), because the biggest legal exposure from AI here is CPNI. The vCISO is the security lead. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.14: AI tools that use CPNI, interact with customers, or can affect network operations must be approved before use.
  - POL-04 4.3 and 4.4: CPNI only through approval-filtered views; never to track calls to competitors.
  - POL-05 4.10 and 4.11: approved tools only; recording and transcription only with the approved notice.
  - STD-05 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Security Manager. Today it lists AI-001 to AI-005 with their conditions. Public generative AI sites will be blocked at the web proxy once AI-005 is rolled out (2026-12-31).

### 2.1 Proposed lightweight AI governance process
A mid-market carrier does not need a standing AI committee with a large charter. It needs a reliable intake gate, a monthly rhythm, and clear stop rules, using existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any team wanting an AI tool, or an AI feature turned on in an existing tool (as happened with agent assist), submits a one-page intake: purpose, users, data (CPNI or not), vendor, decisions or network actions affected | Requesting business owner | 15 minutes |
| 2. Triage | Security Manager assigns a provisional tier with the repository rubric and checks the purchasing gate (no purchase order without approval, POL-01 4.9) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, CPNI review (approval checks, authentication, vendor terms), and a business reviewer. **High:** full MAP and MEASURE assessment like section 4, with a bias and performance plan and a service-impact review by the NOC | Security Manager; Vice President of Regulatory Affairs; business or NOC reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (Vice President of Regulatory Affairs, vCISO, Director of Customer Operations, NOC Director), monthly for 30 minutes. High: the group recommends; the COO and CTO decide and inform the CEO | As listed | Monthly |
| 5. Monitor | Owner reports agreed metrics monthly; High tier also gets a quarterly deep dive; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model or vendor change, new data type, new channel (for example voice), or an incident | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. Re-tier triggers are listed for each use case in section 3.

## 3. MAP
| Item | AI-001 Chatbot | AI-002 Agent assist | AI-003 NOC alarm correlation | AI-004 Churn model | AI-005 Enterprise assistant |
|---|---|---|---|---|---|
| Purpose | Answer common questions and handle simple account tasks without a call | Transcribe calls, summarize, and suggest answers | Group alarms into incidents, rank them, predict battery and optics failures | Score churn risk and suggest retention offers | Drafting and summarizing for staff |
| Users | Customers (web and app); agents receiving escalations | 60 care agents | 48 NOC staff | Marketing, care agents, chatbot | 120 pilot users |
| Affected people | About 205,000 account holders; about 41,000 sessions a month (12% in Spanish) | Callers (about 9,500 contacts a day) | Customers and the 7 PSAPs, through outage detection | Voice and broadband customers scored monthly (about 190,000) | Staff |
| Data | Customer messages; BSS data including CPNI; transcripts kept 90 days by the vendor | Call audio, transcripts, summaries (CPNI and personal information) | Alarms, telemetry, circuit tags (no personal data) | Account, billing, tickets, CDR-derived features (CPNI) | Internal documents (no CPNI allowed) |
| Build or buy | Buy (configured) | Buy (vendor feature) | Buy (configured) | Build | Buy |
| Generative AI? | Yes | Yes (summaries and suggestions) | No (classification and forecasting) | No (gradient-boosted model) | Yes |
| Can act on its own? | Limited account actions on an allow-list with customer confirmation | No | Opens and ranks tickets; no configuration changes | No | No |
| Re-tier triggers | Authentication or address changes; credit or deposit decisions; voice channel | Automatic answers without an agent | Any automated network action or alarm suppression rule | Use in credit, deposit, or service eligibility decisions | Access to customer systems or CPNI |

**Applicable rules and how they bite:**
| Rule | Use cases | Why |
|---|---|---|
| FCC CPNI rules, 47 CFR 64.2001-64.2011 (C-COMMUNICATIONS-R01) | AI-001, AI-002, AI-004 | Online authentication before CPNI (64.2010(c), (e)); call detail by phone only with a password, even if an AI suggests it (64.2010(b)); approval before using voice CPNI to market broadband (64.2007(b), 64.2009(a)); no tracking of calls to competitors (64.2005(b)(2)); campaign records (64.2009(c)); vendors' handling of CPNI is the company's responsibility (222(a)) |
| Outage and 911 rules, 47 CFR 4.9(h) and 9.19(b) | AI-003 | The PSAP clock runs from discovery; the covered 911 duty includes network monitoring of covered facilities |
| Fla. Stat. 934.03(2)(d) | AI-002 | Interception of a wire, oral, or electronic communication is lawful when all parties have given prior consent; the recording notice is the consent mechanism, so it must cover AI transcription |
| FTC Act Section 5 | AI-001, AI-004 | Accuracy of statements about broadband plans, prices, and offers; Section 5 excludes common carriers subject to the Communications Act (15 U.S.C. 45(a)(2)), which counsel reads as limited to common carrier services |
| Fla. Stat. 501.171 | AI-001, AI-002 | Exposure of Florida-defined personal information through a chatbot or transcript store |

**Laws considered and not applicable:**
- **State AI laws (Colorado SB26-189, Texas TRAIGA, Utah AI Policy Act):** the company serves only Florida addresses and does not do business in those states in the sense those laws use, and none of these tools makes a consequential decision in their categories. The chatbot still discloses that it is AI at the start of every chat.
- **Federal AI policy:** EO 14365 (2025) directs federal agencies, including the FCC, to consider a national AI disclosure framework. This review did not identify any FCC rule on AI that applies to these uses as of 2026-10-05.
- **Sector AI rules:** the vertical overlay lists none for communications.

### 3.1 AI-004: the competitor-call feature
The churn model used a feature counting each voice line's calls to the sales numbers of two competing providers. The rule is direct: a carrier "may not use, disclose or permit access to CPNI to identify or track customers that call competing service providers" (47 CFR 64.2005(b)(2)). The feature was removed on 2026-08-28, and the model was retrained without it. Counsel is advising on how to describe this in the CY2026 CPNI certification statement (P03 G-003, G-019). The intake gate now requires the Vice President of Regulatory Affairs to approve every CPNI-derived feature before training.

### 3.2 AI-002: recording consent and transcription
The IVR plays "this call may be recorded for quality and training." Callers are not told that an AI service transcribes and summarizes the call, and transcripts are stored by a subprocessor outside the CCaaS vendor's SOC 2 report (P09 VEN-07). Florida requires all-party consent to intercept a call (934.03(2)(d)), and the company's notice is how that consent is obtained, so the notice must describe what actually happens. Counsel approved new wording on 2026-09-02: "This call may be recorded and transcribed, including by automated tools, for quality, training, and to help our agents serve you." Agents must stop recording and transcription if a caller objects (POL-05 4.11).

## 4. MEASURE (by use case)
Data: production logs and samples from 2026-06-01 to 2026-08-31; tests run 2026-08-11 to 2026-08-28.

| Use case | Trustworthy characteristic | Test or metric | Threshold | Result | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Monthly sample of 50 transcripts graded against the knowledge base and BSS data | Incorrect billing or policy answers under 3% | 150 transcripts: 5% incorrect (late fees and payment arrangements) | **No** |
| AI-001 | Secure and resilient | Red-team set of 60 prompt injection and data extraction prompts | No cross-account data; no action outside the allow-list | No cross-account data; 2 of 60 prompts triggered a paperless-billing change without a request | **Partial** |
| AI-001 | Privacy-enhanced | Account data only after sign-in; approval check before offers; no vendor training on company data | All three | Fallback disabled; offers not approval-checked; training not excluded in the contract | **No** |
| AI-001 | Fair, harmful bias managed | Incorrect-answer and task-completion rates by chat language (Spanish vs English) and customer type | Gap no more than 3 points (incorrect) and 10 points (completion) | Spanish 9% vs English 4% incorrect; completion 31% vs 46% | **No** |
| AI-002 | Valid and reliable | Word error rate on 40 sampled calls; accuracy of 40 summaries against the recording | Word error under 10%; no summary with a wrong account action | 8% word error; 2 of 40 summaries recorded the wrong payment date | **Partial** |
| AI-002 | Fair, harmful bias managed | Word error rate for Spanish-language and accented-English calls vs other English calls | Gap no more than 5 points | Spanish 17% vs English 7% | **No** |
| AI-002 | Accountable and transparent | Recording notice covers AI transcription | Notice in place | Old notice until 2026-10-15 | **No** |
| AI-002 | Privacy-enhanced | No training on company data; transcripts deleted after 90 days | Contractual | Neither in contract | **No** |
| AI-003 | Safe | 911-tagged alarms are never suppressed or grouped below severity 1 | 100% | Replay of 6 months of alarms: 3 of 212 alarms on 911-tagged circuits were grouped under a lower-severity parent incident (all also seen on the raw alarm screen) | **No** |
| AI-003 | Valid and reliable | Precision and recall of incident grouping against NOC-confirmed incidents | Recall at least 98% for service-affecting incidents | Recall 96.5%; precision 91% | **Partial** |
| AI-003 | Fair, harmful bias managed | Predictive maintenance ranks failures in rural and suburban cabinet areas alike: recall by area type | Recall gap no more than 5 points | Rural 71% vs suburban 84% (fewer sensors on older rural cabinets) | **No** |
| AI-003 | Explainable and interpretable | Each grouped incident shows the alarms and rule or feature that grouped them | Available | Available | Yes |
| AI-004 | Privacy-enhanced | Only approval-filtered views; no prohibited features | Both | Competitor-call feature removed 2026-08-28; filter not yet in place | **Partial** |
| AI-004 | Fair, harmful bias managed | Retention-offer rate by preferred language and by county among customers with the same churn score band | Gap no more than 5 points | Language within 2 points; 2 rural counties 8 points lower (fewer agent contacts) | **No** |
| AI-004 | Accountable and transparent | Every model-driven campaign in the register with supervisor approval | 100% | 2 of 4 model-driven campaigns missing | **No** |
| AI-005 | Secure and resilient; privacy-enhanced | Contract bars training; DLP blocks CPNI patterns (account numbers, CDR formats) in prompts | Both | Contract term in place; DLP rules in test | **Partial** |

**Bias and fairness testing plan (all use cases).** The company does not collect race, ethnicity, age, or disability for these purposes and will not start. It compares groups it already records: chat and call language (AI-001, AI-002, AI-004), customer type (AI-001), and county or rural versus suburban service area (AI-003, AI-004). Thresholds are set in the table; any breach is reported to the AI review group the same month, with a fix or a documented reason within 60 days. Language disparities are treated as customer harm: a Spanish-speaking customer who gets a wrong bill answer or a wrong summary is more likely to be misled about what they owe.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** actions only on an allow-list enforced at the API gateway (not only in the prompt); customer confirmation for every change; credits, disputes, disconnections, and authentication changes go to an agent; customers can ask for a person at any time.
- **AI-002:** agents choose whether to use a suggestion and must edit summaries before saving; the tool never reads call detail aloud or bypasses the password step.
- **AI-003:** NOC staff keep a raw alarm view for all 911-tagged circuits; the tool cannot suppress those alarms or change configurations; the PSAP clock starts from the first raw alarm, not from the tool's incident.
- **AI-004:** offers are suggestions; campaign use needs supervisor approval and a register entry; scoring runs only on approval-filtered data.
- **AI-005:** users review outputs; no connection to customer systems.

**Monitoring:** owners report section 4 metrics monthly to the AI review group; AI-003 also gets a quarterly deep dive with the CTO. Results feed the risk register (P01 R-006, R-036 to R-040).

**Incident handling:**
- Any chatbot or agent assist disclosure of CPNI to someone other than the account holder is a suspected incident under POL-03 and follows the P08 matrix (64.2011).
- A 911-affecting alarm missed or delayed because of AI-003 is a severity 2 incident with a root-cause review; the PSAP and NORS clocks apply regardless of cause.
- Vendor incidents must be reported within 24 hours once contracts are amended (POAM-015).
- The chatbot can be switched to "outage messages only" in minutes; agent assist can be disabled per queue.

**Decommissioning criteria:**
- AI-001: stop if the contract is not amended by 2026-12-31, if incorrect answers stay above 3% for three months after 2026-12-31, or if any prompt injection exposes another customer's data.
- AI-002: stop if the notice is not updated by 2026-10-15 or the subprocessor assurance is not obtained by 2027-03-31.
- AI-003: revert to rule-based correlation if any 911-tagged alarm is suppressed after the fix.
- AI-004: stop scoring if the approval filter is not live by 2026-11-30.
- Any tool: stop if the vendor changes data-use terms or the model changes without notice.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | Sign-in only (done 2026-07-24); gateway allow-list (2026-10-31); approval check before offers (2026-11-30); Spanish billing questions routed to bilingual agents until thresholds are met; contract amendment with CPNI, no-training, 90-day deletion, and 24-hour notice terms (2026-12-31) | COO, 2026-09-17 |
| AI-002 | **Approve with conditions**; no new agents until met | New recording notice (2026-10-15); contract amendment and subprocessor assurance (2026-12-31); Spanish word error plan from the vendor; summaries editable before save | COO, 2026-09-17 |
| AI-003 | **Approve with conditions** | Rule: 911-tagged alarms never grouped below severity 1 (2026-10-31); recall target 98% for service-affecting incidents; sensor upgrades on rural cabinets in the 2027 plan; quarterly deep dive | COO and CTO, 2026-09-17; noted by the CEO |
| AI-004 | **Approve with conditions** | Competitor-call feature removed (done 2026-08-28); approval-filtered views (2026-11-30); campaign register entries; county offer-rate monitoring; Vice President of Regulatory Affairs approves new features | COO, 2026-09-17 |
| AI-005 | **Approve pilot with conditions** | DLP rules live (2026-11-15); training for pilot users; public tools blocked at the proxy (2026-12-31) | Security Manager, 2026-09-17 |

The conditions are tracked as POAM-024 in P07 (with POAM-011 for the chatbot redesign and POAM-019 for the approval filter) and in the risk register (P01 R-006, R-036 to R-040). The AI review group holds its first monthly meeting on 2026-10-06.

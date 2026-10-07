# AI Risk Assessment: Generative AI Assistant in the Workforce Scheduling Platform

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (B2B SaaS software publisher) |
| Tier / Vertical | Small / Information |
| AI use cases | AI-001: schedule summaries. AI-002: shift-swap suggestions. Both are features of the WSP's AI assistant, in beta with 40 customers since 2026-07-15 |
| Company role | **Developer and provider** of the AI features. Customers (employers) are the **deployers** who decide how their managers use them |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1) |
| Assessor / date | Director of Product and the IT Manager, with the Engineering Manager and COO, 2026-09-08 to 2026-09-11 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |
| Related items | P01 R-019, R-020, R-021, R-022; P03 G-003, G-019, G-033, G-042; P07 POAM-011; P09 vendor review V-06 |

## 1. GOVERN
- **Accountable owner:** Director of Product. **Decision authority:** the CTO and the Director of Product co-approve AI features. Because AI-002 is rated High (section 3), the Chief Executive Officer also signs its decision.
- **Why this assessment is late:** the assistant went live in beta without an AI risk assessment, bias testing, or an update to the public data-use statement (scenario gap 13). The same review step is now required by POL-01 4.8 for every new AI feature.
- **Policies that apply:**
  - POL-01 4.8: security and privacy review in design for AI features; 4.9: sub-processor review and 30-day notice; 4.10: accurate public AI statements
  - POL-04 4.5: customer data used only to provide the service, never to train models, minimum data to the model provider
  - POL-05 4.8: staff use only approved AI tools (AI-003)
- **Scale for a Small company:** there is no AI committee. The Director of Product, CTO, IT Manager, and COO review the AI inventory quarterly, and before any AI feature leaves beta.
- **Model provider:** the model is bought through an API (SYS-08). The company does not train or fine-tune models. The provider was added as a sub-processor in June 2026 with 12 days' notice instead of 30, and is on click-through API terms with no DPA (P09 V-06).

## 2. MAP
| Item | AI-001 Schedule summaries | AI-002 Shift-swap suggestions |
|---|---|---|
| Purpose | Plain-language summary of a worker's next two weeks of shifts and changes, and a weekly coverage summary for managers | When a worker asks to swap or drop a shift, rank eligible coworkers and explain why, so the manager can fill the shift faster |
| Users | Workers and managers at the 40 beta customers | Managers at the 40 beta customers |
| Affected people | Workers whose schedules are summarized (about 18,000 in the beta) | Workers who ask to swap and workers who are or are not suggested; being suggested leads to more hours and pay |
| Inputs | Structured schedule data, time-off, free-text shift notes | Eligible workers' first names, availability, hours already scheduled this week, a reliability score (share of accepted shifts worked in the last 90 days), and role qualifications |
| Outputs | Generated text shown in the app, labeled "AI-generated" | A ranked list of up to 5 coworkers with a one-line reason each; the manager picks or overrides |
| Build or buy | Company-built feature on a bought model (API) | Company-built feature on a bought model (API) |
| Not intended | Changing schedules, approving time off, anything affecting pay | Automatic approval of swaps, hiring, discipline, or pay decisions. Enabling any of these requires re-assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5 (N51-R01) | **Yes** | Deception: the release notes called AI-002 "fair and unbiased" without testing (P03 G-042), and the public statement that customer data is used only to run schedules does not mention the model provider (G-033). Unfairness: unreasonable handling of worker data in prompts. The FTC's proposed AI-accuracy policy statement (Docket FTC-2026-0727) is **not final** and is a watch item only |
| Customer DPA and CCPA service-provider terms (N51-R03) | **Yes** | Customer data may be used only to provide the service. Sending it to a new sub-processor required 30 days' notice and a DPA. Training on customer data is not allowed |
| CPPA ADMT regulations, Cal. Code Regs. tit. 11, 7001 and 7200 et seq. (N51-R03) | **Customer-side, for AI-002.** Applies to customers that are CCPA businesses | A "significant decision" includes "allocation or assignment of work for employees" (7001(ddd)(4)(B)). Use of ADMT for such decisions must comply by 2027-01-01 (7200(b)). A tool is not ADMT when a human reviewer knows how to interpret the output, reviews it with other relevant information, and has authority to change the decision (7001(e)(1)). **Design AI-002 so customers can show that kind of human involvement**, and give them documentation for their own notices |
| Colorado SB26-189, automated decision-making technology (effective 2027-01-01) | **Possibly, for AI-002** | Developers of ADMT that materially influences consequential decisions, including employment, must give deployers documentation (intended uses, data categories, limitations, human-review instructions). Customers in 46 states are likely to include Colorado employers. Counsel to confirm by 2026-12-15 whether shift allocation is in scope; prepare the documentation either way |
| Federal and state employment anti-discrimination law (for example, Title VII disparate impact) | **Customer-side** | Employers are responsible for discriminatory effects of tools they use. Several state and local laws on AI in employment decisions add notice or testing duties for employers. The company supports customers with test results and documentation |
| 29 CFR 1607.4(D) (Uniform Guidelines, "four-fifths rule") | **Used as a screening benchmark** | A selection rate for a group below 80% of the highest group's rate is generally regarded by federal enforcement agencies as evidence of adverse impact. Used here as a test threshold, not as a legal conclusion |
| DOJ Data Security Program (N51-R04) | No | The model provider is U.S.-based; no covered data transactions (P03 1.4) |

## 3. Risk tier
Repository rubric (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`):

| Use case | Tier | Why |
|---|---|---|
| AI-001 | **Medium** | It interacts directly with workers and managers, and an error can make a worker miss a shift (R-021). It makes no decision; the full schedule is one tap away |
| AI-002 | **High** | Being suggested for a shift means more hours and pay, which is an employment decision. A manager approves every swap, but the ranking is likely to be **a substantial factor**: in the beta, managers picked the top-ranked coworker in 78% of approved swaps |

**Escalation triggers (re-tier and re-assess):** automatic swap approval; use for hiring, discipline, or pay; adding new inputs such as attendance or productivity scores; general availability to all customers; a change of model provider.

## 4. MEASURE
Tests run 2026-09-08 to 2026-09-11 on beta data from 2026-07-15 to 2026-09-04 and on synthetic test tenants.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable (AI-001) | 400 sampled summaries compared with structured schedule data. Critical errors (wrong day, time, or location) must be 0; minor errors under 2% | 2 critical errors (wrong day), 4 minor (1.5%) | **No.** Critical-error threshold missed |
| Valid and reliable (AI-002) | Suggested coworkers must be eligible (role, availability, overtime limits) | 100% of 1,000 synthetic requests returned only eligible coworkers | Yes |
| Safe | Human action required for every change | Summaries change nothing; every swap needs manager approval | Yes |
| Secure and resilient | Prompt injection red-team (20 cases in free-text shift notes); tenant scoping of prompts | 3 of 20 injections changed the output wording; none revealed another worker's or tenant's data | **Partial** (R-022) |
| Accountable and transparent | Outputs labeled AI-generated; public data-use statement and sub-processor notice accurate | Labels present; data-use statement and notice not updated; "fair and unbiased" claim unsupported | **No** |
| Explainable and interpretable | AI-002 gives a reason per suggestion that matches its inputs | 96% of 200 sampled reasons matched the inputs | Yes, monitor |
| Privacy-enhanced | Minimum data in prompts; no retention or training by the provider, in a signed contract | First names sent without need; zero-retention setting on but not in a signed contract | **No** |
| Fair, with harmful bias managed (AI-002) | See the bias testing plan below | Two tests failed | **No** |

### Bias testing plan and results (AI-002)
The platform does not hold race, sex, age, religion, or disability data, so tests use counterfactual inputs and available proxies.

| Test | Groups compared | Metric and threshold | Result |
|---|---|---|---|
| T1. Name counterfactual | Same synthetic request, only the first name changed among names commonly associated with different sexes and ethnicities (1,000 requests) | Top-3 membership should change in no more than 1% of requests | **4.1%. Fail.** Names influence the ranking |
| T2. Preferred language | Workers with a non-English preferred language vs English (beta data, 6,200 swap requests) | Impact ratio of top-3 suggestion rates at least 0.80 (29 CFR 1607.4(D) benchmark) | 0.91. Pass |
| T3. Recurring declared unavailability | Workers with a recurring weekly unavailable day (a possible proxy for religious observance, caregiving, or disability accommodation) vs others | Impact ratio at least 0.80 | **0.71. Fail.** The reliability score counts declined offers on declared-unavailable days against workers |
| T4. Part-time vs full-time | Part-time vs full-time workers, controlling for availability | Impact ratio at least 0.80 | 0.86. Pass |

**Retesting:** T1 to T4 before general availability, after any model or prompt change, and quarterly on production data. Results are shared with customers on request, as P10 conditions below require.

## 5. MANAGE
**Fixes before AI-002 leaves beta:**
1. Remove worker names from prompts; refer to workers by an internal token and add names back after ranking (fixes T1; also R-020 and P03 G-003).
2. Change the reliability score so declined offers on declared-unavailable days do not count (fixes T3).
3. Rerun T1 to T4; all must pass.

**Human-in-the-loop design (AI-002):**
- The manager sees all eligible coworkers, not only the top 5, with the inputs behind each reason.
- The manager must approve every swap and can pick anyone eligible. The "approve top suggestion" one-click button is removed.
- Customers get a written guide on how to interpret the ranking and when to override, matching the human-involvement elements in the CPPA ADMT rules.
- Customer administrators can turn AI-002 off for their tenant, and workers can see that swaps are suggested with AI help.

**Accuracy control (AI-001):** an automated consistency check compares every summary with the structured schedule before display and falls back to the standard schedule view if they differ (R-021).

**Security (both):** only the requesting user's permitted data goes into a prompt; shift notes are filtered for instructions; the 2027 penetration test covers the assistant (R-022).

**Data and contracts:** signed DPA with the model provider with no-training and zero-retention terms; customers re-noticed with a 30-day objection window; public data-use statement updated to describe the AI assistant and the model provider (R-019; POAM-011).

**Monitoring:**
- Monthly: 100 summaries sampled for accuracy; AI-002 override rate and top-pick rate by customer.
- Quarterly: bias tests T1 to T4; results to the quarterly AI review.
- Customer complaints about the assistant go to the Director of Product and are logged.

**Incident handling:** a wrong or harmful output that reaches workers is handled as an incident under POL-03, with the feature flag turned off first if needed. A model provider security incident follows P08 and the DPA notice terms.

**Decommissioning:** the feature flag switches off either feature at once for one tenant or all tenants. If the DPA is not signed by 2026-10-31, calls to the model provider stop and the assistant is switched off.

## 6. Decision
**Decided 2026-09-22.** CTO and Director of Product for AI-001; CTO, Director of Product, and Chief Executive Officer for AI-002.

- **AI-001 (schedule summaries): approved with conditions** to continue in beta with the 40 customers. The consistency check must be live by 2026-11-30. General availability requires zero critical errors in two consecutive monthly samples.
- **AI-002 (shift-swap suggestions): beta continues in unranked mode only.** Managers see eligible coworkers without a ranking until fixes 1 to 3 are done and T1 to T4 pass (target 2026-11-30). No general availability before then.
- **Conditions for both, by 2026-10-31:**
  1. Signed DPA with the model provider, including no-training and zero-retention terms (POAM-011).
  2. Re-notice to customers with a 30-day objection window, and an updated public data-use statement.
  3. The "fair and unbiased" claim withdrawn (done by 2026-10-15, P03 G-042).
  4. Customer documentation for AI-002: intended use, inputs, limitations, test results, and human-review guidance (supports customers under the CPPA ADMT rules and Colorado SB26-189).
- **Next review:** before general availability of either feature, and no later than 2027-03-31.

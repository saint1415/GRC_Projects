# AI Governance Risk Assessment: Enterprise AI Portfolio and AI Assist

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded B2B SaaS software publisher) |
| Tier / Vertical | Enterprise / Information |
| Scope | Enterprise AI portfolio (16 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001 AI Assist, the generative AI feature embedded in the Operations Cloud, in section 7 |
| Company role | **Developer and provider** for product AI (AI-001 to AI-008), where customers are the deployers; **deployer** for internal AI (AI-009 to AI-016) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1); repository risk tier rubric |
| Assessor / date | AI governance council (chaired by the Chief Data and AI Officer), meeting of 2026-08-19; GRC team prepared the portfolio review; red-team and evaluation results from the AI platform engineering team |
| Decision | Executive risk committee, 2026-09-08 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 16 |
| Risk tier | High 4, Medium 8, Low 4 |
| Status | In production 13, Pilot 2, Suspended 1 |
| Council review complete | 11 of 16 |
| Not yet reviewed | 5: AI-002, AI-006, AI-007, AI-008, AI-012 (all due 2026-11-30, or before any re-enable for AI-012) |
| Product AI where the company is the developer | 8 (AI-001 to AI-008), 3 of them High tier because customers can use them in employment or financial decisions |

**Main findings:**
1. **AQ-01's AI was never reviewed.** AI-007 and AI-008 came with the acquisition, and AQ-01 trains pooled models on shared customers' transcripts, which contradicts the company's statement and the CCPA service provider use limit (P03 G-034, G-055; POAM-020).
2. **AI Assist (AI-001) works well but is open to indirect prompt injection** through case content (P07 SI-10; POAM-018), and quality is lower for some consumer languages.
3. **Customers lack developer documentation** for the High-tier product features (AI-002, AI-004, AI-008) that the CPPA ADMT rules and Colorado SB26-189 expect them to have from 2027-01-01.
4. **One internal High-tier tool (AI-012) is suspended** until review and a bias audit.

## 2. GOVERN: AI governance council operating model
**Charter.** The AI governance council was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the cybersecurity and risk committee of the board reviews quarterly.

**Members:** Chief Data and AI Officer (chair); Chief Product Officer; Chief Privacy Officer; CISO; Chief Compliance Officer; General Counsel's delegate; Chief People Officer (for workforce and HR tools); Director of Product Security; a customer advisory representative from the Enterprise customer council; the AI platform engineering lead. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production or general availability |
|---|---|---|
| High | Council vote, then the executive risk committee | Impact assessment; bias and quality testing on representative data; human review design; developer documentation for customers; red-team testing; monitoring plan |
| Medium | Council vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review; red-team testing for generative features |
| Low | Council chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside vendor products and AI that arrives through an acquisition, must be registered before use (POL-05 4.6; STD-05.3; POL-01 4.10). The software factory blocks release of a feature flagged as AI without an inventory ID. The GRC team owns the inventory.

**Policies:** POL-04 4.4 (customer data never trains models serving other customers), 4.8 (no Restricted data in AI tools without council approval and no-training, zero-retention terms); POL-05 4.6 (approved tools only), 4.9 (no unapproved AI claims); POL-01 4.13 (AI statements reviewed against evidence); STD-05.3 (approved AI tools list).

**Cadence:** monthly council meetings; quarterly monitoring review for every High-tier use case; annual re-review of every use case; red-team testing before each major release of a generative feature.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5 (N51-R01) | **Yes** | AI claims must be substantiated (AI Assist "grounded only in your own knowledge base," P03 G-043), and data-use statements must be true (no cross-customer training, G-034). Unreasonable security of AI features can be unfair. The FTC's proposed AI-accuracy policy statement (Docket FTC-2026-0727) is **not final** and is a watch item only |
| Customer DPA and CCPA service provider rules (N51-R03) | **Yes** | Customer data may be used only for that customer. A service provider may use personal information to improve its services only if it does not use it to perform services for another person (Cal. Code Regs. tit. 11, 7050(a)(3)); AQ-01 pooled training fails this test |
| CPPA ADMT rules (Cal. Code Regs. tit. 11, 7200 et seq.) | **Customer-side for product AI; company-side for AI-012** | Businesses using ADMT for significant decisions (including employment, financial or lending services, and health care, 7001(ddd)) must comply by 2027-01-01 (7200(b)). Customers using AI-002, AI-004, or AI-008 in such decisions need pre-use notices, opt-out or appeal handling, and access responses; the company provides documentation and product settings. The company is itself the business for AI-012 |
| CPPA risk assessments (7150) | **Company-side for AI-012 and AI-014 review; customer-side for AI-008** | 7150(b)(3) covers ADMT for significant decisions; 7150(b)(4) covers automated inferences about performance at work |
| Colorado SB26-189 (effective 2027-01-01) | **Yes, as developer** for product AI used in consequential decisions; **as deployer** for AI-012 | Developers must give deployers documentation (intended uses, training data categories, limitations, human-review instructions) and notice of material updates; deployers give notices and human review. Customers in every state include Colorado businesses, and the company has a Colorado office |
| Utah AI Policy Act (Utah Code 13-72, 13-75) | **Customer-side** for AI-007 and AI-001 replies | Generative AI in consumer transactions must disclose that it is AI when clearly asked; the product supports a disclosure message. The act's repeal date is July 1, 2027 (SB 332) |
| Texas Responsible AI Governance Act (HB 149, effective 2026-01-01) | **Yes, low exposure** | No size threshold; prohibitions are intent-based (for example, AI developed with intent to unlawfully discriminate); disclosure duties fall on government agencies and health care service providers, which are customers |
| Employment AI laws (Illinois HB 3773; NYC Local Law 144; California Civil Rights Council ADS regulations) and Title VII | **Yes, for AI-012** | Notice, bias audit (NYC, within 1 year before use for NYC roles), and anti-discrimination duties. EEOC's 2023 technical assistance page was removed, but Title VII disparate impact liability remains by statute |
| California SB 53 (frontier AI) | **No** | The company does not train models with more than 10^26 operations; it fine-tunes smaller models |
| OMB M-26-04 (Unbiased AI Principles for federal LLM procurement) | **Watch** | AI Assist is not enabled in the Government Edition. If agencies request it, new solicitations will carry these terms and a FedRAMP significant change review is needed |
| DOJ Data Security Program (N51-R04) | **Screening** | All three model providers are U.S. companies processing in the United States; checked in the sub-processor reviews |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person, or able to affect physical safety. For product AI, the tier reflects how customers can foreseeably use the feature.

| ID | Use case | Tier | Status | Council review | Company role |
|---|---|---|---|---|---|
| AI-001 | AI Assist: generative case summaries, reply drafts, and knowledge article drafts in the Operations Cloud | Medium | In production (generally available to about 2,300 customers) | Reviewed 2025-11-12; re-reviewed 2026-08-19 | Developer and provider |
| AI-002 | AI Assist agent actions: model proposes account actions (credits, refunds, plan changes, case closure) that an agent confirms with one click | High | Pilot (24 customers; non-financial actions only since 2026-08-19) | Not reviewed (review due 2026-11-30; required before general availability) | Developer and provider |
| AI-003 | Case routing and priority suggestions (machine learning) in the Operations Cloud | Medium | In production | Reviewed 2026-03-11 | Developer and provider |
| AI-004 | Field service schedule optimization: assigns jobs to customers' technicians | High | In production (about 1,900 customers) | Reviewed 2026-05-20 | Developer and provider |
| AI-005 | Data Cloud propensity and churn scores | Medium | In production | Reviewed 2026-02-18 | Developer and provider |
| AI-006 | Data Cloud natural-language analytics assistant (generative) | Medium | Pilot (60 customers) | Not reviewed (review due 2026-11-30) | Developer and provider |
| AI-007 | Conversational AI virtual agents for customers' chats and calls (AQ-01) | Medium | In production (about 1,150 customers) | Not reviewed (AQ-01 pre-acquisition; review due 2026-11-30) | Developer and provider |
| AI-008 | Conversation sentiment and agent quality scoring (AQ-01) | High | In production (about 400 customers) | Not reviewed (AQ-01 pre-acquisition; review due 2026-11-30) | Developer and provider |
| AI-009 | Engineering code assistant | Low | In production | Reviewed 2025-12-03 | Deployer |
| AI-010 | Enterprise generative AI assistant for workforce productivity | Low | In production | Reviewed 2025-12-03 | Deployer |
| AI-011 | SOC alert triage assistant | Low | In production | Reviewed 2026-01-21 | Deployer |
| AI-012 | Recruiting: resume summarization and skills matching in the HR system | High | Suspended (matching disabled 2026-06-30; summaries only) | Not reviewed (review and bias audit required before re-enable) | Deployer |
| AI-013 | Support ticket classification and suggested responses for company support staff | Medium | In production | Reviewed 2026-04-15 | Deployer |
| AI-014 | Sales lead scoring in the CRM | Medium | In production | Reviewed 2026-02-04 | Deployer |
| AI-015 | Contract and invoice analysis for finance and legal | Low | In production | Reviewed 2026-03-11 | Deployer |
| AI-016 | Trial sign-up fraud and abuse scoring | Medium | In production | Reviewed 2026-05-06 | Deployer |

**Tiering notes:** AI-001 stays Medium because a customer's agent reviews and sends every reply and summaries make no decision; enabling automatic sending or using AI-001 outputs to decide eligibility would re-tier it to High. AI-002 is High because one-click credits and refunds at banking customers can be a substantial factor in fee and account decisions; it is limited to non-financial actions until reviewed. AI-004 and AI-008 are High because customers use them to allocate work and to evaluate employees.

## 5. Product AI: developer duties to customers
| Duty | What the company does | Status |
|---|---|---|
| Documentation for deployers (Colorado SB26-189; supports CPPA ADMT compliance by customers) | Documentation pack per feature: intended and prohibited uses, data categories used, known limitations and test results, human-review instructions, how to turn the feature off | Not yet published (POAM-018 milestone, 2026-12-15) |
| Notice of material updates | Release notes flag model or prompt changes that affect outputs; 30 days' notice for High-tier features | In place for AI-001 and AI-003; not for AQ-01 features |
| Customer controls | Tenant-level on and off switches; action limits for AI-002; disclosure message for AI-007; data retention settings | In place except AI-008 retention settings |
| No cross-customer training | AI-001 to AI-006 use per-tenant retrieval or per-tenant models; model providers under no-training and zero-retention terms | **Not met for AI-007 and AI-008** (POAM-020) |

## 6. MEASURE: testing plan for the product portfolio
| Use case | Metric | Groups compared | Threshold for action |
|---|---|---|---|
| AI-001 | Minor-error rate in summaries and drafts | Consumer language (English, Spanish, other) | Any language more than 3 points above English |
| AI-002 | Share of proposed actions overridden by agents; injection test pass rate | Action type | Override rate above 10% or any injection-triggered action |
| AI-003 | Time to first response for suggested priorities | Consumer language; region | Ratio below 0.8 for any group |
| AI-004 | Share of high-value jobs assigned | Technician tenure; part-time status; region | Impact ratio below 0.80, using the four-fifths benchmark in 29 CFR 1607.4(D) as a screening threshold, not a legal conclusion |
| AI-008 | Sentiment and quality scores for the same scripted call | Accent and language of the agent (synthetic voice tests) | Score gap above 5 points |

## 7. Full assessment: AI-001 AI Assist
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Help customers' service agents work faster: summarize long cases, draft replies grounded in the tenant's own knowledge base, and draft knowledge articles from resolved cases |
| Users | Agents and knowledge managers at about 2,300 customers |
| Affected people | Customers' consumers, whose cases are summarized and who receive replies; customers' agents |
| Data | Inputs: case text and history and knowledge articles of the same tenant. Outputs: drafts and summaries stored in the tenant. Prompts go to one of three contracted model providers under no-training and zero-retention terms |
| Build or buy | Company-built orchestration, retrieval, and checks on bought models |
| Not intended | Sending replies without agent review; eligibility, credit, claims, or health care decisions; use in the Government Edition |

### 7.2 Risk tier
Medium (section 4). Escalation triggers: automatic sending, any use in eligibility or pricing decisions, adding consumer-facing chat without an agent, enabling in the Government Edition, or a change of model provider.

### 7.3 MEASURE (tests 2026-07-06 to 2026-08-14)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 600 sampled replies checked for content not found in the tenant's knowledge base or case (target under 2%) | 18 of 600 (3%) contained ungrounded content | **No** |
| Safe | Agent must send every reply; no automatic sending | Confirmed in configuration and logs | Yes |
| Secure and resilient | 20 indirect prompt injection cases placed in case text; 1,000 synthetic cross-tenant retrieval probes | 4 of 20 injections changed summaries and 1 produced a suggested agent action; 0 cross-tenant retrievals | **Partial** (POAM-018) |
| Accountable and transparent | Drafts and summaries labeled AI-generated for agents; product page claims accurate | Labels present; the "grounded only in your own knowledge base" claim is not fully supported (P03 G-043) | **No** |
| Explainable and interpretable | Each draft shows the knowledge articles it used | Citations shown for 92% of drafts | Yes, monitor |
| Privacy-enhanced | No-training and zero-retention terms with all three providers; prompts limited to the requesting tenant | Terms signed; tenant scoping confirmed | Yes |
| Fair, with harmful bias managed | Minor-error rate by consumer language (sample of 900 drafts, 300 per group) | English 3.2%, Spanish 6.1%, other languages 7.4% | **No** (language gap) |

### 7.4 MANAGE
- **Prompt injection:** separate untrusted case content from instructions in prompts, filter instructions in retrieved text, and require explicit agent confirmation for every tool action (POAM-018, by 2026-12-31). Injection tests run in CI for every release.
- **Groundedness:** block drafts below a groundedness threshold and show citations for every draft; change the product page claim to describe retrieval accurately (by 2026-10-30, P03 G-043).
- **Language gap:** language-specific prompts and evaluation sets for Spanish and the next five languages by volume; agents see a "review carefully" banner for languages below threshold until the gap is under 3 points.
- **Monitoring:** monthly 600-draft groundedness sample; quarterly language-quality review; red-team before each major release; customer complaint tracking.
- **Incidents:** a harmful or wrong output that reaches consumers is handled as an incident under POL-03, with the tenant or global feature flag turned off first if needed; a model provider security incident follows P08.
- **Decommissioning or provider change:** each feature can be switched off per tenant or globally; a provider change is a re-assessment trigger and needs the tested failover in POAM-017.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier use case has quarterly quality and fairness metrics (inventory column `monitoring`) reported to the council; threshold breaches trigger re-review.
- **Acquisitions:** AI that arrives through an acquisition is registered on the day of closing and reviewed within 90 days; AQ-01 missed this because the rule was adopted afterwards.
- **Third parties:** model providers are tier-1 sub-processors with no-training and zero-retention terms, annual attestations (P01 R-015), and 30 days' customer notice when added.
- **Resilience:** single-provider dependency for each AI Assist feature is tracked in P05 (DEP-08) and P01 (R-041).

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the council's recommendation of 2026-08-19:
1. **AI-001 AI Assist:** approved to continue with conditions: injection fixes and CI tests by 2026-12-31 (POAM-018); product page claim corrected by 2026-10-30; language plan in 7.4 with the gap under 3 points by 2027-03-31, or Spanish and other affected languages are labeled for careful review until it is.
2. **AI-002 agent actions:** stays in pilot with non-financial actions only; council review and High-tier requirements (including customer documentation) before general availability.
3. **AI-007 and AI-008 (AQ-01):** pooled training on customer transcripts stopped by 2026-10-15; affected models retrained on permitted data or retired, and customers notified by 2026-11-30 (POAM-020); council reviews by 2026-11-30; no new customers for AI-008 until review.
4. **AI-004 and AI-008:** developer documentation packs published by 2026-12-15 so customers can meet the CPPA ADMT and Colorado requirements from 2027-01-01.
5. **AI-006:** may continue in pilot until council review by 2026-11-30.
6. **AI-012:** matching stays disabled until council review, a bias audit, and counsel's confirmation of notice duties (NYC, Illinois, California, Colorado).

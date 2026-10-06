# AI Governance Risk Assessment: AI and Model Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed payment processor serving merchants) |
| Tier / Vertical | Mid-Market / Financial Services |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005); inventory in `ai-use-case-inventory.csv`. Primary use case: AI-001 transaction fraud-detection model |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-003, AI-004, and AI-005 |
| Assessors / date | Chief Risk and Compliance Officer (model risk), Director of Fraud and Merchant Risk, Head of Data Science (developer input, not an approver), Director of Information Security, and the General Counsel, 2026-08-17 to 2026-09-04; independent challenge by an outside model risk firm for AI-001 |
| Decision | Chief Operating Officer, 2026-09-15, on the recommendation of the AI and model risk committee; High-tier decisions reported to the CEO and the audit committee the same day |

## 1. Summary
The company built its own fraud model in 2025 and adopted four other AI tools without a security, privacy, or model risk review (gap 13 in `../00_company-facts.md`). None is out of control, but two make or drive decisions about people at scale and need model risk controls the company does not yet have:
- **AI-001, the fraud model**, declines consumer purchases automatically on both platforms. The people who built it also validate it, and the first fairness test (2026-08-20) flagged one group.
- **AI-002, the merchant risk scoring service**, sets approval and reserves for merchants, including sole proprietors. No one has validated it or tested it for bias, and underwriters do not see its reason codes.
- **AI-003 and AI-004** are generative AI tools that touch dispute and merchant data; **AI-005** writes code that can reach the CDEs.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Transaction fraud-detection model (built in house) | High | Approve continued production with conditions |
| AI-002 | Merchant underwriting and risk monitoring (vendor score) | High | Approve continued production with conditions; validation and bias test by 2026-12-31 |
| AI-003 | Dispute representment drafting assistant | Medium | Approve with conditions |
| AI-004 | Merchant support chatbot | Medium | Approve with conditions; PAN masking by 2026-12-31 or switch off free-text entry |
| AI-005 | Engineering code assistant | Low | Approve with conditions (labeling and review) |

Tiers: 2 High, 2 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI and model program:** Chief Risk and Compliance Officer, who chairs the **AI and model risk committee** (Director of Fraud and Merchant Risk, Director of Information Security, General Counsel, CTO, and the Head of Data Science as a non-voting member). Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.17: AI tools and models must be approved before use.
  - POL-04 4.8 and 4.11: training data tokenized and minimized; no Restricted data in unapproved AI tools.
  - POL-05 4.7 and 4.8: approved tools only; human review of outputs; AI-assisted code labeled and reviewed.
  - STD-10 AI and model risk standard: due 2026-12-31.
- **Approved-tools list:** kept by the Director of Information Security on the intranet since 2026-09-15. It lists AI-003 to AI-005 and an enterprise generative AI assistant with no-training terms. Unapproved generative AI sites are blocked on managed devices from 2026-10-31 (R-023).

### 2.1 Model risk management at this size
A mid-market processor does not need a large model risk department. It needs four things the company lacks today:

| Element | What it means here | Status |
|---|---|---|
| Model inventory | Every model and AI tool, its owner, tier, data, and last validation | Created by this assessment (`ai-use-case-inventory.csv`) |
| Independent validation | Someone other than the developers checks conceptual soundness, data, performance, and fairness before production and at least annually for High-tier models | **Not done.** Data science validates its own model. An outside model risk firm is engaged for AI-001 (first report due 2027-03-31) and AI-002 (2026-12-31) |
| Change control for models | Each new model version passes validation tests, a bias test, and a sign-off by the business owner before release; the prior version is kept for rollback | Partly: release tests exist for AI-001; no bias gate until 2026-10 |
| Ongoing monitoring | Performance, drift, and fairness metrics with thresholds and owners | Partly: daily decline dashboards for AI-001; nothing for AI-002 |

### 2.2 Lightweight governance process
| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any team wanting an AI tool, an AI feature in an existing product, or a new model submits a one-page intake: purpose, users, data, vendor, decisions affected | Business owner | 15 minutes |
| 2. Triage | Provisional tier with the repository rubric; purchasing gate (no purchase order without approval) | Director of Information Security | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, data (no-training clause, retention, PAN exposure), and business review. **High:** full MAP and MEASURE assessment like this one, independent validation, bias test plan, and a legal applicability check | Committee members | Low 1 week; Medium 2 weeks; High 6 weeks |
| 4. Decide | Low: Director of Information Security. Medium: the committee (monthly). High: the committee recommends, the COO decides, and the CEO and audit committee are informed | As listed | Monthly |
| 5. Monitor | Owners report agreed metrics monthly; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new model version, new data type, new decision use, expansion to a new platform or population | Committee | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. Re-tier triggers are listed in section 3.

## 3. MAP
| Item | AI-001 Fraud model | AI-002 Merchant risk | AI-003 Dispute drafting | AI-004 Support chatbot | AI-005 Code assistant |
|---|---|---|---|---|---|
| Purpose | Score each authorization (0 to 999); the switch approves, steps up, sends to review, or declines | Score applicants and existing merchants; set approval, reserves, and limits | Draft representment letters | Answer merchant questions; hand off to agents | Suggest code and tests |
| Users | Authorization switch (automated); 18 fraud analysts | 24 underwriters; 12 merchant risk analysts | 14 dispute analysts | Merchant users | 170 engineers |
| Affected people | Consumers paying about 31,000 merchants (about 2.25 million transactions a day) | About 650 applicants a month and 31,000 merchants, including sole proprietors | Cardholders and merchants in disputes | Merchant users | None directly |
| Data | Tokens, transaction features, labels | Owner identity and bureau-derived attributes, business data, processing history | Masked PAN, merchant evidence, cardholder names | Merchant questions, deposit status | Source code |
| Build or buy | Build | Buy (configured) | Buy | Buy | Buy |
| Generative AI? | No | No | Yes | Yes | Yes |
| Not intended | Merchant pricing, cardholder profiling, credit decisions | Consumer credit; marketing | Automatic submission | Account changes; card data collection | Use with production data |
| Re-tier triggers | Use for any new decision type | Use for pricing or credit lines | Automatic submission | Account actions | Autonomous merges |

**Applicable laws and rules (MAP):**
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45 | **Yes (all)** | Unsupported claims about the fraud model to merchants and ISVs, or wrong chatbot statements about fees and funding, could be deceptive. Practices that cause substantial injury that consumers cannot reasonably avoid can be unfair (15 U.S.C. 45(n)); unjustified decline rates for some cardholder groups (R-021) and unexplained adverse merchant decisions (R-022) are the risks here |
| FTC Safeguards Rule, 16 CFR 314.4 | **Yes** | Training data and vendor data flows are customer information; vendors need contract safeguards and periodic assessment (314.4(f)) |
| PCI DSS v4.0.1 | **Yes** | Training data must never hold PAN (3.2.1); model code and AI-assisted code follow secure development (6.2); AI vendors that see masked or full card data are service providers (12.8) |
| ECOA and Regulation B, 12 CFR 1002 | **AI-001: No. AI-002: to be confirmed by counsel** | The company is not a creditor in the authorization decision; the issuer decides. Whether approving a merchant for processing with reserves is an extension of business credit is not settled here; counsel's opinion is due 2026-12-15. Until then, AI-002 decisions get adverse action reasons as a good practice |
| Colorado SB26-189 (effective 2027-01-01) | **To be assessed by counsel by 2026-12-15** | Covers developers and deployers doing business in Colorado whose automated decision technology materially influences consequential decisions, including financial or lending services, with no small-business exemption in the signed text. The company is both developer and deployer of AI-001 and a deployer of AI-002. Whether a fraud decline or a merchant approval is a consequential decision about a financial service is not settled; the company will not assume it is exempt |
| California CPPA ADMT regulations (11 CCR 7200 et seq.) | **To be assessed by counsel by 2026-12-15** | Apply to CCPA "businesses" using automated decision-making technology for significant decisions, including financial or lending services, with compliance by 2027-01-01 for existing uses. The company exceeds the CCPA revenue threshold. Whether its data is covered, given the CCPA's treatment of data subject to GLBA, and whether these are significant decisions, is not verified here |
| NYDFS AI industry letter (2024-10-16) under Part 500 | **No** | The company holds no New York license |
| Card network rules | **Yes (indirectly)** | Fraud and dispute programs depend on AI-001 and AI-003 accuracy |

## 4. MEASURE
### 4.1 AI-001 transaction fraud-detection model
Results from the 2026-08-20 test run on Q2 2026 transactions (about 205 million across both platforms), with fraud labels matured through July 2026. The outside model risk firm reviewed the test design.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Fraud detection rate (fraud value caught / total fraud value) at least 72%; overall false positive rate at most 1.2% | Detection 79%; false positive rate 0.9% | Yes |
| Valid and reliable (drift) | Weekly population stability index under 0.2 per platform; decline rate within 20% of the 13-week average | Core within limits. Integrated Payments drifted (index 0.27) after the gateway's merchant mix changed in 2026-05; nobody was alerted | **No** |
| Valid and reliable (independence) | Validation by someone other than the developers before each release | Developers validate their own releases | **No** |
| Safe | Fallback rules take over within 1 minute if scoring fails; tested quarterly | Tested 2026-06 (42 seconds) | Yes |
| Secure and resilient | Model artifacts signed; training data tokenized; only the pipeline can deploy | Signed artifacts and tokenized data; 2 data scientists can deploy directly in an emergency path that is not logged to the SIEM | Partial |
| Accountable and transparent | Model documentation (purpose, data, features, limits, owner); threshold changes logged and approved | Documentation exists for the 2025 build, not for the 3 later versions; threshold log in place | Partial |
| Explainable and interpretable | Top reason codes returned with each score and shown to analysts | Reason codes available | Yes |
| Privacy-enhanced | Training data tokens only, minimized; PAN block on load; monthly PAN discovery | All in place (POL-04 4.8); no PAN found in the last 6 monthly scans | Yes |
| Fair, with harmful bias managed | Bias testing plan below | One segment flagged | **No** |

**Bias and fairness testing plan (AI-001).** The company holds no data on cardholders' protected characteristics and must not collect it for this purpose. Unfairness can still enter through features that act as proxies: card type (prepaid cards are used more by consumers without bank accounts), BIN country, and billing ZIP code. The test looks for **unjustified differences in false positive rates**: legitimate purchases declined or challenged.

| Element | Plan |
|---|---|
| Groups compared | (1) Card type: prepaid, debit, credit. (2) BIN country: domestic and international. (3) Billing ZIP code groups: top and bottom quintile of median household income from public Census data (a proxy method, labeled as such; no individual data inferred or stored). (4) Platform: core and Integrated Payments. (5) Merchant category groups |
| Metrics | False positive rate per group; ratio to the overall rate; detection rate per group (so a fix does not simply let fraud through) |
| Threshold | Flag a group if its false positive rate is more than 1.25 times the overall rate **and** at least 0.5 percentage points higher. A flagged group needs a documented business justification or a mitigation before the next release |
| When | Before every release (pre-deployment gate from 2026-10) and monthly on production data |
| Who | The outside model risk firm runs the pre-release test until an internal validator independent of data science is hired; the Director of Fraud and Merchant Risk signs off; the committee sees results monthly |
| Records | Kept for 3 years with the model version and thresholds (POL-01 4.15) |

**2026-08-20 results:**
- **Prepaid cards:** 2.1% against 0.9% overall (2.3 times; 1.2 points). **Flagged.** Prepaid fraud is 1.4 times the average on the same merchants, so the gap is only partly justified.
- **Lowest-income ZIP code quintile:** 1.3% against 0.9% (1.44 times; 0.4 points). Not flagged (below the 0.5-point floor); watched monthly.
- **International BINs:** 2.0% against 0.9%. Not flagged after review: international fraud is 3.0 times the domestic rate on the same merchants, documented by the Director of Fraud and Merchant Risk.
- **Integrated Payments:** 1.2% against 0.8% on the core platform. Not flagged (below the 0.5-point floor), but it moves with the drift above.
- **Merchant categories:** no group flagged.

**Mitigation for prepaid cards:** retrain with a prepaid-specific feature set in the 2026-11 release. Until then, route prepaid transactions in the 800 to 949 band to step-up authentication instead of decline where the merchant supports it. Retest before release.

### 4.2 AI-002 merchant risk scoring
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Score rank-orders 12-month merchant losses (Gini at least 0.40 on the company's own book) | Not measured; the vendor's generic validation only | **No** |
| Accountable and transparent | Vendor documentation of intended use, data categories, and known limitations | Marketing summary only; documentation requested (due 2026-11-30) | **No** |
| Explainable | Reason codes shown to underwriters and usable for adverse decision notices | Available from the vendor but not shown | **No** |
| Fair, with harmful bias managed | Approval and reserve rates compared across groups | Not tested | **No** |
| Privacy-enhanced | Only the data fields the score needs are sent | 6 fields sent that the vendor does not use | Partial |

**Bias and fairness testing plan (AI-002).** Groups: legal form (sole proprietors against incorporated businesses), business age (under 2 years against older), and owner ZIP code income quintile (Census proxy, labeled as such). Metrics: approval rate, average reserve, and 12-month loss rate per group. Threshold: flag a group whose approval rate is below 80% of the most-approved group's rate, or whose reserve is more than 1.25 times the average, unless its loss rate justifies the difference. First test by 2026-12-31, then quarterly. The outside model risk firm runs it; the Chief Risk and Compliance Officer signs off.

### 4.3 Generative AI use cases (NIST AI 600-1)
| AI 600-1 risk | Use case | Relevance | Control |
|---|---|---|---|
| Data privacy | AI-003, AI-004 | Cardholder names and merchant data in prompts; merchants type card numbers into chat (R-025) | No-training and retention terms (signed for AI-003 on 2026-09-10; AI-004 renewal 2026-12); PAN detection and masking in chat by 2026-12-31 |
| Confabulation | AI-003, AI-004 | Wrong facts in a representment or wrong fee and funding answers | Analysts review every draft; chatbot answers only from approved knowledge articles; monthly sample of 100 chats reviewed |
| Information security | AI-005 | Suggested code with vulnerabilities reaching a CDE (R-024) | Label AI-assisted pull requests; security review for CDE repositories; dependency scanning everywhere (POL-05 4.8) |
| Value chain and component integration | AI-003, AI-004, AI-005 | Vendor model changes without notice | Contract clause for notice of material model changes; annual review |
| Human-AI configuration | AI-004 | Merchants may trust the chatbot for account actions | Disclosure that it is an AI; no account changes; agent handoff |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** decline at 950 and above; 800 to 949 to step-up authentication (card-not-present) or merchant review; below 800 approve, subject to merchant rules. Analysts review escalations and a monthly random sample of 300 automatic declines (150 per platform). Merchants and ISVs can allow-list customers and dispute declines through support, reviewed within 2 business days. Threshold changes need the Director of Fraud and Merchant Risk's approval, a logged reason, and a 7-day look-back.
- **AI-002:** no automatic declines. Every decline and every reserve above 10% is decided by an underwriter, who will see the vendor's reason codes from 2026-11-30 and must record the reason in the file.
- **AI-003, AI-004, AI-005:** a person reviews every output before it leaves the company or reaches a repository.

**Monitoring:**
- AI-001: daily decline-rate and false-positive dashboards per platform, with alerts at plus or minus 20% of the 13-week average (R-020); weekly drift index per platform; monthly bias test.
- AI-002: monthly approval and reserve rates by group; quarterly loss back-testing.
- AI-003 and AI-004: monthly quality sample; PAN detection alerts.

**Rollback:** the switch keeps the prior AI-001 version for 30 days. The Director of Fraud and Merchant Risk can roll back or switch to fallback rules within 15 minutes.

**Incidents:** a model failure that causes mass false declines is handled under P08 roles (RS.MA) with merchant and ISV communication; a vendor data exposure follows P08 and the notification matrix.

**Decommissioning:** replace AI-002 if the vendor cannot provide documentation and reason codes by 2027-03-31; switch off AI-004 free-text entry if PAN masking is not live by 2026-12-31.

## 6. Decision and conditions
**AI-001: approve continued production with conditions** (COO, 2026-09-15, reported to the CEO and audit committee):
1. Per-platform drift alerts live by **2026-10-15** (R-020).
2. Bias test as a pre-release gate from **2026-10-31**; prepaid mitigation in the 2026-11 release, retested before release (R-021).
3. Emergency deployment path logged to the SIEM by **2026-10-31**.
4. Independent validation by the outside model risk firm by **2027-03-31**, then annually; model documentation for every version from the next release.
5. Counsel's opinion on Colorado SB26-189 and the California ADMT rules by **2026-12-15**; if either applies, notices and human review processes in place for decisions on or after 2027-01-01 (R-046).

**AI-002: approve continued production with conditions:**
1. Vendor documentation and reason codes to underwriters by **2026-11-30**.
2. Data minimization (remove the 6 unused fields) by **2026-11-30**.
3. First validation and bias test by **2026-12-31** (R-022).
4. Counsel's opinion on ECOA and Regulation B, Colorado SB26-189, and the California ADMT rules by **2026-12-15**.

**AI-003:** approved; condition: masked PAN only, confirmed by monthly sample (from 2026-10).
**AI-004:** approved; conditions: PAN masking in chat and transcript scanning by **2026-12-31**, or free-text entry switched off; no-training terms at the 2026-12 renewal.
**AI-005:** approved; condition: labeling and review rule for AI-assisted changes live by **2026-10-31** (R-024).

All conditions are tracked in POAM-021 (P07). The AI and model risk committee reviews progress monthly and reports to the audit committee each quarter.

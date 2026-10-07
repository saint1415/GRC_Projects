# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Payment Processing, Payments Software Platform, Merchant Consulting, corporate) |
| Tier / Vertical | Multi-Sector / Financial Services |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the regulator- and brand-specific rules for the priority use cases: the transaction fraud-detection model (AI-001, focus), the merchant underwriting model (AI-002), the merchant insights assistant (AI-004), and Merchant Consulting's use of generative AI (AI-007) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27, with independent validation input from the Head of Model Risk Management; presented to the board risk committee 2026-09-10 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 2 High, 6 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Group Chief Compliance Officer, Head of Model Risk Management, and one leader per division. Approves High-tier use cases and the approved-tools list |
| Head of Model Risk Management | Second line. Independent validation of AI-001, AI-002, AI-003, and AI-005 before release and every year |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-03-02, under POL-01 4.12)
1. **Register before use.** Every AI use case that touches cardholder data or customer information, or that supports decisions about cardholders, merchants, or clients, is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: the council approves; a pre-deployment impact assessment, independent validation, and bias testing are required; monitoring is reported quarterly.
3. **Data rules.** Training data for any model is tokens only (POL-04 4.2 and 4.6); no Restricted or Confidential data in unapproved tools (POL-04 4.9); model providers sign no-training and retention terms and are overseen as service providers (POL-01 4.8; 16 CFR 314.4(f)).
4. **Division overlays.** Each division supplement adds its own rules: card brand and sponsor bank expectations for the processor, SOC 2 commitments and merchant terms for the Software division, engagement letters for Merchant Consulting.
5. **Change gate.** A material change (new model version, new provider, new feature that changes how customer data is processed, new decision role) triggers re-assessment before release.
6. **Approved tools only** for workforce generative AI (POL-05 4.6).

**Where the program fell short in 2026.** The standard was adopted after AI-001 to AI-005 were already live. The council's first inventory found that AI-001 is not monitored by cardholder segment, the Software division launched AI-004 without the change gate (scenario gap 6), and consulting staff use public chatbots with client data (AI-007).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Transaction fraud-detection model | Payment Processing | High | In production with conditions |
| AI-002 | Merchant underwriting and risk model | Payment Processing | High | In production; reason-code mapping due |
| AI-003 | Dispute evidence classifier | Payment Processing | Medium | In production |
| AI-004 | Merchant insights assistant (generative) | Software | Medium | In production for about 58,000 merchants; new enrollments paused |
| AI-005 | Gateway card-testing and API abuse detection | Software | Medium | In production |
| AI-006 | Engineer coding assistant | Software (both engineering groups) | Low | Approved |
| AI-007 | Consulting staff generative AI use | Merchant Consulting | Medium | Public chatbots being blocked; approved tool rollout |
| AI-008 | Merchant support virtual agent | Payment Processing | Medium | Pilot |
| AI-009 | Enterprise generative AI assistant | Group | Medium | Approved (pilot for 6,000 users) |

### 2.1 Transaction fraud-detection model (AI-001)
| Item | Description |
|---|---|
| Purpose and intended use | Score each authorization from 0 to 999. The switch applies the merchant's rules and the score bands to approve, step up (3-D Secure challenge for card-not-present), send to review, or decline |
| Users and affected people | The switch (automated); about 1,100 fraud operations staff; merchants (allow-lists and rules in the portal). Affected: consumers paying about 920,000 merchants (about 80 million authorizations a day) and merchants whose sales are declined |
| Data | Inputs: tokens (never PAN), amount, time, merchant category, BIN country, card type, billing ZIP code, and device and IP signals for card-not-present. Training: monthly, on tokenized history in SYS-G4 with fraud and chargeback labels |
| Build or buy | Built in house; validated by model risk management before each release and every year |
| Not intended | Credit decisions, merchant underwriting, pricing, or cardholder profiling |
| Fallback | Velocity and amount rules in the switch (P05 BP-PP06) |

| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45 | **Yes** | Claims about the model to merchants must be substantiated (45(a)); unjustified decline rates for some groups of cardholders could be argued as substantial injury consumers cannot reasonably avoid (45(n)) (P01 PP-015) |
| FTC Safeguards Rule, 16 CFR 314.4(c) | **Yes** | Training data is customer information held on a shared platform; the 2026 gateway log event (P08 section 6.6) shows why every path into SYS-G4 needs the PAN block (P01 PP-016) |
| PCI DSS v4.0.1 | **Yes** | Training data must never contain PAN (3.2.1); the model platform is a connected-to system in the processor's scope |
| ECOA and Regulation B, 12 CFR Part 1002 | **No** | The division is not a creditor here; issuers make the credit authorization decision |
| Colorado SB26-189 (effective 2027-01-01) | **Counsel opinion due 2026-12-15** | It covers automated decision technology that materially influences consequential decisions, including financial or lending services. Whether an automatic decline of a purchase is such a decision is not settled; the group will not assume it is exempt |
| CPPA ADMT regulations (N51-R03) | **Not expected** | Cardholder data subject to GLBA is exempt at the data level (Cal. Civ. Code 1798.145(e)); counsel confirms with the CCPA applicability decision (POAM-021) |
| NYDFS AI industry letter (2024-10-16) | **No** | Guidance for entities regulated under 23 NYCRR Part 500; no group entity holds a New York license |
| Card brand rules | **Yes (indirectly)** | Merchant fraud and dispute thresholds depend on the model working well |

### 2.2 Merchant underwriting model (AI-002)
| Rule | Implication |
|---|---|
| ECOA and Regulation B (12 CFR Part 1002) | Whether a merchant processing agreement is "credit" (the processor bears chargeback and refund exposure) is under counsel review. Until the opinion, the division treats declines as if adverse action rules applied: underwriters decide every decline, and reason codes must match the model's actual drivers |
| Colorado SB26-189 | Covers financial or lending services; many applicants are sole proprietors (individuals). Counsel is reviewing whether deployer duties apply to Colorado applicants from 2027-01-01 |
| FTC Act Section 5 | Approval criteria described to applicants and partners must match practice |

### 2.3 Merchant insights assistant (AI-004)
| Rule or commitment | Implication |
|---|---|
| SOC 2 commitments (CC2.3, CC3.4, CC8.1, CC9.2) | The feature and the model provider (a subservice organization) must be described for the period ending 2026-09-30, and the change evaluated (P09) |
| 16 CFR 314.4(f) | The model provider receives customer information (merchants' customers' names and emails): contract safeguards (signed) and periodic assessment (missing) |
| FTC Act Section 5 (N51-R01) | Marketing says the assistant "never shares your data"; that must be corrected to describe the model provider (P03 SW-G14) |
| Merchant terms and CCPA service provider terms | Merchants are the businesses for their customers' data; the division may use it only to provide the service. Counsel is checking that the assistant's processing fits the terms (POAM-021) |
| DOJ Data Security Program (28 CFR Part 202) | The model provider and its processing locations are screened for covered persons (POL-04 4.10) |
| Colorado SB26-189 | Not applicable: the assistant makes no consequential decision about a consumer. Re-check if its use changes |

### 2.4 Merchant Consulting generative AI use (AI-007)
Engagement letters promise confidentiality of client data; the processor's contract with consulting (being amended, POAM-009) requires group safeguards for customer information (16 CFR 314.4(f)(2)); dispute files may contain PAN, which PCI DSS forbids outside a CDE. Pasting client data into public chatbots breaks all three.

## 3. Risk tiers (repository rubric)
- **High:** AI-001 (inline on payment infrastructure, a critical infrastructure operation; declines purchases with no human before the decision; a failure hits thousands of consumers and merchants within hours) and AI-002 (a substantial factor in decisions about merchant owners, many of them individuals, in a decision that may be credit).
- **Medium:** AI-003, AI-004, AI-005, AI-007, AI-008, AI-009. Humans make the final decision affecting individuals, or the system interacts directly with customers.
- **Low:** AI-006.

**Re-tier triggers:** AI-005 declining individual purchases rather than throttling keys (to High); AI-004 recommending credit, pricing, or customer-level actions (re-assessment); AI-008 taking actions on accounts (to High).

## 4. MEASURE
Results are from monitoring, validation, and tests between 2026-05 and 2026-08.

### 4.1 Transaction fraud-detection model (AI-001)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Fraud detection rate (fraud value caught / total fraud value) at least 75%; overall false positive rate (legitimate transactions declined or challenged) at most 1.2% | Detection 81%; false positive rate 0.9% | Yes |
| Valid and reliable (drift) | Weekly population stability index under 0.2; daily decline rate within 20% of the 13-week average, by merchant category | Weekly drift monitored; daily decline-rate alerts by segment missing. A 2026-06 release raised declines 30% for 2 days in one merchant category, found from merchant complaints | **No** (POAM-014) |
| Safe | Fallback rules take over within 1 minute if the scoring service fails; tested every quarter | Tested 2026-07 (40 seconds) | Yes |
| Secure and resilient | Scoring service in both data centers; training pipeline reads tokens only; access through PAM | In place; pre-training PAN check not yet automated (PP-016) | Partial |
| Accountable and transparent | Threshold changes approved by the head of merchant risk and fraud and logged; model documentation and validation report on file | In place | Yes |
| Explainable and interpretable | Top reason codes returned with each score and shown to analysts | In place | Yes |
| Privacy-enhanced | Tokens only; minimized features; retention per schedule | In place | Yes |
| Fair, with harmful bias managed | Bias testing plan below | One segment flagged | **No** |

#### Bias and fairness testing plan
**Why it matters.** The division holds no data on cardholders' protected characteristics and must not collect it for this purpose. Unfairness can still enter through features that act as proxies: card type (prepaid cards are used more by consumers without bank accounts), BIN country, and billing ZIP code. The test looks for **unjustified differences in false positive rates**: legitimate purchases declined or challenged.

| Element | Plan |
|---|---|
| Groups compared | (1) Card type: prepaid vs debit vs credit. (2) BIN country: domestic vs international. (3) Billing ZIP code groups: ZIP codes in the top vs bottom quintile of median household income, from public Census data (a proxy method, labeled as such; no individual data inferred or stored). (4) Merchant category groups |
| Metrics | False positive rate per group; ratio to the overall rate; detection rate per group (to check that a fix does not simply let fraud through) |
| Threshold | Flag a group if its false positive rate is more than 1.25 times the overall rate **and** at least 0.5 percentage points higher. A flagged group needs a documented business justification (for example a proven fraud pattern) or a mitigation before the next release |
| When | Before every monthly release (pre-deployment) and monthly on production data |
| Who | Fraud analytics runs it; the head of merchant risk and fraud signs off; model risk management reviews it independently each quarter; the Group AI council sees the results each quarter |
| Records | Kept for at least 5 years with the model version and thresholds (POL-01 4.11) |

**2026-08-20 results** (Q2 2026 transactions, labels matured through July):
- **Prepaid cards:** false positive rate 2.2% vs 0.9% overall (2.4 times). **Flagged.** Prepaid fraud rates are 1.5 times the average, which does not justify 2.4 times the false positives. Mitigation: route prepaid transactions in the 800 to 949 band to step-up instead of decline where the merchant supports it, and retrain without the card-type interaction term; retest before the November release.
- **Lowest-income ZIP code quintile:** 1.3% vs 0.9% (1.44 times, 0.4 points). Not flagged (below the 0.5-point floor); watched monthly.
- **International BINs:** 2.1% vs 0.9%. Not flagged as unjustified: international fraud rates are 3.3 times the domestic rate on the same merchants, documented by the head of merchant risk and fraud.
- **Merchant categories:** no group flagged.

### 4.2 Merchant underwriting model (AI-002)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 12-month loss rate of auto-approved merchants within policy | Within policy | Yes |
| Fair, harmful bias managed | Approval rate by business type and by ZIP code income quintile (proxy); flag a gap of more than 5 points without a credit-risk explanation | Home-based sole proprietors 9 points below the average; explained in part by processing history | **Flagged.** Analysis due 2026-12-31 |
| Explainable | Reason codes given to underwriters and applicants match the model's top drivers | 31 of 200 sampled declines cited a reason that was not among the top three drivers | **No** (P01 PP-024) |

### 4.3 Merchant insights assistant (AI-004), using AI 600-1 risk areas
| AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Confabulation | Monthly sample of 200 answers checked against source reports: numeric errors (target under 1%) | 2.1% | **No** |
| Information security (prompt injection) | Red-team test, including indirect injection through order notes and product names written by merchants' customers | Not done | **No** |
| Data privacy | Retrieval limited to the requesting merchant's data; zero-retention terms; per-merchant request logs | Terms signed; logs in place; cross-merchant isolation not independently tested | **No** |
| Value chain and component integration | Model provider in the SOC 2 system description; change gate | Not in description; gate bypassed | **No** |
| Human-AI configuration | Answers labeled and linked to source reports | In place | Yes |

### 4.4 Other use cases
- **AI-007 (consulting):** an endpoint survey in 2026-07 found public chatbot use on 38% of consulting laptops, including pasted dispute letters. **No.**
- **AI-003, AI-005, AI-008:** validation and monitoring in place; AI-008 pilot hands off to a person in 22% of chats and has no access to account changes.

## 5. MANAGE
**Human-in-the-loop design (compensating for real-time automation in AI-001):**
- Score bands: 950 and above automatic decline; 800 to 949 step-up (card-not-present) or review queue (high-value card-present); below 800 approve, subject to merchant rules.
- Analysts review all review-queue cases; a monthly random sample of 300 automatic declines estimates the false decline rate.
- Merchants can allow-list customers and dispute declines through support; disputed declines are reviewed within 2 business days.
- Threshold changes need the head of merchant risk and fraud's approval, a logged reason, and a 7-day look-back on decline rates.
- **AI-002:** underwriters decide every decline and every reserve above policy; reviewers see the application before the model's recommendation.
- **AI-004:** answers are labeled and linked to source reports; merchants can turn the feature off; the assistant cannot change data or settings.

**Monitoring:** daily decline-rate dashboards with alerts at plus or minus 20% of the 13-week average by merchant category and card type (AI-001); weekly drift; monthly bias tests; monthly answer sampling (AI-004); quarterly High-tier report to the council and the board risk committee. Related P01 risks: GR-04, GR-16, GR-17, PP-014, PP-015, PP-016, PP-024, SW-007, SW-008, MC-004.

**Incident handling:** an AI failure that causes mass false declines, discloses customer data, or breaches merchant commitments follows the P08 roles and POL-03. A model provider incident follows the Software division's merchant and ISV notice path.

**Rollback and decommissioning:** AI-001 keeps the prior model version for 30 days after each release; the head of merchant risk and fraud can roll back or switch to fallback rules within 15 minutes. Every use case has an off switch and a fallback that the BIA covers (P05).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 fraud-detection model | **Continue with conditions** (council, 2026-08-27; board risk committee informed 2026-09-10) | Daily decline-rate alerts by merchant category and card type by 2026-11-30 (POAM-014); prepaid step-up routing by 2026-10-15 and retrained model retested before the November release; automated pre-training PAN check by 2026-12-31; counsel's Colorado opinion by 2026-12-15, with notice and review processes ready for decisions on or after 2027-01-01 if it applies |
| AI-002 underwriting model | **Continue with conditions** | Reason-code mapping to the model's actual drivers by 2027-03-31; sole-proprietor approval analysis by 2026-12-31; counsel opinions on ECOA and Colorado by 2026-12-15 |
| AI-004 merchant insights assistant | **Continue for current merchants; pause new enrollments** | Change gate by 2026-10-31; system description for the period ending 2026-09-30 and merchant notice by 2026-11-30 (POAM-017); red-team test including indirect prompt injection and cross-merchant isolation test by 2026-12-31; marketing claims corrected by 2026-11-30; numeric error rate under 1% before enrollments reopen |
| AI-007 consulting use | **Stop public chatbots; replace with the approved tool** | Public chatbots blocked on consulting devices and the enterprise assistant available by 2026-11-30; engagement letter AI terms in the group template (POAM-022) |
| AI-003, AI-005 | **Continue** | Standard monitoring; AI-005 re-tier trigger recorded |
| AI-008 | **Continue pilot** | Disclosure of AI interaction at chat start; no account actions; council review before expanding beyond 5% of chats |
| AI-006, AI-009 | **Approved** | Standard monitoring; AI-009 prohibited for decisions about cardholders, merchants, or clients |

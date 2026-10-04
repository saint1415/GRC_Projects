# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed regional grocery retailer: 5 supermarkets, online ordering, a distribution center) |
| Tier / Vertical | Mid-Market / Retail Trade |
| Scope | Portfolio of 7 AI use cases (AI-001 to AI-007): 6 tools in use and 1 vendor proposal. Inventory in `ai-use-case-inventory.csv`. Registry default use case: AI-001, dynamic pricing and personalized offers |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for AI-004 and AI-007 |
| Assessors / date | vCISO and Security Manager (security), Privacy and Compliance Manager (privacy), General Counsel (legal), with each business owner; 2026-08-24 to 2026-09-04 |
| Decision | Chief Operating Officer for Medium and Low tiers; Chief Executive Officer for High tiers; 2026-09-15 (results reported to the audit committee the same day) |

## 1. Summary
The company uses 6 AI tools and has received 1 proposal for a seventh. Five of the six tools in use were adopted by departments without a security, privacy, or fairness review (SYS-12):
- the 4 tools that affect customers or applicants (AI-001, AI-003, AI-004, AI-006; gap 10, P01 R-025 to R-029);
- the generative AI assistant (AI-007), which marketing and HR staff started on personal paid accounts before IT moved it to an enterprise license in June 2026.

Only AI-002 (demand forecasting) came through the IT purchasing review, in 2025.

Four issues need action before these tools grow:
- **AI-006, hiring screening, auto-rejects applicants.** The adverse impact test failed the four-fifths screening threshold for Black applicants (ratio 0.75). It also breaks the P01 risk appetite ("no AI tool makes employment decisions without human review").
- **AI-001, pricing and offers.** Lower-income ZIP codes get less offer value (ratio 0.73). There is no emergency price freeze for hurricane season, and the data feed sends the payment tender type, including an EBT flag.
- **AI-004, the chatbot.** It gave 4 wrong or unsupported allergen answers in 15 tests. It also accepts and stores card numbers typed into chat.
- **AI-005, facial recognition.** The proposal was rejected. This is the practice the FTC banned Rite Aid from using for 5 years (December 2023 order).

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Pricing and personalized offers engine | Medium | Approve with conditions |
| AI-002 | Demand forecasting and replenishment | Medium | Approve (monitoring) |
| AI-003 | Self-checkout computer vision | Medium | Approve with conditions |
| AI-004 | Customer service chatbot | Medium | Conditional: fixes by 2026-11-30 or scripted FAQ mode |
| AI-005 | Facial recognition for loss prevention (proposal) | High | **Reject**; prohibited use |
| AI-006 | Hiring screening module | High | Approve with conditions; auto-reject off by 2026-10-31 |
| AI-007 | Enterprise generative AI assistant | Low | Approve |

Tiers: 2 High, 4 Medium, 1 Low. Decisions: 1 Approve, 1 Approve (monitoring), 3 Approve with conditions, 1 Conditional, 1 Reject.

## 2. GOVERN
- **Executive accountability:** the Chief Operating Officer, as executive sponsor of the security program, owns the AI program. The vCISO and the Director of E-commerce and Marketing co-lead it (P01 owner for the AI portfolio). Each use case has a business owner (inventory).
- **Decision rights follow the risk acceptance rules in POL-01 4.4:** Low by the Security Manager, Medium by the COO, High by the CEO.
- **Policies:**
  - POL-01 4.13: AI tools that use customer, employee, or supplier data, or that affect prices, offers, hiring, or customers, must be approved before use.
  - POL-01 4.10: vendor terms on security, permitted use, breach notice, and deletion. Purchasing issues no purchase order without approval.
  - POL-01 4.14 and 4.15: claims review, and data sharing review against the privacy notice.
  - POL-04 4.11: no Restricted or Confidential data in an AI tool unless it is on the approved list and the contract prohibits training shared models on company data.
  - POL-05 4.10: approved tools only; a person checks outputs before they reach a customer, supplier, applicant, or price.
  - STD-05 AI use standard: draft in progress, due 2026-12-31 (P06 standards index). This assessment supplies its content.
- **Approved-tools list:** kept by the Security Manager on the intranet. It lists AI-001 to AI-004, AI-006, and AI-007 with their conditions, and lists **prohibited uses**: facial recognition or any other biometric identification of customers or employees (AI-005), and individualized online prices set from a shopper's personal profile.
- **AI inventory:** `ai-use-case-inventory.csv`, owned by the GRC analyst and reviewed by the AI review group each quarter.

### 2.1 Lightweight AI governance process
A 600-person company does not need a standing AI committee with a long charter. It needs a reliable gate and a monthly rhythm, run by roles that already exist.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature switched on in an existing tool, submits a one-page intake: purpose, users, data, vendor, decisions affected | Requesting business owner | 15 minutes |
| 2. Triage | Provisional tier with the repository rubric; purchasing gate check (no purchase order without approval, POL-01 4.10) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy (data use, no-training clause, retention), claims, and a business reviewer. **High:** a full MAP and MEASURE assessment like this one, with a bias testing plan and legal review | Security Manager; Privacy and Compliance Manager; General Counsel for High; HR Director for any employment use | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** recommends and the COO decides. High: the AI review group recommends and the CEO decides | AI review group: vCISO (chair), Director of E-commerce and Marketing, Privacy and Compliance Manager, General Counsel, HR Director | Monthly, 45 minutes |
| 5. Monitor | Owners report the section 5 metrics monthly; High tiers also get a quarterly deep dive; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Each year, or on a trigger: new feature, model or vendor change, new data type, new population, new state, or a complaint pattern | AI review group | Annual |

**Overlap and compensation.** The Director of E-commerce and Marketing co-leads the program and also owns AI-001. That director does not vote on AI-001 results; the vCISO and the Privacy and Compliance Manager review them, and the COO decides.

**Training.** AI tool users and the attendants who act on AI-003 alerts get role training when a tool is introduced or changed (P07 POAM-004 adds this change-driven step).

## 3. MAP
| Item | AI-001 Pricing and offers | AI-002 Forecasting | AI-003 Self-checkout vision | AI-004 Chatbot | AI-006 Hiring screening | AI-007 GenAI assistant |
|---|---|---|---|---|---|---|
| Purpose | Set online prices within plus or minus 10% of shelf price; choose weekly offers for each member, including supplier-funded offers (BP-09, BP-10) | Propose store and DC order quantities (BP-17, BP-07) | Detect items that may not have been scanned at 20 self-checkouts | Answer order, refund, substitution, store, and product questions | Rank hourly store and DC applicants; auto-reject below a cut score | Draft copy, product descriptions, procedures, and summaries |
| Users | Director of E-commerce and Marketing and 3 analysts | Buyers and DC replenishment staff | Self-checkout attendants; Loss Prevention | Customers; customer service staff | 3 recruiters and the 5 Store Managers | About 40 licensed staff in the support center and DC office |
| Affected people | About 52,000 online account holders (prices) and 148,000 members (offers) | None directly | About 1,600 self-checkout transactions a day | About 9,000 chats a month | About 7,800 applicants a year | None directly |
| Data | Purchase history, home ZIP, delivery zone, tender type (with an EBT flag), cost and stock | Aggregated sales, promotions, weather | Video of the scan area; item scans | Names, order numbers, free text | Application answers, work history, ZIP for commute distance | Business content only |
| Build or buy | Buy (configured) | Buy | Buy (POS vendor add-on) | Buy | Buy (ATS module, configured) | Buy (enterprise license) |
| Generative AI? | No | No | No (image classification) | **Yes** | No (ranking model) | **Yes** |
| Live since | 2026-01 | 2025 | 2025-10 | 2026-02 | 2026-03 | 2026-06 (enterprise) |

**Not intended (any of these requires a new assessment):**
- **AI-001:** individualized online prices based on a shopper's profile; in-store shelf prices (set in the ERP); any eligibility decision.
- **AI-003:** identifying, banning, or detaining customers.
- **AI-004:** issuing refunds, taking payments, or giving dietary or medical advice.

### 3.1 Applicable laws and rules
| Rule | Applies to | Applies? | Why |
|---|---|---|---|
| FTC Act Section 5, deception, 15 U.S.C. 45(a)(1) (N44-45-R02) | AI-001, AI-003, AI-004, AI-006, AI-007 | **Yes** | Claims about prices ("same prices online and in store", P03 G-072), personalized savings, chatbot answers, and the privacy notice (G-069) must be truthful. No size threshold |
| FTC Act Section 5, unfairness, 15 U.S.C. 45(n) (N44-45-R02) | AI-001, AI-003, AI-005 | **Yes** | A practice is unfair if it causes or is likely to cause substantial injury that consumers cannot reasonably avoid and that is not outweighed by benefits. Lower offer value or higher prices where shoppers cannot reach a store, and wrongful accusations at self-checkout, are the scenarios to guard against (G-073) |
| FTC Rite Aid order (December 2023) | AI-005, AI-003 | **Enforcement signal** | The order banned Rite Aid from using facial recognition for surveillance for 5 years and required an information security program (N44-45-R02). It shows how the FTC views in-store AI that misidentifies customers |
| Fla. Stat. 501.160, price gouging | AI-001 | **Yes, during declared emergencies** | After the Governor declares a state of emergency, selling an essential commodity at an unconscionable price in the declared area is unlawful. "Commodity" includes food, water, and ice. A price is prima facie unconscionable if it shows a gross disparity from the average price in the 30 days before the declaration, unless the increase is due to added costs or market trends. The prohibition runs for up to 60 days under the initial declaration and can be extended. Enforced by the state attorney or the Department of Legal Affairs. Verified on the Florida Legislature site |
| Title VII, 42 U.S.C. 2000e-2(k) | AI-006 | **Yes** | Disparate impact is established if an employment practice causes a disparate impact on the basis of race, color, religion, sex, or national origin and the employer fails to show it is job related and consistent with business necessity, or refuses an available less discriminatory alternative. Verified on govinfo.gov |
| 29 CFR 1607.4(D), Uniform Guidelines four-fifths rule | AI-006 | **Used as the screening threshold** | A selection rate for a race, sex, or ethnic group below four-fifths of the highest group's rate is generally regarded by federal enforcement agencies as evidence of adverse impact; smaller differences can also count when statistically and practically significant. Verified on eCFR (2026-09-23 version) |
| ADEA, 29 U.S.C. 623(a) and 631(a) | AI-006 | **Yes** | Unlawful to refuse to hire or to classify applicants in ways that deprive them of opportunities because of age; protects people at least 40 years old. Verified on govinfo.gov |
| ADA, 42 U.S.C. 12112(b)(6) | AI-006 | **Yes** | Selection criteria that screen out or tend to screen out people with disabilities must be job related and consistent with business necessity. Verified on govinfo.gov |
| Florida Civil Rights Act, Fla. Stat. 760.10 | AI-006 | **Yes** | Covers employers with 15 or more employees (760.02(7)) and includes age, handicap, pregnancy, and marital status as well as the Title VII grounds. Verified on the Florida Legislature site |
| PCI DSS v4.0.1 (N44-45-R01) | AI-004 | **Yes, by contract** | Card numbers typed into chat are stored in the vendor's transcripts. Card data must not be kept where it is not needed (Requirement 3) or sent by end-user messaging (Requirement 4.2) |
| Fla. Stat. 501.171(2) and (6) | AI-001, AI-003, AI-004 | **Yes** | Reasonable security for personal information; a vendor holding company data must notify the company of a breach within 10 days (P08 notification matrix) |
| CCPA ADMT regulations (N44-45-R06) | All | No | The company does not do business in California (P03 section 1) |
| Colorado SB26-189, Illinois HB 3773, and other state AI laws | AI-006, AI-001 | No | The company operates and hires only in Florida. Recheck before hiring, selling, or delivering in another state |
| Florida AI-specific statute | All | None identified | This assessment did not identify a Florida AI statute that applies to these uses. Florida law beyond the statutes above was not researched |
| FTC proposed AI-accuracy policy statement (Docket FTC-2026-0727, July 2026) | AI-004, AI-007 | No (proposed) | Not final; not treated as a current obligation (P03 section 6) |

**Federal enforcement posture.** EO 14281 (April 23, 2025), section 4, directs federal agencies to deprioritize enforcement of disparate-impact liability and names 42 U.S.C. 2000e-2 (verified on govinfo.gov). The EEOC's 2023 technical assistance on AI selection tools is no longer on its website. Neither change amends the statute. The company keeps testing AI-006 against 42 U.S.C. 2000e-2(k) and uses the four-fifths rule in 29 CFR 1607.4(D) as an internal screening threshold.

## 4. Risk tiers
Tiers use the repository rubric (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). The rubric is defined by the repository, not by any regulation.

| ID | Tier | Rationale | Re-tier triggers |
|---|---|---|---|
| AI-001 | Medium | Directly affects what customers pay and which offers they get, using purchase data. It makes no consequential decision in the rubric categories, and prices stay within bounds the company sets | Individualized prices from a shopper's profile; any input that identifies or infers a protected characteristic or SNAP participation; re-enabling the delivery-zone or ZIP factor; bounds wider than plus or minus 10%; sales in another state |
| AI-002 | Medium | Influences business decisions (orders and stock) with a buyer approving every order. Uses no personal data. Not Low, because poor forecasts affect product availability, especially before hurricanes | Automatic ordering without buyer approval |
| AI-003 | Medium | Interacts with customers, and a mistaken alert can embarrass or harm a customer. An attendant makes every decision | Use to identify, ban, or detain people; any face matching; automatic transaction locks |
| AI-004 | Medium | Interacts directly with customers; a person handles refunds and exceptions | Issuing refunds or credits; dietary or medical answers; payments in chat |
| AI-005 | High | Biometric identification of every customer who enters a store. Not a rubric category, but the company treats it as High by company rule because a false match leads to accusation or exclusion | Not applicable (rejected) |
| AI-006 | High | A substantial factor in an employment decision; today it rejects applicants with no human review | Not applicable (already High) |
| AI-007 | Low | Internal productivity use with no decisions about individuals and no Restricted data | Use with customer, applicant, or employee data; outputs published without review |

## 5. MEASURE
Tests ran from 2026-08-24 to 2026-09-04; the AI-001 fairness test ran on 2026-08-28 (P03 G-073). Thresholds are company-defined screening rules, not legal standards, except where a rule is cited.

| Use case | Trustworthy characteristic | Test or metric | Threshold | Result | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Daily exceptions: prices outside bounds or below item cost | 0 below cost | 9 items below cost on 2026-07-14 after a cost-file error, fixed the next day; no cost floor rule | **No** |
| AI-001 | Safe | Emergency price freeze configured and tested | Configured and tested before hurricane season | Not configured (P01 R-026) | **No** |
| AI-001 | Fair, harmful bias managed | Offer value ratio and price index by ZIP income group (plan below) | Ratio 0.80 or more; price index spread 1.0 point or less | Offer value ratio 0.73 for the lower-income group; price spread 0.4 points | **No** (offers) |
| AI-001 | Privacy-enhanced | Only needed data sent; pseudonymous member ID; no reuse or shared-model training; deletion at termination | All in place | Loyalty number and tender type with an EBT flag sent; contract silent on use and deletion (VEN-07) | **No** |
| AI-001 | Accountable and transparent | Website and app explain that online prices can differ from shelf prices and that offers are chosen from purchase history | Disclosed and accurate | App says "same prices online and in store" (21 of 60 items differed, G-072); offers not explained | **No** |
| AI-001 | Explainable and interpretable | Vendor factor report for each price and offer | Available | Available for prices; not for offers | Partial |
| AI-002 | Valid and reliable | Weighted forecast error by department, 13 weeks | Center store 15% or less; fresh 25% or less | Center store 12%; fresh 27% (produce) | Partial |
| AI-002 | Fair, harmful bias managed | In-stock rate by store for the top 500 items (availability across neighborhoods) | No store more than 2 points below the best store | 96.1% to 97.4% | Yes |
| AI-002 | Secure and resilient | Vendor SOC 2 Type 2; single sign-on; prior week's plan available as fallback (P05 BP-17) | All true | All true | Yes |
| AI-003 | Valid and reliable | False alerts: 400 August alerts (80 per store) reviewed against video by Loss Prevention | 25% or less | 141 of 400 (35%) | **No** |
| AI-003 | Fair, harmful bias managed | False-alert rate by store and time of day | No store more than 1.5 times the lowest store | Store 4 at 52.5% against 27.5% at Store 2 (1.9 times); older lighting at Store 4 | **No** |
| AI-003 | Safe | Observed attendant interventions follow a non-accusatory script; no detention | 100% | 7 of 10 observed; 2 customer complaints of being singled out (May and July 2026) | **No** |
| AI-003 | Privacy-enhanced | Clip retention 30 days; no biometric identification; no model training on clips without approval | All contractual | Vendor keeps clips 90 days and may use them for training; contract does not prohibit face matching | **No** |
| AI-004 | Valid and reliable, safe | 60 scripted questions: 15 allergen, 5 recall, 10 refund policy, 20 order and store, 10 card-number entry | 0 wrong allergen or recall answers; refunds per policy | 4 of 15 allergen answers wrong or unsupported; 2 of 5 recall questions not routed to staff; 3 of 10 refund answers outside policy; 19 of 20 order and store answers correct | **No** |
| AI-004 | Privacy-enhanced | Card numbers blocked; transcripts kept no longer than 90 days | Both | Card number accepted in 10 of 10 tests; 11 of about 27,500 chats from May to July 2026 held full card numbers; transcripts kept 24 months | **No** |
| AI-004 | Secure and resilient | 10 prompt-injection attempts (AI 600-1 information security risk) | 0 succeed | 1 revealed a staff-only coupon code from the knowledge base | **No** |
| AI-004 | Accountable and transparent | Chat window says the customer is talking to an AI and how to reach a person | Both shown | Labeled "virtual assistant" only | Partial |
| AI-006 | Fair, harmful bias managed | Adverse impact ratio of the automated screen (plan below) | 0.80 or more for every group with enough applicants | Black or African American applicants 0.75 | **No** |
| AI-006 | Accountable and transparent | Human review before any rejection; applicant notice of automated screening | Both | Auto-reject below the cut score; no notice | **No** |
| AI-006 | Valid and reliable | Vendor validation evidence that the score predicts job performance for these roles | Validation study on file | Vendor marketing summary only | **No** |
| AI-006 | Safe (for applicants) | Accommodation path for applicants who cannot complete the online assessment | Available | None | **No** |
| AI-007 | Privacy-enhanced | Enterprise license only; no Restricted data; no personal AI accounts from company devices | All true | 9 personal-account sessions found in August web proxy logs; 1 pasted a supplier price list (Confidential) | Partial |
| AI-007 | Valid and reliable (AI 600-1 confabulation) | Claims in generated copy reviewed under POL-01 4.14 before publication; 20 published items sampled | 100% reviewed | 20 of 20 reviewed | Yes |
| All | Explainable and interpretable | Users can see the basis for each output | Available | AI-001 prices, AI-002, AI-003 (replay), and AI-006 (factor list) yes; AI-001 offers and AI-004 no | Partial |

Results: 24 tests, 4 passed (Yes), 4 partial, 16 failed.

### 5.1 AI-001 bias and fairness testing plan
**Groups compared.** The company holds no data on shoppers' race, ethnicity, sex, or age and will not infer it. It compares **geography**, which can act as a proxy for protected groups and for income: members' home ZIP codes in the two counties, grouped into lower, middle, and higher thirds by median household income from public Census data. Payment tender type is not used for grouping, and the EBT flag will be removed from the feed.

| Metric | How measured | Flag when | Result (2026-08-28) |
|---|---|---|---|
| Offer value ratio | Average weekly offer value per active member in each ZIP group, divided by the highest group | Below 0.80 | Higher $6.10; middle $5.40 (0.89); **lower $4.45 (0.73)** |
| Price index spread | Average online price divided by shelf price for a fixed 250-item basket, by delivery zone and ZIP group | Spread above 1.0 percentage point, or lower-income groups above higher-income groups | 0.4 points; the delivery-zone factor has been off since launch (configuration checked 2026-08-26) |
| Supplier-funded offers | Share of supplier-funded offer value reaching each ZIP group | Reported for context | Lower group gets 21% of supplier-funded value with 31% of active members |

**Cause.** The offer model favors members with high past spending, and supplier campaign rules let suppliers target "high-value shoppers" by spend tier. **Fix:** a minimum weekly offer value for every active member, and a review of supplier targeting rules that use spend tiers (with the P09 second-person campaign check, PI1.2). **Frequency:** monthly from October 2026, and before any model, input, or campaign-rule change.

### 5.2 AI-006 adverse impact testing plan
**Population.** 3,240 applications for hourly store and DC roles from 2026-03-02 to 2026-07-31. 1,944 (60%) passed the automated screen. Selection rate means the share that passed. Voluntary self-identification data (71% of applicants for race and ethnicity) is stored apart from the screening data and was used only for this test.

| Group | Applicants | Passed | Rate | Ratio to highest |
|---|---|---|---|---|
| White | 1,020 | 663 | 65.0% | 1.00 |
| Hispanic or Latino | 640 | 371 | 58.0% | 0.89 |
| Black or African American | 520 | 255 | 49.0% | **0.75** |
| Asian | 70 | 44 | 62.9% | 0.97 (small group) |
| Two or more races or other | 60 | 37 | 61.7% | 0.95 (small group) |
| Men | 1,050 | 672 | 64.0% | 1.00 |
| Women | 1,190 | 714 | 60.0% | 0.94 |

- The difference between Black and White applicants is statistically significant (two-proportion z-test, z about 6.0) and fails the four-fifths screening threshold. Hispanic or Latino applicants pass the threshold, but the gap is also statistically significant (z about 2.9), so it is monitored.
- **Cause analysis with the vendor:** 2 features drive most of the gap: **commute distance** (computed from the applicant's home ZIP code) and **employment gaps** over 6 months. Re-scoring the same applicants without them raised the ratio to 0.87 for Black applicants and 0.94 for Hispanic or Latino applicants.
- **Age and disability.** Date of birth is not collected, so age cannot be tested directly. The model's "years since first job" feature can act as an age proxy and will be removed. There is no accommodation path for applicants who cannot complete the online assessment.
- **Frequency.** Quarterly, and before any change to the model, features, or cut score.

## 6. MANAGE
### 6.1 Model risk controls
Controls scaled by tier. Mapping to SP 800-53 Rev. 5 and CSF 2.0 is an author mapping.

| Control | Low | Medium | High | SP 800-53 | CSF 2.0 | Status today |
|---|---|---|---|---|---|---|
| Inventory entry, owner, and tier before use | Yes | Yes | Yes | PM-9; CM-8 | GV.RM-01; ID.AM-02 | Done in this assessment; purchasing gate not yet enforced for SaaS add-ons |
| Vendor terms: no training of shared models on company data, deletion at exit, breach notice, model change notice | Yes | Yes | Yes | SA-9; SA-4 | GV.SC-05 | Missing for AI-001, AI-003, AI-004, AI-006; present for AI-002 and AI-007 |
| Data minimization and retention limits | Yes | Yes | Yes | SI-12; PT-2 | PR.DS-01 | Gaps in AI-001, AI-003, AI-004 |
| Pre-deployment testing against section 5 thresholds | No | Yes | Yes | RA-3; CA-2 | ID.RA-01 | Not done for any tool before launch |
| Bias and fairness testing with named groups and thresholds | No | Where it affects people | Yes, before launch and quarterly | RA-3; PM-9 | GV.RM-01 | Started with this assessment |
| Human review and override, documented | Output check | Yes | Before every action | PL-4; AC-5 | GV.RR-02 | Missing for AI-006 |
| Change control for configuration, rules, and model versions | No | Yes | Yes | CM-3 | PR.PS-01 | Business makes AI-001 campaign and rule changes without tickets (P09 CC8.1) |
| Monitoring metrics reported to the AI review group | No | Monthly | Monthly plus quarterly deep dive | CA-7 | ID.IM-01 | Starts October 2026 |
| Disclosure to affected people | No | AI interaction and personalization | Notice before use | PT-5 | GV.OC-03 | Missing for AI-001, AI-004, AI-006 |
| Role training for users and operators | Yes | Yes | Yes | AT-3 | PR.AT-02 | Change-driven step added (POAM-004) |

### 6.2 Human-in-the-loop design
- **AI-001:** the Director of E-commerce and Marketing sets bounds (plus or minus 10%), a hard floor at item cost, excluded items (infant formula, baby food, bottled water, ice, and over-the-counter medicines stay at shelf price), and campaign rules. An analyst reviews the daily exception report. Either can freeze all online prices to shelf prices with one setting. A second person checks supplier campaign settings.
- **AI-002:** buyers approve every proposed order and override it for declared emergencies and supplier shortages.
- **AI-003:** the attendant watches the replay before speaking to the customer, uses the standard script, and never detains anyone. Disputes go to Loss Prevention.
- **AI-004:** allergen, recall, and refund-exception questions hand off to staff (by phone outside chat hours). Only staff issue refunds.
- **AI-006:** recruiters review every applicant (auto-reject off). Interim step from 2026-09-08 until then: recruiters review all auto-rejected applicants each week and re-invite qualified ones.
- **AI-007:** staff edit every draft; claims go through the POL-01 4.14 review.

### 6.3 Emergency pricing guardrail (AI-001 and AI-002)
When the Governor declares a state of emergency that covers either county, the Director of E-commerce and Marketing (or the COO) turns on the price freeze the same day. Online prices then cannot rise above their average over the 30 days before the declaration, and AI-001 surge factors stay off for the whole emergency period, including any extension. Buyers override AI-002 forecasts for emergency items (water, ice, batteries, and canned goods). Both steps are added to the hurricane plan (P01 R-026, R-037). The freeze is tested by 2026-10-15 and before each hurricane season.

### 6.4 Monitoring
- Owners report the section 5 metrics to the AI review group each month. The first meeting is 2026-10-06.
- AI-006 gets a quarterly deep dive with the General Counsel.
- Complaints about prices, offers, self-checkout alerts, chatbot answers, and hiring are tagged in the customer service and HR systems and reviewed each quarter.
- Results feed the risk register (P01 R-025 to R-030) and the audit committee report each quarter.

### 6.5 Incident handling
- **AI vendor security incident** with customer or loyalty data: follow P08 `ir-runbook.md`. The vendor must notify the company within 10 days under Fla. Stat. 501.171(6) (and within 72 hours under the contract amendments).
- **Card numbers in chatbot transcripts:** purge them under POL-04 4.2, and record the purge in the PCI DSS evidence file.
- **Pricing error:** correct it, refund affected orders, and log it. A price increase during a declared emergency goes to the General Counsel the same day.
- **Hiring:** a complaint or charge involving AI-006 goes to the HR Director and General Counsel. Screening data and model versions are kept for the life of any claim.
- **Self-checkout:** a customer complaint of a wrongful accusation is reviewed by Loss Prevention against the video within 2 business days.

### 6.6 Decommissioning criteria
- **AI-001:** switch to shelf prices online and standard weekly offers if a fairness flag is not fixed within 30 days, if the vendor will not sign the data use amendment by 2026-11-30, or if the vendor changes data use terms.
- **AI-003:** switch off alerts at a store whose false-alert rate stays above 40% for 2 consecutive months.
- **AI-004:** switch to scripted FAQ mode (no generative answers) on 2026-11-30 if the card-number block, allergen and recall routing, and AI disclosure are not live.
- **AI-006:** stop using the score if adverse impact remains below the 0.80 threshold for 2 consecutive quarters after the features are removed, unless the vendor's validation study shows job-relatedness and no less discriminatory alternative is available (General Counsel decides).
- **Any tool:** stop if the vendor changes the model or data use without notice. On exit, the vendor deletes company data and confirms in writing.

## 7. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | Emergency price freeze configured and tested (2026-10-15); cost floor and daily exception report (2026-10-31); "same prices" claim removed and disclosure added (2026-10-31, G-072); minimum offer floor and supplier targeting review (2026-11-30); EBT flag and loyalty number replaced with a pseudonymous ID (2026-11-30); vendor data use, no-training, deletion, and 72-hour notice amendment (2026-11-30, VEN-07); privacy notice rewritten (2026-11-30, POAM-022); delivery-zone and ZIP factors stay off; monthly fairness tests | COO, 2026-09-15 |
| AI-002 | **Approve** (monitoring) | Fresh forecast error reviewed monthly; emergency override in the hurricane plan (2026-10-15) | COO, 2026-09-15 |
| AI-003 | **Approve with conditions** | Attendant script and training at all 5 stores (2026-10-31); Store 4 camera and lighting recalibration (2026-11-30); monthly false-alert sampling; vendor terms: 30-day retention, no face matching or biometric identification, no training on clips without approval (2026-12-31, R-027) | COO, 2026-09-15 |
| AI-004 | **Conditional** | Card-number pattern block and transcript purge; allergen and recall questions routed to staff; refund answers limited to the published policy; staff-only content removed from the knowledge base; AI disclosure in the chat window; transcript retention 90 days; all by 2026-11-30, or scripted FAQ mode | COO, 2026-09-15 |
| AI-005 | **Reject** | Listed as a prohibited use; purchasing blocks biometric analytics; any re-proposal needs a full High assessment and a CEO decision (R-030) | CEO, 2026-09-15 |
| AI-006 | **Approve with conditions** | Interim weekly review of auto-rejected applicants (started 2026-09-08); auto-reject off (2026-10-31); commute distance, employment gap, and years-since-first-job features removed and adverse impact retested (2026-11-30); accommodation path and applicant notice of automated screening (2026-11-30); vendor validation study (2026-12-31); quarterly adverse impact testing | CEO, 2026-09-15 |
| AI-007 | **Approve** | Enterprise license only; personal AI accounts blocked on company devices by the web filter (2026-10-31); no Restricted data (POL-04 4.11) | Security Manager, 2026-09-15 |

The conditions are tracked as POAM-023 in P07 (owner: vCISO; final milestone 2026-12-31) and in the risk register (P01 R-025 to R-030). STD-05, the AI use standard, will carry the process in section 2.1 and the controls in section 6.1 (due 2026-12-31).

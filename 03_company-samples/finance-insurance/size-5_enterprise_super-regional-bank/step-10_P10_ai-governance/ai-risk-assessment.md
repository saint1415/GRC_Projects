# AI Governance Risk Assessment: Enterprise AI Portfolio and the AI Credit Underwriting Model

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded bank holding company); Cris Santos Bank, N.A. |
| Tier / Vertical | Enterprise / Finance and Insurance |
| Scope | Enterprise AI portfolio (16 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the machine learning credit underwriting model for consumer unsecured personal loans and credit cards, in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook; NIST AI 600-1 (Generative AI Profile) for generative use cases; SR 26-2 revised model risk management guidance (2026-04-17) for non-generative models; repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Data and Analytics Officer), portfolio review of 2026-08-19; Model Risk Management and the Fair Lending Officer prepared the AI-001 evidence |
| Decision | Executive risk committee, 2026-09-18 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 16 |
| Risk tier | High 3, Medium 10, Low 3 |
| Status | In production 13, Pilot 2, Not enabled 1 |
| AI governance committee review complete | 12 of 16 |
| Not yet reviewed | 4: AI-009, AI-012, AI-014, AI-015 (AI-009, AI-012, and AI-015 due 2026-11-30 under POAM-023; AI-014 must be reviewed before any use) |
| In the scope of SR 26-2 (non-generative models) | 10, all in the Model Risk Management inventory; 9 validated (AI-014 is not in use) |
| Generative AI use cases (outside SR 26-2 scope) | 6: AI-008, AI-009, AI-010, AI-011, AI-012, AI-015; governed by the generative provisions of STD-01.8, still in draft (POAM-023) |
| Credit models with fair lending testing complete | AI-002 complete; AI-001 complete for personal loans, not yet for the credit card segment (POAM-022) |

**Main findings:** the credit underwriting model (AI-001) was validated and fair lending tested for personal loans, and a less discriminatory alternative was adopted, but the credit card pilot started before its own fair lending testing, and 3 of its 40 reason codes are too general for Regulation B. Four use cases have not been reviewed, three of them generative, and the generative AI standard is still a draft because SR 26-2 leaves generative and agentic models outside its scope.

## 2. GOVERN: operating model
**Two lines of review, one inventory.** Model Risk Management (second line, under the Chief Risk Officer) validates every non-generative model under SR 26-2 and holds the model inventory. The AI governance committee reviews every AI use case, generative or not, for purpose, data, fairness, customer impact, and security. The GRC team keeps one AI inventory that links to the model inventory, so no model is governed twice or not at all.

**Committee members:** Chief Data and Analytics Officer (chair); Head of Model Risk Management; Chief Compliance Officer and Fair Lending Officer; Chief Privacy Officer; CISO; General Counsel's delegate; Chief Human Resources Officer (for workforce tools); Head of Consumer Lending; Head of Digital Banking Technology. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Independent validation (non-generative); fair lending or adverse impact testing; impact assessment; human review design; notice to affected people (adverse action notices); monitoring plan |
| Medium | Committee vote | Human oversight design; output quality monitoring; disclosure where customers interact with AI; privacy and security review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Policies:** POL-01 4.13 (models used in credit, fraud, or BSA/AML decisions are inventoried and validated; credit models fair lending tested; generative use cases approved by the committee); POL-04 4.8 (no Restricted data in AI tools without approval and no-training terms); POL-05 4.7 (approved tools only); STD-01.8 Model and AI Risk Standard; STD-05.3 approved AI tools list.

**Intake.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use. The intake gate in change management goes live by 2026-12-31 (POAM-023), because AI-009 and AI-015 arrived as vendor feature releases before it existed (R-059).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier model; annual re-review of every use case; AI risks roll up to enterprise risk ER-07 (P01), which the board risk committee sees quarterly.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| ECOA and Regulation B, 12 CFR 1002.4(a) and 1002.6(b)(1) | **Yes** (AI-001, AI-002, AI-013) | A creditor must not discriminate on a prohibited basis in any aspect of a credit transaction or take a prohibited basis into account in any system of evaluating creditworthiness |
| Regulation B amendment, 12 CFR 1002.6(a) (91 FR 21620, effective 2026-07-21) | **Yes, changes the test** | 1002.6(a) now states the Act does not provide for the "effects test". Outcome disparities are not by themselves a Regulation B violation; the bank still measures them as a warning sign that an input may act as a proxy for a prohibited basis |
| Regulation B, 12 CFR 1002.6(b)(2) | **Yes** | Age may be used only in an empirically derived, demonstrably and statistically sound system and an elderly applicant's age must not get a negative value. AI-001 does not use age |
| Regulation B, 12 CFR 1002.9 | **Yes** | Adverse action notice within 30 days of a completed application, with specific principal reasons; a statement that the applicant failed to achieve a qualifying score is insufficient (1002.9(b)(2)) |
| Regulation B, 12 CFR 1002.12(b)(1) | **Yes** | Keep applications and information used to evaluate them for 25 months after notice (consumer credit); AI-001 scoring logs are kept 25 months or longer |
| FCRA, 15 U.S.C. 1681m(a) | **Yes** | Adverse action based on a consumer report requires notice, the credit score used, the consumer reporting agency's contact details, and the consumer's rights |
| CFPB Circulars 2022-03 and 2023-03 | **No longer in effect** | Withdrawn on 2025-05-12 (90 FR 20084), per the vertical research file; the 1002.9 duty itself is unchanged |
| CFPB supervision | **Yes** | The bank has more than $10 billion in assets, so the CFPB supervises it for federal consumer financial law (12 U.S.C. 5515) |
| SR 26-2 revised model risk management guidance (Federal Reserve, OCC, FDIC; 2026-04-17) | **Yes, as guidance** | Most relevant to banking organizations over $30 billion; superseded SR 11-7 and SR 21-8. Covers traditional and non-generative AI models; generative and agentic AI models are outside its scope. It is guidance, not an enforceable standard, but supervisors can act on unsafe practices |
| Interagency Guidelines, 12 CFR 30 App. B | **Yes** | The models process customer information; vendors are service providers (III.D) |
| OCC heightened standards, 12 CFR 30 App. D | **Yes** | Model risk is part of the risk governance framework; Model Risk Management is an independent risk management unit |
| UDAAP, 12 U.S.C. 5531 and 5536 | **Yes** (AI-007, AI-008, AI-013) | Customer-facing and targeting uses must not be unfair, deceptive, or abusive |
| Federal equal employment opportunity laws | **Yes, for AI-014** | Counsel reviews adverse impact before any use |
| State AI laws (for example, Colorado SB26-189, effective 2027-01-01) | **No** | Applications are accepted only from residents of the six footprint states; the GRC team rechecks each year whether any footprint state has enacted a comparable law |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = makes or is a substantial factor in a consequential decision (here, credit or employment).

| ID | Use case | Tier | Status | Committee review | SR 26-2 scope |
|---|---|---|---|---|---|
| AI-001 | Machine learning credit underwriting (personal loans and credit cards) | High | In production (loans); pilot (cards) | Reviewed 2026-02-18; re-reviewed 2026-08-19 | In scope; validated 2026-02 |
| AI-002 | Small business credit scoring | High | In production | Reviewed 2025-11-12 | In scope; validated 2025-10 |
| AI-003 | Payment fraud scoring (wires, instant payments, treasury) | Medium | In production | Reviewed 2025-09-24 | In scope |
| AI-004 | Card transaction fraud detection (card processor's model) | Medium | In production | Reviewed 2025-10-22 | In scope (vendor model) |
| AI-005 | AML alert prioritization | Medium | In production | Reviewed 2025-12-10 | In scope |
| AI-006 | Login risk and behavioral biometrics | Medium | In production | Reviewed 2026-01-21 | In scope (vendor model) |
| AI-007 | Collections prioritization and contact strategy | Medium | In production | Reviewed 2026-03-18 | In scope |
| AI-008 | Customer virtual assistant (generative) | Medium | In production | Reviewed 2026-04-15 | Outside (generative) |
| AI-009 | Contact center agent assist (generative) | Medium | Pilot | Not reviewed (due 2026-11-30) | Outside (generative) |
| AI-010 | Enterprise generative AI assistant for employees | Medium | In production | Reviewed 2026-02-18 | Outside (generative) |
| AI-011 | Developer code assistant | Low | In production | Reviewed 2026-01-21 | Outside (generative) |
| AI-012 | Cyber Defense Center alert triage assistant | Low | In production | Not reviewed (due 2026-11-30) | Outside (generative) |
| AI-013 | Marketing offer targeting | Medium | In production | Reviewed 2026-05-20 | In scope |
| AI-014 | Resume screening feature in the HR system | High | Not enabled | Not reviewed (required before any use) | In scope (vendor model) |
| AI-015 | Commercial credit memo drafting assistant (generative) | Medium | Pilot | Not reviewed (due 2026-11-30) | Outside (generative) |
| AI-016 | Loan document extraction | Low | In production | Reviewed 2025-10-22 | In scope (low materiality) |

**Tiering notes:** AI-001 is High because it decides clear approvals automatically and its recommendation drives declines. AI-013 is Medium, not High, because it selects who receives an offer, not whether credit is granted; its audiences still get a fair lending review for steering. AI-015 is Medium because credit officers decide and sign; letting it recommend a rating or decision would re-tier it to High. AI-010 is Medium rather than Low because Restricted data is allowed in its approved tenant.

## 5. Generative AI outside SR 26-2
SR 26-2 says generative and agentic AI models are outside its scope, but that the bank's risk management and governance practices should guide controls for tools the guidance does not cover. The bank's answer is the generative provisions of STD-01.8 (draft; approval due 2026-10-31 under POAM-023):
- **Use limits:** no generative tool may make or recommend a credit, fraud, or BSA/AML decision about a customer; drafts only, with a named human owner.
- **Data:** Restricted data only in approved tenants with no-training and deletion terms (POL-04 4.8).
- **Testing:** prompt-injection and data leakage red-teaming before release for customer-facing tools (AI-008); accuracy sampling for agent and memo tools (AI-009, AI-015), using the NIST AI 600-1 risk list (confabulation, information security, data privacy, harmful bias).
- **Transparency:** customers are told when they are talking to the virtual assistant and can reach a person.
- **Monitoring:** complaint and error monitoring monthly; any customer harm is an incident under P08.

## 6. MEASURE: fair lending testing across credit models
| Model | Status | Method | Result |
|---|---|---|---|
| AI-001 personal loans | Complete (version 2.0 in 2026-04; version 2.1 retested 2026-07) | Approval-rate ratios with surname and geography proxies for race and ethnicity and first-name proxies for sex; age from the application; marginal effect of each input; less discriminatory alternative (LDA) search | No ratio below 0.80; the Black to White ratio of 0.84 triggered an LDA search under STD-01.8 (any ratio under 0.90). Version 2.1 improved it to 0.88 with a Gini loss of 0.005 and was adopted 2026-06-15 |
| AI-001 credit cards | **Not done** (pilot of 17,100 applications) | Same method, plus line-assignment comparisons | Due 2026-12-15 before any rollout beyond 15% of digital applications (POAM-022) |
| AI-002 small business | Complete (2025-12) | Surname and geography proxies for principal owners; census tract minority share | No flag |
| AI-013 offer targeting | Per campaign | Audience composition by census-tract minority share against the eligible population | No campaign flagged in 2026 |

## 7. Full assessment: AI-001 machine learning credit underwriting model
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Estimate the probability of default for consumer unsecured personal loan and credit card applications; recommend approve, decline, or refer; recommend a loan amount or credit line; return the top 4 reason codes for adverse action notices |
| Users | Consumer lending underwriters and the digital and branch application channels |
| Affected people | Applicants for personal loans and credit cards. Scored from 2026-03-02 to 2026-08-14: 118,400 applications (101,300 personal loans; 17,100 credit cards). Outcomes: 49,800 automatically approved; 41,600 declined after underwriter review; 21,400 underwritten manually in the refer band; 5,600 withdrawn or incomplete |
| Data | Consumer report attributes from two consumer reporting agencies; stated and verified income; debt-to-income; deposit cash-flow data for existing customers. Excluded by design: age, ZIP code or other location fields, and any prohibited basis |
| Build or buy | Built by the bank's data science team on the machine learning platform (Cloud provider B); version 2.1 released 2026-06-15 through the model release gate (P04) |
| Human role | Clear approvals within policy cutoffs are automatic. Every decline recommendation is reviewed by an underwriter before the notice goes out; underwriters overturned 2.9% of decline recommendations (1,206). Refer-band applications are underwritten manually |
| Not intended | Mortgage, home equity, or business credit; pricing beyond the approved rate grid; applicants outside the six footprint states. Any of these requires re-assessment |

### 7.2 Risk tier
**High** (section 4): the model decides clear approvals and is a substantial factor in every decline.

### 7.3 MEASURE
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Independent validation by Model Risk Management (SR 26-2): out-of-time performance against the prior scorecard; calibration by score decile | Gini 0.61 against 0.52 for the prior scorecard; calibration within 5% in every decile; validation report 2026-02-12 | Yes |
| Safe | Automatic decisions limited to clear approvals within policy cutoffs; no automatic declines | Limits held for all 118,400 applications | Yes |
| Secure and resilient | Model artifact hashed and verified at start-up; release gate checks Model Risk Management approval; scoring logs kept 25 months or longer (12 CFR 1002.12(b)(1)); synthetic identity screening upstream | All in place (P04 control rows) | Yes |
| Accountable and transparent | Named owner; inventory entry; override tracking; applicant notices | In place | Yes |
| Explainable and interpretable | Reason codes are specific enough for 1002.9(b)(2) and match the model's actual drivers | 37 of 40 codes are specific; 3 are general ("credit profile does not meet requirements", "insufficient credit attributes", "model risk factors") and appeared as a principal reason in about 3,100 of 41,600 decline notices. In 200 sampled declines, the first reason matched the largest adverse contributor in 194 | **No** |
| Privacy-enhanced | Data minimization; consumer report data used only for the application; no transfer to vendors | In place | Yes |
| Fair, with harmful bias managed | Approval-rate ratios and LDA search (section 6) | Personal loans: pass after version 2.1. Credit cards: not tested | **No** (credit card segment) |

### 7.4 Bias and fairness testing plan (credit card segment and ongoing)
| Item | Plan |
|---|---|
| Data | All credit card pilot applications since 2026-07-06 (17,100), plus a retroactive scoring of 2025 card applications for a larger base; then every quarter for both products |
| Groups compared | Race and ethnicity estimated with surname and geography proxies (the bank does not collect them for these products); sex estimated with first-name proxies; age 62 or older against younger applicants; census tract minority share |
| Metrics and thresholds | Approval-rate ratio: flag below 0.80, and run an LDA search below 0.90. Average credit line by group, controlling for score: flag a statistically significant difference at the 5% level. Reason code frequency by group: flag if one code is twice as frequent. Underwriter override rates by group: flag a difference over 3 percentage points (currently at most 1.2) |
| Proxy review | For every flag, test whether each input predicts group membership; remove or constrain inputs that act as close proxies and are not needed for accuracy |
| Less discriminatory alternative | Compare model versions with and without flagged inputs; prefer the version with smaller disparities where accuracy is comparable; the Head of Model Risk Management documents the trade-off |
| Who and when | Fair Lending Officer with Model Risk Management; card results by 2026-12-15 (POAM-022); quarterly after that to the Chief Compliance Officer and the board risk committee through ER-07 |

### 7.5 MANAGE
- **Human in the loop:** underwriters review every decline recommendation before notice and record their reason when they overturn it; refer-band applications are fully manual; automatic approvals are sampled monthly by credit risk review.
- **Adverse action notices:** the 3 general reason codes are rewritten into specific principal reasons by 2026-11-15; applicants who received a notice with a general code as a principal reason are sent a corrected statement of specific reasons by the same date (POAM-022). Notices keep the FCRA 1681m(a) credit score and consumer reporting agency disclosures.
- **Monitoring:** monthly population stability and approval rates against the validation baseline (flag a change of more than 10 percentage points in approval rate); quarterly fair lending metrics; annual revalidation, or sooner after a material change, by Model Risk Management.
- **Change control:** new versions need Model Risk Management approval, fair lending testing, and committee sign-off; the release gate blocks unapproved versions (P04).
- **Incidents:** a security incident in the credit decisioning service follows P08 and POL-03; a fair lending issue goes to the Chief Compliance Officer and counsel.
- **Decommissioning:** revert to the prior scorecard if validation fails, if a fairness flag cannot be explained or fixed within one quarter, or if reason codes cannot meet 1002.9(b)(2).

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier model has quarterly performance and fairness metrics (inventory column `monitoring`); drift or threshold breaches trigger re-review.
- **Third parties:** AI vendors are tiered under STD-01.3; contracts require notice of material model changes and bar training on bank data (POL-04 4.8). Vendor models in SR 26-2 scope (AI-004, AI-006, AI-014, AI-016) are validated through vendor documentation, outcomes analysis, and the bank's own testing.
- **Incident handling:** AI incidents (unsafe or misleading output, bias finding, data misuse) are logged as incidents and follow P08 where security or customer information is involved.
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice or change data-use terms; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-18, on the AI governance committee's recommendation of 2026-08-19:
1. **AI-001 personal loans:** approved to continue. Conditions: reason code rewrite and corrected statements by 2026-11-15 (POAM-022).
2. **AI-001 credit cards:** the pilot stays at 15% of digital applications, with every decline reviewed by an underwriter, until card fair lending testing is complete with no unexplained flag (due 2026-12-15, POAM-022). Expansion needs committee and executive risk committee approval.
3. **Generative AI:** approve the generative provisions of STD-01.8 by 2026-10-31; AI-009 and AI-015 stay in pilot scope, and AI-012 stays as is, until review by 2026-11-30 (POAM-023).
4. **AI-014:** stays disabled; any request to enable it needs committee review and an adverse impact analysis first (P01 R-065).
5. **Intake gate:** live in change management by 2026-12-31 so vendor AI features cannot be switched on without an inventory ID (POAM-023).

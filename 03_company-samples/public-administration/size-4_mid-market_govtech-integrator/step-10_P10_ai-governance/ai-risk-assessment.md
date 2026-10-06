# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed GovTech systems integrator serving state and local agencies) |
| Tier / Vertical | Mid-Market / Public Administration |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. Deep assessment of AI-001, the AI eligibility assistant |
| Company role | **Developer** of AI-001 and AI-004 (the agencies are the deployers); **user** of AI-002, AI-003, and AI-005 |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-001 to AI-004 |
| Assessors / date | Director of Data and AI (owner), Director of Information Security and the vCISO (security), Director of Contracts and Compliance and the General Counsel (privacy and law); the AG-03 information security manager, an AG-03 quality control supervisor, and AG-03's civil rights coordinator took part for AI-001. Fieldwork 2026-08-10 to 2026-09-04 |
| Decision | Chief Executive Officer for AI-001 (High tier), 2026-09-17, with AG-03's written agreement; Chief Operating Officer for the others |
| Links | P01 R-009, R-010, R-011, R-031 to R-034; `../00_company-facts.md` gap 9; POL-01 4.14; POL-04 4.8; POL-05 4.9; STD-05; POAM-022 |

## 1. Summary
The company builds AI into a public benefits workflow and sells it to agencies, so its AI risk is mostly **developer risk**: if the eligibility assistant is wrong or biased, agency staff may act on it and people may go without food or medical assistance. The assistant has been in production for AG-03 since 2025-11 after a pre-launch accuracy review, but with no subgroup testing since launch and no monitoring of how often caseworkers accept wrong suggestions (gap 9). A Colorado county (AG-44) goes live on 2027-04-05, which brings the company under Colorado's automated decision-making law as a developer.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | AI eligibility assistant (AG-03; AG-44 contracted) | **High** | Approve with conditions; suggested outcomes restricted from 2026-10-01; expansion and AG-44 go-live gated |
| AI-002 | AI coding assistant | Low | Approve with conditions (retroactive review) |
| AI-003 | Support ticket summarization and routing | Medium | Approve with conditions |
| AI-004 | Public records redaction assistant | Medium | Approve with conditions |
| AI-005 | General-purpose public AI tools | High (if agency data is entered) | Not approved; blocked |

Tiers: 2 High, 2 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Director of Data and AI, supported by the vCISO. Each use case has a business owner (inventory).
- **Policies:** POL-01 4.14 (AI approved before use; no AI output replaces a decision that law gives to agency staff); POL-04 4.8 (Regulated or Restricted data only to approved AI services with signed terms; never FTI or CJI); POL-05 4.9 (approved tools only); STD-05 AI use and development standard (due 2026-12-31).
- **Approved AI list:** kept by the Director of Information Security. On 2026-09-17: the managed model service (AI-001 and AI-004 only, provisional until signed data-use terms, P03 PR-04), the coding assistant (AI-002), and the ticketing AI feature (AI-003).

### 2.1 AI governance process (mid-market scale)
A mid-market company does not need a standing AI committee with a large charter. It needs a short gate, a monthly rhythm, and a stricter path for features it sells to agencies.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any team wanting an AI tool, or wanting to build or switch on an AI feature, submits a one-page intake: purpose, users, people affected, data, model or vendor, decisions affected, customers | Requesting business owner | 15 minutes |
| 2. Triage | Provisional tier with the repository rubric; purchasing gate (no purchase order without approval, POL-01 4.9); flag any agency customer in a state with an AI law | Director of Information Security | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy (data-use, retention, no-training terms), and a business reviewer. **High or any feature sold to agencies:** full MAP and MEASURE assessment like this one, with bias testing, the deploying agency's participation, and a legal review of program rules | Director of Information Security; Director of Contracts and Compliance; Director of Data and AI; General Counsel | Low 1 week; Medium 2 weeks; High 6 weeks |
| 4. Decide | Low: Director of Information Security. Medium: the **AI review group** (Director of Data and AI, vCISO, Director of Contracts and Compliance, VP of Engineering), monthly. High: the AI review group recommends; the CEO decides with the deploying agency's written agreement | As listed | Monthly |
| 5. Monitor | Owner reports agreed metrics monthly (Medium and High) with a quarterly deep dive and bias test (High); incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: model version change, new data type, new program, new region or customer, new state, or a pattern of complaints | AI review group | Annual |

## 3. MAP
| Item | AI-001 Eligibility assistant | AI-002 Coding assistant | AI-003 Ticket summaries | AI-004 Redaction assistant | AI-005 Public AI tools |
|---|---|---|---|---|---|
| Purpose | Read verification documents, extract fields, flag missing verifications, and suggest an outcome per program with a reason summary citing the agency policy manual | Code completion and chat | Summarize tickets; suggest category and priority | Suggest redactions of personal identifiers before records are released | Drafting, summarizing |
| Users | About 310 AG-03 caseworkers (3 regions); AG-44 caseworkers from 2027-04-05 | About 150 engineers | 45 support staff | Records custodians at 6 municipal customers | Any staff (blocked) |
| Affected people | Applicant households: about 118,000 applications processed with it from 2025-11 to 2026-06; many low-income, elderly, disabled, or with limited English | None directly | Agency users who file tickets | People named in released records | Anyone whose data is entered |
| Data | Application data, household composition, income documents, Social Security numbers. **No FTI** | Source code | Ticket text (regulated attachments blocked) | Constituent records | Unknown |
| Build or buy | Build on a bought model | Buy | Configure | Build on a bought model | Buy |
| Generative AI? | Yes | Yes | Yes | Yes (plus pattern matching) | Yes |

**FTI boundary (AI-001).** FTI is prohibited in the AG-03 tenant (Pub. 1075 sec. 2.C.11.2). IRS income match results are FTI and must never reach the assistant. Copies of tax returns or W-2s provided by the applicant are not FTI under Pub. 1075, so the assistant may read them. The AG-03 eligibility API sends no IRS or SSA income match fields (confirmed with AG-03 in 2026-08; P03 PR-03).

**Applicable laws and rules (AI-001):**
| Rule | Applies? | What it means for the assistant |
|---|---|---|
| SNAP certification by state staff, 7 CFR 272.4(a)(2) | **Yes** (program rule, reaches the company by contract) | "Volunteers and other non-State agency employees shall not conduct certification interviews or certify SNAP applicants." Neither the assistant nor company staff may decide. The caseworker's decision must be real, not a rubber stamp |
| Medicaid eligibility by the single State agency, 42 CFR 431.10(b)(3) and (c)(2) | **Yes** | The single State agency is responsible for determining eligibility and may delegate that authority only to a government agency with merit personnel standards. Same conclusion as for SNAP |
| TANF | Yes, under each state's program rules | The contracts apply the same human-decision rule to all three programs |
| SNAP denial notice and fair hearings, 7 CFR 273.10(g)(1)(ii) and 273.15(a); Medicaid fair hearings, 42 CFR 431.200(a) | **Yes** | A denial notice must explain the basis for the denial and the right to a fair hearing. The reason must come from the caseworker's finding, and the assistant's output and version must be kept so the agency can explain a case at a hearing |
| SNAP processing deadlines, 7 CFR 273.2(g)(1) and (i)(3)(i) | **Yes** | 30 days for normal processing; benefits by the 7th calendar day for expedited households. A wrong "more verification needed" flag can push a household past these dates |
| SNAP nondiscrimination, 7 CFR 272.6(a) | **Yes** | No discrimination in any aspect of program administration for reasons of age, race, color, sex, disability, religious creed, national origin, or political beliefs. This is why the bias tests compare those groups where data allows |
| SNAP bilingual requirements, 7 CFR 272.4(b) | **Yes** (agency duty) | Agencies must serve single-language minority households; the assistant must work as well on non-English documents |
| SNAP and Medicaid confidentiality, 7 CFR 272.1(c); 42 CFR 431.306(b) | **Yes** | The model service must be bound to comparable confidentiality terms before more data flows (P03 PR-04; R-033) |
| Fla. Stat. 501.171(2) | **Yes** (directly) | Reasonable measures to protect personal information sent to the model service |
| **Colorado SB26-189** (C.R.S. 6-1-1701 to -1709 as reenacted; signed 2026-05-14; effective 2027-01-01) | **Yes, for AG-44**, as the developer | Covers developers and deployers doing business in Colorado whose automated decision-making technology materially influences consequential decisions, including essential government services. **Developer duties:** documentation to deployers (intended uses, categories of training data, known limitations, and instructions for human review) and notice of material updates. **Deployer duties (AG-44):** notice at the point of interaction, an explanation after an adverse outcome, the person's rights to correct data and to meaningful human review or reconsideration, and 3 years of records. Enforcement by the Colorado Attorney General, with a 60-day cure period until 2030-01-01; no private right of action. No small-business exemption appears in the signed act. Attorney General rules were due by 2027-01-01; their adoption is not yet confirmed |
| Texas TRAIGA and other state AI laws | Not today | No customers in those states. Re-check under POL-01 4.15 before contracting in a new state |
| Federal preemption efforts (EO 14365) | Watch only | The executive order does not itself preempt state law. Track litigation over Colorado's law; comply until a court or statute says otherwise |
| HIPAA | No | AG-03 placed its eligibility functions outside its health care component (45 CFR 164.105) |

**AI-004 law.** Each state's public records law decides what is exempt; the agency's records custodian, not the company, makes that call. A missed redaction can disclose personal information, including motor vehicle record information protected by 18 U.S.C. 2721 when it appears in municipal files.

## 4. Risk tiers
Tiers use the repository rubric (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

- **AI-001 High.** The assistant is a substantial factor in consequential decisions about essential government services (food, cash, and medical assistance). The caseworker formally decides, but in the validation sample caseworkers accepted 23 of the 42 wrong suggestions (section 5). At that rate the suggestion shapes the outcome.
- **AI-004 Medium.** It influences what is released, but the custodian approves every redaction and no decision about an individual is made.
- **AI-003 Medium.** It interacts with agency users' requests and influences priority, but staff set the final priority.
- **AI-002 Low.** Internal productivity with no decisions about individuals and no regulated data, provided the data rules hold.
- **AI-005 High if agency data is entered**, which is why it is blocked rather than tiered for use.

**Re-tier triggers:** AI-003 becomes High if it starts closing or prioritizing security tickets without review. AI-004 becomes High if any customer turns on automatic release. AI-002 becomes Medium if it is connected to repositories that hold agency data samples.

## 5. MEASURE
**AI-001 validation sample.** AG-03 quality control staff re-worked 600 randomly selected applications from 2026-05 to 2026-07 without seeing the AI output, and the results were compared with the assistant's extraction and suggestions. Thresholds are set by this assessment (repository rubric), not by regulation.

| Trustworthy characteristic | Test / metric (threshold) | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Field accuracy for income and household size (98% or better); outcome agreement with QC (95% or better) | Income fields 97.2% (errors on multi-page pay stubs and handwritten statements); outcome agreement 93.0% (42 of 600 wrong) | **No** |
| Valid and reliable: confabulation (AI 600-1) | Reason summaries citing policy sections not in the manual (0) | 4 of 600 (0.7%) | **No** |
| Safe | Wrong suggestions caught by caseworkers (80% or better); cases pushed past SNAP deadlines by the assistant (0) | Caseworkers caught 19 of 42 (45%) and accepted 23; 9 of the 23 led to incorrect denials, which AG-03 has reopened. No deadline misses found | **No** |
| Secure and resilient | Prompt-injection test with 25 crafted documents (0 changed outcomes); model service within FedRAMP scope; access limited to assigned caseworkers | 2 of 25 changed the suggestion. FedRAMP scope confirmed (part of the provider authorization). Access correctly limited through AG-03's identity provider | **No** |
| Accountable and transparent | Applicants told that an automated tool helps staff; model version and prompt template logged per case | General notice in the online application since launch, but not on paper applications or at interviews. Version logged; prompt template not logged | **Partial** |
| Explainable and interpretable | Each suggestion shows extracted fields linked to source pages; reviewer can rebuild the basis for a sampled denial (95% or better) | Source links present; basis rebuilt in 92% of 50 sampled denials | **Partial** |
| Privacy-enhanced | Only fields needed sent to the model; SSNs masked; signed retention and no-training terms | SSNs masked since 2026-02; whole documents still sent; terms are standard terms only (R-033) | **Partial** |
| Fair, with harmful bias managed | Error rate by group compared with its reference group (flag at more than 3 percentage points) | Spanish-language documents: income extraction errors 7.8% vs 2.9% English. Haitian Creole: 4 of 31 (12.9%; too few to judge). Households with a member aged 60 or older: outcome errors 10.4% vs 6.2% (medical expense deductions missed). Households with a member receiving disability benefits: 9.1% vs 6.6%. Sex of head of household: 7.2% vs 6.8%, not flagged. Race and ethnicity: not tested | **No** (2 flags) |

**What the results say.** The core problem is automation bias, not only model error: caseworkers accepted more wrong suggestions than they caught. Asking a language model to reason about income limits and deductions also creates avoidable errors, because the calculation is deterministic and the rules are already configured in the platform.

### 5.1 AI-001 bias testing plan
| Item | Plan |
|---|---|
| Groups compared | Document language (Spanish, Haitian Creole, other non-English vs English); age (household member 60 or older vs none); disability (household member receiving disability benefits vs none); sex of head of household; race and ethnicity (from voluntary civil rights data the agency collects, used only with the agency's written approval and only for testing) |
| Metrics | Field extraction error rate; outcome disagreement with QC; **adverse-error rate** (suggested denial or "more verification needed" where QC found the household eligible); caseworker acceptance of wrong suggestions |
| Thresholds | Flag if a group's error or adverse-error rate exceeds its reference group by more than 3 percentage points, or the adverse-error ratio is above 1.25 (repository rubric, not regulation) |
| Sample | 1,500 cases re-worked blind by AG-03 quality control, stratified so each group has at least 150 cases; repeated with AG-44 cases on a pre-production copy before go-live |
| Timing | Before suggestions return (due 2026-12-31); quarterly on 400 new cases; before any model version change; before AG-44 go-live |
| Response to a flag | Stop suggestions for the affected case type, fix, retest. Report every flag to the deploying agency's civil rights contact |
| Owner | Director of Data and AI, with agency quality control |

**Other use cases (2026-08 samples):**
| Use case | Test | Threshold | Result | Pass? |
|---|---|---|---|---|
| AI-002 | Secrets scanning on code with assistant suggestions; vendor data terms | 0 secrets; no training on company code | 0 secrets in 4 weeks of commits; enterprise terms exclude training, retention 30 days | Yes, after review |
| AI-003 | Summary accuracy on 100 tickets; severity 1 and security tickets never down-prioritized | 95% accurate; 0 down-prioritized | 96% accurate; 1 security ticket suggested as low priority (corrected by staff) | **Partial** |
| AI-004 | Recall of personal identifiers on 200 documents by type | 99% recall on typed text; reported separately for scans and handwriting | 99.4% typed; 91% scanned; 78% handwritten | **Partial**: limits must be stated to custodians |

## 6. MANAGE
**AI-001 human-in-the-loop design (required before suggested outcomes return):**
- **Review first.** The caseworker checks extracted fields against the documents and records a finding before the suggested outcome is shown.
- **No AI text in notices.** Denial and pending notices use reason codes the caseworker selects.
- **Adverse suggestions get extra review.** A suggested denial or "more verification needed" requires the caseworker to open the source page; a supervisor reviews 10% of AI-assisted denials each week.
- **Override is simple and expected,** with a reason code, and never counted against the caseworker. Override rates are reported by team.

**AI-001 technical changes:**
- Move income and deduction calculations to the platform's deterministic rules engine; the model only extracts and summarizes.
- Check every policy citation against the current manual and block any that do not match.
- Send only the fields each step needs (SSNs are already masked).
- Treat text inside uploaded documents as data (prompt-injection filtering and labeling).
- Log model version and prompt template per case; rerun the validation set before any version change.

**Colorado developer package for AG-44 (due 2027-02-28):** intended and prohibited uses; categories of data used to build and evaluate the feature; known limitations, including the subgroup results in section 5; instructions for meaningful human review and for reconsideration requests; how the company will notify AG-44 of material updates; and the records the company keeps to support AG-44's 3-year record duty. AG-44 owns the deployer notice and explanation; the company builds the screens and letters AG-44 needs.

**Other use cases:**
- **AI-002:** enterprise data terms confirmed; no agency data or production secrets in prompts (POL-05 4.9); secrets scanning continues; quarterly review of the vendor's terms.
- **AI-003:** severity 1 and security tickets bypass AI prioritization; quarterly accuracy check of 100 tickets.
- **AI-004:** the user guide states recall limits for scanned and handwritten pages; custodians must review every page of those documents; the assistant never releases documents.

**Monitoring:** AI-001 monthly QC sample of 150 cases, acceptance and override rates, adverse-error rate; quarterly bias test; fair hearing requests and complaints on AI-assisted cases tagged and reviewed. Results go to the AI review group and into the risk register (R-009, R-010).

**Incident handling (P08 and POL-03):**
- Applicant data exposed through the model service or a prompt-injection attack is a security incident: the deploying agency is told within 1 hour, and the 10-day notice under Fla. Stat. 501.171(6)(a) applies to Florida agencies if a breach is determined.
- A pattern of wrong suggestions (for example after a model update) is an AI incident: switch suggestions off, tell the agency within 1 business day, and give it the list of affected cases.

**Decommissioning (AI-001).** Turn off suggestions, or the whole feature, if signed data-use terms are not in place by 2026-12-31; outcome agreement stays below 95% or the adverse-error threshold is missed for 2 months in a row; a bias flag stays unresolved for 90 days; or the agency withdraws approval. On shutdown, delete prompts and outputs held outside the case record.

## 7. Decision
**AI-001: approve with conditions.** Chief Executive Officer, 2026-09-17, with AG-03's written agreement:
1. **From 2026-10-01, suggested outcomes are shown only after the caseworker records a finding** (interim review-first switch). Extraction continues.
2. **By 2026-11-30:** the full review-first design, deterministic calculations, citation checking, prompt-injection filtering, and prompt template logging are live (R-009, R-034).
3. **By 2026-12-31:** the 1,500-case bias test is complete with no unresolved flag (R-010); signed data-use and no-training terms for the model service (R-033); STD-05 issued.
4. **By 2027-02-28:** the Colorado developer package is delivered to AG-44 (R-011); AG-44 go-live requires a passed bias test on AG-44 cases and the CEO's sign-off.
5. **Expansion** to AG-03's other 3 regions requires 2 consecutive months meeting every threshold in section 5, a new CEO approval, and AG-03's written agreement.

**AI-002, AI-003, AI-004: approve with the conditions in section 6** (Chief Operating Officer, 2026-09-17). **AI-005: not approved**; engineers use AI-002, and an enterprise general-purpose assistant with contract terms will be evaluated through the process in section 2.1 in 2027 Q1.

All conditions are tracked as POAM-022.

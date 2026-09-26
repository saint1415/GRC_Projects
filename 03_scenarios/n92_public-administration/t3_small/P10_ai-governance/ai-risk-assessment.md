# AI Risk Assessment: AI Eligibility Assistant (SNAP, TANF, Medicaid)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (GovTech systems integrator serving state and local agencies) |
| Tier / Vertical | Small / Public Administration |
| AI use case | AI-001: the AI eligibility assistant (SYS-11), a pilot feature of the ACMP that recommends SNAP, TANF, and Medicaid eligibility outcomes to 40 AC-03 caseworkers in one region, since May 2026 |
| Company role | **Developer and operator.** The company built the feature on a managed large language model service. AC-03, the state human services agency, is the **deployer** and makes every eligibility decision |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the Generative AI Profile (NIST AI 600-1), because the assistant uses a large language model |
| Assessor / date | Data and AI Lead with the IT Manager and the Contracts and Compliance Manager; AC-03 information security manager and an AC-03 quality control supervisor took part. Fieldwork 2026-07-20 to 2026-08-14; approved 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |
| Links | P01 R-018, R-019, R-020; scenario-facts gap 14; POL-04 4.8; POL-05 4.9 |

**Why this assessment exists now.** The pilot started in May 2026 without an AI risk assessment, bias testing, a written human-review rule, or notice to applicants (scenario-facts gap 14). This is the first assessment.

## 1. GOVERN
- **Accountable owner (company):** Data and AI Lead. **Business owner (deployer):** AC-03's program director for the pilot region.
- **Decision authority.** The use case is High tier (section 3), so the Chief Executive Officer approves it, as for any High risk (POL-01 4.4). AC-03 must also agree in writing to any change in scope or design, because the decisions and the program are AC-03's.
- **Policies that apply:**
  - POL-04 4.8: Regulated or Restricted data may go to an AI service only if it is on the approved list and meets POL-01 4.9
  - POL-01 4.9: no vendor gets agency data before a security review and contract terms
  - POL-05 4.9: staff use only AI tools on the approved list
  - POL-01 4.3: risk assessment after major changes (a model version change counts)
- **Approved AI services list.** Kept by the IT Manager. On 2026-08-31 it has one entry: the cloud provider's managed model service, **only** for SYS-11 with AC-03 pilot data, and **provisional** until the vendor review closes (condition 2, section 6). No general-purpose AI assistant is approved (AI-002).
- **AI inventory.** Kept by the Data and AI Lead and reviewed quarterly.
- **Scale for a Small company.** There is no AI committee. An AI review group (Data and AI Lead, IT Manager, Contracts and Compliance Manager, Chief Operating Officer) meets quarterly. For SYS-11 the AC-03 information security manager and a program policy specialist join.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Speed up application processing. For each SNAP, TANF, or Medicaid application in the pilot region, the assistant: (1) reads uploaded verification documents (pay stubs, identity documents, leases, utility bills) and extracts fields into the case; (2) flags missing verifications; (3) suggests an outcome per program (likely eligible, likely ineligible, or more verification needed) with a short reason summary that cites AC-03's policy manual |
| Users / operators | 40 AC-03 caseworkers, who are state merit system employees, in one region |
| Affected people | Applicant households in the pilot region: about 9,600 applications were processed with the assistant from May to July 2026. Many are low-income, elderly, disabled, or have limited English |
| Data | **Inputs:** application data, household composition, income and expense documents, and Social Security numbers (sent in full today; see Privacy). **Retrieval:** AC-03's policy manual. **Outputs:** extracted fields, a suggested outcome, and a reason summary, stored in the case record. **Training:** none by the company. The foundation model is pre-trained by the provider; the provider's standard terms say customer prompts are not used for training, but retention settings and the service's FedRAMP scope have not been confirmed (R-020) |
| FTI boundary | FTI is prohibited in the AC-03 tenant (Pub. 1075 sec. 2.C.11.2). IRS income match results obtained from the IRS or a secondary source are FTI and must **never** reach the assistant. Copies of tax returns or W-2s provided by the applicant are not FTI (Pub. 1075, "Information Received from Taxpayers or Third Parties"), so the assistant may read them. The AC-03 eligibility API sends no income match fields (interface specification, confirmed with AC-03 in August 2026). Caseworkers pasting IRS data into notes is tracked as R-030 |
| Build or buy | **Build on a bought model.** The company wrote the application logic, prompts, and retrieval; the language model is the cloud provider's managed service (SaaS, outside the SSP boundary, P02 section 7) |
| Not intended | Making, approving, or issuing eligibility decisions; generating notice text; conducting interviews; fraud scoring; use in any other tenant or for any other program. Any of these would require a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | What it means for the assistant |
|---|---|---|
| SNAP certification by merit staff, 7 CFR 272.4(a)(2) | **Yes** (AC-03 program rule, reaches the company by contract) | State merit employees perform interviews and certify households; "volunteers and other non-State agency employees shall not ... certify SNAP applicants." The assistant and company staff may not make the decision. It stays advisory, and the caseworker's decision must be real, not a rubber stamp |
| Medicaid eligibility by the single State agency, 42 CFR 431.10(b)(3) and (c)(2) | **Yes** (same path) | The Medicaid agency is responsible for determining eligibility and may delegate only to a government agency with merit-based personnel standards. Same conclusion as for SNAP |
| TANF | Yes, under AC-03's state program rules | Not analyzed separately. The AC-03 contract applies the same human-decision rule to all three programs |
| SNAP denial notice and fair hearings, 7 CFR 273.10(g)(1)(ii) and 273.15(a); Medicaid fair hearings, 42 CFR 431.200(a) | **Yes** | A denial notice must explain the basis for the denial and the right to a fair hearing. The reason must come from the caseworker's own finding, and the assistant's output must be kept so AC-03 can explain a case at a hearing |
| SNAP processing deadlines, 7 CFR 273.2(g)(1) and (i)(3)(i) | **Yes** | 30 days for normal processing; benefits by the 7th calendar day for expedited households. A wrong "more verification needed" flag can push a household past these dates |
| SNAP nondiscrimination, 7 CFR 272.6(a) (citing Title VI of the Civil Rights Act, 42 U.S.C. 2000d, section 504, the ADA, and the Age Discrimination Act) | **Yes** | No discrimination in certification on the basis of age, race, color, sex, disability, religious creed, national origin, or political beliefs. This is why the bias tests below compare those groups where data allows |
| SNAP bilingual requirements, 7 CFR 272.4(b) | **Yes** (AC-03 duty) | AC-03 must serve single-language minority households, which in Florida includes many Spanish-speaking households. The assistant must work as well on Spanish-language documents |
| SNAP and Medicaid confidentiality, 7 CFR 272.1(c); 42 CFR 431.306(b) | **Yes** | Access to applicant data is limited to persons subject to comparable confidentiality standards. The model service must be bound by contract terms before data flows (R-020) |
| Fla. Stat. 501.171(2) | **Yes** (directly) | Reasonable measures to protect personal information such as Social Security numbers, including data sent to the model service |
| HIPAA | No | AC-03 placed its eligibility functions outside its health care component (45 CFR 164.105); no business associate designation |
| State AI laws (Colorado SB26-189, effective 2027-01-01; Texas TRAIGA) | Not today | The company and AC-03 are in Florida. Colorado's law covers developers and deployers doing business in Colorado whose technology materially influences decisions about essential government services. If a prospective out-of-state customer is in Colorado or Texas, reassess before contracting |
| OMB M-25-21 (federal agency AI) | No | Applies to federal agencies only. Its "high-impact AI" minimum practices are a useful comparison, not an obligation |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal/projects/P10_ai-governance/README.md`).

**Why High:** the assistant is a substantial factor in consequential decisions about essential government services (food, cash, and medical assistance). The caseworker formally decides, but in the pilot **caseworkers accepted about 90% of suggestions** (R-018), and in the validation sample they accepted most of the suggestions that were wrong (section 4). At that level the suggestion is shaping the outcome.

**Minimum controls for High (rubric):** human review before action, pre-deployment bias testing, an impact assessment (this document), notice to affected people, and ongoing monitoring. On 2026-08-31 only the first exists, and only informally.

## 4. MEASURE
**Validation sample.** AC-03 quality control staff re-worked 400 randomly selected pilot applications (May to July 2026) without seeing the AI output, and the results were compared with the assistant's extraction and suggestions.

| Trustworthy characteristic | Test / metric (threshold) | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Field accuracy for income and household size (98% or better); agreement of the suggested outcome with the QC outcome (95% or better) | Income fields 96.1% (errors on multi-page pay stubs and handwritten statements); outcome agreement 91.5% (34 of 400 wrong) | **No** |
| Valid and reliable: confabulation (AI 600-1) | Reason summaries that cite policy text not in AC-03's manual (0) | 7 of 400 (1.8%) cited policy sections that do not exist | **No** |
| Safe | Share of wrong suggestions caught by caseworkers (80% or better); cases pushed past SNAP processing deadlines by the assistant (0) | Caseworkers caught 13 of 34 (38%) and accepted 21. 8 of the 21 led to incorrect denials, which AC-03 has reopened. No deadline misses found in the sample | **No** |
| Secure and resilient | Prompt-injection test with 20 crafted documents (0 changed outcomes); model service FedRAMP scope confirmed; access limited to the 40 pilot caseworkers | 3 of 20 test documents changed the suggestion. FedRAMP scope not confirmed. Access correctly limited through AC-03's identity provider | **No** |
| Accountable and transparent | Applicants told that an automated tool helps staff; model version, prompt template, and output logged per case | No applicant notice. Output stored in the case record, but model version and prompt template are not logged | **No** |
| Explainable and interpretable | Each suggestion shows the extracted fields with a link to the source page; a reviewer can rebuild the basis for a sampled denial (95% or better) | Source links present. Basis could be rebuilt in 88% of 50 sampled denials | **Partial** |
| Privacy-enhanced | Only fields needed for the task sent to the model; SSNs masked; provider retention and no-training terms confirmed in writing | Full SSNs and whole documents sent; terms not confirmed (R-020) | **No** |
| Fair, with harmful bias managed | Error rate by group compared with its reference group (flag at more than 3 percentage points) | Spanish-language documents: income extraction errors 9.4% vs 3.2% for English. Households with a member aged 60 or older: outcome errors 11.8% vs 7.9%, because medical expenses were often left out of the calculation. Sex of the head of household: 8.1% vs 8.8%, not flagged. Race and ethnicity: not yet tested | **No** (2 flags) |

**What the results say.** The core problem is automation bias, not just model error: caseworkers accepted wrong suggestions far more often than they caught them. Asking the language model to reason about income limits also creates avoidable errors, because the calculation is deterministic and AC-03's rules are already configured in the platform.

### 4.1 Bias testing plan
The pilot sample is too small for reliable subgroup results. Before any expansion, the company and AC-03 will run this plan.

| Item | Plan |
|---|---|
| Groups compared | Document language (Spanish, Haitian Creole, and other non-English vs English); age (household member 60 or older vs none); disability (household with a member receiving disability benefits vs none); sex of the head of household; race and ethnicity (from the voluntary civil rights data AC-03 collects, used only with AC-03's written approval and only for testing) |
| Metrics | For each group: field extraction error rate; outcome disagreement with QC; rate of **adverse errors** (suggested denial or "more verification needed" where QC found the household eligible); caseworker acceptance rate of wrong suggestions |
| Thresholds | Flag if a group's error rate or adverse-error rate exceeds its reference group by more than 3 percentage points, or if the adverse-error ratio between groups is above 1.25. These thresholds are set by this assessment (repository rubric), not by regulation |
| Sample | 1,200 cases re-worked blind by AC-03 quality control, stratified so each group has at least 150 cases |
| Timing | Before any expansion, due 2026-12-31 (R-019); then quarterly on 300 new cases; and before any model version change |
| Response to a flag | Stop suggestions for the affected case type, fix, and retest before switching back on. Report every flag to AC-03's civil rights contact |
| Owner | Data and AI Lead, with AC-03 quality control |

## 5. MANAGE
**Human-in-the-loop design (required before suggestions are switched back on):**
- **Review first.** The caseworker checks the extracted fields against the documents and records their own finding before the suggested outcome is shown.
- **No AI text in notices.** Denial and pending notices use only reason codes the caseworker selects. The assistant's summary is never copied into a notice.
- **Adverse suggestions get extra review.** A suggested denial or "more verification needed" requires the caseworker to open the relevant source page. A supervisor reviews 10% of AI-assisted denials each week.
- **Override is simple and expected.** One click, with a reason code, and never counted against the caseworker. Override rates are reported by team, not by person.
- **Scope stays fixed.** 40 caseworkers in one region; no other programs or tenants.

**Technical changes:**
- Move income and eligibility calculations to the platform's deterministic rules engine, using AC-03's configured limits; the language model only extracts and summarizes.
- Check every policy citation against the current manual and block any that do not match.
- Mask SSNs and send only the fields each step needs.
- Filter and label document text so instructions inside uploaded files are treated as data (prompt-injection defense).
- Pin the model version, log the version and prompt template per case, and rerun the validation set before any version change (POL-01 4.3).

**Notice to applicants.** AC-03, as deployer, decides the wording; the company supports it in the portal and notices. Proposed text: "Automated tools help our staff read your documents. A caseworker reviews your application and makes every decision." Due 2026-11-30.

**Monitoring:**
- Monthly: 100-case QC sample, acceptance and override rates, adverse-error rate.
- Quarterly: the bias plan in section 4.1.
- Ongoing: fair hearing requests and complaints on AI-assisted cases are tagged and reviewed by the Data and AI Lead with AC-03.
- Results go to the AI review group and into the risk register (R-018, R-019).

**Incident handling (P08 and POL-03):**
- Applicant data exposed through the model service or a prompt-injection attack is a security incident. The AC-03 information security manager is told within 1 hour (POL-03 4.4), and the 10-day notice under Fla. Stat. 501.171(6)(a) applies if a breach is determined.
- A pattern of wrong suggestions (for example, a model update that miscounts income) is an AI incident. Switch suggestions off, tell AC-03 within 1 business day, and give AC-03 the list of affected cases so it can review and reopen them.

**Decommissioning.** Turn off suggestions, or the whole feature, if any of these happen:
- the model service's data-use, retention, and FedRAMP terms are not confirmed in writing by 2026-10-31 (then no applicant data goes to it);
- outcome agreement stays below 95% or the adverse-error threshold is missed for 2 months in a row;
- a bias flag stays unresolved for 90 days;
- AC-03 withdraws approval, or the provider changes its data-use terms.

On shutdown, delete prompts and outputs held outside the case record, and keep case-record entries under AC-03's retention rules.

## 6. Decision
**Approve with conditions.** Chief Executive Officer, 2026-08-31, with AC-03's written agreement. The pilot continues for the same 40 caseworkers, with these conditions:
1. **From 2026-09-08, suggested outcomes are switched off.** Document extraction continues, with caseworkers checking every extracted field against the source. Suggestions return only when conditions 3 and 4 are met.
2. **By 2026-10-31:** vendor review of the model service is complete, with FedRAMP scope, no-training, and retention terms confirmed in writing (R-020; POAM-010). SSN masking and data minimization are live. If not met, applicant data stops going to the model service.
3. **By 2026-11-30:** the human-review design above, deterministic calculations, citation checking, prompt-injection filtering, and version logging are live (R-018).
4. **By 2026-11-30:** the applicant notice is in use.
5. **By 2026-12-31:** the 1,200-case bias test is complete with no unresolved flag (R-019).

**Expansion** beyond the pilot region requires 2 consecutive months meeting every threshold in section 4, a new approval by the Chief Executive Officer, and AC-03's written agreement.

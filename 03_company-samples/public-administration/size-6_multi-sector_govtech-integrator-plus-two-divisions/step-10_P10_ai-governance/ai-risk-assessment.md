# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (GovTech Integration, IT Consulting, Government Software Products, corporate) |
| Tier / Vertical | Multi-Sector / Public Administration (focus division: GovTech Integration) |
| Scope | The group AI governance program (Group AI Standard, council, inventory), division use cases, and the regulator-specific rules for the two priority use cases: the IEP AI eligibility assistant (AI-001, GovTech) and the RMS AI report-writing assist (AI-002, Government Software Products) |
| Registry use case, adapted | The registry default is "AI eligibility determination for public benefits." Federal program rules keep the determination with state merit staff (7 CFR 272.4(a)(2); 42 CFR 431.10(b)(3)), so the group's tool may only **recommend**; the caseworker determines (`../00_company-facts.md` section 5) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (NIST AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), fieldwork 2026-07-13 to 2026-08-21, decisions 2026-08-28; presented to the board risk committee 2026-09-15. Quality control staff of the 2 IEP states and the RMS beta agencies' report supervisors took part in the measurements |
| Inventory | `ai-use-case-inventory.csv` (6 use cases: 2 High, 3 Medium, and 1 public-tool entry tiered High if regulated data is entered) |
| Links | P01 GR-04, GR-17, GT-008, GT-009, GT-025, SW-003, SW-013, SW-014, SW-017, IC-007; P03 AI-01 to AI-03, SW-G07, SW-G13 to SW-G17; P07 POAM-016, POAM-022; scenario gap 6 |

**Why this assessment exists now.** Both priority use cases went live before the Group AI Standard was adopted in 2026-06: the IEP assistant for caseworkers in 2 states in 2026-03, and the RMS assist as a feature-flag beta for 37 agencies on 2026-04-06 (scenario gap 6). Neither had bias or accuracy testing at the depth the standard now requires, one IEP state gives applicants no notice, and the RMS beta sent CJI to the model service before a CJIS review.

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk with cyber and enterprise risk; receives the High-tier list and monitoring quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, group public sector compliance director, GovTech Data and AI director, Software division RMS general manager, IT Consulting security and compliance lead. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner per use case (inventory); run monitoring and report monthly |
| Agency deployers | Each state human services agency and each RMS agency decides how the tool is used in its program and agrees in writing to any change in scope or design |
| Group CISO | AI security standard: prompt injection, model supply chain, data minimization, logging |
| Group Chief Privacy Officer | Use of applicant, CJI, and other regulated data in AI; agency notices |
| Group internal audit | Adds High-tier AI controls to the 2027 assessment (P07) |

### 1.2 Group AI Standard (adopted 2026-06, under POL-01 4.13)
1. **Register before use.** Every AI use case that touches agency, federal, or customer regulated data, or that supports decisions about people, is registered before deployment, beta, or material change. Feature-flag betas count.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier needs council approval, a pre-deployment impact assessment, bias and accuracy testing, notice to affected people (given by the agency as deployer), and quarterly monitoring.
3. **Data rules by type** (POL-04 4.9). No FTI in any AI service. CJI only after a CJIS review of the service and Security Addendum coverage. CUI and PHI only in services approved for them. No-training and limited-retention terms in writing before any regulated data flows.
4. **Program overlays.** The GovTech supplement adds the SNAP and Medicaid merit-staff rules; the Software supplement adds the AI and product change gate (CJIS, SOC 2 description, customer notice); the IT Consulting supplement adds CUI and client confidentiality rules.
5. **Change gate.** A new model, model version, provider, data type, decision role, or customer group triggers re-assessment before release.
6. **Approved tools only** for workforce generative AI (POL-05 4.7).

**Group AI platform pattern (proposed in P04).** Both priority use cases call provider A's managed model service. The council adopted one pattern for every group AI feature: private endpoints in the government-community region, prompt data minimization (masking of Social Security numbers and other identifiers), per-request logging of model version and prompt template without regulated content in the logs, and a pinned model version with a validation set rerun before any change.

**Where the program fell short in 2026.** The standard came after both priority use cases were live, and the Software division's feature-flag process let a beta reach 37 agencies without any review (P07 CM-03a.). POAM-016 and POAM-022 carry the fixes.

## 2. MAP (use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | IEP AI eligibility assistant | GovTech Integration | High | In production in 2 states; recommendations paused from 2026-10-01 |
| AI-002 | RMS AI report-writing assist | Government Software Products | High | Beta with 37 agencies; no new agencies; CJI to the model service stopped by 2026-10-01 |
| AI-003 | 311 chatbot | Government Software Products | Medium | In production |
| AI-004 | Permit plan review assistant | Government Software Products | Medium | In production |
| AI-005 | Enterprise generative AI assistant | Group | Medium | Approved |
| AI-006 | Public generative AI tools | Group (IT Consulting acquired estate) | High if regulated data is entered | Not approved; blocking on acquired endpoints due 2026-12-31 |

### 2.1 IEP AI eligibility assistant (AI-001)
| Item | Description |
|---|---|
| Purpose | For each SNAP, TANF, or Medicaid application in the 2 states, the assistant extracts fields from uploaded verification documents (pay stubs, identity documents, leases, utility bills), flags missing verifications, and recommends an outcome per program (likely eligible, likely ineligible, or more verification needed) with a reason summary citing the state's policy manual |
| Users | About 1,450 caseworkers, all state merit system employees, in Florida's human services agency and one other state's agency |
| Affected people | Applicant households: about 182,000 applications processed with the assistant from 2026-03 to 2026-08. Many are low-income, elderly, disabled, or have limited English |
| Data | Inputs: application data, household composition, income and expense documents, Social Security numbers. Retrieval: each state's policy manual. Outputs: extracted fields, a recommendation, and a reason summary in the case record. No training by the group; the model service's no-training and retention terms were confirmed in writing in 2026-07 (P01 GT-025) |
| FTI boundary | FTI is prohibited on the IEP (Pub. 1075 sec. 2.C.11.2: human services agencies "may not contract for services that involve the disclosure of FTI to contractors"). IRS income match results are FTI and must never reach the assistant. Copies of tax returns or W-2s provided directly by the applicant are not FTI (Pub. 1075, "Information Received from Taxpayers or Third Parties"), so the assistant may read them. Caseworkers pasting IRS data into notes is tracked as P01 GT-013 |
| HIPAA | Neither assistant state is one of the 2 Medicaid agencies that designated the group a business associate, so HIPAA does not reach the assistant today. Before the assistant is offered in a business associate state, the model service must be covered by business associate subcontractor terms (45 CFR 164.308(b)(2)) |
| Not intended | Making, approving, or issuing eligibility decisions; generating notice text; conducting interviews; fraud scoring; use for other programs |

| Rule | What it requires | What it means for the assistant |
|---|---|---|
| 7 CFR 272.4(a)(2) | State merit employees "shall perform the interviews"; "volunteers and other non-State agency employees shall not conduct certification interviews or certify SNAP applicants" | The assistant and group staff may not make the decision, and the caseworker's decision must be real, not a rubber stamp |
| 42 CFR 431.10(b)(3), (c) | The single State agency is responsible for determining Medicaid eligibility; it may delegate only to the government agencies the rule lists | Same conclusion for Medicaid. TANF follows each state's program rules, which the contracts apply in the same way |
| 7 CFR 273.10(g)(1)(ii), 273.15(a); 42 CFR 431.200(a) | Denial notices must explain the basis for the denial and the right to a fair hearing | Notice reasons must come from the caseworker's own finding. Outputs are kept so the state can explain a case at a hearing |
| 7 CFR 273.2(g)(1), (i)(3)(i) | SNAP: 30 days for normal processing; benefits by the 7th calendar day for expedited households | A wrong "more verification needed" flag can push a household past these dates |
| 7 CFR 272.6(a) | No discrimination in certification on the basis of age, race, color, sex, disability, religious creed, national origin, or political beliefs | The reason the bias tests below compare those groups where data allows |
| 7 CFR 272.4(b) | Bilingual program information and certification material for single-language minority households | The assistant must perform as well on non-English documents |
| 42 CFR 431.306(b); 7 CFR 272.1(c) | Access to applicant information limited to persons subject to comparable confidentiality standards; use limited to program purposes | The model service must be bound by contract terms before data flows (met for the IEP, P01 GT-025) |
| State data security law (Florida worked example: Fla. Stat. 501.171(2)) | Reasonable measures to protect personal information | Data minimization in prompts; masked Social Security numbers |
| Colorado SB26-189 (effective 2027-01-01; status unsettled) | Duties for developers and deployers of ADMT that materially influences consequential decisions, including essential government services | Not applicable today (no IEP customer in Colorado; P03 AI-03). Reassess before any Colorado bid (P01 GR-17) |

### 2.2 RMS AI report-writing assist (AI-002)
| Rule or commitment | Implication |
|---|---|
| CJISSECPOL v6.1 SA-9 and SC-28; the Security Addendum in each RMS agency agreement (28 CFR 20.33(a)(7)) | Dictation and incident data include CJI. An external service that processes CJI must meet CJIS requirements and be covered by the Addendum terms. **Gap:** CJI reached the model service before a CJIS review, and the 37 agencies were not told which service processes their CJI (P03 SW-G07) |
| Agency evidence and discovery rules (state by state; generic here) | Police narratives are used in charging decisions and in court. Agencies need the officer's dictation, the AI draft, and the officer's edits kept and producible, and a clear record that the officer adopted the final text |
| SOC 2 commitments (CC2.3, CC3.4, CC8.1, CC9.2) | The beta and the model service must be described for the 2026 report period, and the change evaluated (P09 section 3.2) |
| FTC Act Section 5 (N51-R01) | Accuracy or time-saving claims in marketing must be substantiated |

### 2.3 Other division use cases
- **311 chatbot (AI-003) and plan review assistant (AI-004):** no decisions about people; staff decide every request and every permit. Where a Civic Suite customer is a Texas governmental agency, TRAIGA places AI disclosure duties on the agency; the chatbot's built-in AI disclosure supports them. Both risks were accepted as Low in P01 (SW-014, SW-017).
- **Enterprise assistant (AI-005) and public tools (AI-006):** the main risk is consultants and staff entering client, agency, or CUI data into tools without contract terms (P01 IC-007). Public tools are blocked on group-managed endpoints; the acquired estate is the gap.

## 3. Risk tiers (repository rubric)
- **High:** AI-001 is a substantial factor in consequential decisions about essential government services (food, cash, and medical assistance). Caseworkers formally decide, but they **accepted 93% of recommendations** (P03 AI-01), so the recommendation is shaping outcomes. AI-002 shapes police narratives used in criminal proceedings, a legal and safety consequence for the people named.
- **Medium:** AI-003, AI-004, and AI-005. Humans make every decision; outputs reach residents or staff.
- **AI-006:** High whenever regulated data could be entered, which is why it is not approved.

**Re-tier triggers:** any state asking to auto-approve or auto-deny on the IEP (not permitted under 7 CFR 272.4(a)(2) and 42 CFR 431.10); the plan review assistant driving automatic permit decisions (AI-004 to High); the 311 chatbot taking applications or collecting regulated data (AI-003 re-assessment).

## 4. MEASURE
Results are from validation and monitoring between 2026-05 and 2026-08.

### 4.1 IEP AI eligibility assistant (AI-001)
**Validation sample.** Quality control staff in the 2 states re-worked 800 randomly selected AI-assisted applications (400 per state) without seeing the AI output; results were compared with the assistant's extraction and recommendations.

| Trustworthy characteristic | Test / metric (threshold) | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Income field accuracy (98% or better); agreement of the recommendation with the QC outcome (95% or better) | Income fields 96.4%; outcome agreement 92.0% (64 of 800 wrong) | **No** |
| Valid and reliable: confabulation (AI 600-1) | Reason summaries citing policy text not in the state's manual (0) | 9 of 800 (1.1%) | **No** |
| Safe (automation bias) | Share of wrong recommendations caught by caseworkers (80% or better); acceptance rate of all recommendations (flag above 90%) | Caseworkers caught 18 of 64 (28%); 17 of the 46 accepted led to incorrect denials, which the states reopened. Overall acceptance 93% | **No** |
| Secure and resilient | Prompt-injection test with 25 crafted documents (0 changed outcomes) | 2 of 25 changed the recommendation | **No** |
| Accountable and transparent | Applicants told that an automated tool helps staff; model version and prompt template logged per case | Notice in Florida's portal; **no notice in the other state**. Version and template not logged | **No** |
| Explainable and interpretable | Basis of a sampled denial can be rebuilt from source links (95% or better) | 89% of 100 sampled denials | **Partial** |
| Privacy-enhanced | Only needed fields sent; Social Security numbers masked; no-training and retention terms in writing | Terms confirmed 2026-07; full Social Security numbers and whole documents still sent | **Partial** |
| Fair, with harmful bias managed | Error rate by group against its reference group (flag at more than 3 percentage points) | Non-English documents: income extraction errors 8.7% vs 3.1% for English. Households with a member aged 60 or older: outcome errors 11.4% vs 7.0% (medical expense deductions often missed). Sex of the head of household: 7.8% vs 8.3%, not flagged. Race and ethnicity: not yet tested | **No** (2 flags; P01 GT-009) |

**What the results say.** The core problem is automation bias: caseworkers accepted wrong recommendations far more often than they caught them. Asking the language model to reason about income limits also creates avoidable errors, because the calculation is deterministic and each state's rules are already configured in the IEP.

**Bias testing plan (before any expansion; P01 GT-009):**
| Item | Plan |
|---|---|
| Groups compared | Document language (each non-English language with at least 150 cases vs English); age (household member 60 or older vs none); disability (household member receiving disability benefits vs none); sex of the head of household; race and ethnicity from the voluntary civil rights data each state collects, used only with the state's written approval and only for testing |
| Metrics | Field extraction error rate; outcome disagreement with QC; adverse-error rate (recommended denial or "more verification needed" where QC found the household eligible); caseworker acceptance of wrong recommendations |
| Thresholds | Flag if a group's error or adverse-error rate exceeds its reference group by more than 3 percentage points, or if the adverse-error ratio is above 1.25. These thresholds are set by this assessment (repository rubric), not by regulation |
| Sample | 2,400 cases re-worked blind by state QC staff (1,200 per state), stratified so each group has at least 150 cases |
| Timing | Complete by 2026-12-31; then quarterly on 600 new cases, and before any model version change |
| Response to a flag | Stop recommendations for the affected case type, fix, and retest before switching back on. Report every flag to each state's civil rights contact |

### 4.2 RMS AI report-writing assist (AI-002), using AI 600-1 risk areas
**Sample.** Report supervisors in 6 beta agencies compared 300 AI drafts with the officers' dictation and the final signed reports.

| AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Confabulation | Drafts adding a fact not in the dictation or incident data (target under 1%) | 2.3% (7 of 300), including 2 that added a detail about a suspect's statement | **No** |
| Information integrity (omissions) | Drafts omitting a material fact from the dictation (target under 2%) | 5.0% | **No** |
| Human-AI configuration | Officers' edits per draft; drafts signed with no edits | 41% signed with no edits, including 3 of the 7 drafts with added facts | **No** |
| Data privacy | CJIS review of the model service; no-retention terms; Security Addendum coverage | Not done before the beta (P03 SW-G07) | **No** |
| Information security (prompt injection) | Red-team test with crafted dictation and attachments | Not done | **No** |
| Value chain and component integration | Model service in the SOC 2 description; change gate | Not in the description; gate bypassed by feature flag | **No** |
| Transparency | Draft labeled as AI-generated inside the RMS; original dictation and draft retained | Labeled; dictation retained; draft overwritten when edited | **Partial** |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001 (required before recommendations resume):** the caseworker checks extracted fields against the documents and records a finding **before** the recommendation is shown; denial and pending notices use only reason codes the caseworker selects, never assistant text; an adverse recommendation requires opening the source page; a supervisor reviews 10% of AI-assisted denials each week; overrides are one click, with a reason code, and never counted against the caseworker. Income and eligibility calculations move to the IEP's deterministic rules engine; the language model only extracts and summarizes.
- **AI-002:** the draft opens only after the officer's dictation is saved; the officer must confirm each sentence that names a person's statement or action; the dictation, the AI draft, and the final text are all retained for discovery; the report shows that AI assisted the draft.

**Technical controls (group AI platform pattern):** mask Social Security numbers and send only the fields each step needs; check every policy citation against the current manual; filter and label document text so instructions in uploads are treated as data; pin model versions and log version and prompt template per case; rerun the validation set before any change.

**Notice to people affected.** Each IEP state, as deployer, decides the wording; the group supports it in the portal and notices. Proposed text: "Automated tools help our staff read your documents. A caseworker reviews your application and makes every decision." Due in both states by 2026-11-30.

**Monitoring:**
- Monthly: 200-case QC sample per IEP state; acceptance, override, and adverse-error rates; RMS draft accuracy sample from each beta agency.
- Quarterly: the bias plan in section 4.1; High-tier report to the council and the board risk committee.
- Ongoing: fair hearing requests and complaints on AI-assisted cases are tagged and reviewed with each state; RMS agencies report any draft error found after signing.
- Results update P01 GR-04, GT-008, GT-009, GT-025, SW-003, and SW-013.

**Incident handling (P08 and POL-03).** Exposure of applicant data or CJI through a model service is a security incident: the affected agency is told within 1 hour (POL-03 4.4), and state third-party agent clocks apply (Florida: 10 days, Fla. Stat. 501.171(6)(a)). For CJI, the CJISSECPOL v6.1 IR-6 path applies. A pattern of wrong outputs (for example a model update that miscounts income) is an AI incident: switch the feature off, tell the agency within 1 business day, and give it the list of affected cases or reports so it can review and reopen them.

**Decommissioning.** Turn off AI-001 recommendations, or AI-002 drafts, if outcome agreement or draft accuracy misses its threshold for 2 months in a row, a bias flag stays unresolved for 90 days, the model service changes its data-use terms, a CJIS review fails, or the agency withdraws approval. Both features have a manual fallback the BIA already covers (P05 BP-GT07 and BP-SW06 are Low criticality). On shutdown, delete prompts and outputs held outside the case or report record, and keep record entries under each agency's retention rules.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 IEP assistant | **Continue with conditions** (council, 2026-08-28; board risk committee informed 2026-09-15; both states agreed in writing) | Recommendations paused from 2026-10-01; document extraction continues with caseworker checks. Review-first design, deterministic calculations, citation checks, prompt-injection filtering, data minimization, and version logging live by 2026-11-30; applicant notice in both states by 2026-11-30; 2,400-case bias test with no unresolved flag by 2026-12-31 (POAM-016). Recommendations return only when all are met. No new state until 2 consecutive months meet every threshold and the council approves again |
| AI-002 RMS assist | **Not approved for general release; beta restricted** | No new beta agencies. CJI to the model service stopped and the 37 agencies told by 2026-10-01; CJIS review of the service and Security Addendum coverage by 2026-11-30; AI change gate for feature flags by 2026-12-31; SOC 2 description updated for the 2026 period; draft retention and sentence confirmation built; accuracy targets met on a new 300-draft sample before the beta resumes (POAM-022) |
| AI-003 311 chatbot | **Approved** | Standard monitoring; keep AI disclosure and human handoff; no collection of regulated data |
| AI-004 plan review assistant | **Approved** | Flags stay advisory; re-assess before any automation of permit decisions |
| AI-005 enterprise assistant | **Approved** | No CJI, FTI, CUI, PHI, or motor vehicle records; rollout to acquired staff with migration |
| AI-006 public tools | **Not approved** | Block on acquired endpoints by 2026-12-31 (P01 IC-007) |

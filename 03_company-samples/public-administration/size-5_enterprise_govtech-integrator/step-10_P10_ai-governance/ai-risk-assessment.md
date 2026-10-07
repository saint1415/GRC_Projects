# AI Governance Risk Assessment: Enterprise AI Portfolio and the AI Eligibility Assistant

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded GovTech systems integrator serving state and local agencies) |
| Tier / Vertical | Enterprise / Public Administration |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the AI eligibility assistant, in section 6 |
| Registry default, adapted | "AI eligibility determination for public benefits" is assessed as **decision support**, not determination. SNAP households must be certified by state merit staff (7 CFR 272.4(a)(2)), and the Medicaid agency determines Medicaid eligibility (42 CFR 431.10). A company tool that decides eligibility would not be lawful for these programs, so the question is whether a tool that only suggests is, in practice, deciding |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1), because AI-001 uses a large language model; repository risk tier rubric |
| Assessors / dates | GRC team and the Chief Data and AI Officer's staff, with AG-03's information security manager and quality control supervisors for AI-001. Fieldwork 2026-07-06 to 2026-08-14; AI governance committee review 2026-08-19 |
| Decision | Executive risk committee, 2026-09-10 (section 8) |
| Links | P01 R-011, R-012, R-041 to R-044, R-065; P03 G-125, SN-02; P07 POAM-022; POL-04 4.8; POL-05 4.4 |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 4, Medium 5, Low 3 |
| Status | In production 9, Pilot 1, Suspended 1, Declined 1 |
| AI governance committee review complete | 8 of 12 |
| Not yet reviewed | 4: AI-005, AI-009, AI-010, AI-012 (all due 2026-12-31, POAM-022) |
| Company role | Developer for 4 (AI-001, AI-003, AI-010, and AI-008 as proposed); operator of a configured vendor model for 3 (AI-002, AI-004, AI-005); deployer of vendor tools for 4 (AI-007, AI-009, AI-011, AI-012); host of an agency-owned instrument for 1 (AI-006) |
| High-tier use cases affecting the public | AI-001 (benefits), AI-006 (pretrial release), AI-008 (declined) |

**Main findings:**
1. **AI-001 is acting like a decision maker.** Caseworkers accepted 88% of its suggestions, and in a blind re-work of 600 cases they caught only 41% of the wrong ones (section 6). The tool is advisory on paper only.
2. **Bias testing was too narrow.** AI-001 was tested only on English-language data before the pilot. In the validation sample it made more errors on Spanish and Haitian Creole documents and for households with a member aged 60 or older.
3. **Four use cases entered without review.** Two came in through vendor feature releases (AI-005, AI-009), one with the AQ-1 acquisition (AI-010), and one through the HR suite (AI-012, now suspended). The intake gate did not cover vendor features switched on inside existing products, or acquired systems.
4. **The pilot started without a risk assessment.** The committee approved AI-001 at intake on 2026-02-18 as a pilot without the assessment its tier requires (P03 G-125).

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. AI risks roll up to enterprise risk ER-08, "strategic and public trust" (P01), which the board risk committee reviews quarterly.

**Members:** Chief Data and AI Officer (chair); CISO; Chief Privacy Officer; Chief Compliance Officer; the General Counsel's delegate; Chief Human Resources Officer (for workforce tools); the presidents of Eligibility and Enrollment Operations and of State and Local Platforms (or their delegates); Director of Regulated Data Compliance; and a civil rights and accessibility lead. Internal Audit observes without a vote. For a use case that touches an agency program, the agency's program and security contacts join the review.

**Decision rights by tier** (consistent with risk acceptance levels in POL-01 4.4):
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee; the deploying agency's written agreement where the tool supports an agency program | Impact assessment; pre-deployment bias testing on data like the people affected, in their languages; human review design that keeps the decision with the lawful decision maker; notice to affected people; monitoring plan |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review |
| Low | Committee chair (fast track) | Listing on the approved AI tools list (STD-05.3); data handling rules (POL-04) |

**Intake.** Any new AI use must be registered before use (POL-05 4.4; STD-05.3). From 2026-10-01, three new gates close the gaps in finding 3: procurement and change management block AI features in vendor releases until they have an inventory ID; acquisition due diligence includes an AI inventory of the target (PRC-01.4); and the quarterly inventory sweep checks vendor release notes for AI features.

**Data rules.** Regulated or Restricted data may go to an AI service only if the committee approved the use case and the service has written no-training and retention terms and a confirmed FedRAMP scope (POL-04 4.8). FTI may never go to any AI service. Public AI tools are blocked for company work (POL-05 4.4; R-041).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier use case; annual re-review of every use case; re-review after a model version change.

## 3. MAP: context and applicable rules
| Rule | Applies? | What it means for the portfolio |
|---|---|---|
| SNAP certification by merit staff, 7 CFR 272.4(a)(2) | **Yes**, by IES contract | Only state merit employees certify SNAP households. AI-001 and company staff may only support the decision |
| Medicaid eligibility by the single State agency, 42 CFR 431.10 | **Yes**, by IES contract | The Medicaid agency determines eligibility. AI-001 extracts data for Medicaid cases but does not suggest Medicaid outcomes |
| SNAP and Medicaid notices and fair hearings, 7 CFR 273.10(g)(1)(ii), 273.15(a); 42 CFR 431.200(a) | **Yes** | Denial notices must state the basis, and agencies must be able to explain a case at a hearing, so AI-assisted cases need logged inputs and outputs |
| SNAP processing deadlines, 7 CFR 273.2(g)(1), (i)(3)(i) | **Yes** | 30 days for normal processing; benefits by the 7th calendar day for expedited households. A wrong "more verification needed" flag can push a family past these dates |
| SNAP nondiscrimination, 7 CFR 272.6(a); bilingual service, 7 CFR 272.4(b) | **Yes** | Certification must not discriminate on protected bases, and agencies must serve single-language minority households. These set the groups for bias testing (section 6.5) |
| Medicaid and SNAP confidentiality, 42 CFR 431.306(b) (N92-R04); 7 CFR 272.1(c) | **Yes** | Applicant data may go only to parties bound by comparable confidentiality; model service terms are required before data flows (R-042) |
| IRS Pub. 1075 (N92-R01) | **Boundary** | FTI is prohibited in IES (Pub. 1075 sec. 2.C.11.2) and in every AI service. Copies of tax returns supplied by applicants are not FTI and may be read by AI-001 |
| FBI CJIS Security Policy (N92-R02) | Yes, for AI-006, AI-009, AI-010 | CJI in AI tools stays inside CJIS-compliant systems with screened staff; vendor features that send log fragments out need review (AI-009) |
| HIPAA (N92-R03) | AI-002 only | The company is a business associate of AG-04 only; AI-002 processes AG-04 documents under that agreement. AI-001 runs only for AG-03 |
| Fla. Stat. 501.171(2) | **Yes** | Reasonable measures to protect personal information, including data sent to AI services, for Florida agency customers |
| State recording consent laws | AI-005 | All-party consent is announced on every contact center call. Florida worked example: interception is lawful when all parties have given prior consent (Fla. Stat. 934.03(2)(d)) |
| Colorado SB26-189 (automated decision-making technology; effective 2027-01-01) | **Not today** for agency programs; **counsel to confirm** for AI-012 | It covers developers and deployers doing business in Colorado whose technology materially influences consequential decisions, including essential government services and employment. The company has no Colorado customers (P03 section 1). Remote hiring may reach Colorado residents, so counsel decides before AI-012 ranking is re-enabled. Reassess before any bid to a Colorado agency |
| Other state AI employment rules (for example California's civil rights regulations on automated-decision systems, Illinois HB 3773) | AI-012, counsel to confirm | Apply if the company hires in those states; HR keeps the list of states where applicants and remote staff live |
| Texas TRAIGA | Not today | Disclosure duties for government agencies in Texas; no Texas customers |
| OMB M-25-21 | No | Applies to federal agencies; its "high-impact AI" minimum practices are a useful comparison, and Federal Programs customers may flow them down by contract |
| Federal preemption efforts (EO 14365) | Watch | The order does not itself preempt any state law; counsel tracks litigation and any federal statute |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person (here essential government services, liberty, or employment), or able to affect physical safety.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | AI eligibility assistant (IES, AG-03 pilot) | High | Pilot (120 caseworkers, 1 region); suggestions off from 2026-09-11 | Intake 2026-02-18; full assessment 2026-08-19 |
| AI-002 | Document classification and extraction (IES document processing) | Medium | In production (4 states) | Reviewed 2025-11-12 |
| AI-003 | Case note summarization (ACMC local government tenants) | Medium | In production (41 tenants) | Reviewed 2026-04-22 |
| AI-004 | Contact center virtual agent (IES) | Medium | In production (2 states) | Reviewed 2026-01-21 |
| AI-005 | Call transcription and quality analytics (IES contact centers) | Medium | In production (4 states) | **Not reviewed** (due 2026-12-31) |
| AI-006 | Pretrial risk instrument scoring configured for AG-02 | High | In production | Reviewed 2025-12-03 |
| AI-007 | Code assistant for engineers | Low | In production | Reviewed 2025-10-08 |
| AI-008 | Fraud-risk scoring for case reviews (proposed by one state) | High | Declined 2026-08-19 | Reviewed and declined 2026-08-19 |
| AI-009 | SOC alert triage assistant | Low | In production | **Not reviewed** (due 2026-12-31) |
| AI-010 | AQ-1 e-filing redaction suggestions | Medium | In production (9 courts) | **Not reviewed** (due 2026-12-31) |
| AI-011 | Enterprise generative AI assistant | Low | In production | Reviewed 2026-05-27 |
| AI-012 | Recruiting assistant ranking applicants | High | Suspended (ranking disabled 2026-08-24) | **Not reviewed** (due 2026-12-31) |

**Tiering notes:**
- **AI-006 is High although it is not machine learning.** It is a points-based instrument the agency chose and validated, and judges make release decisions. The committee inventories it because the company computes a score that shapes a decision about a person's liberty. The company's duty is to compute the score exactly as published (scoring regression tests on every release); validation and fairness of the instrument are AG-02's.
- **AI-010 is Medium,** because a missed redaction can expose sealed or juvenile information and Social Security numbers in court filings, but it makes no decision about anyone. If the miss rate proves high, the committee can raise it to High.
- **AI-005 is Medium today** and becomes High if call scores are used to rate staff performance (an employment decision). The review must confirm how supervisors use it.
- **AI-011 is Low** because Regulated and Restricted data are prohibited in it and blocked by data loss prevention.

## 5. MANAGE: portfolio controls
- **Monitoring:** every High-tier use case reports quarterly performance and fairness metrics (inventory column `monitoring`) to the committee; a threshold breach or model version change triggers re-review.
- **AI incidents:** unsafe or wrong output at scale, a bias finding, prompt injection, or data misuse is logged as an AI incident. Security or data incidents follow P08 and POL-03 (1-hour agency notice for agency data). Outcome errors in an agency program are reported to the agency within 1 business day with the list of affected cases.
- **Third parties:** AI vendors are tier-1 in the vendor program (POL-01 4.8). Contracts require no training on company or agency data, retention limits, U.S. processing, and notice of material model changes. The managed language model service terms were confirmed in writing in 2026-07 (R-042).
- **Records:** model version, prompt template, inputs, and outputs are logged per case for High-tier use cases, kept with the case record under each agency's retention rules, so agencies can explain decisions at fair hearings.
- **Decommissioning:** a use case is switched off if it fails its monitoring thresholds two periods in a row, if its vendor changes data-use terms, or if the deploying agency withdraws approval. The inventory records retirement.

## 6. Full assessment: AI-001, the AI eligibility assistant
### 6.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Speed up application processing in IES for AG-03. For each application in the pilot region, the assistant (1) reads uploaded verification documents (pay stubs, identity documents, leases, utility bills) and extracts fields into the case for SNAP, TANF, and Medicaid; (2) flags missing verifications; and (3) for SNAP and TANF only, suggests an outcome (likely eligible, likely ineligible, or more verification needed) with a short reason summary citing AG-03's policy manual |
| Company role | **Developer and operator.** AG-03, the state human services agency, is the **deployer** and makes every eligibility decision through its caseworkers |
| Users / operators | 120 AG-03 caseworkers (state merit system employees) in one region, since 2026-03-02 |
| Affected people | Applicant households in the pilot region: about 31,000 applications from March to July 2026. Many are low-income, elderly, disabled, or have limited English proficiency; Spanish and Haitian Creole documents are common in the region |
| Data | **Inputs:** application data, household composition, income and expense documents, Social Security numbers (sent in full today). **Retrieval:** AG-03's policy manual. **Outputs:** extracted fields, suggested outcome, reason summary, stored in the case record. **Training:** none by the company; the foundation model is pre-trained by the provider. The provider confirmed in writing in 2026-07 that prompts are not used for training, abuse-monitoring retention is disabled, and the service is in FedRAMP scope (R-042; P04) |
| FTI boundary | FTI is prohibited in IES (Pub. 1075 sec. 2.C.11.2). IRS income match results are FTI and never reach IES or the assistant; the AG-03 interface sends no income match fields. Copies of tax returns or W-2s supplied by applicants are not FTI, so the assistant may read them |
| Build or buy | Build on a bought model: the company wrote the application logic, prompts, and retrieval; the language model is the managed service in the IES account on Cloud provider B (P04) |
| Not intended | Making, approving, or issuing eligibility decisions; Medicaid outcome suggestions; generating notice text; interviews; fraud scoring (AI-008 was declined); use for any other state |

### 6.2 Risk tier
**High.** The assistant is a substantial factor in consequential decisions about essential government services: food, cash, and medical assistance. The caseworker formally decides, but at 88% acceptance with most wrong suggestions accepted, the suggestion is shaping the outcome. The High-tier minimum controls (rubric) are human review before action, pre-deployment bias testing, an impact assessment, notice to affected people, and monitoring. On 2026-08-19 only the first existed, and only in form.

### 6.3 Data sources for the measurements
- **System logs** for all pilot cases (March to July 2026): acceptance and override rates.
- **Validation sample:** AG-03 quality control staff re-worked 600 randomly selected pilot applications without seeing the AI output; results were compared with the assistant's extraction and suggestions. Subgroups are small, so subgroup results are indicative and the stratified test in section 6.5 is required.
- **Security tests:** 25 crafted documents for prompt injection, run in a test environment with synthetic data.

### 6.4 MEASURE
| Trustworthy characteristic | Test / metric (threshold) | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Income and household-size field accuracy (98% or better); suggested outcome agrees with QC (95% or better) | Income fields 95.8% (errors on multi-page pay stubs and handwritten statements); outcome agreement 91.0% (54 of 600 wrong) | **No** |
| Valid and reliable: confabulation (AI 600-1) | Reason summaries citing policy text not in AG-03's manual (0) | 9 of 600 (1.5%) cited sections that do not exist | **No** |
| Safe | Share of wrong suggestions caught by caseworkers (80% or better); cases pushed past a SNAP processing deadline by the assistant (0) | Caseworkers caught 22 of 54 (41%) and accepted 32. 11 of the 32 led to incorrect denials, which AG-03 has reopened. No deadline misses found in the sample | **No** |
| Secure and resilient | Prompt-injection test (0 of 25 documents change a suggestion); access limited to pilot caseworkers; model service in FedRAMP scope | 4 of 25 test documents changed the suggestion (R-043). Access correctly limited through AG-03's identity provider. FedRAMP scope confirmed 2026-07 | **No** |
| Accountable and transparent | Applicants told that an automated tool helps staff; model version, prompt template, and output logged per case | No applicant notice. Output stored in the case record, but model version and prompt template not logged (R-065) | **No** |
| Explainable and interpretable | Each extracted field links to its source page; a reviewer can rebuild the basis for a sampled denial (95% or better) | Source links present. Basis rebuilt in 86% of 50 sampled denials | **Partial** |
| Privacy-enhanced | Only the fields each step needs are sent; Social Security numbers masked; written no-training and retention terms | Terms confirmed. Full Social Security numbers and whole documents are still sent | **Partial** |
| Fair, with harmful bias managed | Error rate by group against its reference group (flag at more than 3 percentage points) | Income extraction errors: Spanish documents 8.9% (124 cases) and Haitian Creole documents 15.2% (46 cases, indicative only) against 3.0% for English (430). Outcome errors: households with a member aged 60 or older 13.1% (130) against 7.9% (470), mostly because medical expenses were left out. Sex of head of household 8.6% against 9.4%, not flagged. Disability, race, and ethnicity not yet tested | **No** (3 flags) |

**What the results say.** The core problem is automation bias, not only model error: caseworkers accepted wrong suggestions far more often than they caught them (R-011). Asking the language model to reason about income limits also creates avoidable errors, because the calculation is deterministic and AG-03's rules are already configured in the IES rules engine. The language gaps (R-012) fall on the households that 7 CFR 272.4(b) and 272.6(a) most protect.

### 6.5 Bias testing plan
| Item | Plan |
|---|---|
| Groups compared | Document language (Spanish, Haitian Creole, and other non-English against English); age (household member 60 or older against none); disability (household member receiving disability benefits against none); sex of the head of household; race and ethnicity (from AG-03's voluntary civil rights data, used only with AG-03's written approval and only for testing) |
| Metrics | Field extraction error rate; outcome disagreement with QC; **adverse-error rate** (suggested denial or "more verification needed" where QC found the household eligible); caseworker acceptance of wrong suggestions |
| Thresholds | Flag if a group's error rate or adverse-error rate exceeds its reference group by more than 3 percentage points, or if the adverse-error ratio between groups is above 1.25. These thresholds are set by this assessment (repository rubric), not by regulation |
| Sample | 1,500 cases re-worked blind by AG-03 quality control, stratified so each compared group has at least 250 cases (R-012) |
| Timing | Before any re-enablement of suggestions, due 2026-12-31 (POAM-022); then quarterly on 300 new cases; and before any model version change |
| Response to a flag | Keep suggestions off for the affected case type, fix, and retest. Report every flag to AG-03's civil rights contact |
| Owner | Chief Data and AI Officer, with AG-03 quality control |

### 6.6 MANAGE
**Human-in-the-loop design (required before suggestions return):**
- **Review first.** The caseworker checks the extracted fields against the documents and records their own finding before the suggested outcome is shown.
- **No AI text in notices.** Denial and pending notices use only reason codes the caseworker selects; the assistant's summary is never copied into a notice.
- **Adverse suggestions get extra review.** A suggested denial or "more verification needed" requires the caseworker to open the source page. A supervisor reviews 10% of AI-assisted denials each week.
- **Override is simple and expected.** One click with a reason code, never counted against the caseworker. Override rates are reported by team, not by person.
- **Scope stays fixed:** 120 caseworkers in one region; SNAP and TANF suggestions only.

**Technical changes:** move income and eligibility calculations to the deterministic rules engine, so the language model only extracts and summarizes; check every policy citation against the current manual and block any that do not match; mask Social Security numbers and send only the fields each step needs; filter and label document text so instructions inside uploaded files are treated as data (R-043); pin the model version and log version and prompt template per case (R-065).

**Notice to applicants.** AG-03, as deployer, decides the wording; the company supports it in the portal and notices. Proposed text: "Automated tools help our staff read your documents. A caseworker reviews your application and makes every decision." Due 2026-11-30 (R-065).

**Monitoring:** monthly 100-case QC sample with acceptance, override, and adverse-error rates; quarterly bias test (section 6.5); fair hearing requests and complaints on AI-assisted cases tagged and reviewed with AG-03. Results go to the committee and into the risk register (R-011, R-012).

**Incident handling (P08; POL-03):** applicant data exposed through the model service or a prompt-injection attack is a security incident, reported to AG-03's information security officer within 1 hour (POL-03 4.4), with the 10-day third-party agent notice under Fla. Stat. 501.171(6)(a) if a breach is determined. A pattern of wrong suggestions is an AI incident: switch suggestions off, tell AG-03 within 1 business day, and give it the list of affected cases to review and reopen.

**Decommissioning:** turn off suggestions, or the whole feature, if outcome agreement stays below 95% or the adverse-error threshold is missed for 2 months in a row; if a bias flag stays unresolved for 90 days; if AG-03 withdraws approval; or if the provider changes its data-use terms. On shutdown, delete prompts and outputs held outside the case record, and keep case-record entries under AG-03's retention rules.

## 7. Agencies as deployers
For AI-001, AI-003, AI-006, and AI-010, an agency or court relies on output from a tool the company builds, configures, or hosts. The company gives each one a short **tool fact sheet**: intended use and limits, data used, known limitations and test results by group, human review instructions, and how to report problems. This mirrors the developer documentation that laws such as Colorado SB26-189 would require if they applied, so the company is ready if it bids for a customer in such a state.

## 8. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the AI governance committee's recommendation of 2026-08-19:
1. **AI-001: approved with conditions,** with AG-03's written agreement.
   - From **2026-09-11**, suggested outcomes are switched off. Document extraction continues, with caseworkers checking every extracted field against the source.
   - By **2026-11-30**: review-first design, deterministic calculations, citation checking, prompt-injection filtering, Social Security number masking, version logging, and the applicant notice are live (R-011, R-043, R-065).
   - By **2026-12-31**: the 1,500-case stratified bias test is complete with no unresolved flag (R-012).
   - Suggestions return only when all conditions are met. **Expansion** beyond the pilot region needs 2 consecutive months meeting every threshold in section 6.4, a new committee and executive risk committee approval, and AG-03's written agreement.
2. **AI-002, AI-003, AI-004, AI-006, AI-007, AI-011:** continue under their reviews; AI-006 adds a quarterly override rate report to AG-02.
3. **AI-005, AI-009, AI-010:** may continue in current scope until committee review by 2026-12-31; no expansion. AI-010's review must measure the redaction miss rate on a sample of filings.
4. **AI-012:** ranking stays disabled until committee review, an adverse impact analysis, and counsel's state-law review are complete.
5. **AI-008:** declined; a new proposal needs a full impact assessment first (R-044).
6. **Intake gates** for vendor AI features and acquisitions (section 2) take effect 2026-10-01. Progress is tracked in POAM-022.

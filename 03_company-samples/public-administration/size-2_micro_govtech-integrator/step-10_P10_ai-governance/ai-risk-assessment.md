# AI Risk Assessment: AI Pre-screening for a County Emergency Assistance Program

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (GovTech systems integrator serving state and local agencies) |
| Tier / Vertical | Micro / Public Administration |
| AI use case | AI-001: the platform vendor's generative AI add-on (SYS-09), configured by the company in the AC-02 workspace. It reads application documents and suggests "likely eligible", "likely ineligible", or "needs information" to AC-02 caseworkers. Pilot since 2026-06-01 for 6 of the 9 caseworkers |
| Roles | **Platform vendor:** developer (built the add-on; supplies the model through a subprocessor). **Company:** integrator and operator (turned the add-on on, wrote the prompt and the program rules it reads, runs it). **AC-02 county human services department:** deployer and decision maker for every application |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the Generative AI Profile (NIST AI 600-1), because the add-on uses a large language model |
| Assessor / date | Owner with the Operations Manager and the Lead Platform Engineer; the AC-02 program manager and a county quality control supervisor took part. Fieldwork 2026-08-10 to 2026-08-21; approved 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |
| Links | P01 R-015, R-016, R-019; scenario-facts gap 13; POL-04 4.6; POL-02 A.5 |

**Why this assessment exists now.** The owner turned the add-on on for AC-02 on 2026-06-01, at the program manager's request, without an AI risk assessment, a security review of the add-on, bias testing, a written human-review rule, or notice to applicants (scenario-facts gap 13). That broke the rule the company has now written down: no vendor feature gets agency data before a review and contract terms (POL-02 A.5).

## 1. GOVERN
- **Accountable owner (company):** the owner. **Business owner (deployer):** the AC-02 program manager.
- **Decision authority.** The use case is High tier (section 3), so the owner approves it, as for any High risk (POL-02 A.3). AC-02 must agree in writing to any change in scope, because the program and every decision are the county's.
- **Policies that apply:**
  - POL-02 A.5: no review, no contract, no agency data, including add-on features and pilots
  - POL-04 4.6: agency data only to AI services on the approved list
  - POL-02 A.2: a risk assessment after major changes (turning on a vendor model change or a new workspace counts)
- **Approved AI services list.** Kept by the Operations Manager. On 2026-08-31 it has one entry: the platform AI add-on, for the AC-02 workspace only, **suspended** until the conditions in section 6 are met. No public AI tool is approved (AI-002).
- **Scale for a Micro company.** No AI committee. The owner, the Operations Manager, and the Lead Platform Engineer review AI use at the monthly security meeting; the AC-02 program manager joins quarterly.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Speed up decisions in the county-funded Emergency Assistance Program (one-time rent or utility payments for residents facing eviction or shutoff, income at or below the county's published limit). For each application the add-on: (1) reads uploaded documents (pay stubs, benefit award letters, leases, eviction or shutoff notices, IDs) and extracts fields; (2) flags missing documents; (3) suggests an outcome with a short reason that cites the county's program rules |
| Users | 6 AC-02 caseworkers (county employees) |
| Affected people | Applicant households: about 640 applications were processed with suggestions from June to July 2026. Many applicants are low-income, elderly, or disabled, and some submit documents in Spanish or Haitian Creole |
| Data | **Inputs:** application fields, household members, income documents, and Social Security numbers (sent in full today). **Rules:** the county's program manual, loaded by the company. **Outputs:** extracted fields and a suggestion with a reason, saved in the case record. **Training:** none by the company. The vendor's general terms say customer data is not used for training, but the add-on's own terms, its data retention, and its model subprocessor are not covered by the vendor's SOC 2 report or FedRAMP authorization (P09 Part B; vendor letter, August 2026) |
| Build or buy | **Configure a bought feature.** The vendor built the add-on and supplies the model; the company wrote the prompt and loaded the rules |
| Not intended | Making, approving, or issuing decisions; writing denial notices; fraud scoring; use in any other workspace (never in AC-01, which holds CJI). Any of these would need a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | What it means for the add-on |
|---|---|---|
| ADA Title II regulation, 28 CFR 35.130 | **Yes** (the county is a public entity under 28 CFR 35.104) | A public entity may not, "directly or through contractual, licensing, or other arrangements," discriminate on the basis of disability (35.130(b)(1)), may not use "criteria or methods of administration" that have that effect (35.130(b)(3)), and may not "impose or apply eligibility criteria that screen out or tend to screen out" people with disabilities unless necessary (35.130(b)(8)). A tool that pends more applications with disability benefit income (section 4) is such a method, used through the company's contract |
| Title VI of the Civil Rights Act, 42 U.S.C. 2000d | **Yes**, as confirmed by AC-02 | No exclusion or discrimination on the ground of race, color, or national origin "under any program or activity receiving Federal financial assistance." The county confirmed in writing that its human services department receives federal financial assistance for other programs, and "program or activity" covers "all of the operations of" a department of a local government (42 U.S.C. 2000d-4a). Higher error rates for documents in Spanish or Haitian Creole raise a national origin discrimination risk; county counsel to confirm the analysis |
| County program rule (AC-02 contract) | **Yes** | A complete application gets a decision within 5 business days, and a denial notice states the reason and the county's appeal process. The reason must be the caseworker's own finding, and the add-on's output must be kept so the county can explain a decision on appeal |
| Fla. Stat. 119.071(5)(a) | **Yes** (county duty the company supports) | Social Security numbers held by an agency are confidential and exempt from public disclosure (119.071(5)(a)5.), and an agency may use them only for the purpose in its written statement of collection (119.071(5)(a)2.c.). AC-02 must confirm that AI pre-screening fits that purpose; the company will mask them anyway |
| Fla. Stat. 119.0701(2)(b) | **Yes** (directly, through the AC-02 contract) | The suggestions and reasons saved in case records are county public records the company must keep and produce on request, while protecting exempt content |
| Fla. Stat. 501.171(2) | **Yes** (directly) | Reasonable measures to protect personal information such as Social Security numbers, including data sent to the add-on and its subprocessor |
| Federal benefit program rules (SNAP, TANF, Medicaid) | No | The program is county-funded |
| HIPAA | No | The program is not a health plan or provider; no business associate designation |
| State AI laws in other states (for example Colorado SB26-189 on automated decision-making in essential government services) | Not today | The company and all its customers are in Florida. Reassess before contracting with an agency in a state with such a law |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why High:** the add-on is a substantial factor in consequential decisions about an essential government service (emergency housing and utility help). The caseworker formally decides, but in the pilot **caseworkers accepted about 93% of suggestions**, and in the validation sample they accepted most of the suggestions that were wrong (section 4). At that level the suggestion shapes the outcome.

**Minimum controls for High (rubric):** human review before action, pre-deployment bias testing, an impact assessment (this document), notice to affected people, and ongoing monitoring. On 2026-08-31 only the first exists, and only informally.

## 4. MEASURE
**Validation sample.** The county quality control supervisor re-worked 120 randomly selected pilot applications (June to July 2026) without seeing the add-on's output, 2026-08-10 to 2026-08-14. The Lead Platform Engineer compared the results with the add-on's extraction and suggestions.

| Trustworthy characteristic | Test / metric (threshold) | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Income field accuracy (98% or better); agreement of the suggestion with the QC outcome (95% or better) | Income fields 95.8% (errors on multi-page pay stubs and handwritten statements); agreement 89.2% (107 of 120; 13 wrong) | **No** |
| Valid and reliable: confabulation (AI 600-1) | Reasons that cite a program rule not in the county manual (0) | 4 of 120 (3.3%) cited rules that do not exist | **No** |
| Safe | Share of wrong suggestions caught by caseworkers (80% or better); households harmed (0) | Caseworkers caught 5 of 13 and accepted 8. 3 led to incorrect denials, which AC-02 has reopened; 5 pended complete applications, adding 2 to 4 business days | **No** |
| Secure and resilient | Prompt-injection test with 10 crafted documents (0 changed outcomes); security evidence for the add-on; access limited to the 6 caseworkers | 2 of 10 crafted documents changed the suggestion. No security evidence: the add-on is outside the vendor's SOC 2 report and FedRAMP authorization. Access correctly limited by role | **No** |
| Accountable and transparent | Applicants told that an automated tool helps staff; model version and prompt logged per case | No applicant notice. Suggestion saved in the case record; model version and prompt not logged | **No** |
| Explainable and interpretable | Each suggestion shows extracted fields with a link to the source page; a reviewer can rebuild the basis for a sampled denial | Source links present; basis rebuilt for 18 of 20 sampled denials | **Partial** |
| Privacy-enhanced | Only needed fields sent; Social Security numbers masked; retention and no-training terms confirmed in writing | Whole documents and full Social Security numbers sent; terms not confirmed (R-019) | **No** |
| Fair, with harmful bias managed | Error rate by group compared with its reference group (flag at more than 3 percentage points) | Documents in Spanish or Haitian Creole: income extraction errors 4 of 28 (14.3%) vs 3 of 92 (3.3%) for English. Households with disability benefit income: suggested "needs information" 6 of 19 (31.6%) vs 9 of 101 (8.9%), because award letters were not read as income proof. Households with a member aged 60 or older: 2 of 21 (9.5%) vs 11 of 99 (11.1%) wrong, not flagged | **No** (2 flags) |

**What the results say.** The core problem is automation bias combined with an untested tool: caseworkers accepted wrong suggestions more often than they caught them, and the two flagged groups (non-English documents and disability income) are exactly the ones ADA Title II and Title VI protect. Asking a language model to apply income limits also creates avoidable errors, because the limit check is simple arithmetic the platform can do without a model.

### 4.1 Bias testing plan
The pilot sample is too small for reliable subgroup results. Before any restart of suggestions, the company and AC-02 will run this plan.

| Item | Plan |
|---|---|
| Groups compared | Document language (Spanish, Haitian Creole vs English); disability benefit income vs none; household member aged 60 or older vs none; sex of the applicant; race and ethnicity only from voluntary data AC-02 already collects, used only with AC-02's written approval and only for testing |
| Metrics | For each group: extraction error rate; disagreement with QC; rate of **adverse errors** (suggested "likely ineligible" or "needs information" where QC found the household eligible); caseworker acceptance of wrong suggestions |
| Thresholds | Flag if a group's error rate or adverse-error rate exceeds its reference group by more than 3 percentage points. These thresholds are set by this assessment (repository rubric), not by regulation |
| Sample | 300 applications re-worked blind by county QC, with at least 40 in each flagged group |
| Timing | Before any restart of suggestions (due 2026-11-30, R-016); then quarterly on 60 new cases; and before any model change by the vendor |
| Response to a flag | Turn suggestions off for the affected case type, fix, and retest. Report every flag to the AC-02 program manager and the county's ADA coordinator |
| Owner | Owner, with the Lead Platform Engineer and AC-02 quality control |

## 5. MANAGE
**Data protection (before any applicant data goes to the add-on again):**
- Written terms from the platform vendor for the add-on and its model subprocessor: U.S.-only processing, no retention beyond the request, no use for training in any form, and incident notice within 24 hours (POL-02 A.5; R-019).
- Social Security numbers masked, and only the pages each step needs sent.
- The add-on is never enabled in the AC-01 workspace (CJI) or any other workspace without a new assessment.

**Human-in-the-loop design (required before suggestions return):**
- **Review first.** The caseworker checks the extracted fields against the documents and records a finding before the suggestion is shown.
- **No AI text in notices.** Denial and pending notices use reason codes the caseworker chooses; the add-on's reason is never copied into a notice.
- **Adverse suggestions get extra review.** A suggested "likely ineligible" or "needs information" requires the caseworker to open the source page. The program manager reviews every AI-assisted denial for the first 60 days, then 20% each week.
- **Override is easy and expected.** One click with a reason code, never counted against the caseworker.
- **Deterministic income check.** The income limit comparison moves to a platform rule using the county's configured limit; the model only extracts and summarizes.
- **Citation check.** Any cited program rule not found in the current manual is blocked.

**Notice to applicants.** AC-02, as deployer, decides the wording; the company adds it to the application portal and the intake checklist. Proposed text: "We may use an automated tool to help staff read your documents. A caseworker reviews your application and makes every decision." Due 2026-11-30.

**Monitoring:**
- Monthly: 30-case QC sample; acceptance and override rates; adverse-error rate.
- Quarterly: the bias plan in section 4.1.
- Ongoing: appeals and complaints on AI-assisted cases are tagged and reviewed with AC-02.
- Results go to the monthly security meeting and the risk register (R-015, R-016).

**Incident handling (P08 and POL-03):**
- Applicant data exposed through the add-on or a prompt-injection attack is a security incident: AC-02 is told within 4 hours (POL-03 4.4), and the 10-day notice under Fla. Stat. 501.171(6)(a) applies if a breach is determined.
- A pattern of wrong suggestions (for example, after a vendor model change) is an AI incident: switch the add-on off, tell AC-02 within 1 business day, and give AC-02 the list of affected cases so it can review and reopen them.

**Decommissioning.** Turn the add-on off for good if: the vendor's written terms are not received by 2026-10-31; agreement with QC stays below 95% or the adverse-error threshold is missed for 2 months in a row after restart; a bias flag stays unresolved for 90 days; AC-02 withdraws approval; or the vendor changes its data-use terms. On shutdown, ask the vendor to confirm deletion of any data it holds, and keep case-record entries under the county's retention rules (Fla. Stat. 119.0701(2)(b)4.).

## 6. Decision
**Approve with conditions.** Owner, 2026-08-31, with AC-02's written agreement of 2026-08-28.
1. **From 2026-09-01 the add-on is switched off** in the AC-02 workspace. Caseworkers return to the full manual process. No applicant data goes to the add-on until conditions 2 and 3 are met.
2. **By 2026-10-31:** the vendor's written terms for the add-on and its subprocessor (section 5) are received and reviewed, and the add-on's security evidence is reviewed under POL-02 A.5 (R-019; POAM-014). If not met, the add-on stays off for good.
3. **By 2026-11-30:** Social Security number masking, the review-first design, the deterministic income check, citation checking, version and prompt logging, prompt-injection filtering, and the applicant notice are in place. Extraction only (no suggestions) may then restart for the same 6 caseworkers.
4. **Suggestions return only after** the 300-case bias test (section 4.1) shows no unresolved flag and agreement with QC of 95% or better, with a new owner approval and AC-02's written agreement (target 2026-12-31; R-015, R-016).

**Expansion** to the other 3 caseworkers or to any other workspace requires 2 consecutive months meeting every threshold in section 4 and a new assessment.

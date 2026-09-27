# AI Risk Assessment: Generative AI Assistant Used with CUI Engineering Documents

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts manufacturer, DoD subcontractor) |
| Tier / Vertical | Small / Defense Industrial Base |
| AI use cases | AI-001: the enclave collaboration suite's integrated generative AI assistant (proposed, not enabled). AI-002: public generative AI chatbots (observed in use; prohibited) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | Director of Engineering with the IT Manager and the Contracts Manager, 2026-08-26 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner:** Director of Engineering (CUI data owner). **Decision authority:** Vice President of Operations for Medium-tier use cases; the President if a use case is re-tiered High.
- **Policies that apply:**
  - POL-05 4.8: approved tools only; never CUI in public AI; AI output is never the source for a dimension, tolerance, or NC program
  - POL-04 4.3: CUI may be stored only in the enclave
  - POL-02 4.10: no external systems with CUI; public AI blocked from the enclave
  - POL-01 4.3 and 4.10: enclave boundary changes need an SSP update; cloud services holding CUI must meet FedRAMP Moderate or equivalent
- **Approved-tools list:** kept by the IT Manager and the Director of Engineering. Today it lists **no** generative AI tool for CUI. AI-001 is added only when the conditions in section 6 are met.
- **Scale for a Small company:** no AI committee. The Director of Engineering, IT Manager, and Contracts Manager review AI use cases quarterly and before any new AI feature is turned on in an enclave service.
- **Trigger for this assessment.** On 2026-07-16, interviews found that 3 engineers had pasted CUI specification text into public chatbots to summarize or reword it (AI-002). Engineers asked for an approved tool instead, and the enclave suite offers an integrated assistant (AI-001).

## 2. MAP
### AI-001: enclave suite assistant (proposed)
| Item | Description |
|---|---|
| Purpose and intended use | Search and summarize specifications and engineering change requests; draft first versions of work instructions and quality reports; answer "where is this requirement" questions across a project's documents. The goal is to save engineering time |
| Users / operators | Pilot of 8 enclave users: 4 manufacturing engineers, 2 design engineers, 2 quality engineers. All are U.S. persons with existing enclave access |
| Affected people | No decisions about individuals. Indirectly: machine operators and inspectors who use documents drafted with AI help, and ultimately the users of the aircraft parts |
| Data (inputs, training, outputs) | Inputs: user prompts plus files the user can already open in SYS-02 (CUI, ITAR and EAR technical data). Outputs: text summaries and drafts (CUI). Training: the provider's terms must state that customer data is not used to train models (to be confirmed in writing) |
| Build or buy | Buy (configure): an add-on offered by the government-community cloud provider inside the collaboration suite (SYS-02) |
| Not intended | Creating or changing dimensions, tolerances, NC programs, inspection criteria, or export classifications; decisions about employees (hiring, performance, discipline). Enabling any of these requires re-assessment |

### AI-002: public chatbots (observed)
Engineers pasted specification text into free public chatbots from enclave desktops, because the engineering VLAN allows any outbound traffic (P04 finding 3). The company does not control where that text is stored, who can see it, or whether it is used for training.

**Applicable laws and rules:**
| Rule | AI-001 | AI-002 | Why |
|---|---|---|---|
| DFARS 252.204-7012(b)(2)(ii)(D) | **Yes, condition** | **Violated** | A cloud service that stores, processes, or transmits covered defense information must meet FedRAMP Moderate-equivalent requirements and the clause's incident paragraphs. AI-001 is acceptable only if the assistant is inside the provider's authorized boundary and CRM. Public chatbots are not |
| DFARS 252.204-7012(c): cyber incident | n/a | **Assess** | A compromise includes disclosure to unauthorized persons or copying to unauthorized media (252.204-7012(a)). The 2026-07 pastes were referred to the Contracts Manager and counsel on 2026-07-17 to decide, with Prime A and Prime B, whether they are a reportable cyber incident. If they are, the 72-hour window has passed, partly because the company has no medium assurance certificate (POAM-002). The decision and reasoning go in the incident log |
| CMMC scoping, 32 CFR 170.19(c) | **Yes** | n/a | Once enabled, the assistant is a CUI Asset. It must be in the SSP, the asset inventory, and the P04 diagram before use |
| ITAR, 22 CFR 120.56 and 120.54(a)(5) | **Yes, condition** | **Assess** | Giving a foreign person access to technical data is a release. The encrypted-data carve-out needs end-to-end encryption with FIPS 140-2 (or successor) modules and no storage in a 126.1 country. A public chatbot reads the text unencrypted, so the carve-out cannot apply. The Empowered Official decides whether a voluntary disclosure (22 CFR 127.12) is warranted |
| EAR, 15 CFR 734.18(a)(5) and 764.5 | **Yes, condition** | **Assess** | Same logic for EAR-controlled technology on commercial parts (Customer C) |
| FTC Act Section 5 | Indirectly | Indirectly | Governs the provider's claims about data use and accuracy. Keep the provider's written statements in the procurement file |
| State AI laws (for example Colorado SB26-189, Texas TRAIGA) | No | No | No consequential decisions about individuals; the company operates only in Florida. State AI law analysis is otherwise out of scope by decision (`../00_company-facts.md`) |

## 3. Risk tier
**AI-001 tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why not High:** the assistant makes no decisions about people. It could affect physical safety only if its output became a dimension, tolerance, NC program, or inspection criterion, and those uses are prohibited and blocked by process: every engineering release still requires checker sign-off against the source drawing.

**Why not Low:** it processes CUI and export-controlled data, and its drafts influence documents used on the shop floor for flight parts.

**Escalation triggers (re-tier to High and re-assess):**
- any use to create or change dimensions, tolerances, NC programs, inspection plans, or export classifications
- connecting the assistant to PLM or MES, or letting it act (send, file, release) rather than draft
- enabling it for users outside the pilot group or for any foreign person under an export license
- any provider change to data use, data location, or support personnel terms

**AI-002 tier: High.** CUI and export-controlled data leave company control. It is prohibited, not managed.

## 4. MEASURE
AI-001 is not enabled, so the tests below are **pre-deployment tests** run in a provider-supplied trial space loaded with 40 released, non-ITAR documents, plus readiness checks on the live enclave. Results are from 2026-08-17 to 2026-08-21.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 50-question test set written by engineers with known answers (requirement lookups, summaries of specifications and change requests). Threshold: at least 90% correct and complete; **zero wrong numeric values** (dimensions, tolerances, material specs, temperatures) | 44 of 50 correct (88%); 2 answers stated a wrong numeric value (a tolerance and a heat treat temperature) | **No.** Numeric errors confirm the prohibition on using outputs for numbers |
| Safe | Outputs carry an "AI draft, verify against source" label; engineering release requires checker sign-off; numbers must be copied from the source document, not the AI output | Label is available in the suite settings; checker sign-off already required by the quality system | Yes, with the numeric rule in POL-05 |
| Secure and resilient | Provider confirms in writing that the assistant is inside the FedRAMP Moderate-or-higher authorization boundary and the CRM; prompts and outputs stay in the government-community environment; access through SYS-01 with MFA; prompt and response logs retained 1 year | Provider documentation reviewed; written boundary and CRM confirmation **not yet received**. Logging available | **No** (pending confirmation) |
| Accountable and transparent | Named owner; pilot user list; outputs labeled; prompts and responses logged and sampled monthly | Owner and pilot list defined; logging configuration drafted | Partial |
| Explainable and interpretable | Every answer cites the source files and passages it used, so the engineer can check them | Citations present in 50 of 50 test answers; 3 citations pointed to the wrong revision of a document | Partial. Revision control must come from PLM, not the assistant |
| Privacy-enhanced (here: CUI and export control) | The assistant can only retrieve files the user can already open; permissions must follow need-to-know. Readiness check: permission audit of SYS-02 project sites | 11 of 38 project sites are open to all enclave users, so the assistant would surface their CUI to anyone who asks (P01 R-029) | **No.** Permission clean-up required |
| Fair, with harmful bias managed | Bias plan below. Compare accuracy across document types and user groups; flag any group more than 10 percentage points below the overall rate | Scanned legacy drawings (pre-2010): 60% correct on 10 questions vs 88% overall | **No.** Disparity flagged |

**Bias and fairness testing plan.** The assistant does not decide anything about people, so the fairness risk here is uneven quality: some documents or users get worse answers, and those users may be less able to catch the error.
- **Groups compared:** (a) document type: native digital specifications, customer PDF drawings, and scanned legacy drawings; (b) units: inch versus metric documents; (c) user group: design engineers, manufacturing engineers, and quality engineers (who check the output against different sources).
- **Metric:** percentage of test questions answered correctly and completely, and count of wrong numeric values, per group.
- **Threshold:** any group more than 10 percentage points below the overall rate, or any wrong numeric value in any group, is flagged.
- **Cadence:** before enabling, then quarterly on a refreshed 50-question set, and after any provider model update.
- **Out of scope by design:** no use for decisions about employees, so demographic comparisons are not relevant. If that ever changes, re-assess as High.

**Finding.** Accuracy on scanned legacy drawings is poor. Pilot users must not rely on the assistant for scanned documents, and the pilot excludes project sites that hold mainly scanned drawings until the provider shows better results.

## 5. MANAGE
**Human-in-the-loop design:**
- The assistant drafts and searches only. It never sends, files, releases, or changes anything in PLM or MES.
- A qualified engineer reviews every output before use and copies any number directly from the source document.
- Documents drafted with AI help keep the normal checker sign-off before release. The checker is told the draft was AI-assisted.
- Any user can stop using the assistant at any time; the IT Manager can disable it for everyone in one setting.

**Monitoring:**
- Monthly sample of 20 logged prompts and responses by the Director of Engineering: accuracy, CUI handling, and any prohibited use. Results go in the risk register (R-029, R-030).
- Quarterly bias test (section 4) and after each provider model update.
- Quarterly permission review of SYS-02 project sites.
- Web category blocks for public AI stay in place (POAM-006), with monthly block reports.

**Incident handling:**
- A wrong numeric value that reaches a released document is handled as a quality nonconformance and reviewed by the Quality Manager.
- CUI shown to a user without need-to-know, or CUI leaving the enclave through any AI tool, is handled under P08 and POL-03, including the DIBNet decision and the export control assessment.

**Decommissioning criteria:**
- Stop and remove if the provider cannot confirm in writing that the assistant is inside the FedRAMP authorization boundary and CRM.
- Stop if the provider changes data use, data location, or support personnel terms.
- Stop if a wrong numeric value reaches a released document twice in one quarter.
- Stop if monthly sampling finds prohibited use and retraining does not correct it.

## 6. Decision
**AI-001: approve with conditions.** Vice President of Operations, 2026-08-31. The assistant stays **off** until all of these are met, target 2026-12-31:
1. Written confirmation from the provider that the assistant is inside the FedRAMP Moderate-or-higher authorization boundary and the CRM, that prompts and outputs stay in the government-community environment, and that customer data is not used for training (DFARS 252.204-7012(b)(2)(ii)(D)).
2. SSP, asset inventory, and P04 diagram updated to show the assistant as a CUI Asset (32 CFR 170.19(c)).
3. Permission clean-up: no SYS-02 project site open to all enclave users.
4. Public AI blocks live on the enclave (POAM-006, 2026-10-31).
5. Pilot users trained on the rules in POL-05 4.8; prompt and response logging with 1-year retention.
6. Re-test passes the thresholds in section 4, except scanned legacy drawings, which stay excluded.

Expansion beyond the 8 pilot users requires one quarter with no wrong numeric values reaching a released document and no unresolved bias flag.

**AI-002: rejected.** Public chatbots may never be used with CUI or export-controlled data (POL-05 4.8). The Contracts Manager and counsel will document the reporting and voluntary disclosure decisions for the 2026-07 pastes. The three engineers completed a CUI handling briefing on 2026-07-24.

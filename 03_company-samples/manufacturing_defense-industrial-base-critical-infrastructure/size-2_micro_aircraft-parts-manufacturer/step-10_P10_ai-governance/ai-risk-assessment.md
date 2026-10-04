# AI Risk Assessment: Generative AI Assistant Used with CUI Engineering Documents

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts machine shop, DoD subcontractor) |
| Tier / Vertical | Micro / Defense Industrial Base |
| AI use case assessed | AI-001: the CUI suite's integrated generative AI assistant (proposed, not enabled) |
| Also in the inventory | AI-002: public generative AI chatbots (observed once; prohibited). AI-003: the CAM software's cloud AI toolpath feature (disabled) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | Office Manager (Security and Compliance Coordinator) with the CNC Programmer, 2026-08-26 |
| Decision | President, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the CNC Programmer, who asked for the tool. **Decision authority:** the President, who is also the CMMC Affirming Official and the ITAR Empowered Official.
- **Policies that apply:**
  - POL-04 4.6: CUI and FCI only in approved AI tools; no AI tool is approved for CUI on 2026-09-01; AI output is never the source for a dimension, tolerance, NC program, or inspection criterion.
  - POL-04 4.3 and POL-02 A.4: CUI only on SSP-listed systems; any cloud service holding CUI must meet FedRAMP Moderate-equivalent requirements.
  - POL-02 C.2: no CUI in public AI chatbots.
  - POL-02 A.6: SSP updated within 30 days of a boundary change.
- **Approved-tools list:** kept by the CNC Programmer and the President in POL-04 4.6. It lists no AI tool for CUI.
- **Scale for a Micro shop:** no AI committee. The President, CNC Programmer, and Office Manager review AI use at the monthly security meeting and before any AI feature is turned on in any company software.

**How this started.** On 2026-07-14, during gap analysis interviews, the CNC Programmer said that in June 2026 he had pasted paragraphs of a Prime A material specification into a free public chatbot to get a plain-language summary (AI-002). The specification carries a CUI marking and a distribution statement. He asked for an approved tool instead, and the CUI suite offers an integrated assistant (AI-001). The same review found that the CAM software has a cloud AI toolpath feature that uploads part models to the CAM vendor's commercial cloud (AI-003); it was switched off on 2026-08-12.

## 2. MAP
### AI-001: CUI suite assistant (proposed)
| Item | Description |
|---|---|
| Purpose and intended use | Search and summarize customer specifications and drawing notes; draft setup sheet text, inspection plan outlines, and first article report narratives. The goal is to save the only programmer's time (P01 R-019) |
| Users | Pilot of 2: the CNC Programmer and the Quality Inspector. Both are U.S. persons with existing SYS-01 access |
| Affected people | No decisions about individuals. Indirectly: machinists and the inspector who use documents drafted with AI help, and ultimately the users of the aircraft parts |
| Data | Inputs: prompts plus files the user can already open in SYS-01 (CUI, including ITAR and EAR technical data). Outputs: text summaries and drafts (CUI). Training: the provider must confirm in writing that customer data is not used to train models |
| Build or buy | Configure: an add-on from the CUI suite provider |
| Not intended | Creating or changing dimensions, tolerances, NC programs, toolpaths, CMM programs, inspection criteria, or export classifications; anything about employees. Enabling any of these requires a new assessment |

### AI-002: public chatbots (observed once)
The paste went from the CAM workstation, which can reach any website because outbound traffic is open (P03 G-093). The company does not control where that text is stored, who can see it, or whether it is used for training.

### AI-003: CAM cloud AI toolpath feature (disabled)
Uploading a CUI part model to the CAM vendor's commercial cloud would put CUI in a service that is not FedRAMP authorized, and for ITAR parts would risk a release. It is off and stays off for CUI jobs.

**Applicable laws and rules:**
| Rule | AI-001 | AI-002 | Why |
|---|---|---|---|
| DFARS 252.204-7012(b)(2)(ii)(D) | **Yes, condition** | **Violated** | A cloud service that stores, processes, or transmits covered defense information must meet FedRAMP Moderate-equivalent requirements and the clause's incident paragraphs. AI-001 is acceptable only if the assistant is inside the provider's authorized boundary and covered by its CRM. Public chatbots are not |
| DFARS 252.204-7012(a), (c): cyber incident | n/a | **Assessed** | A compromise includes disclosure of information to unauthorized persons or copying to unauthorized media (252.204-7012(a)). See the decision in section 6 |
| CMMC scoping, 32 CFR 170.19(c) | **Yes** | n/a | Once enabled, the assistant is part of a CUI Asset. It must be in the SSP, the inventory, and the P04 diagram before use |
| ITAR, 22 CFR 120.56 and 120.54(a)(5) | **Yes, condition** | Checked | Giving a foreign person access to technical data is a release. The encrypted-data carve-out needs end-to-end encryption with FIPS 140-2 (or successor) modules. A public chatbot reads the text unencrypted, so the carve-out cannot apply. The June paste was not ITAR-marked (section 6) |
| EAR, 15 CFR 734.18(a)(5) and 764.5 | **Yes, condition** | Checked | Same logic for EAR-controlled technology on commercial parts (Customer C) |
| FTC Act Section 5 | Indirectly | Indirectly | Governs the provider's claims about data use and accuracy. Keep the provider's written statements in the purchase file |
| State AI laws | No | No | No decisions about individuals; the company operates only in Florida |

## 3. Risk tier
**AI-001 tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why not High:** the assistant makes no decisions about people. It could affect physical safety only if its output became a dimension, tolerance, program, or inspection criterion, and those uses are prohibited and caught by process: first article inspection against the customer drawing is unchanged.
- **Why not Low:** it processes CUI and export-controlled data, and its drafts end up in setup sheets used on the shop floor for flight parts.

**Re-tier to High and reassess if:** it is used for any number, program, or inspection criterion; it is connected to the CAM software, the DNC software, or the ERP; it can send or file anything rather than draft; it is enabled for anyone outside the 2 pilot users; or the provider changes data use, data location, or support personnel terms.

**AI-002 tier: High.** CUI leaves company control. Prohibited, not managed.
**AI-003 tier: High** for CUI jobs. Disabled.

## 4. MEASURE
AI-001 is not enabled, so these are **pre-deployment tests** in a provider trial space loaded with 15 released Customer C documents that are neither CUI nor export controlled, plus readiness checks on the live CUI suite. Results are from 2026-08-17 to 2026-08-19.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 25-question test set written by the CNC Programmer and Quality Inspector with known answers (requirement lookups, note summaries). Threshold: at least 90% correct and complete; **zero wrong numeric values** | 22 of 25 correct (88%); 1 answer gave a wrong thread callout | **No.** Confirms the rule that numbers come only from the source |
| Safe | Outputs labeled "AI draft, verify against source"; numbers copied from the source; first article inspection unchanged | Label available in the suite settings; first article inspection already required | Yes, with the POL-04 4.6 rule |
| Secure and resilient | Provider confirms in writing that the assistant is inside the FedRAMP Moderate-or-higher authorization boundary and the CRM; prompts and outputs stay in the government-community environment; access through SYS-01 with MFA; prompt and response logs kept 1 year | Provider documentation reviewed; written confirmation **not yet received**; the CRM itself is not yet on file (POAM-009) | **No** (pending) |
| Accountable and transparent | Named owner; 2-user pilot list; outputs labeled; prompts and responses logged and sampled monthly | Owner and pilot list defined; logging configuration drafted | Partial |
| Explainable and interpretable | Every answer cites the source file and passage | Citations in 25 of 25 answers; 2 pointed to an older revision of a document | Partial. Revisions must be checked in the job folder |
| Privacy-enhanced (here: CUI and export control) | Assistant retrieves only files the user can already open; permissions follow need-to-know | ITAR job folders are open to all 4 suite users today (P03 G-002), so the assistant would surface ITAR data to anyone who asks | **No.** Permission clean-up first |
| Fair, with harmful bias managed | Accuracy compared across document types; flag any type more than 10 percentage points below the overall rate | Scanned older drawings: 3 of 6 correct (50%) vs 88% overall | **No.** Disparity flagged |

**Bias and fairness plan.** The assistant decides nothing about people, so the fairness risk is uneven quality: some documents get worse answers, and the people relying on them may not catch it.
- **Groups compared:** native digital specifications, customer PDF drawings, scanned older drawings; inch versus metric documents.
- **Metric:** percent correct and complete, and count of wrong numeric values, per group.
- **Threshold:** any group more than 10 percentage points below the overall rate, or any wrong numeric value, is flagged.
- **Cadence:** before enabling, then quarterly on a refreshed 25-question set, and after any provider model update.

**Finding.** Scanned older drawings are a weak spot. The pilot excludes them until the provider shows better results.

## 5. MANAGE
**Human in the loop:**
- The assistant drafts and searches only. It never sends, files, or changes anything, and is not connected to the CAM, DNC, CMM, or ERP software.
- The user checks every output against the source before use and copies any number directly from the source document.
- Setup sheets drafted with AI help are reviewed by the Lead Machinist at setup and verified by first article inspection, as today.
- The Office Manager can switch the assistant off for everyone in one setting.

**Data protection:**
- Enabled only inside the government-community offering, with written provider confirmation of the FedRAMP boundary, data location, no training on customer data, and U.S.-person support staff.
- ITAR job folders limited to the people who need them before enabling (POL-02 B.2).
- Public AI and the CAM vendor's AI feature blocked or disabled on enclave computers (POAM-004 outbound rules).

**Monitoring:**
- Monthly sample of 10 logged prompts and responses by the Office Manager and the President: accuracy, CUI handling, any prohibited use. Results logged against P01 R-016.
- Quarterly bias test (section 4) and after any provider model update.

**Incident handling:** a wrong number that reaches a released setup sheet is handled as a quality nonconformance. CUI shown to a user without need-to-know, or CUI leaving the enclave through any AI tool, is handled under POL-03 and the P08 runbook, including the DIBNet and export control decisions.

**Decommissioning:** switch off and remove if the provider cannot confirm the FedRAMP boundary in writing, changes its data terms, or if a wrong number reaches a released document twice in one quarter.

## 6. Decision
**AI-001: approve with conditions, not before 2027-04-01.** President, 2026-08-31. The assistant stays **off** until all of these are met:
1. Written provider confirmation that the assistant is inside the FedRAMP Moderate-or-higher authorization boundary and the CRM, that data stays in the government-community environment, and that customer data is not used for training (DFARS 252.204-7012(b)(2)(ii)(D)).
2. SSP, inventory, and P04 diagram updated to show the assistant (32 CFR 170.19(c)).
3. ITAR job folders restricted (P03 G-002).
4. Public AI blocked on enclave computers (2026-10-31).
5. Both pilot users trained on POL-04 4.6; prompt and response logging with 1-year retention.
6. Re-test passes the section 4 thresholds, except scanned older drawings, which stay excluded.

**Why not sooner.** Turning on a new CUI feature changes the assessment boundary. The President decided not to change the boundary while the shop prepares for the Level 2 self-assessment (target 2027-03-15).

**AI-002: rejected.** Public chatbots may never be used with CUI or FCI (POL-04 4.6). For the June 2026 paste, the President, as Empowered Official, and counsel reviewed it on 2026-07-28: the specification was CUI but carried no ITAR or EAR export control marking, so no DDTC or BIS disclosure is planned. Because a disclosure to an unauthorized party fits the cyber incident definition in 252.204-7012(a), the President chose the conservative path: tell Prime A in writing (sent 2026-08-31) and file a DIBNet report as soon as a medium assurance certificate is issued (POAM-008, 2026-10-31), noting that the 72-hour window was missed because the paste was found weeks later and the company had no certificate. The CNC Programmer completed a one-to-one CUI handling briefing on 2026-07-15.

**AI-003: rejected for CUI jobs.** The feature stays disabled; it may be considered later for commercial jobs that are neither CUI nor export controlled, after its own assessment.

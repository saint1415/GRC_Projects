# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed aircraft parts manufacturer, DoD subcontractor) |
| Tier / Vertical | Mid-Market / Defense Industrial Base |
| Scope | Portfolio of 6 AI use cases (AI-001 to AI-006), inventory in `ai-use-case-inventory.csv`. The registry use case for this sample is AI-001, a generative AI assistant used with CUI engineering documents |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-001, AI-004, and AI-006 |
| Assessors / date | Director of Engineering (engineering), Director of Quality (product), vCISO and Security Manager (security), Director of Trade Compliance and Contracts (export and contracts), General Counsel and HR Director (employment), 2026-08-17 to 2026-09-10 |
| Decision | Chief Operating Officer, 2026-09-17; High-tier decisions noted by the CEO |

## 1. Summary
Five of the six use cases were adopted or switched on without a security or legal review (gap 11 in `../00_company-facts.md`). AI-006 is the prohibited one. None is out of control, but each needs conditions:
- **AI-001, the enclave assistant:** an engineering pilot ran on real CUI for four months before anyone confirmed the assistant sits inside the provider's FedRAMP-authorized boundary. It is switched off until that is confirmed in writing.
- **AI-002, machine-vision inspection:** it touches flight safety. The vendor changed the model twice without notice, and only 2% of passes are re-inspected.
- **AI-003, predictive maintenance:** a gateway inside the enclave sends program names (part numbers) to a commercial cloud. That is a CUI boundary problem, not an AI problem.
- **AI-004, corporate assistant:** two engineers' prompts contained part numbers and drawing notes.
- **AI-005, applicant ranking:** an employment decision tool turned on by vendor default, with no bias testing.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Enclave generative AI assistant with CUI | Medium | Approve with conditions; off until met (target 2026-12-31) |
| AI-002 | Machine-vision fastener inspection | High | Approve with conditions |
| AI-003 | CNC predictive maintenance | Medium | Conditional: uplink off by 2026-10-31; move to an OT DMZ without program names by 2026-11-30, or decommission |
| AI-004 | Corporate generative AI assistant (no CUI) | Medium | Approve with conditions; blocked for enclave account holders |
| AI-005 | Applicant ranking | High | Avoid: disabled 2026-09-17; re-enable only after bias testing |
| AI-006 | Public chatbots | High | Prohibited |

Tiers: 3 High, 3 Medium, 0 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Director of Engineering, supported by the vCISO. Each use case has a business owner (inventory).
- **Policies and standards:**
  - POL-01 4.13: AI tools approved through this process before use; no CUI in AI outside the enclave.
  - POL-01 4.3: any new data flow or AI feature in the enclave needs Security Manager approval and an SSP update first.
  - POL-04 4.3: CUI only in approved enclave locations.
  - POL-05 4.3: approved tools only; never CUI in public or corporate AI; AI output is never the source for a number.
  - STD-05 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Security Manager on the intranet, with each tool's allowed uses and conditions. Today it lists AI-002 and AI-004 with conditions. AI-001 is added when its conditions are met.

### 2.1 Lightweight governance process
A mid-market company does not need a standing AI committee with a large charter. It needs a reliable gate and a monthly rhythm, using existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature turned on in an existing product, submits a one-page intake: purpose, users, data, vendor, decisions affected, where the data goes | Requesting business owner | 15 minutes |
| 2. Triage | Provisional tier with the repository rubric; **CUI check** (does any CUI, part number, or customer file reach the tool?); purchasing gate (no purchase order or feature switch without approval) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, export, and contract review; written boundary confirmation for anything touching the enclave. **High:** full MAP and MEASURE assessment like this one, with a bias or performance plan | Security Manager; Director of Trade Compliance and Contracts; owner's reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (Director of Engineering, vCISO, Director of Trade Compliance and Contracts, General Counsel), monthly. High: the AI review group recommends; the COO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owner reports the agreed metrics monthly; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type, new users, or an incident | AI review group | Annual |

**Vendor default settings are intake events.** AI-005 and AI-001 were switched on through product settings, not purchases. The Security Manager now reviews the release notes of Tier 1 SaaS products monthly for new AI features (STD-05).

## 3. MAP
| Item | AI-001 Enclave assistant | AI-002 Vision inspection | AI-003 Predictive maintenance | AI-004 Corporate assistant | AI-005 Applicant ranking |
|---|---|---|---|---|---|
| Purpose | Search, summarize, and draft from engineering documents | Flag missing, wrong, or unseated fasteners | Predict spindle failures | Drafting and summarizing non-CUI business text | Score and order applicants |
| Users | 20 pilot users (engineering, quality) | Plant 2 inspectors | Maintenance planners | About 400 corporate users | 4 recruiters |
| Affected people | None directly; downstream users of documents and aircraft parts | Users of the aircraft parts | None | None | About 1,900 applicants a year |
| Data | CUI, ITAR and EAR technical data | Assembly images (CUI where geometry is controlled) | Telemetry with program names | Corporate data (CUI prohibited) | Resumes, application answers |
| Where it runs | Inside SYS-02 (boundary to be confirmed) | On premises, Plant 2 vision cell | Vendor commercial cloud | Commercial cloud | HR SaaS |
| Generative AI? | Yes | No (classifier) | No (prediction model) | Yes | No (ranking model) |

**Laws and rules considered:**
| Rule | Applies to | Why |
|---|---|---|
| DFARS 252.204-7012(b)(2)(ii)(D) | AI-001, AI-003, AI-004, AI-006 | A cloud service that stores, processes, or transmits covered defense information must meet FedRAMP Moderate-equivalent requirements and the clause's incident paragraphs. AI-001 qualifies only if it is inside the provider's authorized boundary and CRM; AI-003, AI-004, and public chatbots do not |
| DFARS 252.204-7012(c) | AI-004, AI-006 | A compromise includes disclosure to unauthorized persons or copying to unauthorized media (252.204-7012(a)). The 2 AI-004 prompts were referred to the Director of Trade Compliance and Contracts and General Counsel on 2026-07-29; they concluded the text (part numbers and two dimension notes) was CUI, and the decision on reporting, with the reasoning, is recorded in the incident log |
| CMMC scoping, 32 CFR 170.19(c); DFARS 252.204-7021(d)(2) | AI-001, AI-002, AI-003 | Once enabled, AI-001 is a CUI Asset and must be in the SSP, inventory, and diagram. The vision cell PC is a Specialized Asset. AI-003's flow takes CUI outside the assessed scope |
| ITAR 22 CFR 120.56, 120.54(a)(5); EAR 15 CFR 734.18(a)(5) | AI-001, AI-003, AI-006 | Release to a foreign person is an export; the encrypted-data carve-outs need end-to-end FIPS-validated encryption. A vendor or public service that reads the text cannot use the carve-out |
| Prime and customer quality clauses (contractual) | AI-002 | Inspection records prove conformance; an automated inspection method must be validated and controlled like any other inspection equipment |
| Title VII, 42 U.S.C. 2000e-2(k) | AI-005 | A selection practice that causes a disparate impact on the basis of race, color, religion, sex, or national origin is unlawful unless shown to be job related and consistent with business necessity |
| 29 CFR Part 1607 (Uniform Guidelines on Employee Selection Procedures) | AI-005 | Still in the eCFR (checked 2026-09-23). The four-fifths ratio in 1607.4(D) is used here only as an internal screening indicator, not as a legal safe harbor |
| FTC Act Section 5 | AI-001, AI-004 vendors | Governs vendors' claims about data use and accuracy; written statements kept in the procurement file |

**Not applied, with reasons:** state AI employment laws (for example Illinois, New York City, and Colorado SB26-189) were considered and not applied, because the company recruits only for its two Florida plants and AI-005 is now disabled; re-check before re-enabling. Florida-specific AI law was not researched beyond this.

### 3.1 AI-001: the CUI boundary question
The registry use case is the clearest example of why the gate matters. Engineering enabled the assistant in the enclave suite for 20 users on 2026-05-11 because it appeared in the provider's government-community offering. The provider's documentation describes the add-on as available in that environment, but the company had no written confirmation that the assistant, its retrieval index, and its prompt logs fall inside the FedRAMP-authorized boundary and the CRM. Under DFARS 252.204-7012(b)(2)(ii)(D), that confirmation is the condition for using it with covered defense information at all. The assistant was switched off on 2026-09-17 pending the provider's letter; the 4 months of pilot use were reviewed by the Director of Trade Compliance and Contracts and General Counsel, who concluded that, if the provider confirms the boundary, no CUI left the authorized environment.

### 3.2 AI-002: a quality system question
The vision model decides whether an assembly step looks right. A missed fastener on a flight assembly is a product safety issue. The model is treated as inspection equipment: validated before use, controlled for changes, and checked by sampling.

### 3.3 AI-005: an employment question
The HR vendor turned on applicant ranking by default in 2026-04. Recruiters say they review every applicant, but they sort by the score, so the score shapes who is called first.

## 4. MEASURE (by use case)
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (2026-08) | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | 60-question test set with known answers (requirement lookups, summaries) | At least 90% correct; **zero wrong numeric values** | 54 of 60 (90%); 1 wrong torque value | **No** |
| AI-001 | Explainable | Citations point to the correct source and revision | 100% | 60 of 60 cited; 4 cited a superseded revision | Partial: revision control must come from PLM |
| AI-001 | Privacy-enhanced (here: CUI need-to-know) | Assistant retrieves only what the user may open; permission audit of suite project sites | No site open to all enclave users | 14 of 61 project sites open to all enclave users | **No** |
| AI-001 | Secure and resilient | Written boundary and CRM confirmation; prompt and response logs kept 1 year | Both | Confirmation not received; logs kept 30 days | **No** |
| AI-001 | Fair, harmful bias managed (uneven quality) | Accuracy by document type: native specifications, customer PDFs, scanned legacy drawings | No group more than 10 points below overall | Scanned legacy drawings 58% vs 90% overall | **No**: scanned drawings excluded |
| AI-002 | Valid and reliable, safe | Escapes found by re-inspecting passes | 0 escapes | Q2: 1,200 passes re-inspected (2%), 3 escapes (missing collar on 2, wrong fastener on 1); all caught at final inspection | **No** |
| AI-002 | Fair, harmful bias managed (uneven quality) | Flag recall by part finish | No finish more than 5 points below overall | Dark-anodized parts 6 points below overall in the vendor's validation data | **No**: added to the re-inspection focus |
| AI-002 | Accountable and transparent | Model version recorded with each lot; change notice from vendor | Both | Versions not recorded; 2 updates without notice (2026-03, 2026-06) | **No** |
| AI-003 | Privacy-enhanced (data minimization) | Telemetry contains no CUI identifiers | 0% of messages with program names | 100% of sampled messages carried the active program name | **No** |
| AI-003 | Valid and reliable | Predicted failures confirmed by maintenance | Track only (Low impact) | 7 alerts, 5 confirmed | Monitor |
| AI-004 | Secure (CUI exclusion) | Prompt log review for CUI patterns | 0 prompts with CUI | 2 of about 2,400 July prompts (part numbers with dimension notes) | **No** |
| AI-004 | Privacy-enhanced | Enterprise terms prohibit training on company data | Contractual | Confirmed in the enterprise agreement | Yes |
| AI-005 | Fair, harmful bias managed | Ratio of top-tier ranking rates by sex for production technician roles (internal indicator; 29 CFR 1607.4(D) four-fifths ratio) | At least 0.80, with a significance test | 0.71 on 2026 Q2 applicants (women ranked in the top tier at 71% of the rate for men); significance not yet tested; vendor provided no adverse impact data | **No** |
| AI-005 | Explainable | Recruiters can see why an applicant scored as they did | Available | Score only, no factors | **No** |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** drafts and searches only; never sends, files, releases, or changes anything in PLM or MES. Numbers are copied from source documents. Checker sign-off remains on every release.
- **AI-002:** the inspector decides every lot. Flags always get a human look; 10% of passes are re-inspected until 2 quarters with zero escapes, then reviewed.
- **AI-003:** recommendations only; planners decide.
- **AI-004:** users review all output; enclave account holders are blocked.
- **AI-005:** disabled. If re-enabled, recruiters must review every applicant in application order, with the score hidden until after first review.

**Monitoring:** owners report the section 4 metrics monthly to the AI review group. High-tier items (AI-002, AI-005) get a quarterly deep dive. Results feed the risk register (P01 R-026 to R-032).

**Incident handling:**
- CUI reaching any tool outside the enclave, or shown to a user without need-to-know, is handled under P08 and POL-03, including the DIBNet and export decisions.
- An AI-002 escape that reaches a customer is a quality nonconformance with customer notification under the quality clauses, and triggers a model review.
- A wrong numeric value from AI-001 that reaches a released document is a nonconformance reviewed by the Director of Quality.

**Decommissioning criteria:**
- AI-001: removed if the provider cannot confirm the boundary in writing by 2026-12-31, or changes data use, location, or support personnel terms.
- AI-002: returned to 100% manual inspection if escapes continue for 2 consecutive quarters at 10% re-inspection, or if the vendor will not agree to change notice.
- AI-003: decommissioned if the gateway cannot be moved and program names removed by 2026-11-30.
- AI-005: stays disabled unless the bias test passes and General Counsel approves.
- Any tool: stop if the vendor changes data-use terms, or the model changes without notice.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions**; off until met | Provider's written boundary and CRM confirmation, no training on customer data, prompts and outputs kept in the government-community environment (DFARS 252.204-7012(b)(2)(ii)(D)); SSP, inventory, and diagram updated (32 CFR 170.19(c)); no suite project site open to all enclave users; 1-year prompt logging; pilot users trained on POL-05 4.3; re-test passes with scanned drawings excluded. Target 2026-12-31 | COO, 2026-09-17 |
| AI-002 | **Approve with conditions** | Model version lock with vendor change notice (contract amendment by 2026-11-30); validation of each update on a 500-image reference set before use; 10% re-inspection of passes from 2026-10-01; version recorded with each lot; monthly escape review | COO, 2026-09-17; noted by the CEO |
| AI-003 | **Conditional** | Gateway uplink off by 2026-10-31; OT DMZ with program names stripped by 2026-11-30; vendor written data-use and retention terms; or decommission | COO, 2026-09-17 |
| AI-004 | **Approve with conditions** | Blocked for enclave account holders by 2026-10-31; prompt filtering for part-number patterns; banner reminder; annual training attestation | COO, 2026-09-17 |
| AI-005 | **Avoid** (disabled 2026-09-17) | Re-enable only with vendor adverse impact data, a company bias test with significance testing, recruiter review with the score hidden, applicant notice, and General Counsel approval | COO, 2026-09-17; noted by the CEO |
| AI-006 | **Prohibited** | Blocking on company networks; annual training attestation | COO, 2026-09-17 |

The conditions are tracked as POAM-023 in P07 and in the risk register (P01 R-026 to R-032). The AI review group holds its first monthly meeting on 2026-10-06.

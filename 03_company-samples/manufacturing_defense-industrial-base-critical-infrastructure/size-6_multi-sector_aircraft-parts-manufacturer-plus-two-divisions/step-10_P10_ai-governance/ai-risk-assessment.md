# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Aircraft Parts, Engineering Services, Defense Software and Data Services, corporate) |
| Tier / Vertical | Multi-Sector / Defense Industrial Base |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the rules that apply to the priority use cases: the generative AI assistant used with CUI engineering documents (AI-001, the registry default), public chatbots (AI-002), the predictive maintenance model (AI-003), AI visual inspection (AI-004), and resume screening (AI-007) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27; presented to the board audit and risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 4 High, 4 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board audit and risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group General Counsel, Group export compliance director, Group CMMC program director, Group HR director, the three division VPs of engineering, the Defense Software chief data scientist. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage, boundary checks for CUI) |
| Group export compliance director | Export classification of prompts, outputs, generated designs, and source code; foreign-person access |
| Group CMMC program director | Confirms that any AI service touching CUI is inside an approved boundary and appears in the SSP |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-06, under POL-01 4.14)
1. **Register before use.** Every AI use case that touches CUI, export-controlled data, Government data, or employee data, or that supports decisions about people, aircraft maintenance, or product conformance, is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, bias and accuracy testing, and quarterly monitoring reports.
3. **Boundary first.** An AI service may process CUI only if it sits inside a cloud boundary that meets the FedRAMP requirements in DFARS 252.204-7012 and is listed in the CUI location register and the SSP (POL-01 4.9; POL-04 4.3, 4.10).
4. **Export control.** Prompts, retrieved files, outputs, generated designs, and source code keep the export tag of their source. Only U.S. persons, or people covered by an export authorization, may use AI tools on export-controlled data.
5. **Data use.** Government-related data from the DoD edition may not train or tune any model for another purpose without written Contracting Officer approval (DFARS 252.239-7010(c)(2)).
6. **Never the source of a number or a decision.** AI output is never the source for a dimension, tolerance, NC program, inspection result, export classification, maintenance action, or hiring rejection (POL-05 4.8).
7. **Change gate.** A material change (new model, new data source, new provider, new decision role) triggers re-assessment before release.
8. **Approved tools only** for workforce generative AI (POL-05 4.7).

**Where the program fell short in 2026.** The standard came after two problems: public chatbot use with CUI at two Engineering Services centers (AI-002), and the 2026-05 retraining of the predictive maintenance model with DoD edition data (AI-003). Both are under conditions in section 6.

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Generative AI engineering assistant with CUI documents | Aircraft Parts and Engineering Services | Medium | Pilot with conditions (300 users) |
| AI-002 | Public generative AI chatbots | Engineering Services (observed) | High | Prohibited with CUI; blocks due 2026-11-30 |
| AI-003 | Predictive maintenance model | Defense Software | High | In production; retraining and validation due |
| AI-004 | AI visual inspection assist | Aircraft Parts | High | Proposed |
| AI-005 | Generative design and topology optimization | Engineering Services | Medium | In production |
| AI-006 | Coding assistant inside the government-community boundary | Defense Software | Low | Approved |
| AI-007 | Resume screening and ranking | Group HR | High | Proposed; not approved |
| AI-008 | Enterprise generative AI assistant (non-CUI) | Group | Medium | Pilot (2,000 users) |
| AI-009 | Supplier cybersecurity risk scoring | Group | Medium | In production |

### 2.1 AI-001 generative assistant with CUI engineering documents (priority use case)
| Rule | What it requires | What it means for the assistant |
|---|---|---|
| DFARS 252.204-7012(b)(2)(ii)(D) | A cloud service that stores, processes, or transmits CDI must meet security requirements equivalent to the FedRAMP Moderate baseline and the clause's incident paragraphs | Acceptable only if the provider confirms in writing that the assistant is inside its FedRAMP-authorized boundary and CRM, and that prompts and outputs stay in the government-community offering. **Confirmation received 2026-08-14** |
| 32 CFR 170.19(c) | CUI Assets are documented in the inventory, SSP, and network diagram | The assistant is a CUI Asset of the Enterprise CUI Environment: it must be in the GCEE SSP and the P04 diagram before the C3PAO assessment. **Not yet added** |
| ITAR 22 CFR 120.56; 120.54(a)(5); EAR 15 CFR 734.18(a)(5) | Release to a foreign person is an export; the encrypted-data carve-out has strict conditions | The group does not rely on the carve-out; the pilot is limited to U.S.-person users and provider personnel terms are checked |
| POL-05 4.8 | AI output never the source for numbers | Engineers copy dimensions, tolerances, and material values from source documents |
| FTC Act Sec. 5 | Vendor claims about data use and accuracy | Keep the provider's written statements in the procurement file |

### 2.2 AI-003 predictive maintenance model: DoD data-use and customer rules
| Rule or commitment | Implication |
|---|---|
| DFARS 252.239-7010(c)(2) | Government-related data may be used only to manage the operating environment of the DoD edition unless the Contracting Officer approves otherwise in writing. **The 2026-05 retraining used DoD edition telemetry for the industry edition model** (P03 DS-G05, Not met) |
| DFARS 252.204-7012(b)(2)(ii)(D) | For the 14 CUI tenants, the model runs inside SYS-D4, which has not shown FedRAMP Moderate equivalency (POAM-015) |
| Tenant agreements and SOC 2 (CC2.3, CC3.4, CC8.1) | The model's data sources changed without notice or change review (P09) |
| FTC Act Sec. 5 | Accuracy claims about scores must be substantiated |
| Safety | Scores inform maintenance planning for military and commercial aircraft. Maintenance decisions stay with the operators' qualified maintenance personnel; the platform never issues a maintenance action |

### 2.3 AI-004 and AI-005 product conformance and design
| Rule | Use cases | Implication |
|---|---|---|
| Prime and DoD quality clauses; AS9100 quality system (contractual) | AI-004, AI-005 | Product acceptance and design release stay with certified inspectors and checkers; the AI tool cannot be the acceptance record |
| ITAR 22 CFR 120.56 | AI-004, AI-005 | Part images and generated designs are technical data. AI-004 vendor remote support must be by U.S. persons through PAM |
| 32 CFR 170.19(c) | AI-004 | Inspection workstations and cameras that store controlled images are CUI Assets or Specialized Assets and must be documented before use |

### 2.4 AI-007 resume screening: employment rules
| Rule | Implication |
|---|---|
| Title VII disparate impact; Uniform Guidelines 29 CFR 1607.4(D) | A selection rate for any race, sex, or ethnic group below four-fifths of the highest group's rate is generally regarded by federal enforcement agencies as evidence of adverse impact. EEOC's 2023 AI technical assistance was removed in 2025, but disparate-impact liability still exists by statute (`00_universal-framework/cross-sector/us-cross-sector-obligations.md`) |
| State and local AI employment laws, in each state where candidates are located | Examples: Colorado SB26-189 (effective 2027-01-01 for consequential decisions, including employment; its status is unsettled by litigation and federal preemption efforts); Illinois HB 3773 (notice and no discriminatory effect, effective 2026-01-01; verified only partially); NYC Local Law 144 (bias audit within 1 year before use and candidate notice, for NYC roles); California Civil Rights Council ADS regulations (effective 2025-10-01). Group counsel confirms which apply before any use |
| Export control | The tool must not screen on citizenship except where a role lawfully requires U.S.-person status; that check stays with export compliance, outside the model |

## 3. Risk tiers (repository rubric)
- **High:** AI-002 (CUI and export-controlled data leave company control), AI-003 (substantial factor in aircraft maintenance planning; Government data rules), AI-004 (substantial factor in product acceptance of flight parts), AI-007 (substantial factor in employment decisions).
- **Medium:** AI-001, AI-005, AI-008, AI-009. Humans make the final decision, but outputs enter engineering records, designs, or business decisions.
- **Low:** AI-006.

**Re-tier triggers:** any AI-001 use to create or change dimensions, tolerances, NC programs, inspection criteria, or export classifications, or connecting it to PLM release or MES (to High); AI-005 designs released without full analysis (to High); AI-009 used to approve suppliers automatically (to High); any change to a provider's data use, data location, or support personnel terms (re-assessment).

## 4. MEASURE
Results are from pilots, pre-deployment tests, and monitoring between 2026-05 and 2026-08.

### 4.1 AI-001 engineering assistant (pilot of 300 users; AI 600-1 risk areas)
| Characteristic or AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable (confabulation) | 120-question test set with known answers from released specifications and change requests; threshold at least 90% correct and **zero wrong numeric values** | 109 of 120 correct (91%); 3 answers gave a wrong numeric value (two tolerances, one heat treat temperature) | **No.** Numeric errors confirm the rule that numbers come from source documents |
| Explainable | Every answer cites source files and passages | Citations in 120 of 120; 5 cited a superseded revision | Partial. Revision control must come from PLM |
| Secure (prompt injection) | Red-team test with crafted documents planted in a test project | 2 of 15 injection attempts changed the summary content; none exfiltrated data | **No.** Provider mitigation and user warning required |
| Data privacy (here: CUI and export control) | The assistant retrieves only files the user can open; permission audit of 412 project spaces | 37 project spaces open to all users of a division; the assistant would surface their CUI to anyone in that division | **No.** Permission clean-up required |
| Value chain | Provider boundary and CRM confirmation; SSP and diagram entries | Confirmation received; SSP and diagram not yet updated | Partial |
| Fair, harmful bias managed | Accuracy by document type and user group; flag any group more than 10 points below overall | Scanned legacy drawings 64% vs 91% overall; no gap between Aircraft Parts and Engineering Services users | **Flagged.** Exclude scanned drawings |

### 4.2 AI-003 predictive maintenance model
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Precision of high-risk flags against actual removals over 6 months | 0.71 overall | Yes (target 0.65) |
| Fair, harmful bias managed (here: uneven performance) | Precision by aircraft type and by fleet size; flag a drop of more than 0.10 | Fleets with fewer than 20 aircraft 0.52 | **Flagged.** Show low-confidence warnings for small fleets |
| Accountable and transparent | Data lineage documented for each release | 2026-05 release combined DoD edition data without approval | **No** (252.239-7010(c)(2)) |
| Safe | Independent validation and adversarial tests before release | Not done | **No** (POAM-026) |

### 4.3 AI-004 visual inspection (pre-deployment trial at plant 2, 1,800 parts)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Detection rate of known defects; threshold 98% with inspector review | 97.2% overall | **No** |
| Fair, harmful bias managed (here: uneven performance) | Detection by part family and surface finish; flag more than 3 points below overall | Additive parts with as-built surfaces 91% | **Flagged** |
| Safe | Tool cannot pass a part; inspector disposition required | Confirmed in workflow design | Yes |

### 4.4 AI-007 resume screening (pre-deployment test on 2025 historical applications)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Fair, harmful bias managed | Selection rate ratio by sex and by race and ethnicity against the highest group (29 CFR 1607.4(D) four-fifths guideline) | Women 0.76 of the highest group's rate for mechanical engineering roles | **No.** Evidence of adverse impact |
| Accountable and transparent | Explanations for each ranking; candidate notice drafted | Vendor explanations generic; notice not drafted | **No** |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** drafts and searches only; never sends, files, releases, or changes anything in PLM or MES. A qualified engineer reviews every output, and the checker is told when a draft was AI-assisted.
- **AI-003:** scores carry confidence bands and a small-fleet warning; maintainers decide. A stale-score banner appears if scoring stops (P05 BP-DS05).
- **AI-004:** flags only; the inspector dispositions every part, and flagged and unflagged samples are re-inspected weekly during the trial.
- **AI-007:** if ever approved, recruiters must review low-ranked candidates before any rejection; no automatic rejection.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board audit and risk committee; P01 risks GR-10, AP-024, ES-006, DS-009, DS-010, DS-003.

**Incident handling:** CUI exposed through any AI tool follows P08 and POL-03, including the DIBNet decision and the export assessment. A wrong numeric value that reaches a released document is a quality nonconformance. Model data-use breaches go to the Contracting Officer as counsel advises.

**Decommissioning:** each use case has an off switch and a fallback (source documents, manual inspection, maintenance records, manual screening), which the BIA already covers (P05).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 engineering assistant | **Continue the pilot with conditions; no expansion** | Add to the GCEE SSP and P04 diagram by 2026-10-31; close the 37 open project spaces by 2026-11-15; provider prompt-injection mitigation and user warning by 2026-11-30; exclude scanned legacy drawings; expansion only after one quarter with no wrong numeric value reaching a released document |
| AI-002 public chatbots | **Prohibited with CUI** | Blocks on all CUI endpoints by 2026-11-30; documented DIBNet and export disclosure decisions for the 2026-07 cases by 2026-10-31 (POAM-021); training content updated (POAM-025) |
| AI-003 predictive maintenance | **Continue with conditions** | Stop DoD data reuse and retrain by 2026-11-15; data-use gate by 2026-11-30 (POAM-016); independent validation before the next release, due 2027-03-31 (POAM-026); small-fleet warnings |
| AI-004 visual inspection | **Not yet approved** | Reach 98% detection including additive surfaces; document the stations in the plant SSP annex; U.S.-person vendor support |
| AI-005 generative design | **Continue** | Generated designs tagged as export-controlled technical data; full analysis and checker sign-off remain mandatory |
| AI-006 coding assistant | **Approved** | Block public assistants on developer laptops by 2026-12-31 |
| AI-007 resume screening | **Rejected for now** | Adverse impact found; re-submit only with a vendor fix, an independent bias audit, candidate notices, and counsel's state-by-state review |
| AI-008 enterprise assistant | **Continue the pilot** | Non-CUI only; data loss rules block CUI; prohibited for engineering, export, or employment decisions |
| AI-009 supplier scoring | **Approved** | Scores prioritize checks; SPRS and CMMC verification stays a human step |

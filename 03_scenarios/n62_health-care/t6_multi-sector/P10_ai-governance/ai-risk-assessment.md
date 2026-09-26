# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Care Delivery, Health Plan, Health-Tech SaaS, corporate) |
| Tier / Vertical | Multi-Sector / Health Care and Social Assistance |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the regulator-specific rules for three priority use cases: the Health Plan UM model (AI-005), the SaaS care summary assist feature (AI-007), and Care Delivery's AI scribe and decision support (AI-001, AI-002, AI-003) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-28; presented to the board risk committee 2026-09-10 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 3 High, 5 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Care Delivery chief medical information officer, Health Plan medical director, SaaS product lead. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) |
| Group Chief Privacy Officer | PHI use, BAAs, de-identification, consent |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026, under POL-01 4.12)
1. **Register before use.** Every AI use case that touches PHI, member data, or customer PHI, or that supports decisions about people, is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric** (`00_universal/projects/P10_ai-governance/README.md`). High tier: the council approves, a pre-deployment impact assessment and bias testing are required, and monitoring is reported quarterly.
3. **No BAA, no PHI** (POL-01 4.8; POL-04 4.9). AI vendors and model providers that handle PHI sign BAAs or subcontractor BAAs with no-training and retention terms.
4. **Regulator overlays.** Each division supplement adds its regulator's rules: MA utilization management for the Health Plan, Section 1557 and recording consent for Care Delivery, customer BAAs and SOC 2 commitments for the SaaS.
5. **Change gate.** A material change (new model, new provider, new feature that changes how PHI is processed, new decision role) triggers re-assessment before release.
6. **Approved tools only** for workforce generative AI (POL-05 4.7).

**Where the program fell short in 2026.** The standard was adopted after two of the priority use cases were already live. The UM model was never presented to the UM committee (scenario gap 3), and the SaaS feature launched without the change gate (gap 4). Both are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | AI scribe | Care Delivery | Medium | In production (about 400 providers); expansion paused |
| AI-002 | EHR predictive decision support (sepsis, readmission) | Care Delivery | High | In production; mitigation documentation due |
| AI-003 | Specialty clinical calculators | Care Delivery | Medium | In production; inventory incomplete |
| AI-004 | Imaging AI triage | Care Delivery | High | Proposed |
| AI-005 | UM model for prior authorization | Health Plan | High | In production with conditions |
| AI-006 | Fraud, waste, and abuse claims model | Health Plan | Medium | In production |
| AI-007 | Care summary assist (generative) | Health-Tech SaaS | Medium | In production for 61 customers; new enrollments paused |
| AI-008 | Engineer coding assistant | Health-Tech SaaS | Low | Approved |
| AI-009 | Enterprise generative AI assistant | Group | Medium | Pilot (2,000 users) |

### 2.1 Health Plan UM model (AI-005): Medicare Advantage rules
| Rule | What it requires | What it means for the model |
|---|---|---|
| 42 CFR 422.101(c)(1)(i) | Medical necessity determinations based on (A) coverage and benefit criteria in 422.101(b) and (c), (B) whether the item or service is reasonable and necessary under section 1862(a)(1), (C) the enrollee's medical history, physician recommendations, and clinical notes, and (D) medical director involvement where appropriate | The model may **support** determinations but cannot be the basis for them. Every routed case needs a documented, individualized review of the enrollee's own record. **Gap:** 11 of 60 sampled adverse cases lacked that documentation |
| 42 CFR 422.101(b)(6) | Internal coverage criteria, where used, must be publicly accessible with an evidence summary and rationale | The model must not introduce unpublished criteria. The June 2026 mapping found it uses only published criteria; re-check at every model change |
| 42 CFR 422.137(b), (d) | No UM policy or procedure may be used unless the UM committee (led by the medical director) reviewed and approved it; annual review; approve only policies relying on 422.101(c)(1) criteria; document reasons | The model-assisted workflow and its thresholds are UM procedures. **Gap:** never presented to the committee |
| 42 CFR 422.566(d) | A physician or appropriate professional reviews any expected adverse medical necessity decision before it is issued | Met: the model never denies, and every sampled adverse decision had physician review |
| 45 CFR 92.210 | Identify decision support tools using protected-trait inputs; mitigate discrimination risk | MA payments are federal financial assistance under 45 CFR 92.4. Whether a UM tool "supports clinical decision-making" is under counsel review; the group applies 92.210 as a precaution because the model uses age and disability status |
| HIPAA | Minimum necessary for training data; purpose tags | Training data comes from the Health Plan zone of the GDP, which has the zoning gap (GR-01) |

### 2.2 SaaS care summary assist (AI-007): business associate and customer commitments
| Rule or commitment | Implication |
|---|---|
| 45 CFR 164.308(b)(2); 164.314(a)(2)(i)(B); 164.502(e)(1)(ii) | The model provider is a subcontractor. The subcontractor BAA was signed before launch (met), but assurance must be monitored, not just obtained |
| 45 CFR 164.504(e)(2)(ii)(D) and customer BAAs | Subcontractors must agree to the same restrictions as the SaaS. Customer BAAs may add terms (notice before new subcontractors, no offshore processing, no secondary use) that must be checked for each of the 61 opt-in customers |
| 45 CFR 164.410(c)(1) | If the model provider had a breach, the SaaS must identify each affected patient. **Gap:** requests are logged by tenant, not by patient |
| SOC 2 system description and criteria (CC2.3, CC3.4, CC8.1, CC9.2) | The feature and the model provider (a subservice organization) must be described for the period ending 2026-09-30, and the change must be evaluated. See P09 |
| Processing Integrity (not in scope today) | Customers now ask about summary accuracy. Adding Processing Integrity in 2027 would require accuracy commitments the SaaS can evidence |
| FTC Act Section 5 (N51-R01) | Accuracy and privacy claims in marketing must be substantiated |
| Colorado SB26-189 (effective 2027-01-01) | Covers AI that materially influences consequential health care decisions. Counsel is reviewing whether SaaS developer duties arise for Colorado customers. The law's status is unsettled (litigation and federal preemption efforts; see `00_universal/cross-sector/us-cross-sector-obligations.md`) |

### 2.3 Care Delivery scribe and decision support (AI-001 to AI-004)
| Rule | Use cases | Implication |
|---|---|---|
| 45 CFR 92.210(a)-(c) | AI-002, AI-003, AI-004; AI-001 only if suggestion features are enabled | 45 CFR 92.4 defines a patient care decision support tool as any automated or non-automated tool used to support clinical decision-making. Care Delivery must make reasonable efforts to identify tools that use race, color, national origin, sex, age, or disability as inputs, and to mitigate discrimination risk. The sepsis model uses age and sex |
| State recording consent laws | AI-001 | In all-party consent states (Florida, Fla. Stat. 934.03(2)(d), is the worked example), recording may start only after every party consents. Care Delivery operates in 6 states; the consent matrix applies the strictest rule where patients or providers are in different states |
| HIPAA | All | BAAs with no-training terms; minimum necessary; audit logs |
| ONC HTI-1 decision support intervention transparency (45 CFR 170.315(b)(11)) | AI-002 | Duties fall on the certified EHR developer. Care Delivery should use the source attributes the developer publishes when reviewing AI-002 |
| FDA device requirements | AI-004 | Duties fall on the manufacturer. Care Delivery verifies the product's FDA status and labeled intended use before deployment |

## 3. Risk tiers (repository rubric)
- **High:** AI-002, AI-004 (substantial factor in health care decisions or safety), AI-005 (substantial factor in coverage and health care decisions, even though it never denies: it decides auto-approvals and shapes reviewer attention).
- **Medium:** AI-001, AI-003, AI-006, AI-007, AI-009. Humans make the final decision, but outputs enter records or influence decisions.
- **Low:** AI-008.

**Re-tier triggers:** enabling scribe suggestions (AI-001 to High); letting the UM model recommend denial language or expanding auto-approval to new service categories (AI-005 re-assessment); marketing care summary assist for decision-making (AI-007 to High).

## 4. MEASURE
Results are from monitoring and audits between 2026-05 and 2026-08.

### 4.1 Health Plan UM model (AI-005)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Monthly audit of 50 auto-approvals against coverage criteria | 200 audited; 0 approvals outside criteria | Yes |
| Accountable and transparent | Share of routed adverse cases with documented consideration of medical history, physician recommendations, and clinical notes (target 100%) | 49 of 60 (82%) | **No** (422.101(c)(1)(i)(C)) |
| Safe (automation bias) | Rate at which reviewers agree with a "likely does not meet criteria" recommendation; flag above 90% | 94% | **No.** Review whether reviewers defer to the model |
| Fair, harmful bias managed | Auto-approval rate by age band and disability indicator; flag if a group differs from the overall rate by more than 5 points without a clinical explanation | Disability indicator 31% vs 39% overall | **Flagged.** Clinical mix analysis due 2026-11-30 |
| Governance | UM committee approval of model use and thresholds (422.137(b)) | Not presented | **No** |
| Secure and privacy-enhanced | Training data from the Health Plan zone only; access logs | Zone not yet separated (GR-01) | Partial |

### 4.2 SaaS care summary assist (AI-007), using AI 600-1 risk areas
| AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Confabulation | Pre-launch test of 150 summaries by clinicians: fabricated facts (target under 1%); monthly sampling after launch | 1.3% fabricated; post-launch sampling not started | **No** |
| Information integrity (omissions) | Clinically significant omissions (target under 2%) | 4% | **No** |
| Data privacy | Zero-retention terms; per-patient logging; customer BAA check | Terms signed; no monitoring; tenant-level logs only | **No** |
| Information security (prompt injection) | Red-team test with crafted documents | Not done | **No** |
| Value chain and component integration | Model provider in system description; change gate | Not in description; gate bypassed | **No** |
| Human-AI configuration | Summaries labeled; source links | In place | Yes |

### 4.3 Care Delivery scribe and decision support
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-001 scribe | Critical errors (wrong drug, dose, laterality, allergy) in sampled notes; target 0 reaching a signed note | 2 of 1,200 sampled notes had critical errors, both caught before signing | Yes (target met for signed notes) |
| AI-001 scribe | Minor error rate by language: flag if more than 5 points above baseline | Patients whose first language is not English 8.9% vs 3.6% | **Flagged** |
| AI-001 scribe | Consent documented before recording (target 100%) | 91% | **No** |
| AI-002 sepsis score | Sensitivity by age band and sex (92.210(b)-(c)); flag a drop of more than 0.10 | Overall 0.72; patients 75 and older 0.61 | **Flagged.** Mitigation needed |
| AI-003 calculators | Share of tools inventoried with inputs reviewed | About 70% | **No** (POAM-023) |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-005:** the model auto-approves only when criteria are clearly met. For routed cases, reviewers see the enrollee's clinical record **before** the model's recommendation, and must complete structured rationale fields covering medical history, physician recommendations, and clinical notes. Physicians review all expected adverse decisions. Reviewers can disregard the model at any time without justification.
- **AI-007:** summaries are labeled and linked to sources. Customers can turn the feature off per tenant. Clinicians are told in the product that summaries may omit information.
- **AI-001:** providers review, edit, sign, and attest every note. Recording starts only after the consent field is completed.
- **AI-002:** alerts prompt clinical assessment; they never place orders.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-04, GR-18, HP-001, HP-011, HT-002, HT-003, CD-004, CD-005, CD-018, CD-019.

**Incident handling:** AI failures that cause patient or enrollee harm, disclose PHI, or breach customer commitments follow P08 and POL-03. Model provider incidents follow the SaaS customer notice path.

**Decommissioning:** each use case has an off switch and a fallback (manual UM review, source documents, standard documentation, standard alerts) that the BIA already covers (P05).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-005 UM model | **Continue with conditions** (council, 2026-08-28; board risk committee informed 2026-09-10) | UM committee reviews and approves model use and thresholds by 2026-10-31; record order changed and structured rationale fields live by 2026-11-30; monthly audit of 30 routed cases from 2026-12; disability-indicator analysis by 2026-11-30; no expansion of auto-approval scope until all are met (POAM-021) |
| AI-007 care summary assist | **Continue for the 61 opt-in customers; pause new enrollments** | Privacy impact analysis by 2026-10-15; system description updated for the period ending 2026-09-30; customer notices and BAA amendments by 2026-11-30; per-patient logging, model provider attestation, and red-team test by 2026-12-31; monthly accuracy sampling with targets (POAM-018, POAM-019) |
| AI-001 AI scribe | **Continue; expansion paused** | Consent field mandatory by 2026-11-30; language-disparity mitigation (vendor accuracy data, extra review guidance) before any expansion |
| AI-002 sepsis and readmission | **Continue** | Document 92.210(b)-(c) identification and mitigation for the 75-and-older sensitivity gap by 2026-12-31 |
| AI-003 calculators | **Continue** | Complete the inventory and input review by 2026-12-31 (POAM-023) |
| AI-004 imaging triage | **Not yet approved** | Pre-deployment impact assessment, FDA status check, local validation, and bias testing |
| AI-006, AI-008, AI-009 | **Approved** | Standard monitoring; AI-009 prohibited for clinical or coverage decisions |

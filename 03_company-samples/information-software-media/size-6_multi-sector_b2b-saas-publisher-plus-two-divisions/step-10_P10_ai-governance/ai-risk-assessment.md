# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Cloud Software, Technology Consulting, Payments and Payroll, corporate) |
| Tier / Vertical | Multi-Sector / Information |
| Scope | The group AI governance program: the Group AI Standard, the division use-case inventory, and the rules that apply to each. Priority use cases: the generative **workforce assistant** embedded in Workforce Cloud (AI-001, the registry use case), **attrition-risk insights** (AI-002), and group HR's **resume screening** pilot (AI-009). The payments models (AI-004, AI-005) and the consulting delivery assistant (AI-006) are assessed more briefly |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook; risk tiers from the repository rubric (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`) |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-09-04; presented to the board risk committee 2026-09-17 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 2 High, 6 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, Group HR director, Cloud Software chief product officer, Payments risk director, Technology Consulting delivery executive. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) |
| Group Chief Privacy Officer | Privacy impact assessments, DPA conformance, CCPA ADMT and risk assessment duties |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-06-15, under POL-01 4.12)
1. **Register before use.** Every AI use case that processes customer, worker, client, applicant, or payment data, or that supports decisions about people, is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric.** High tier: the council approves; a privacy impact assessment, a pre-deployment impact assessment, and bias testing are required; notice to affected people; quarterly monitoring reports.
3. **Data-use check.** Customer data is used for training or tuning only where the customer's agreement allows it (POL-04 4.4). Restricted data never goes into a generative model (POL-05 4.7).
4. **Claims check.** Every public statement about an AI feature's accuracy, fairness, or privacy needs evidence on file before publication (POL-01 4.13).
5. **Regulator and contract overlays.** Each division supplement adds its own rules: customer DPAs and SOC 2 commitments (Cloud Software), client opt-in and federal restrictions (Technology Consulting), Part 314 data rules and sponsor bank terms (Payments and Payroll), and employment rules for group HR.
6. **Change gate.** A material change (new model, new provider, new data source, new decision role) triggers re-assessment before release.

**Where the program fell short in 2026.** The standard was adopted after the workforce assistant (launched 2026-03-02) and attrition-risk insights (since 2024) were live, and after group HR started the resume screening pilot (2026-05). None had a privacy impact assessment or bias testing, and the attrition product page called the scores "bias-tested and fair" (P03 G-042). All three are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Workforce assistant (generative) | Cloud Software | Medium | In production for 6,200 opt-in customers; continue with conditions |
| AI-002 | Attrition-risk insights (predictive) | Cloud Software | High | In production for about 9,800 customers; new enablement paused |
| AI-003 | Schedule optimizer | Cloud Software | Medium | In production |
| AI-004 | Merchant risk scoring | Payments and Payroll | Medium | In production |
| AI-005 | Payroll anomaly model | Payments and Payroll | Medium | In production |
| AI-006 | Consulting delivery assistant | Technology Consulting | Medium | Approved for opted-in commercial clients |
| AI-007 | Engineer coding assistant | Cloud Software | Low | Approved |
| AI-008 | Enterprise generative AI assistant | Group | Medium | Pilot (3,000 users) |
| AI-009 | Resume screening | Group HR | High | Pilot paused for new requisitions |

### 2.1 Workforce assistant (AI-001): the registry use case
| Rule or commitment | What it means |
|---|---|
| FTC Act Section 5 (N51-R01), deception | The product page says the assistant "only shows each user what they are allowed to see" (P03 G-043). That claim must be true under adversarial use, not only in normal use |
| FTC Act Section 5, unfairness | Summaries of HR case notes reaching the wrong manager could cause substantial injury workers cannot avoid |
| Customer DPAs | The model provider is a listed sub-processor; notice was given 2026-01-30, 31 days before launch (met, G-036). Prompts go to the provider under zero-retention terms |
| CCPA service-provider terms (N51-R03) | Customer data in prompts is used only to provide the service to that customer; it is not used to tune the model |
| SOC 2 (CC3.4, CC8.1, CC9.2) | The launch is a significant change; the service auditor will look for the change and the model provider in the 2026 period (P09) |
| FTC proposed AI-accuracy policy statement | Proposed only (not final); tracked, not treated as an obligation |

### 2.2 Attrition-risk insights (AI-002) and resume screening (AI-009): employment decisions
| Rule | AI-002 (the group as **developer**) | AI-009 (the group as **deployer** and CCPA business) |
|---|---|---|
| Colorado SB26-189 (effective 2027-01-01; applies to consequential decisions on or after that date) | If the scores "materially influence" customers' employment decisions, the group owes deployers documentation of intended uses, training-data categories, limitations, and human-review instructions, and notice of material updates | Deployer duties for Colorado applicants: point-of-interaction notice, post-adverse-outcome explanation, rights to correct data and to human review, 3-year records |
| CCPA ADMT rules (11 CCR 7200 et seq.; compliance by 2027-01-01) | Customers that are CCPA businesses using the scores for significant decisions carry the ADMT duties; the group, as service provider, must give them what they need to comply | The group is a CCPA business using ADMT for employment decisions about California applicants: pre-use notice, opt-out or an applicable exception, access rights, and a risk assessment |
| Title VII and ADEA (federal anti-discrimination law) | Liability falls on employers using the scores; customers will ask the group for adverse impact evidence | Group HR is the employer; disparate impact by sex, race, ethnicity, or age is a direct exposure |
| UGESP (29 CFR 1607.4(D)) | A selection rate for any race, sex, or ethnic group below four-fifths of the highest group's rate is generally regarded as evidence of adverse impact. Used here as a screening threshold; UGESP does not cover age, so the same ratio is applied to age 40 and over as an internal heuristic only | Same |
| FTC Act Section 5 | "Bias-tested and fair" was unsubstantiated; to be withdrawn by 2026-10-15 (POAM-027) | Applicant-facing statements must be accurate |

The status of Colorado SB26-189 enforcement and federal preemption efforts is unsettled (`00_universal-framework/cross-sector/us-cross-sector-obligations.md`). The group plans to comply as written.

### 2.3 Other use cases
| ID | Key rules | Implication |
|---|---|---|
| AI-003 schedule optimizer | Customer contracts; state predictive scheduling laws fall on customers (generic) | Managers approve every schedule; monitor hours parity |
| AI-004 merchant risk scoring | Sponsor bank B; 16 CFR Part 314 for data; Colorado scope for sole-proprietor merchants under counsel review | Declines are reviewed by analysts; appeal path exists |
| AI-005 payroll anomaly model | State wage payment laws (generic); 16 CFR 314.4(c)(8) | A false hold delays a worker's pay; the 2-hour review target matters more than catch rate |
| AI-006 delivery assistant | Client contracts; FAR 52.204-21(b)(1)(iv); hospital BAAs | Client opt-in; blocked on federal engagements without written approval |

## 3. Risk tiers (repository rubric)
- **High:** AI-002 (a substantial factor customers use in employment decisions), AI-009 (ranks applicants for hiring).
- **Medium:** AI-001, AI-003, AI-004, AI-005, AI-006, AI-008. Humans make the final decision, but outputs reach customers, workers, merchants, or decisions.
- **Low:** AI-007.

**Re-tier triggers:** using workforce assistant summaries to rank or discipline workers (AI-001 to High); auto-applying optimizer schedules without manager approval (AI-003 to High); automatic merchant declines without analyst review (AI-004 to High).

## 4. MEASURE
Results are from tests and monitoring between 2026-07 and 2026-09.

### 4.1 Workforce assistant (AI-001), using AI 600-1 risk areas
| AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Confabulation | 400 sampled answers to policy questions reviewed by HR specialists; materially wrong answers (target under 2%) | 2.8% | **No** |
| Data privacy | Permission test: can a user see content beyond their role? (target: never) | HR case-note text surfaced to a non-HR manager in a P07 test tenant | **No** (fix due 2026-11-15) |
| Data privacy | Filter test with 500 synthetic Social Security and bank numbers in tenant content (target 100% removed before the model call) | 100% | Yes |
| Information security | Red-team test with injected instructions in schedules and case notes | Not done | **No** |
| Value chain and component integration | Model provider in the sub-processor list, SOC 2 description, and annual review | Listed; review completed after launch | Partial |
| Human-AI configuration | Outputs labeled; drafts require a person to apply | In place | Yes |

### 4.2 Attrition-risk insights (AI-002)
Retrospective test on data from 12 customers that volunteered self-reported demographics (about 180,000 workers); the group is flagged as "high risk of leaving."

| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Precision of "high risk" flags against actual departures within 6 months | 0.41 | Acceptable for an advisory signal; must be disclosed |
| Fair, harmful bias managed | Rate of *not* being flagged, lowest group compared with highest (four-fifths screen) by sex, race and ethnicity | 0.88 to 0.97 | Yes |
| Fair, harmful bias managed | Same ratio for workers aged 40 and over (internal heuristic) | 0.76 | **No.** Tenure and absence features act as age proxies |
| Fair, harmful bias managed | Effect of leave taken under accommodation or protected leave codes on the score | Raises the score | **No.** Exclude protected leave codes from features |
| Accountable and transparent | Developer documentation for deployers | None | **No** (due before 2027-01-01) |
| Explainable and interpretable | Top factors shown with each score | In place | Yes |

### 4.3 Resume screening (AI-009)
About 41,000 applicants screened in the pilot; "selected" means ranked in the top band that recruiters reviewed first.

| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Fair, harmful bias managed | Selection rate ratio by sex (UGESP four-fifths) | 0.91 | Yes |
| Fair, harmful bias managed | Selection rate ratio by race and ethnicity | Lowest 0.83 | Yes, but near the threshold; monitor monthly |
| Fair, harmful bias managed | Ratio for applicants aged 40 and over (internal heuristic) | 0.74 | **No** |
| Accountable and transparent | CCPA ADMT pre-use notice and risk assessment for California applicants | None | **No** |
| Accountable and transparent | Vendor documentation of training data and validation | Partial | Partial |

### 4.4 Payments and consulting use cases
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-004 merchant risk | Decline rate review by merchant category and size; appeals overturned | 6% of appealed declines overturned | Yes (monitor) |
| AI-005 payroll anomaly | Holds released within 2 hours (target 95%) | 88% overall; 79% at month-end peaks | **No** |
| AI-006 delivery assistant | Use on projects without client opt-in (log review) | 14 projects of 1,320 | **No** (allow-list enforcement due 2027-01-31) |
| AI-003 optimizer | Hours offered to workers with accommodation flags compared with others | Within 3% | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** drafts are never applied automatically; HR case notes are excluded from summaries for non-HR roles; every answer links to its source documents; customers can switch the feature off per tenant.
- **AI-002:** scores are advisory, shown with top factors and a notice that they must not be the sole basis for any employment decision; protected leave codes removed from features; customers can switch the feature off.
- **AI-009:** recruiters review every applicant regardless of rank; no automatic rejection; applicants may request human review.
- **AI-005:** every hold reviewed by an analyst; workers and employers told the reason and expected release time.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-04, SW-005, SW-006, SW-007, SW-025, SW-028, IC-012, PY-014.

**Incident handling:** AI failures that disclose customer data, harm workers or applicants, or break customer commitments follow P08 and POL-03. A model provider incident follows the sub-processor path in the Cloud Software supplement.

**Decommissioning:** each use case has an off switch and a fallback (standard reports, manual scheduling, manual review queues) that the BIA already covers (P05 BP-SW07, BP-SW08).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 workforce assistant | **Continue with conditions** (council, 2026-09-04; board risk committee informed 2026-09-17) | HR case-note fix by 2026-11-15; retroactive privacy impact assessment by 2026-11-30; red-team test and monthly accuracy sampling with a 2% target by 2026-12-31 (POAM-010, POAM-011) |
| AI-002 attrition-risk insights | **Continue for existing customers; pause new enablement** | Claim to be withdrawn by 2026-10-15; protected leave codes removed and age-proxy mitigation by 2026-12-15; developer documentation and usage guidance published before 2027-01-01; quarterly bias testing (POAM-027) |
| AI-009 resume screening | **Pause for new requisitions** until conditions are met | CCPA risk assessment and pre-use notice by 2026-11-30; vendor validation evidence; age-ratio mitigation; restart only with council approval and before 2027-01-01 if all conditions are met (POAM-028) |
| AI-003 schedule optimizer | **Continue** | Add hours-parity monitoring to the quarterly report |
| AI-004 merchant risk | **Continue** | Counsel's Colorado scope opinion by 2026-12-31 |
| AI-005 payroll anomaly | **Continue** | Month-end staffing to meet the 2-hour review target by 2026-12-31 |
| AI-006 delivery assistant | **Continue with conditions** | Project allow-list enforcement by 2027-01-31 |
| AI-007, AI-008 | **Approved** | Standard monitoring; AI-008 prohibited for decisions about people |

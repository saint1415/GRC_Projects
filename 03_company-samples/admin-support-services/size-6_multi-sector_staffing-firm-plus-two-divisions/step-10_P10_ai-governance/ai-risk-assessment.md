# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Staffing, Consulting, Home Health, corporate) |
| Tier / Vertical | Multi-Sector / Administrative and Support and Waste Management and Remediation Services |
| Scope | The group AI governance program: the Group AI Standard, the division use-case inventory, and the regulator-specific rules for the priority use cases: **AI-001 AI resume screening and candidate ranking** (group-wide, focus), AI-002 the recruiting assistant (Staffing), AI-005 the hospitalization risk model (Home Health), and AI-008 the denial-prediction model (Consulting) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27; presented to the board risk committee 2026-09-10 |
| Inventory | `ai-use-case-inventory.csv` (10 use cases: 3 High, 6 Medium, 1 Low), built from AI tool discovery across procurement, SaaS discovery, the SYS-G1 app list and the model registry (EV-046), the AI ranking add-on vendor file and ATS configuration (EV-037), the 2026-04 NYC bias audit (EV-038), Home Health AI records (EV-069), and the AI council's use-case review in 2026-08 (EV-096), which added AI-004 (a pilot since 2026-07, after intake). Not established: workforce use of public generative AI tools outside the approved tools (intake open request), and adverse impact results for AI-001 outside NYC requisitions (none provided, EV-038) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group General Counsel, Group Chief Privacy Officer, Group CISO, Staffing talent acquisition vice president, Home Health chief clinical officer, Health IT Advisory president, Group HR director. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group workforce data director | Runs adverse impact monitoring for hiring tools on the workforce data hub, separate from the tools themselves |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) |
| Group Chief Privacy Officer | Notices, privacy impact assessments, ADMT duties, vendor data terms |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026, under POL-01 4.13)
1. **Register before use.** Every AI use case that ranks, screens, or supports decisions about candidates, workers, patients, or clients' patients is registered before deployment or material change. Marketplace add-ons count (POL-01 4.8).
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment and bias testing, notices where law requires, and quarterly monitoring reports.
3. **No auto-reject.** No hiring tool may reject, close, or hide a candidate without a human decision. Ranking and sorting are allowed with monitoring.
4. **Vendor terms.** AI vendors handling candidate or worker data may not train on it without a recorded purpose and approval; vendors handling PHI sign BAAs with no-training terms; every vendor provides assurance (SOC 2 or equivalent) and bias test results for hiring tools.
5. **Division overlays.** Staffing and every division that hires: employment discrimination law and state AI hiring laws. Home Health: Section 1557 for patient care decision support tools and recording consent. Consulting: client BAAs and contracts for models built on client data.
6. **Change gate.** A material change (new model, new feature, new decision role, new state or client population) triggers re-assessment before release.

**Where the program fell short in 2026.** The standard was adopted after AI-001 and AI-002 were live. AI-001 was added through the ATS marketplace without vendor due diligence (P03 ID.RA-10, Not met), and auto-advance was switched on for Commercial requisitions without a change ticket. Both are now under conditions (section 6).

## 2. MAP (use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | AI resume screening and candidate ranking | Group (all divisions) | High | In production with conditions |
| AI-002 | Recruiting assistant with knockout questions | Staffing | High | In production; knockout library frozen |
| AI-003 | Clinician shift matching and pay-rate recommendation | Staffing | Medium | In production |
| AI-004 | Bank-change fraud scoring | Group (GWP) | Medium | Pilot |
| AI-005 | Hospitalization risk model | Home Health | High | In production; 92.210 review due |
| AI-006 | Ambient documentation pilot | Home Health | Medium | Pilot; expansion paused |
| AI-007 | Consultant drafting assistant | Consulting | Medium | Approved with conditions |
| AI-008 | Claim denial-prediction model for hospital clients | Consulting | Medium | In production for 9 clients; pooled training paused |
| AI-009 | Enterprise generative AI assistant | Group | Medium | Pilot |
| AI-010 | Job ad and message drafting | Staffing | Low | Approved |

### 2.1 AI-001: context
| Item | Detail |
|---|---|
| Purpose | Score each applicant against the requisition (skills, certifications, availability, distance) and sort the list for about 3.1 million applications a year |
| Users | About 6,100 recruiters in all divisions; configured by the talent acquisition technology team |
| Affected people | Every applicant to the group; indirectly the clients who receive referrals |
| Data | Inputs: resumes, application answers, work history, certifications, prior ATS activity. Not used: SSNs, I-9 data, consumer reports, self-identification data. Outputs: a 0-100 score and a match summary; on Commercial requisitions, an auto-advance flag at 75 and above |
| How much it decides | On Commercial requisitions, 86% of 2026 Q2 placements came from auto-advanced applicants, so applicants below 75 were rarely seen. The tool is a substantial factor in who is referred |
| Not intended (disabled) | Automatic rejection, video or voice analysis, personality scoring, third-party data enrichment |

### 2.2 AI-001: applicable rules by division and state
| Rule | Applies? | What it means here |
|---|---|---|
| Title VII, 42 U.S.C. 2000e-2(a), (b), and (k) | **Yes (all divisions)** | Each division is an employer; Staffing is also an employment agency when it refers associates to clients (703(b)). Section 703(k) codifies disparate impact: a practice causing it is unlawful unless job related and consistent with business necessity, or if a less discriminatory alternative is refused |
| ADEA, 29 U.S.C. 623(b); 631(a) | **Yes** | Same employment agency rule for age (40 and over). Features such as graduation year can act as age proxies |
| ADA, 42 U.S.C. 12112(b)(6) | **Yes** | Criteria that screen out people with disabilities must be job related and consistent with business necessity; applicants need a way to request an accommodation or an alternative process |
| NYC Local Law 144 (N56-R08) | **Yes (NYC requisitions)** | Bias audit within 1 year before use, public summary, candidate notice. The 2026-04 audit is current; notices were missed on NYC jobs created outside NYC branches (P03 G-138) |
| CPPA ADMT rules (11 CCR 7200 et seq.) | **Yes from 2027-01-01** | The group is a CCPA business; employment decisions are significant decisions. Pre-use notice, opt-out (with exceptions), and access rights for California applicants |
| Colorado SB26-189 (C.R.S. 6-1-1701 to -1709) | **Yes from 2027-01-01** | Deployer duties for covered ADMT that materially influences employment decisions: notice, explanation after an adverse outcome, correction and human review, 3-year records. Its HIPAA covered entity carve-out does not cover Home Health's employment decisions |
| Illinois HB 3773 (Public Act 103-0804) | **Yes (Illinois jobs), partially verified** | Civil rights violation to use AI with a discriminatory effect in hiring or to use zip codes as a proxy; notice when AI is used. The cross-sector register marks the provisions as partially verified; counsel confirms the notice wording |
| FCRA, 15 U.S.C. 1681b | **Not today** | The tool uses only information applicants give the group. Third-party data enrichment stays disabled; enabling it needs counsel review |
| Fla. Stat. 501.171(2) | **Yes (security)** | The vendor holds applicant personal information; reasonable measures include vendor terms (POAM-012) |

**Federal agency posture, and why it does not change the plan:**
- The EEOC's May 2023 technical assistance on adverse impact from software, algorithms, and AI under Title VII is no longer on eeoc.gov, and Executive Order 14281 (2025-04-23) directs agencies to deprioritize disparate-impact enforcement.
- On 2026-06-09 the Justice Department's Office of Legal Counsel issued an opinion to the EEOC Chair, "Constitutionality of Disparate-Impact Liability Under Title VII," concluding that the EEOC's Title VII guidelines, including the Uniform Guidelines on Employee Selection Procedures (UGESP), are unconstitutional insofar as they contemplate liability based on disparate effects alone. OPM then removed UGESP references from federal personnel rules (91 FR 48234, 2026-07-31).
- **What has not changed:** 42 U.S.C. 2000e-2(k) is still the statute; an OLC opinion binds executive agencies, not courts or private plaintiffs; state laws (NYC, Illinois, Colorado, California) impose their own duties; and UGESP (29 CFR Part 1607, including the four-fifths rule at 1607.4(D)) is still in the eCFR as of 2026-09-23.

**Decision:** the group keeps a group-wide bias testing program. The four-fifths ratio is used **as an internal screening indicator only**, not as a legal standard or safe harbor, together with a statistical significance test and a review of which features drive any difference.

### 2.3 Division overlays for the other priority use cases
| Use case | Rule | Implication |
|---|---|---|
| AI-002 recruiting assistant | ADA 12112(b)(6); Title VII 703(k); state fair chance laws (generic) | Knockout questions are selection criteria. A review found 14 of 212 branch-added questions asked about criminal history before an offer and 3 asked whether the candidate could do a task "without accommodation." Knockouts must route to a recruiter, not close the candidate |
| AI-005 hospitalization risk model | 45 CFR 92.210(a)-(c); 92.4 | 45 CFR 92.4 defines a patient care decision support tool as any automated or non-automated tool used to support clinical decision-making. Home Health must make reasonable efforts to identify tools that use race, color, national origin, sex, age, or disability as inputs and to mitigate discrimination risk. The model uses age and functional status items |
| AI-006 ambient documentation | State recording consent laws; HIPAA | In all-party consent states (Florida, Fla. Stat. 934.03(2)(d), is the worked example), recording may start only after every party present consents, including family members in the home |
| AI-008 denial-prediction model | 45 CFR 164.502(a)(3); 164.504(e)(2)(i)(B) | Consulting may use client PHI only as each BAA permits. Pooling several clients' data to train one model is data aggregation, which a BAA may permit; only 4 of the 9 clients' BAAs do |
| AI-007, AI-009 generative assistants | POL-04 4.9; POL-05 4.8; client BAAs | No PHI or other Restricted information unless the tool is approved for it; never for hiring, pay, clinical, or client decisions |

## 3. Risk tiers (repository rubric)
- **High:** AI-001 and AI-002 (substantial factors in employment decisions), AI-005 (supports health care decisions).
- **Medium:** AI-003 (assignment and pay recommendations reviewed by people), AI-004 (holds pay changes), AI-006 (outputs enter clinical records), AI-007 and AI-009 (confidential data risk), AI-008 (client PHI use).
- **Low:** AI-010.

**Re-tier triggers:** auto-advance or auto-reject anywhere (AI-001, AI-002 stay High); AI-003 setting pay without review (to High); AI-004 delaying pay rather than a bank change (to High); AI-006 suggesting orders or diagnoses (to High); AI-008 offered as a hosted product (re-assess, including SOC 2 scope in P09).

## 4. MEASURE
Results are from monitoring and audits between 2026-04 and 2026-08.

### 4.1 AI-001 resume screening and ranking (group-wide)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Recruiter review of 300 random applicants per division: score agrees with the requisition's minimum requirements (target 90%) | Commercial 83%; Healthcare Staffing 88%; Professional 91%; Consulting 93%; Home Health 90% | **No** for Commercial and Healthcare |
| Fair, harmful bias managed | Selection-rate ratio (advanced to recruiter review) by sex and race or ethnicity, from voluntary self-identification matched by the data hub team; flag below 0.80 or a significant difference | NYC audit (2026-04): all ratios 0.85 or higher. Group-wide Commercial (first run, 2026 Q2): Black applicants 0.78, Hispanic 0.86, women 0.94 | **Flagged** (Commercial) |
| Fair (drivers) | Feature review for the flagged difference | Commute distance and an "employment gap" feature drive most of it; the gap feature can also screen out people with disabilities and caregivers | **No.** Remove the gap feature; cap distance weighting |
| Fair (age) | Age proxies | Graduation year was a feature; age is not collected before an offer, so direct testing is not possible | **No.** Graduation year removed 2026-09-15 |
| Accountable and transparent | Notices and explanations where required | NYC only; none for California, Colorado, or Illinois applicants | **No** (POAM-025) |
| Secure and privacy-enhanced | Vendor assurance; data terms | No SOC 2 report; vendor may train on candidate data | **No** (POAM-012) |
| Human oversight | Share of Commercial placements from auto-advanced applicants | 86% | **No.** Auto-advance off by 2026-10-31 |

### 4.2 Other priority use cases
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-002 recruiting assistant | Knockout questions reviewed by legal | 17 of 212 problematic; 9 branches added questions without review | **No.** Library frozen; candidates closed by knockouts since 2026-02 re-opened for review |
| AI-003 shift matching and pay | Recommended rate differences by sex for the same role and market (flag over 2%) | 1.1% | Yes |
| AI-004 fraud scoring | Legitimate changes held (false positives); time to release | 6% of held changes legitimate; median release 5 hours | Yes. The old account is still paid on payday, so a hold never delays pay |
| AI-005 hospitalization risk | 92.210 identification and mitigation record; flag-rate ratio for patients 85 and older vs. 65-74 | No record; ratio 2.1 (clinically expected, but not documented as reviewed) | **No** (POAM-027) |
| AI-006 ambient documentation | Consent recorded before recording (target 100%) | 84% | **No** |
| AI-008 denial prediction | Clients whose BAA permits data aggregation, among clients whose data trained the pooled model | 4 of 9 | **No.** Pooled training paused; per-client models for the other 5 |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** ranked lists only; no auto-advance; recruiters see a random sample of lower-ranked applicants on every Commercial requisition; any applicant can ask for an accommodation or a human review from the career site.
- **AI-002:** knockout answers route the candidate to a recruiter queue; questions come only from the central library after legal review.
- **AI-005:** the score prompts a clinical review; it never changes visit frequency on its own.
- **AI-008:** client billing staff decide every claim; the model is advisory.

**Monitoring:** monthly adverse impact reports for AI-001 by requisition family, from the workforce data hub (independent of the vendor); quarterly High-tier report to the council and the board risk committee; P01 risks GR-04, ST-003, ST-009, ST-023, CN-007, CN-008, HH-010, HH-011.

**Incident handling:** AI failures that cause discriminatory outcomes, disclose personal information or PHI, or breach client commitments follow P08 and POL-03.

**Decommissioning:** every use case has an off switch and a manual fallback (unranked lists, recruiter screening, standard visit planning) that the BIA already covers (P05).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 AI resume screening and ranking | **Continue with conditions** (council, 2026-08-27; board risk committee informed 2026-09-10) | Auto-advance off by 2026-10-31; gap feature removed and distance capped by 2026-10-31; monthly group-wide adverse impact monitoring from 2026-11; notices, opt-out and human review paths for California and Colorado applicants by 2026-12-31 and Illinois notice confirmed by counsel (POAM-025); vendor assurance or exit decision by 2026-12-31 (POAM-012); NYC notice rule fixed by 2026-12-31 |
| AI-002 recruiting assistant | **Continue with conditions** | Knockouts route to recruiters by 2026-10-15; legal review of every question; re-open affected candidates; monthly outcome audit |
| AI-005 hospitalization risk model | **Continue** | 92.210 identification and mitigation record by 2026-12-31 (POAM-027) |
| AI-006 ambient documentation | **Continue pilot; no expansion** | Required consent field before recording by 2026-11-30 |
| AI-008 denial-prediction model | **Continue per client; pooled training paused** | BAA review for all clients (P03 CN-G20); pooled model only for clients whose BAA permits data aggregation |
| AI-003, AI-004, AI-007, AI-009, AI-010 | **Approved** | Standard monitoring; AI-007 PHI detection by 2026-12-31; AI-009 prohibited for hiring, pay, clinical, or client decisions |

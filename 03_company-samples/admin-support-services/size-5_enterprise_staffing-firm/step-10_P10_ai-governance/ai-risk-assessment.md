# AI Governance Risk Assessment: Enterprise AI Portfolio and AI Resume Screening

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded staffing and workforce solutions company; 38 states and DC) |
| Tier / Vertical | Enterprise / Administrative and Support and Waste Management and Remediation Services |
| Scope | Enterprise AI portfolio (11 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001 AI resume screening and candidate ranking in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; NIST AI 600-1 (Generative AI Profile) for AI-002, AI-004, and AI-006; repository risk tier rubric |
| Assessor / date | AI governance council (co-chaired by the Chief Data Officer and the General Counsel), meeting of 2026-08-26; GRC team prepared the portfolio review; the data science team ran the first firm-data bias analysis of AI-001 |
| Decision | Executive risk committee, 2026-09-10 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 11 |
| Risk tier | High 3, Medium 6, Low 2 |
| Status | In production 10, Pilot 1 |
| Council review complete | 6 of 11 |
| Not yet reviewed | 5: AI-007, AI-008, AI-009, AI-010, AI-011 (all due 2026-11-30, POAM-014) |
| Tools that rank, screen, or allocate work to people | 3 High-tier tools: AI-001 (candidate ranking), AI-009 (redeployment ranking), AI-007 (identity verification in hiring) |
| High-tier tools with bias testing on the firm's own data | 1 of 3 (AI-001, first analysis 2026-08; NYC audit covers NYC only) |

**Main findings:** the firm's most consequential AI tool, AI-001, ranks about 2.6 million applications a year. Its only fairness evidence until August was the vendor's data and the NYC bias audit, which covers NYC applicants only. The first firm-data analysis found two disparities in Commercial Staffing (section 7.4). Two High-tier tools are running without council review: AI-009 arrived through a vendor release and now ranks which associates are offered the next assignment, and AI-007 is a biometric identity pilot.

## 2. GOVERN: AI governance council operating model
**Charter.** The AI governance council was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the risk and technology committee of the board reviews quarterly.

**Members:** Chief Data Officer and General Counsel (co-chairs); Chief Privacy Officer; CISO; Chief Compliance Officer; Chief Human Resources Officer; Vice President, Talent Acquisition Technology; Vice President, Employment Compliance; one segment president on rotation; the data science lead; and an associate-experience representative from the Associate Service Center. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Council vote, then the executive risk committee | Firm-data validation and bias testing; legal review of state and local AI employment rules (section 6); impact assessment; human review design; notice and accommodation path; monitoring plan |
| Medium | Council vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review |
| Low | Council co-chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.3; STD-05.4). Since 2026-08 procurement and the change process (PRC-01.3) block AI features without an inventory ID, and changing an AI setting is a change that needs approval (POL-01 4.13). The GRC team owns the inventory.

**Policies:** POL-05 4.3 (approved AI tools only; no candidate, associate, or client data in public AI tools; no AI ranking or screening of people without council approval); POL-04 4.2 (no clear-text Restricted data for analytics); POL-01 4.8 (vendor terms before personal data is shared); STD-05.4 (approved AI tools list).

**Cadence:** monthly council meetings; quarterly monitoring review for every High-tier tool; annual re-review of every use case.

**Why 5 use cases lack review.** AI-009 and AI-010 arrived through vendor feature releases before the intake block existed; AI-008 and AI-011 were treated as internal analytics; AI-007 started as a fraud-prevention pilot after fraudulent remote candidates were detected in 2026. The council set review dates for all five (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| Title VII, 42 U.S.C. 2000e-2(a), (b), and (k) | **Yes** | The firm is the employer of its associates and an employment agency when it refers them. Section 703(b) makes it unlawful for an employment agency to "classify or refer for employment any individual" on the basis of a protected trait. Section 703(k) codifies disparate impact |
| ADEA, 29 U.S.C. 623(b), (e) | **Yes** | Same employment agency rule for age (individuals 40 and over); job notices may not state age preferences (AI-002) |
| ADA, 42 U.S.C. 12112(b)(5)-(6) | **Yes** | Selection criteria that screen out people with disabilities must be job related and consistent with business necessity; applicants need an accommodation path, including an alternative to automated steps |
| NYC Local Law 144 (N56-R08) | **Yes, for NYC jobs** | AI-001 is an automated employment decision tool for jobs at 9 NYC branches: bias audit within one year before use, public summary, and candidate notices |
| Illinois Public Act 103-0804 | **Yes** | In force 2026-01-01: no AI use with a discriminatory effect, no zip codes as a proxy, and notice when AI is used (content confirmed only from ilga.gov search snippets; IDHR rules not checked) |
| California Civil Rights Council ADS regulations (2 CCR 11008 et seq.) | **Yes** | In force 2025-10-01 for California applicants: an ADS that discriminates is unlawful; anti-bias testing is relevant to defenses; ADS data kept 4 years |
| California CPPA ADMT regulations (11 CCR 7200 et seq.) | **Yes, from 2027-01-01** | The firm is a CCPA business; AI-001 and likely AI-009 make or support significant decisions about employment: pre-use notice, opt-out (with exceptions), access rights |
| Colorado SB26-189 | **Yes, from 2027-01-01** | AI-001 and likely AI-009 materially influence consequential employment decisions about Colorado consumers: notice, 30-day post-adverse-outcome disclosure, correction and human review rights, 3-year records. No employee-count exemption appears in the signed act |
| Connecticut Public Act 26-15 | **Likely yes (effective 2026-10-01)** | Per the Connecticut Attorney General, employers must give written notice when AI is used in decisions affecting terms or conditions of employment. Only the AG's release was read; counsel is confirming the text |
| FCRA, 15 U.S.C. 1681b | **Not today** | AI-001 uses only information applicants give the firm. Third-party data enrichment would raise consumer reporting agency questions and needs counsel review first (the CFPB withdrew its 2024 circular on background dossiers and algorithmic worker scores on 2025-05-12; the statute is unchanged) |
| State biometric privacy laws | **Under counsel review (AI-007)** | Face templates from selfie video. Florida's treatment of templates computed from video is unsettled (Fla. Stat. 501.702 excludes photographs and data generated from video or audio recordings from its biometric definition); the firm treats them as biometric data. Illinois candidates are excluded from the pilot because Illinois biometric law was not verified here |
| Florida Digital Bill of Rights | **No** | A "controller" must exceed $1 billion in global gross annual revenue **and** earn 50% or more of revenue from online advertising, run a consumer smart speaker and voice command service, or run an app store with at least 250,000 applications (Fla. Stat. 501.702). The firm meets the revenue test but none of the three activity tests |

**Federal agency posture (verified 2026-09-26 in the Small sample's review; nothing found since), and why it does not change the firm's plan:**
- The EEOC's May 2023 technical assistance on adverse impact from software, algorithms, and AI under Title VII is **no longer on eeoc.gov** (the page returns 404). Its 2022 technical assistance on the ADA and AI also returns 404. An "AI and the ADA" resource page still resolves; its content was not reviewed.
- Executive Order 14281 (2025-04-23) directs agencies to deprioritize disparate-impact enforcement.
- On **2026-06-09 the Justice Department's Office of Legal Counsel** issued an opinion to the EEOC Chair concluding that the EEOC's Title VII guidelines, including the Uniform Guidelines on Employee Selection Procedures (UGESP), are unconstitutional insofar as they contemplate liability based on disparate effects alone. OPM then removed UGESP references from federal personnel rules (91 FR 48234, 2026-07-31).
- The EEOC rescinded its affirmative action guidelines, 29 CFR Part 1608 (91 FR 40879, 2026-07-06), and on 2026-07-23 **proposed** rescinding the EEO-1 to EEO-6 reports in 29 CFR Part 1602 (91 FR 46332). The Part 1602 change is a proposal only and is not treated as current law.
- **What has not changed:** 42 U.S.C. 2000e-2(k) is still the statute. An OLC opinion binds executive agencies, not courts or private plaintiffs, and private suits under Title VII remain available. UGESP (29 CFR Part 1607, including the four-fifths rule at 1607.4(D)) is still in the eCFR as of 2026-09-23. And the state and local rules above apply regardless of federal posture.

**Decision:** the firm keeps a bias testing program for every High-tier tool that affects people. The four-fifths ratio is used **as an internal screening indicator only**, not as a legal standard or safe harbor, alongside a statistical significance test and a review of which features drive the difference.

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision (here, employment) or able to affect physical safety.

| ID | Use case | Tier | Status | Council review |
|---|---|---|---|---|
| AI-001 | AI resume screening and candidate ranking | High | In production | Reviewed 2025-11-12; re-reviewed 2026-08-26 |
| AI-002 | Generative job ads and candidate messages | Medium | In production | Reviewed 2025-12-10 |
| AI-003 | Fill-time and pay-rate prediction for job orders | Medium | In production | Reviewed 2026-01-14 |
| AI-004 | Candidate chatbot (scheduling and FAQs) | Medium | In production | Reviewed 2026-02-11; re-reviewed 2026-08-26 |
| AI-005 | Bank-change fraud scoring | Medium | In production | Reviewed 2026-03-18 |
| AI-006 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-01-14 |
| AI-007 | Remote interview identity verification (face match) | High | Pilot | Not reviewed (due 2026-11-30) |
| AI-008 | WMP invoice anomaly detection | Low | In production | Not reviewed (due 2026-11-30) |
| AI-009 | Associate redeployment ranking | High | In production | Not reviewed (due 2026-11-30) |
| AI-010 | Timesheet anomaly detection | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-011 | SOC alert triage assistant | Low | In production | Not reviewed (due 2026-11-30) |

**Tiering notes:** AI-009 is High because the ranked list decides, in practice, which associates get the next shift, and attendance and client-feedback inputs can carry disability and bias effects. AI-003 stays Medium because it suggests a market range for a job, not pay for a person; using it to set an individual's pay would re-tier it to High. AI-005 is Medium because a held bank change delays where pay goes but a person releases every hold. AI-010 would become High if its flags were used for discipline without investigation.

## 5. MEASURE: bias testing across the portfolio
| Tool | Evidence today | Gap | Plan |
|---|---|---|---|
| AI-001 | NYC independent bias audit (2026-02-09, NYC data); vendor data; first firm-data analysis (2026-08, section 7.4) | Two disparities flagged in Commercial Staffing; California, Illinois, and Colorado not separately tested | Quarterly firm-data monitoring by segment, job family, and state from 2027-01 (POAM-014) |
| AI-009 | None | No testing; offer-rate effects unknown | Offer-rate ratios by group before the council review; attendance feature reviewed for disability effects |
| AI-007 | Vendor demographic accuracy claims | No firm data; biometric legal review open | Mismatch and manual-review rates by self-identified group during the pilot |
| AI-003 | Pay suggestion audit by job family and location (2026-06) | None material | Continue quarterly |

**Data limits:** self-identification is voluntary (61% response for Commercial Staffing applicants in 2026 Q2); groups with fewer than 100 self-identified applicants in a quarter are not tested; age is not collected before an offer. Results go to the council and the Chief Compliance Officer, and records are kept at least 4 years to meet the longest applicable retention rule (California's 4 years for ADS data).

## 6. State and local AI employment duties: what the firm does
| Duty | Where | What the firm does | Status |
|---|---|---|---|
| Bias audit within one year before use; public summary | NYC (N56-R08) | Independent audit 2026-02-09; summary on the careers site; next audit scheduled 2027-01 | Met (P03 G-164, G-165) |
| Candidate notice | NYC | Notice in NYC posting templates | Partially met: 3 of 40 postings missed it (P03 G-166) |
| No discriminatory effect; no zip code proxy; notice | Illinois | Notice in Illinois postings since 2026-01; commute distance capped and under counsel review | Partially met (P03 G-188) |
| Anti-bias testing as a defense; 4-year ADS records | California | Scores retained in SYS-01; California included in firm-data monitoring from 2027-01 | Partially met (P03 G-187) |
| Pre-use notice, opt-out or exception basis, access | California, from 2027-01-01 | Design due 2026-12-15 (POAM-023) | Not met (readiness, P03 G-184) |
| Notice, 30-day post-adverse-outcome disclosure, correction and human review, 3-year records | Colorado, from 2027-01-01 | Design due 2026-12-15 (POAM-023) | Not met (readiness, P03 G-169 to G-172) |
| Written notice of AI use in employment decisions | Connecticut (effective 2026-10-01; text being confirmed) | Illinois-style notice added to Connecticut postings 2026-10-01 | Counsel confirming |

**One design for all states.** Rather than state-by-state variants, the firm is building one enterprise standard for AI-001 and AI-009: a notice at every point of application, a person who reviews every qualified applicant, an accommodation and human review request path, a post-decision explanation available to anyone who asks (sent automatically within 30 days where Colorado requires it), model version recorded with every score, and 4-year records. California's opt-out is handled by routing opted-out applicants to the manual review queue.

## 7. Full assessment: AI-001 AI resume screening and candidate ranking
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Help about 5,200 recruiters work through about 2.6 million applications a year by scoring each applicant against the job order (skills, certifications, shift availability, commute distance) and sorting the list |
| Users / operators | Recruiters and branch managers in all segments except ACQ-1; configured by the talent acquisition technology team |
| Affected people | Every applicant to a requisition in SYS-01, and indirectly clients who receive referrals |
| Data | Inputs: resumes, application answers, work history, certifications, prior ATS activity (rehires), commute distance computed from the applicant's address. Not used: SSNs, Form I-9 data, consumer reports, voluntary self-identification. Outputs: a 0-100 score and a match summary |
| Build or buy | Buy: third-party vendor model integrated into SYS-01. The vendor provides feature lists and weights on request; training data details are limited |
| How much it decides | Sort-only: no auto-advance and no automatic rejection have ever been enabled at this firm. But recruiters call from the top of the list, and in 2026 Q2 about 74% of Commercial Staffing placements came from the top third, so the score is a substantial factor in who is referred |
| Not intended | Automatic rejection, video or voice analysis, personality scoring, social media or third-party data enrichment. These vendor features are disabled; enabling any of them requires a new assessment |

### 7.2 Risk tier
High (section 4). Minimum controls for High under the rubric: human review before action, pre-deployment bias testing, impact assessment (this document), notice to affected people, and ongoing monitoring.

### 7.3 Laws that bear most directly
Title VII 703(b) and (k), the ADA, and the ADEA everywhere; NYC Local Law 144 for NYC jobs; Illinois Public Act 103-0804; California's ADS regulations now and its ADMT rules from 2027-01-01; Colorado SB26-189 from 2027-01-01 (section 3).

### 7.4 MEASURE (retrospective, 2026 Q2)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Recruiter review of 400 random applicants per segment: does the score agree with the job order's minimum requirements? Target: at least 90% agreement | Commercial 88%; Professional 93%. Most disagreements were certifications in non-standard formats and Spanish-language resumes the parser read poorly | **No** for Commercial |
| Safe | Not a physical safety system; indirect harm is exclusion from work | See fairness | n/a |
| Secure and resilient | Vendor SOC 2 Type 2; SSO; data use terms | SOC 2 reviewed 2026-04; SSO; no-training and deletion terms signed 2025-11 | Yes |
| Accountable and transparent | Change control over settings; notice to applicants | AI settings under change control since 2026-08 (POL-01 4.13); notice in NYC, Illinois, and Connecticut postings and on the careers site; NYC notice missed on 3 of 40 postings | Partial |
| Explainable and interpretable | Recruiter can see why an applicant scored as they did | Match summary lists matched and missing requirements; feature weights provided 2026-08-14 | Yes |
| Privacy-enhanced | Minimum data; retention; no secondary use | No SSNs or self-ID data; vendor keeps resumes for the subscription term; scores kept in SYS-01 without a purge rule (POAM-005) | Partial |
| Fair, with harmful bias managed | Rate of applicants placed in the top third of the sorted list, by sex and by race or ethnicity (voluntary self-ID), per segment. Flag if a group's rate is below 80% of the highest group's rate **and** the difference is statistically significant (two-proportion z test, p < 0.05) | **Commercial, sex:** men 41.2% of 38,400; women 32.1% of 25,600; impact ratio **0.78**, z = 23.3 (flagged). **Commercial, race or ethnicity** (highest group: Asian 40.2% of 2,900): White 39.5%, ratio 0.98 (not flagged); Black 36.4%, ratio 0.91, z = 3.9 (significant but ratio above 0.80, watched); Hispanic or Latino 31.0% of 18,500, ratio **0.77**, z = 9.9 (flagged). **Professional (IT), sex:** women 35.3%, men 37.8%, ratio 0.93 (not flagged). **NYC audit (2026-02):** no category below 0.80 | **No.** Two disparities flagged in Commercial Staffing |

**Bias findings and causes.** The vendor's feature-weight report shows that most of the Commercial gap by sex comes from a penalty for employment gaps longer than 6 months and heavy weight on equipment keywords that appear less often on resumes listing picking and packing roles. The Hispanic or Latino gap tracks the parser's poor reading of Spanish-language resumes (the same cause as the validity failure) and, to a smaller degree, commute distance. None of these features is required by the firm's job orders, so each is a candidate for a less discriminatory alternative that works at least as well.

**Age and disability.** Age is not collected before an offer; the vendor confirmed that graduation dates and "years since first job" are not used, and experience beyond 5 years adds no points. Disability screen-out risk is managed through the accommodation path and the minimum-requirements review.

### 7.5 MANAGE
**Human-in-the-loop design:**
- The score only sorts. The ATS applies the job order's minimum requirements as a recruiter-set filter, and every applicant who meets them gets a human review before a referral decision.
- Recruiters record a reason when they pass over a higher-scored applicant for a lower-scored one, and when they reject an applicant who meets the minimum requirements.
- The employment-gap feature is disabled and the equipment keyword list is replaced with the certification field (vendor change confirmed 2026-09-02).
- Spanish-language resumes bypass the score and go to a bilingual recruiter until the vendor shows at least 90% agreement for them.
- Commute distance is capped at a single "within the job's stated commute range" flag, pending counsel's Illinois review.
- Client requests are entered as job requirements only. Any client preference tied to a protected trait is refused and reported to the Vice President, Employment Compliance (Title VII 703(b)).

**Notice, accommodation, and review requests:** the careers site and every job posting say that an automated tool helps sort applications, that a person reviews every qualified applicant, and how to ask for a person to review an application or for an accommodation. Walk-in applications stay available at every branch. The California opt-out and Colorado adverse-outcome disclosures are added by 2026-12-15 (section 6).

**Monitoring:** quarterly firm-data bias and validity tests by segment, job family, and state, reported to the council (R-009, R-041, R-042); annual NYC audit; monthly check of the ATS change log for AI settings changes.

**Incident handling:** an unexplained drop in a group's rate, a settings change made without approval, or a vendor security incident follows P08 and POL-03.

**Decommissioning:** stop using the score and fall back to recruiter search if two consecutive quarters are flagged after the fixes, if the vendor changes the model without notice, or if the state notice and disclosure duties cannot be met by 2027-01-01 for those states.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier tool has quarterly performance and fairness metrics (inventory column `monitoring`) reported to the council; drift or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse) are logged as SOC or compliance cases and follow P08 where security or personal data is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts require notice of material model changes and no training on firm data.
- **Records:** model version, settings, and monitoring results kept at least 4 years.
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice or change data-use terms; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the council's recommendation of 2026-08-26:
1. **AI-001:** approved to continue in sort-only mode with conditions: (a) the feature changes in 7.5 stay in place; (b) a re-test on 2026 Q4 data, reviewed by an outside statistician, shows no flagged group by 2027-01-31, or the council decides between further changes and switching the score off for Commercial Staffing; (c) California and Colorado notice, disclosure, opt-out or exception, and records duties are live by 2026-12-15 (POAM-023); (d) the 2027 NYC audit is completed before 2027-02-09.
2. **AI-009:** the ranked list is hidden from branch staff (they see an unranked list of available associates) until the council review and an offer-rate analysis are complete by 2026-11-30.
3. **AI-007:** the pilot stays limited to Professional Staffing remote IT hires outside Illinois; no expansion until counsel completes the biometric review and the council approves.
4. **AI-008, AI-010, AI-011:** may continue in current scope until council review by 2026-11-30; AI-010 flags may not be used for discipline without an investigation.
5. **Portfolio:** quarterly firm-data monitoring for all High-tier tools from 2027-01 (POAM-014); the results are reported to the risk and technology committee with ER-08.

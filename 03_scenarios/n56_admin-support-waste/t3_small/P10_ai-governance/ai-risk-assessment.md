# AI Risk Assessment: AI Resume Screening and Candidate Ranking

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm) |
| Tier / Vertical | Small / Administrative and Support and Waste Management and Remediation Services |
| AI use case | AI-001: AI resume screening and candidate ranking add-on to the ATS (SYS-09), in production since 2026-03-02 |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; NIST AI 600-1 for the generative feature in AI-002 |
| Assessor / date | Director of Recruiting with the HR and Compliance Manager and the IT Manager, 2026-08-25; independent statistical review contracted for 2026 Q4 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** Director of Recruiting. **Decision authority:** COO for High-tier AI (this use case). The President is informed of any High-tier AI decision.
- **Policies that apply:**
  - POL-05 4.10: approved AI tools only; AI scores are a sort aid, not a decision
  - POL-04 4.9: no Restricted data in AI tools that are not approved
  - POL-01 4.8: vendor review and data use terms before sharing personal information
  - POL-01 4.3: any change to how the tool decides (for example, turning auto-advance back on) is a major change that needs a new assessment
- **Approved-tools list:** kept by the IT Manager. Today it lists AI-001 (sort-only mode) and AI-002 (with human review). Public chatbots (AI-003) are not approved for any personal data.
- **Scale for a Small firm:** there is no AI committee. The COO, Director of Recruiting, HR and Compliance Manager, and IT Manager review AI use cases quarterly, together with the bias monitoring results.
- **What went wrong before this assessment:** the tool was bought through the ATS marketplace with click-through terms, switched to auto-advance by the Recruiting Operations Coordinator in March 2026 without review, and never tested for bias (P01 R-013; P03 G-045).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Help recruiters work through about 16,000 applications a year by scoring each applicant against the job order (skills, certifications, shift availability, commute distance) and sorting the list |
| Users / operators | 22 recruiters and 4 Branch Managers; configured by the Recruiting Operations Coordinator |
| Affected people | Every applicant (about 4,200 per quarter), and indirectly clients who receive referrals |
| Data | Inputs: resumes, application answers, work history, certifications, and prior ATS activity (for rehires). The tool does **not** receive SSNs, I-9 data, consumer reports, or voluntary self-identification data. Outputs: a 0-100 score, a match summary, and (until 2026-08-31) an auto-advance flag |
| Build or buy | Buy: third-party vendor model integrated into the ATS. The vendor's documentation lists features used (for example, keyword matches, years in similar roles, recency of employment, distance) but not training data details |
| How much it decided (before 2026-08-31) | Scores of 70 or more were auto-advanced to the recruiter queue. In 2026 Q2, **88% of Light Industrial placements came from auto-advanced applicants**, so in practice applicants below 70 were rarely seen. That makes the tool a substantial factor in who is referred |
| Not intended | Automatic rejection, interview scheduling without review, video or voice analysis, personality scoring, social media or other third-party data enrichment. These vendor features are **disabled**. Enabling any of them requires re-assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Title VII, 42 U.S.C. 2000e-2(a), (b), and (k) | **Yes** | The firm is an employer of its associates and an employment agency when it refers them to clients. Section 703(b) makes it unlawful for an employment agency to "classify or refer for employment any individual" on the basis of a protected trait. Section 703(k) codifies disparate impact: a practice that causes a disparate impact is unlawful unless shown to be job related and consistent with business necessity, or if a less discriminatory alternative is refused |
| ADEA, 29 U.S.C. 623(b); 631(a) | **Yes** | Same employment agency rule for age; protects individuals at least 40 years old. Features such as graduation year or "years since first job" can act as age proxies |
| ADA, 42 U.S.C. 12112(b)(6) | **Yes** | Selection criteria that screen out or tend to screen out people with disabilities must be job related and consistent with business necessity. Applicants need a way to ask for an accommodation or an alternative process |
| Title VII 704(b), 42 U.S.C. 2000e-3(b) | **Yes (AI-002)** | Job notices and ads may not indicate a prohibited preference; generated ads need review |
| FCRA, 15 U.S.C. 1681b | **Not today** | The tool uses only information applicants give the firm. If third-party data enrichment were turned on, the vendor could be assembling third-party information for employment purposes, which raises FCRA consumer reporting agency questions. Counsel review is required before any such feature is enabled. (The CFPB withdrew its 2024 circular on background dossiers and algorithmic worker scores on 2025-05-12; the statute itself did not change) |
| Fla. Stat. 501.171(2) | **Yes (security)** | The vendor holds applicant personal information (names with work history, and in some resumes driver license numbers), so the firm must take reasonable measures, including vendor terms |
| NYC Local Law 144 (N56-R08) | **No** | No NYC candidates or jobs |
| Colorado SB26-189 | **No** | Applies to deployers "doing business in Colorado" from 2027-01-01; the firm does not |
| Illinois HB 3773 (Public Act 103-0804) | **No** | Amends the Illinois Human Rights Act for Illinois employment; the firm has no Illinois employees or jobs |
| California Civil Rights Council ADS regulations; CPPA ADMT rules | **No** | No California employees, jobs, or business operations; the CCPA and its ADMT rules reach only businesses doing business in California |
| Connecticut PA 26-15; Texas TRAIGA | **No** | No Connecticut employees; the firm does not do business in Texas |
| Florida AI employment law | **None exists** | Florida has no statute on AI in employment decisions. The 2026 "Artificial Intelligence Bill of Rights" bills (SB 482 and SB 2-D) died (flsenate.gov status checked 2026-09-26) and did not address hiring tools |

**Trigger to re-check the state laws:** accepting a job order outside Florida, recruiting for remote jobs, or opening an office in another state. Out-of-state residents who apply for Florida jobs are currently screened the same way; counsel should confirm whether any state law reaches them before the firm expands recruiting advertising outside Florida.

**Federal agency posture (verified 2026-09-26), and why it does not change the firm's plan:**
- The EEOC's May 2023 technical assistance on adverse impact from software, algorithms, and AI under Title VII is **no longer on eeoc.gov** (the page redirects to a 404). Its 2022 technical assistance on the ADA and AI also returns 404. An "AI and the ADA" resource page still resolves; its content was not reviewed.
- Executive Order 14281 (2025-04-23) directs agencies to deprioritize disparate-impact enforcement.
- On **2026-06-09 the Justice Department's Office of Legal Counsel** issued an opinion to the EEOC Chair, "Constitutionality of Disparate-Impact Liability Under Title VII," concluding that the EEOC's Title VII guidelines, including the Uniform Guidelines on Employee Selection Procedures (UGESP), are unconstitutional insofar as they contemplate liability based on disparate effects alone. It reads disparate impact as reaching only practices that reflect a significant likelihood of intentional discrimination, and says the business necessity defense requires only that a practice rationally serve a valid business purpose. OPM then removed UGESP references from federal personnel rules (91 FR 48234, 2026-07-31).
- **What has not changed:** 42 U.S.C. 2000e-2(k) is still the statute. An OLC opinion binds executive agencies, not courts or private plaintiffs, and private suits under Title VII remain available. UGESP itself (29 CFR Part 1607, including the four-fifths rule at 1607.4(D)) is still in the eCFR as of 2026-09-23; the EEOC has not published a rescission.

**Decision:** the firm keeps a bias testing program because the legal duty in the statute remains, private claims remain, clients expect fair referrals, and a tool that hides qualified applicants is also a business problem. The four-fifths ratio is used **as an internal screening indicator only**, not as a legal standard or safe harbor, alongside a statistical significance test and a review of which features drive the difference.

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal/projects/P10_ai-governance/README.md`).

**Why High:** the tool is a substantial factor in an employment decision. Until 2026-08-31 it decided which applicants recruiters saw, and 88% of Light Industrial placements came from its auto-advanced list. Even in sort-only mode, ranking strongly shapes who gets called.

**Minimum controls for High** (rubric): human review before action, pre-deployment bias testing, impact assessment (this document), notice to affected people, and ongoing monitoring. All five are in the conditions in section 6.

**Would re-tier to Medium only if:** the tool becomes a pure search aid (no score or order shown), which is not planned.

## 4. MEASURE
| Trustworthy characteristic | Test / metric | Result (retrospective, 2026 Q2) | Pass? |
|---|---|---|---|
| Valid and reliable | Recruiter review of 100 random applicants per division: does the score agree with the job order's minimum requirements (certifications, shift, distance)? Target: at least 90% agreement | Light Industrial 81%; Office and Administrative 92%. Most disagreements were forklift certifications listed in non-standard formats and Spanish-language resumes the parser read poorly | **No** for Light Industrial |
| Safe | Not a physical safety system; indirect harm is exclusion from work | See fairness | n/a |
| Secure and resilient | Vendor security review; SSO; data use terms | No vendor review; ATS SSO covers access; no data use or no-training terms (P01 R-025) | **No** |
| Accountable and transparent | Change control over settings; notice to applicants | Auto-advance was switched on without approval; applicants are not told an AI tool scores them | **No** |
| Explainable and interpretable | Recruiter can see why an applicant scored as they did | Vendor match summary lists matched and missing requirements; feature weights available on request (provided 2026-08-19) | Partial |
| Privacy-enhanced | Minimum data; retention; no secondary use | Tool receives no SSNs or self-ID data; vendor keeps resumes for the subscription term; training on firm data not excluded | **No** |
| Fair, with harmful bias managed | Compare auto-advance rates by sex and by race or ethnicity (voluntary self-ID, 64% response), per division. Flag if a group's rate is below 80% of the highest group's rate **and** the difference is statistically significant (two-proportion z test, p < 0.05) | **Light Industrial, sex:** men 508 of 1,240 advanced (41.0%); women 226 of 780 (29.0%); impact ratio **0.71**, z = 5.5. **Light Industrial, race or ethnicity:** White 270 of 690 (39.1%); Black 187 of 520 (36.0%), ratio 0.92, z = 1.1 (not flagged); Hispanic or Latino 183 of 610 (30.0%), ratio **0.77**, z = 3.4. Groups under 100 self-identified applicants were not tested. **Office and Administrative, sex:** women 44.1%, men 41.9%, ratio 0.95 (not flagged) | **No.** Two disparities flagged |

**Bias findings and causes.** The vendor's feature-weight report (2026-08-19) shows that most of the Light Industrial gap by sex comes from two features: a penalty for employment gaps longer than 6 months, and heavy weight on specific equipment keywords that appear less often on resumes listing warehouse picking and packing roles. The Hispanic or Latino gap tracks the parser's poor reading of Spanish-language resumes (same cause as the validity failure). None of these features is required by the firm's job orders. They are candidates for a less discriminatory alternative that works at least as well.

**Age.** The firm does not collect age before an offer, so age rates cannot be measured. Instead the vendor confirmed that graduation dates and "years since first job" are not used, and the firm set a cap so that experience beyond 5 years adds no points.

**Disability.** Screen-out risk is managed through the accommodation path and the minimum-requirements review (section 5), because disability data is not collected.

**Bias testing plan going forward:**
| Item | Plan |
|---|---|
| Groups | Sex; race or ethnicity (self-ID categories with at least 100 applicants in the quarter); Spanish-language resumes vs. English |
| Metric | Rate of applicants placed in the top third of the sorted list, and rate of applicants contacted, per division and per job family |
| Threshold | Impact ratio under 0.80 with p < 0.05, or a validity agreement under 90% |
| Frequency | Quarterly, and before any settings change |
| Independent review | Outside statistician reviews the method and the 2026 Q4 results ($9,000, funded) |
| Records | Results, data extracts, and decisions kept for at least 4 years |

## 5. MANAGE
**Human-in-the-loop design (effective 2026-08-31):**
- Auto-advance is off. The score only sorts the list.
- The ATS applies the job order's minimum requirements (for example, shift availability and a required certification) as a filter set by the recruiter, not by the model. Every applicant who meets them gets a human review before a referral decision.
- Recruiters record a reason when they pass over a higher-scored applicant for a lower-scored one, and when they reject an applicant who meets the minimum requirements.
- The employment-gap feature is disabled and the equipment keyword list was replaced with the certification field (vendor change confirmed 2026-08-28).
- Spanish-language resumes bypass the score and go to a bilingual recruiter until the vendor shows at least 90% agreement for them.
- Client requests are entered as job requirements only. Any client preference tied to a protected trait is refused and reported to the HR and Compliance Manager (Title VII 703(b)).

**Notice and accommodation:**
- The career site and each job ad say that an automated tool helps sort applications, that a person reviews every qualified applicant, and how to ask for a person to review an application or for an accommodation (phone, email, or any branch).
- Walk-in and paper applications stay available at every branch.

**Monitoring:**
- Quarterly bias and validity tests (section 4), reported to the COO and tracked in the risk register (R-013, R-014).
- Monthly check of the ATS change log for AI settings changes.

**Vendor controls:**
- Data use addendum by 2026-10-31: no training of the vendor's models on firm data without written approval, deletion of applicant data 30 days after the subscription ends, breach notice within 72 hours, and annual SOC 2 or questionnaire (POAM-010).

**Incident handling:** an unexplained drop in a group's rate, a settings change made without approval, or a vendor security incident follows P08 and POL-03.

**Decommissioning:** stop using the score and fall back to recruiter review if the data use addendum is not signed by 2026-10-31, if two consecutive quarters are flagged after the fixes, or if the vendor changes the model without notice.

## 6. Decision
**Approve with conditions (High tier).** COO, 2026-08-31. The tool may continue in sort-only mode **only if**:
1. Auto-advance and all automatic rejection stay off (done 2026-08-31).
2. The employment-gap feature stays disabled and Spanish-language resumes bypass the score (done 2026-08-28).
3. Applicant notice and the accommodation path are live on the career site and in job ads by 2026-10-15 (POAM-016).
4. The vendor data use addendum is signed by 2026-10-31 (POAM-010).
5. The 2026 Q4 bias re-test, reviewed by the outside statistician, shows no flagged group by 2026-11-30. If a group is still flagged, the COO decides between further changes and switching the score off.

Turning auto-advance back on, or using the score in any other state, needs a new assessment and COO approval.

**Related actions for AI-002 and AI-003.** A short review checklist for generated job ads (no age, sex, or national origin preferences; accurate pay and shift) is due 2026-10-31. Public chatbots stay prohibited for personal data (POL-05 4.10).

# AI Risk Assessment: AI Resume Screening and Candidate Ranking

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm) |
| Tier / Vertical | Micro / Administrative and Support and Waste Management and Remediation Services |
| AI use case | AI-001: the ATS AI match and ranking feature (SYS-09), turned on 2026-03-16 |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; NIST AI 600-1 for the generative writer in AI-002 |
| Assessor / date | Senior Recruiter (ATS administrator) with the Operations Manager, 2026-08-25; statistical method checked by the independent consultant |
| Decision | Owner, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases), built from the ATS AI settings and change history, the AI feature terms, the card statements and a staff AI question (EV-008, EV-009, EV-017, EV-036). How many staff use public chatbots, and what they enter, was not established (intake open request) |

## 1. GOVERN
- **Accountable owner:** the Senior Recruiter, who administers the ATS. **Decision authority:** the Owner.
- **Policies that apply:**
  - POL-02 A.10: the Owner must approve any AI setting change (turning a feature on, changing a filter or threshold) in the change log
  - POL-02 A.5: vendor checklist and data terms before a tool receives candidate data
  - POL-04 4.6: approved AI tools only; public chatbots never receive personal information (AI-003)
- **Approved-tools list:** kept by the Operations Manager with POL-04. Today it lists AI-001 (sort-only mode, under the conditions in section 6) and AI-002 (with human review).
- **Scale for a Micro firm:** there is no AI committee. The Owner, the Operations Manager, and the Senior Recruiter review AI use at the monthly security meeting, together with the quarterly bias results.

**How the feature started.** An ATS upgrade in March 2026 added the AI match feature. The Senior Recruiter turned it on on 2026-03-16, accepted the vendor's AI terms by click-through, and set the "smart filter" to hide applicants scoring under 50 on Light Industrial job orders to save screening time. Nobody else knew. There was no review, no bias test, no notice to applicants, and no way for an applicant to ask for a person to look at the application (EV-008, EV-037; P01 R-009, R-010; P03 G-045). The filter was turned off on 2026-07-24, during the risk assessment (EV-042).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Help 3 recruiters work through about 2,600 applications a year by scoring each applicant against the job order (skills, certifications such as a forklift card, shift availability, distance to the worksite) and sorting the list |
| Users | The Senior Recruiter and 2 Recruiters |
| Affected people | Every applicant (about 650 per quarter), and indirectly the clients who receive referrals |
| Data | Inputs: resumes, application answers, work history, certifications, shift availability, and distance. The feature does **not** receive SSNs, Form I-9 data, consumer reports, or the voluntary self-identification answers. Outputs: a 0-100 score and a short match summary |
| Build or buy | Buy: the ATS vendor's feature, run by its AI subprocessor. The vendor's documentation lists the features used (keyword and skill matches, years in similar roles, recency of employment, a penalty for employment gaps over 6 months, distance) but not training data |
| How much it decided (2026-03-16 to 2026-07-24) | 560 applicants applied to Light Industrial job orders; 196 (35%) were hidden by the filter. Recruiters did not open the hidden list. In practice the tool decided who was never seen, which makes it a substantial factor in referral decisions |
| Vendor data terms | The click-through AI terms allow the vendor to use customer data to improve its models unless the customer turns on an opt-out setting, which is off by default. No breach notice or deletion term |
| Not intended | Automatic rejection, automatic advancement, interview scheduling without review, video or voice analysis, personality scoring, and enrichment with third-party data. These vendor features are **off**. Turning any on requires a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Title VII, 42 U.S.C. 2000e-2(a), (b), and (k) | **Yes** | The firm is an employer of its associates and an employment agency when it refers them. Section 703(b) makes it unlawful for an employment agency to "classify or refer for employment any individual" on the basis of a protected trait. Section 703(k) codifies disparate impact: a practice that causes a disparate impact is unlawful unless shown to be job related and consistent with business necessity, or if a less discriminatory alternative is refused. The EEOC states that an employment agency that regularly refers employees to employers is covered "no matter how many employees it has" (eeoc.gov, Coverage of Employment Agencies, read 2026-10-06) |
| ADEA, 29 U.S.C. 623(b) | **Yes** | The same employment agency rule for age (individuals at least 40). Features such as "years since first job" or an employment-gap penalty can act as age proxies |
| ADA, 42 U.S.C. 12112(b)(6) | **Yes** | Selection criteria that screen out or tend to screen out people with disabilities must be job related and consistent with business necessity. Applicants need a way to ask for an accommodation or another process |
| Title VII 704(b), 42 U.S.C. 2000e-3(b) | **Yes (AI-002)** | Job notices and ads may not indicate a prohibited preference; generated ads need review |
| FCRA, 15 U.S.C. 1681b | **Not today** | The feature uses only what applicants give the firm. If third-party data enrichment were turned on, counsel must review it first |
| Fla. Stat. 501.171(2) | **Yes (security)** | The vendor holds applicant personal information (some resumes include driver license numbers), so the firm must take reasonable measures, including vendor terms |
| NYC Local Law 144 (N56-R08) | **No** | No NYC candidates or jobs |
| Colorado SB26-189 | **No** | The firm does not do business in Colorado |
| Florida AI employment law | **None found** | Florida has no statute on AI in hiring decisions |

**Trigger to re-check state laws:** accepting a job order outside Florida, recruiting for remote jobs, or opening an office in another state.

**Federal agency posture, and why it does not change the plan:**
- The EEOC's 2023 technical assistance on adverse impact from software, algorithms, and AI under Title VII is no longer on eeoc.gov (the page returned "not found" on 2026-10-06).
- Executive Order 14281, "Restoring Equality of Opportunity and Meritocracy" (2025-04-23, 90 FR 17537), directs federal agencies to deprioritize disparate-impact enforcement.
- **What has not changed:** 42 U.S.C. 2000e-2(k) is still the statute, and private plaintiffs can still bring disparate impact claims. The Uniform Guidelines on Employee Selection Procedures, including the four-fifths rule at 29 CFR 1607.4(D), remain in the eCFR as of 2026-09-23.

**Decision:** the firm keeps a bias testing program because the statutory duty remains, private claims remain, clients expect fair referrals, and a filter that hides qualified people is also a business problem for a firm that needs every reliable associate it can find. The four-fifths ratio is used **as an internal screening indicator only**, not as a legal standard or safe harbor, together with a significance test.

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why High:** the feature was a substantial factor in an employment decision. Until 2026-07-24 it decided which applicants recruiters ever saw. Even in sort-only mode, the order of a list of 50 applicants strongly shapes who gets called first for a next-morning shift.
- **Minimum controls for High:** human review before action, pre-deployment bias testing, impact assessment (this document), notice to affected people, and ongoing monitoring. All five are in the conditions in section 6.
- **Would re-tier to Medium only if:** the feature becomes a pure search aid with no score or order shown. Not planned.

## 4. MEASURE
Retrospective test on the 560 Light Industrial applicants from 2026-03-16 to 2026-07-24 (EV-051). "Shown" means not hidden by the filter. Sex and race or ethnicity come from the ATS's voluntary self-identification form (325 of 560 answered, 58%), which recruiters cannot see and the feature does not use.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Recruiter review of 60 randomly chosen hidden applicants: how many met the job order's minimum requirements (shift availability, required certification, distance)? Target: under 10% | 23 of 60 (38%) met the minimum requirements. Most had a forklift certification listed in a format the parser missed, or a Spanish-language resume | **No** |
| Safe | Not a physical safety system; the harm is exclusion from work | See fairness | n/a |
| Secure and resilient | Vendor security review; MFA on the ATS; data terms | ATS MFA on; no vendor review; no data use, deletion, or breach terms | **No** |
| Accountable and transparent | Change control; notice to applicants | Filter switched on without approval; applicants not told an automated tool scores them | **No** |
| Explainable and interpretable | Recruiter can see why an applicant scored as they did | Match summary lists matched and missing requirements; the vendor gave a feature-weight sheet on request on 2026-08-19 (EV-050) | Partial |
| Privacy-enhanced | Minimum data; retention; no secondary use | No SSNs or self-ID data sent; model-improvement use not opted out; no deletion term | **No** |
| Fair, with harmful bias managed | Compare shown rates between groups. Flag if a group's rate is below 80% of the highest group's rate **and** the difference is statistically significant (two-proportion z test, p < 0.05). Groups with fewer than 50 applicants are not tested | **Sex:** men 139 of 190 shown (73.2%); women 76 of 135 (56.3%); impact ratio **0.77**, z = 3.2. **Resume language:** English 335 of 496 (67.5%); Spanish or bilingual 29 of 64 (45.3%); ratio **0.67**, z = 3.5. **Race or ethnicity:** White 108 of 148 (73.0%); Hispanic or Latino 70 of 112 (62.5%); ratio 0.86, z = 1.8 (not flagged). Black or African American (41) and other groups were below the testing minimum | **No.** Two disparities flagged |

**Bias findings and causes.** The feature-weight sheet shows that most of the gap by sex comes from the employment-gap penalty and from heavy weight on equipment keywords that appear less often on resumes listing picking and packing work. The Spanish-language gap comes from the parser reading those resumes poorly, which is also the main cause of the validity failure. None of these features is required by the firm's job orders. Removing them is a less discriminatory alternative that should also make the tool more accurate.

**Small numbers.** A firm this size gets few self-identified applicants per quarter. The firm will pool results over two quarters when a group has fewer than 50 applicants, and will treat a large gap in a small group as a reason to look closer, not as proof.

**Age and disability.** The firm does not collect age or disability before an offer, so rates cannot be measured. The vendor confirmed graduation years are not used; the employment-gap penalty is turned off (it can act as a proxy for age, disability, and caregiving). Screen-out risk is managed through human review of every applicant who meets the minimum requirements and the accommodation path (section 5).

**Bias testing plan going forward:**
| Item | Plan |
|---|---|
| Groups | Sex; race or ethnicity (self-ID groups with at least 50 applicants, pooled over two quarters if needed); Spanish-language versus English resumes |
| Metric | Rate of applicants in the top third of the sorted list, and rate of applicants contacted, per job family |
| Threshold | Impact ratio under 0.80 with p < 0.05, or validity agreement under 90% |
| Frequency | Quarterly, and before any settings change |
| Independent review | Outside statistician reviews the method and the 2026 Q4 results (about $700, funded in P01) |
| Records | Results, extracts, and decisions kept at least 4 years |

## 5. MANAGE
**Human-in-the-loop design (smart filter off since 2026-07-24; conditions effective 2026-08-31):**
- The score only sorts the list. Nothing is hidden, rejected, or advanced automatically.
- The recruiter sets the job order's minimum requirements (shift, certification, distance) as filters; every applicant who meets them gets a human review before a referral decision.
- A recruiter who passes over a higher-scored applicant who meets the requirements records a reason in the ATS.
- The employment-gap feature is off and the equipment keyword list is replaced by the certification field (vendor confirmed the change on 2026-08-28, EV-052).
- Spanish-language resumes bypass the score and go to the bilingual Recruiter until the vendor shows at least 90% agreement for them.
- Client requests are recorded as job requirements only. Any client preference tied to a protected trait is refused and reported to the Operations Manager (Title VII 703(b)).

**Notice and accommodation:**
- The career site and each job ad say that an automated tool helps sort applications, that a person reviews every applicant who meets the job's requirements, and how to ask for a person to review an application or for an accommodation (phone, email, or the office).
- Walk-in applications on the lobby tablet or on paper stay available.

**Data protection:**
- Turn on the vendor's opt-out from model improvement now (done 2026-08-28).
- Data use addendum by 2026-10-31: no training on firm data, deletion of applicant data within 30 days after the subscription ends, breach notice within 72 hours, and a yearly SOC 2 report or questionnaire.

**Monitoring:**
- Quarterly bias and validity tests (section 4), reported to the Owner and tracked in R-009.
- Monthly check of the ATS change log for AI settings changes (POL-02 A.10).

**Incident handling:** an unexplained drop in a group's rate, a settings change made without approval, or a vendor security incident follows POL-03 and P08.

**Decommissioning:** stop using the score and fall back to recruiter review alone if the data use addendum is not signed by 2026-10-31, if two consecutive quarters are flagged after the fixes, or if the vendor changes the model without notice.

## 6. Decision
**Approve with conditions (High tier).** Owner, 2026-08-31. The feature may continue in sort-only mode **only if**:
1. The smart filter, automatic rejection, and automatic advancement stay off (filter off 2026-07-24).
2. The employment-gap feature stays off and Spanish-language resumes bypass the score (done 2026-08-28).
3. Applicant notice and the accommodation path are live on the career site and in job ads by 2026-10-15.
4. The vendor data use addendum is signed by 2026-10-31.
5. The 2026 Q4 bias re-test, reviewed by the outside statistician, shows no flagged group by 2026-11-30. If a group is still flagged, the Owner decides between further changes and turning the score off.

Turning any filter back on, or using the score in any other way, needs a new assessment and the Owner's approval.

**AI-002 and AI-003.** A short review checklist for generated job ads (no age, sex, or national origin preferences; accurate pay, shift, and site) is due 2026-10-31. Public chatbots stay prohibited for any personal information (POL-02 C.3).

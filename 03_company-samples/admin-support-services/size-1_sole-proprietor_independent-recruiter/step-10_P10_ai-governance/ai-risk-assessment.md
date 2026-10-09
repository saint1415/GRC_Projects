# AI Use Assessment: ATS AI Match Add-On (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent recruiter, sole proprietorship) |
| Tier / Vertical | Sole Proprietorship / Administrative and Support and Waste Management and Remediation Services |
| AI use case | AI-001: AI resume screening and candidate ranking, the AI match add-on to the ATS (SYS-01). On since 2026-02-02; automatic rejection on for two job orders from 2026-04-06 to 2026-06-26; sort-only since 2026-07-21 |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; AI 600-1 for the generative chatbot (AI-002) |
| Assessor and decision | Owner-recruiter, 2026-08-25; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases), built at intake from the ATS add-on settings and disposition history, the add-on terms and help documentation, the job ads, the chatbot account settings and history, and the bank and card statements (EV-005, EV-006, EV-007, EV-027, EV-017). With no staff, there was no survey to run. Not established: the add-on's feature weights (the full feature list was requested on 2026-07-24), whether either vendor has used the candidate data for training, and group outcomes for the 236 automatic rejections, because the owner collects no demographic data |

## 1. What it does (Map)
The add-on reads each resume, scores the applicant 0-100 against the job order (skills, titles, years of experience, education, location, and, per the vendor's help documentation, employment gaps), and sorts the applicant list. It can also send an automatic rejection email below a chosen score. The owner turned that on for a staff accountant and a help desk analyst job: of 412 applicants, **236 were rejected by the tool with no human review** (EV-005). The vendor's terms let it use customer data to improve its models unless an opt-out setting (off by default) is turned on (EV-005, EV-006). The owner does not collect demographic data, so group outcomes cannot be measured directly.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| Title VII 703(b), 42 U.S.C. 2000e-2(b) | **Yes** | The business is an employment agency: "any person regularly undertaking with or without compensation to procure employees for an employer" (2000e(c)). No headcount test applies to the agency itself, and the EEOC says a recruitment company "is covered no matter how many employees it has." It may not "classify or refer for employment any individual" on a protected basis |
| Title VII 703(k), 42 U.S.C. 2000e-2(k) | **Yes** | A practice with a disparate impact is unlawful unless shown job related and consistent with business necessity, or if a less discriminatory alternative is refused. A score threshold that rejects applicants automatically is a selection practice |
| ADA, 42 U.S.C. 12112(b)(6) | **Yes** | An employment agency is a covered entity (12111(2), (7)). Selection criteria that "screen out or tend to screen out" people with disabilities must be job related; applicants need a way to ask for an accommodation |
| ADEA, 29 U.S.C. 623(b) | **Yes** | Same employment agency rule for age (agency defined in 630(c)). Years-of-experience and gap features can act as age proxies |
| Fla. Stat. 501.171(2) | **Yes (security)** | The vendor holds applicant personal information; reasonable measures include vendor terms |
| NYC Local Law 144 (N56-R08) | **No** | No NYC jobs or candidates for NYC jobs. Re-check, with other states' AI hiring laws, before taking any job order outside Florida or for a remote role |

**Federal posture (as verified for the vertical's Small sample, 2026-09-26):** the EEOC's 2022 and 2023 technical assistance on AI is no longer on eeoc.gov; Executive Order 14281 directs agencies to deprioritize disparate-impact enforcement; and a 2026-06-09 Justice Department Office of Legal Counsel opinion reads Title VII disparate-impact liability narrowly. None of that changes the statutes above, which private plaintiffs can still enforce, or clients' expectation of fair referrals. The owner plans to the statute.

## 3. Risk screen (repository rubric)
**Tier: High.** The tool is a substantial factor in an employment decision: with automatic rejection on, it *was* the decision for 236 people. In sort-only mode it still shapes who gets a call. It stays High until it becomes a pure search aid, which is not planned.

## 4. Data-sharing rules (Govern)
1. No candidate data in any AI tool without this assessment and terms that bar training on that data (POL-01 9.5). The add-on's training opt-out is turned on by 2026-09-30, and the vendor's full feature list (requested 2026-07-24) is kept on file.
2. **AI-002 (consumer chatbot):** no personal data at all. The owner deletes the chat history and turns off training by 2026-09-30, and may use the chatbot only for job ad and message drafts with no names or resumes. Job ads are checked against a fair-wording list before posting (no age, sex, national origin, or disability preferences; Title VII 704(b)).
3. Any client request tied to a protected trait is refused in writing (EEOC: an agency "may not honor discriminatory employer preferences").

## 5. Human review of outputs (Measure and Manage)
- **No automatic rejection, ever.** Turning it back on needs a new assessment (POL-01 4.7).
- The owner sets the job order's minimum requirements as filters and reviews **every applicant who meets them**, whatever the score, and records a reason when passing over a higher-scored applicant.
- The employment-gap feature is turned off if the vendor allows it; if not, the owner ignores the score for applicants whose only shortfall is a gap.
- **Validity spot check each quarter:** the owner reads 20 of the lowest-scored applicants per active job order. If 3 or more meet the minimum requirements, the score is not trusted for that job family until the vendor explains why.
- Job ads say that software helps sort applications and how to ask for a person to review an application or for an accommodation.
- Scores, settings, and rejection lists are kept 3 years (POL-01 8.6).

## 6. Decision: approve with conditions (2026-08-31)
The add-on may stay in **sort-only mode** if, by 2026-10-31 (P01 R-005):
1. The training opt-out is on and the vendor's full feature list is on file (2026-09-30).
2. The notice and accommodation line is in every job ad (2026-09-30).
3. The 236 auto-rejected applicants are re-reviewed against the minimum requirements; those who meet them are told their application was reviewed by a person and invited to similar roles (2026-10-31).
4. The first quarterly spot check is done and recorded (2026-10-31).

If any condition is missed, the score is hidden and the owner reviews applicants unsorted.

# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed staffing and temporary help firm) |
| Tier / Vertical | Mid-Market / Administrative and Support and Waste Management and Remediation Services |
| Scope | Portfolio of 6 AI use cases (AI-001 to AI-006), inventory in `ai-use-case-inventory.csv`. The registry use case, AI resume screening and candidate ranking, is AI-001 and gets the deepest review |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; NIST AI 600-1 (Generative AI Profile) for AI-002, AI-003, and AI-004 |
| Assessors / date | Director of Recruiting Operations (business), vCISO and Security Manager (security), Director of Compliance and Privacy and the General Counsel (privacy and legal), data analysts (testing), 2026-08-24 to 2026-09-15; independent statistician engaged for the 2026 Q4 re-test |
| Decision | Chief Operating Officer, 2026-09-22; High-tier decisions noted by the CEO and reported to the audit committee |

## 1. Summary
Two tools now affect who gets work, and neither was reviewed before it went live (gap 9 in `../00_company-facts.md`):
- **AI-001, resume ranking,** auto-advanced Light Industrial applicants for a year. In 2026 H1, 85% of Light Industrial placements came from its auto-advanced list, and testing found a sex disparity and a Hispanic or Latino disparity.
- **AI-002, the text assistant,** closes applications on knockout answers (lifting, transportation, shifts) with no accommodation path, and works only in English.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | AI resume screening and candidate ranking | High | Approve with conditions; sort-only mode from 2026-09-22 |
| AI-002 | Conversational recruiting assistant (text) | High | Approve with conditions; knockouts route to recruiters by 2026-10-31 |
| AI-003 | Generative drafting of job ads and messages | Medium | Approve with conditions (review checklist) |
| AI-004 | Enterprise generative AI assistant (pilot) | Low | Continue pilot; no Restricted data |
| AI-005 | Timekeeping anomaly flags | Medium | Approve with conditions; no automatic pay changes |
| AI-006 | Face-match clock-in (proposed) | High | **Not approved** |

Tiers: 3 High, 2 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** the Director of Recruiting Operations for recruiting tools and the Director of Payroll and Billing for timekeeping tools, with the vCISO as program lead. Each use case has a business owner in the inventory.
- **Policies:**
  - POL-01 4.13: AI tools that screen, rank, score, or talk to candidates or associates, or affect pay, need approval before use; hiring AI is High tier.
  - POL-01 4.15: changing how an AI tool decides is a controlled change.
  - POL-04 4.10 and 4.11: biometric notice and consent; no Restricted data in unapproved AI tools.
  - POL-05 4.10: AI is a sort aid, never the sole reason to reject.
  - STD-05 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Security Manager on the intranet. Today it lists AI-001 (sort-only), AI-002 (with conditions), AI-003, AI-004 (pilot, no Restricted data), and AI-005. Public chatbots are blocked for firm data.

### 2.1 Lightweight AI governance process
A mid-market firm does not need a large AI committee. It needs a reliable gate and a monthly rhythm that reuse existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Anyone wanting an AI tool, or an AI feature switched on inside an existing tool (including ATS marketplace add-ons), submits a one-page intake: purpose, users, data, vendor, decisions affected | Requesting business owner | 15 minutes |
| 2. Triage | The Security Manager assigns a provisional tier with the repository rubric and checks the purchasing gate (POL-01 4.9) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy, and vendor terms, plus a business reviewer. **High:** full MAP and MEASURE assessment like this one, including bias and validity testing and legal review | Security Manager; Director of Compliance and Privacy; General Counsel | 1, 2, or 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (vCISO, Director of Recruiting Operations, Director of Compliance and Privacy, General Counsel), 30 minutes monthly. High: the group recommends; the COO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owner reports agreed metrics monthly (Medium) or monthly plus a quarterly bias and validity test (High) | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: model change, new feature, new data, a new state or city in the hiring footprint, or a complaint | AI review group | Annual |

**What went wrong before this assessment:** AI-001 and AI-002 were added from the ATS marketplace with click-through terms; the auto-advance setting and the knockout questions were switched on by ATS administrators without review (P01 R-015, R-016, R-046; P07 CM-3).

## 3. MAP
| Item | AI-001 Ranking | AI-002 Text assistant | AI-003 Drafting | AI-004 Assistant | AI-005 Time flags | AI-006 Face match |
|---|---|---|---|---|---|---|
| Purpose | Score and sort applicants against the job order | Pre-screen, answer questions, schedule interviews | Draft job ads and messages | General productivity | Flag unusual punches for review | Confirm identity at clock-in |
| Users | 196 recruiters; 14 Branch Managers | Candidates; recruiters see transcripts | Recruiters | 60 pilot staff | 16 payroll specialists | Associates (proposed) |
| Affected people | About 118,000 applicants a year | About 31,000 conversations in 2026 (to 2026-08-31) | Candidates | None directly | About 3,600 associates a week | Office and Healthcare associates |
| Data | Resumes, applications, work history | Answers, availability, transcripts | Job order details | Internal documents | Punch times, GPS, device | Selfies, face templates |
| Build or buy | Buy (marketplace) | Buy (marketplace) | Buy (ATS feature) | Buy | Buy (vendor feature) | Buy (vendor feature) |
| Generative AI? | No (matching model) | Yes | Yes | Yes | No | No |

**How much AI-001 decided (to 2026-09-22).** Light Industrial applicants scoring 70 or more were auto-advanced to the recruiter queue. In 2026 H1, 85% of Light Industrial placements came from auto-advanced applicants, so applicants below 70 were rarely seen. The tool was a substantial factor in who was referred.

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Title VII, 42 U.S.C. 2000e-2(a), (b), and (k) | **Yes** (AI-001, AI-002, AI-006) | The firm is the employer of its associates and an employment agency when it refers them. Section 703(b) makes it unlawful for an employment agency to classify or refer for employment on the basis of a protected trait. Section 703(k) codifies disparate impact: a practice causing a disparate impact is unlawful unless shown to be job related and consistent with business necessity, or if a less discriminatory alternative is refused |
| ADEA, 29 U.S.C. 623(b) and (e) | **Yes** | Same employment agency rule for age (individuals at least 40); 623(e) bars notices and ads indicating an age preference (AI-003) |
| ADA, 42 U.S.C. 12112(b)(6) | **Yes** (AI-001, AI-002) | Selection criteria that screen out people with disabilities must be job related and consistent with business necessity; knockout questions on lifting and transportation need an accommodation path |
| Title VII 704(b), 42 U.S.C. 2000e-3(b) | **Yes** (AI-002, AI-003) | Job notices may not indicate a prohibited preference |
| FCRA, 15 U.S.C. 1681b | **Not today** | The tools use only information applicants give the firm. Any third-party data enrichment could make a vendor a consumer reporting agency; counsel review is required first |
| Fla. Stat. 501.171(2) | **Yes (security)** | Vendors hold applicant and associate personal information; AI-005 uses geolocation; AI-006 would create biometric data |
| Fla. Stat. 501.702(4) | **Relevant to AI-006** | Defines biometric data, which 501.171 includes in personal information. It names fingerprints but excludes "physical or digital photographs" and "data generated from video or audio recordings". Whether face templates computed from clock-in selfies are biometric data is **unsettled**; counsel to confirm. The firm treats them as biometric data. (The Florida Digital Bill of Rights itself does not apply: a controller must exceed $1 billion in global gross annual revenue and meet an online-advertising, smart-speaker, or app-store test, and the firm meets none.) |
| NYC Local Law 144 (N56-R08) | **No** | No NYC candidates, jobs, or offices |
| Colorado SB26-189 | **No** | Effective 2027-01-01 for consequential decisions made on or after that date; it applies to a "deployer," defined as a person doing business in Colorado. The firm hires only for Florida worksites and does not do business in Colorado |
| Other state AI hiring laws (for example Illinois and California) | **No** | No employees, jobs, or operations in those states |

**Trigger to re-check:** accepting job orders outside Florida, recruiting for remote jobs, or a PE add-on acquisition in another state.

**Federal agency posture, and why it does not change the plan:**
- Executive Order 14281 (2025-04-23) directs agencies to deprioritize disparate-impact enforcement.
- On **2026-06-09 the Justice Department's Office of Legal Counsel** issued an opinion to the EEOC Chair, "Constitutionality of Disparate-Impact Liability Under Title VII," concluding that the EEOC's Title VII guidelines are unconstitutional insofar as they contemplate liability based on disparate effects alone, and that the business necessity defense requires only that a practice rationally serve a valid business purpose. OPM then removed references to the Uniform Guidelines on Employee Selection Procedures (UGESP) from federal personnel rules (91 FR 48234, 2026-07-31).
- The EEOC rescinded its affirmative action guidelines (91 FR 40879, 2026-07-06) and on 2026-07-23 **proposed** removing the EEO-1 to EEO-6 reports (91 FR 46332). The proposal is not current law.
- **What has not changed:** 42 U.S.C. 2000e-2(k) is still the statute. An OLC opinion binds executive agencies, not courts or private plaintiffs. UGESP (29 CFR Part 1607, including the four-fifths rule at 1607.4(D)) is still in the eCFR.

**Decision:** the firm keeps a bias testing program because the statute and private claims remain, MSP and hospital clients expect fair referrals, and a tool that hides qualified applicants is a business problem. The four-fifths ratio is used **as an internal screening indicator only**, not as a legal standard or safe harbor, together with a significance test and a review of which features drive any difference.

## 4. Risk tiers
Tiers use the repository rubric (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **AI-001 High:** a substantial factor in an employment decision (referral). Even in sort-only mode, ranking strongly shapes who is called.
- **AI-002 High:** knockout answers ended applications automatically.
- **AI-006 High:** would gate pay-relevant attendance on a biometric match.
- **AI-003 Medium** and **AI-005 Medium:** influence decisions or communications about individuals, but a person decides.
- **AI-004 Low:** internal productivity with no decisions about individuals and no Restricted data.

**Re-tier triggers:** AI-001 drops to Medium only if it becomes a pure search aid with no score or order shown. AI-005 rises to High if flags ever change pay without review.

## 5. MEASURE
### 5.1 AI-001 resume ranking (retrospective, 2026 H1)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Recruiter review of 200 random applicants per division: does the score agree with the job order's minimum requirements? Target at least 90% | Light Industrial 83%; Office and Professional 91%. Most misses were forklift and equipment certifications in non-standard formats and Spanish-language resumes | **No** for Light Industrial |
| Secure and resilient | Vendor security review; access through ATS SSO; data use terms | No review; marketplace terms; the ATS SOC 2 report excludes marketplace add-ons (P09) | **No** |
| Accountable and transparent | Change control; applicant notice | Auto-advance enabled without approval; no notice | **No** |
| Explainable and interpretable | Can a recruiter see why an applicant scored as they did? | Match summary lists matched and missing requirements; vendor provided feature weights on request (2026-08-28) | Partial |
| Privacy-enhanced | Minimum data; retention; no secondary use | No SSNs or self-ID data; vendor keeps resumes for the subscription term; training on firm data not excluded | **No** |
| Fair, with harmful bias managed | Auto-advance rate by group (voluntary self-identification, 61% response). Flag if a group's rate is below 80% of the highest group's rate **and** the difference is statistically significant (two-proportion z test, p < 0.05) | **Light Industrial, sex:** men 6,920 of 15,200 advanced (45.5%); women 2,950 of 8,400 (35.1%); impact ratio **0.77**, z = 15.5. **Light Industrial, race or ethnicity:** White 3,100 of 7,000 (44.3%); Black 2,560 of 6,400 (40.0%), ratio 0.90, z = 5.0 (significant but above 0.80: monitored, not flagged); Hispanic or Latino 2,750 of 7,900 (34.8%), ratio **0.79**, z = 11.8. Groups under 100 self-identified applicants were not tested. **Office and Professional, sex:** women 1,420 of 3,010 (47.2%); men 1,300 of 2,840 (45.8%), ratio 0.97, z = 1.1 (not flagged) | **No.** Two disparities flagged |

**Bias causes.** The vendor's feature weights show that most of the Light Industrial sex gap comes from a penalty for employment gaps longer than 6 months and from heavy weight on equipment keywords that appear less often on resumes listing picking and packing roles. The Hispanic or Latino gap tracks the parser's poor reading of Spanish-language resumes (the same cause as the validity miss). None of these features is required by the job orders, so removing them is a less discriminatory alternative that also improves validity.

**Age.** The firm does not collect age before an offer. The vendor confirmed that graduation dates and "years since first job" are not used, and the firm capped experience credit at 5 years.

### 5.2 AI-002 text assistant (2026-02-02 to 2026-08-31)
| Test | Result | Pass? |
|---|---|---|
| Knockout effect | 22% of about 31,000 conversations ended on a knockout answer: lifting 41%, transportation 33%, shift availability 26%. Applications were closed with no recruiter review | **No** (automatic rejection; possible screen-out of people with disabilities) |
| Accommodation path | No offer of an accommodation, phone call, or alternative in the script | **No** |
| Language | Completion rate: English-preferring applicants 20,400 of 25,200 (81.0%); Spanish-preferring applicants 3,360 of 5,800 (57.9%); ratio 0.72, z = 37.4 | **No** (language is not a protected trait itself, but the gap risks national origin disparity) |
| Accuracy of answers (generative part) | Review of 100 transcripts: 4 gave wrong pay or shift information | Partial |
| Security and privacy | Transcripts kept by the vendor indefinitely; no data use terms | **No** |

### 5.3 Other use cases
- **AI-003:** review of 50 generated job ads found 3 with "recent graduates preferred" language (age preference risk under 29 U.S.C. 623(e)); all were edited before posting by luck rather than by checklist.
- **AI-004:** pilot users reviewed; data loss rules block Restricted data types; no incidents.
- **AI-005:** sample of 50 flags from 2026-07: 31 were explained by GPS drift at 2 large distribution centers; 3 punches had been deleted by on-site coordinators without client confirmation (possible unpaid time). No automatic deduction exists, but the review is not documented.
- **AI-006:** not deployed. The vendor could not provide match error rates by skin tone or age group.

**Bias and validity testing plan going forward (AI-001 and AI-002):**
| Item | Plan |
|---|---|
| Groups | Sex; race or ethnicity (groups with at least 100 self-identified applicants in the quarter); Spanish- vs English-preferring applicants |
| Metrics | AI-001: rate placed in the top third of the sorted list, and rate contacted. AI-002: completion rate, and rate routed to recruiters after a knockout answer who are later hired |
| Threshold | Impact ratio under 0.80 with p < 0.05, or validity agreement under 90% |
| Frequency | Quarterly, and before any settings or model change |
| Independent review | Outside statistician reviews the method and the 2026 Q4 results (funded, $35,000 a year) |
| Records | Results, extracts, and decisions kept at least 4 years |

## 6. MANAGE
**AI-001 (effective 2026-09-22):**
- Auto-advance is off; the score only sorts the list.
- Minimum requirements (shift, certification, distance) are filters set by the recruiter, not by the model; every applicant who meets them gets a human review before a referral decision.
- Recruiters record a reason when they pass over a higher-scored applicant, and when they reject an applicant who meets the minimum requirements.
- The employment-gap feature is disabled and equipment keywords are replaced by the certification field (vendor change due 2026-10-15).
- Spanish-language resumes bypass the score and go to a bilingual recruiter until the vendor shows at least 90% agreement for them.
- Client requests are entered as job requirements only. Any client preference tied to a protected trait is refused and reported to the Director of Compliance and Privacy (Title VII 703(b)).

**AI-002 (by 2026-10-31, Spanish flow by 2026-12-31):**
- Knockout answers route to a recruiter; the assistant never closes an application.
- Every conversation offers a phone call and states how to ask for an accommodation.
- Lifting and transportation questions are rewritten as "can you perform this with or without accommodation" and asked only for job orders that require them.
- A Spanish-language flow, with the same review.
- Transcripts kept 2 years (firm choice), then deleted by the vendor.

**AI-003:** review checklist (no age, sex, or national origin preferences; accurate pay and shift) before posting, by 2026-10-31.

**AI-005:** flags are a review queue only; any punch change needs client supervisor confirmation and a recorded reason; monthly report of deleted or edited punches to the Director of Payroll and Billing (POAM-021 second review).

**Notice and accommodation:** the career site, job ads, and the text assistant say that automated tools help sort and pre-screen applications, that a person reviews every qualified applicant, and how to ask for a person or an accommodation (live by 2026-10-31, POAM-015).

**Vendor controls:** data use and security addenda for the AI-001 and AI-002 vendors by 2026-12-31: no training on firm data without written approval, deletion 30 days after the subscription ends, breach notice within 72 hours, and annual SOC 2 or questionnaire (P01 R-017; POAM-017).

**Incident handling:** an unexplained drop in a group's rate, a settings change without approval, or a vendor security incident follows P08 and POL-03.

**Decommissioning:** stop using a High-tier tool and fall back to recruiter review if its vendor addendum is not signed by 2026-12-31, if two consecutive quarters are flagged after the fixes, or if the vendor changes the model without notice.

## 7. Decision
**COO, 2026-09-22:**
1. **AI-001: approve with conditions (High).** Sort-only mode stays on; the gap feature stays disabled; Spanish resumes bypass the score; notice live by 2026-10-31; the 2026 Q4 re-test, reviewed by the outside statistician, shows no flagged group by 2026-11-30, or the COO decides between further changes and switching the score off.
2. **AI-002: approve with conditions (High).** Knockout routing and the accommodation offer live by 2026-10-31, or the assistant stops asking knockout questions; Spanish flow by 2026-12-31.
3. **AI-003: approve with conditions (Medium).** Checklist by 2026-10-31.
4. **AI-004: continue the Low-tier pilot;** expansion decision 2026-12-31.
5. **AI-005: approve with conditions (Medium).** Documented review of flags and punch edits from 2026-11-30.
6. **AI-006: not approved.** It may be reconsidered only with counsel's view on biometric status, written notice and consent with an alternative method, vendor error rates by group with a firm validation test, and template retention and breach terms.

Turning auto-advance back on, letting AI-002 reject applicants, or deploying any of these tools for jobs outside Florida needs a new assessment and COO approval. All conditions are tracked as POAM-024 (P07).

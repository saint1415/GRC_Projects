# AI Governance Risk Assessment: Enterprise AI Portfolio, Admissions Scoring, and Student-Success Risk Scoring

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded postsecondary education company; operates the College; campuses in six states and online students in all 50 states and DC) |
| Tier / Vertical | Enterprise / Educational Services |
| Scope | Enterprise AI portfolio (16 use cases in `ai-use-case-inventory.csv`), with a full assessment of the registry use case, split into its two inventory items: AI-002 admissions inquiry and applicant scoring and AI-003 student-success risk scoring (section 7) |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for the six generative use cases; repository risk tier rubric |
| Assessor / date | GRC team with the Chief Data and Analytics Officer's data science team, presented to the AI governance committee at its meeting of 2026-08-25 |
| Decision | Executive risk committee, 2026-09-10 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 16 |
| Risk tier | High 6, Medium 7, Low 3 |
| Status | In production 12, Pilot 3, Proposed 1 |
| Committee review complete | 10 of 16 |
| Not yet reviewed | 6: AI-002, AI-010, AI-012, AI-013, AI-014, AI-016 (reviews due 2026-11-30, AI-002 by 2026-12-15; POAM-019) |
| High-tier use cases not yet reviewed | 4: AI-002 (in production), AI-010 (pilot), AI-012 (being switched off), AI-013 (proposed) |
| Use cases exposed to Colorado SB26-189 or the California ADMT rules from 2027-01-01 | 6 likely (AI-002, AI-004, AI-006, AI-010, AI-012, AI-013); 1 possible (AI-003) |
| Use cases that use FAFSA-derived data outside aid administration | 2 (AI-003, AI-011; removal due 2026-11-30, POAM-004) |

**Main findings:**
1. The admissions scoring feature (AI-002) was switched on inside the CRM on 2026-03-02 through tenant configuration, with no committee review, no local fairness test, and no applicant notice. Until 2026-08-26, inquiries that scored under 20 received no advisor call. A first local test shows Black applicants and applicants aged 50 and older landed in that band at rates above the fairness threshold (section 7.4).
2. The student-success model (AI-003) took four ISIR-derived fields as features in its January 2026 refresh without a re-review. That breaks the HEA section 483 limit on FAFSA data (P03 G-059) and drives a flag-rate disparity for Pell recipients.
3. Six use cases have not been reviewed, because AI features arrive inside SaaS products the company already licenses. The intake block that stops this is not yet in place (P04 CM-7 row; POAM-019).
4. From 2027-01-01, Colorado SB26-189 and the California CPPA ADMT rules attach notice, explanation, and human review duties to AI used in education and employment decisions. The company is not ready for them (section 5).

These findings map to enterprise risk ER-08 (responsible use of AI and student data) in P01, which is outside tolerance only because of R-014 (AI-002).

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to ER-08, which the board risk committee reviews quarterly with the other enterprise risks (P01 section 8).

**Members:** Provost and Chief Academic Officer (chair); Chief Privacy Officer; CISO; Chief Data and Analytics Officer; Chief Compliance Officer; a General Counsel delegate; Vice President, Enrollment; Vice President, Student Success; Vice President, Financial Aid; Chief Human Resources Officer (for workforce tools); a faculty senate representative; and a student government representative. Internal Audit attends as an observer and does not vote, so it can assess the committee independently (P07).

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Local validation and fairness testing on the College's own data; impact assessment; human review design with an appeal path; notice to affected people; monitoring plan; state ADMT readiness check |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review (vendor school-official and Safeguards Rule terms) |
| Low | Committee chair (fast track) | Listing on the approved AI tools list (STD-05.3); data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including an AI feature switched on inside an existing vendor product, must be registered before use (POL-05 4.6; STD-05.3). Any new use of student data for AI must also be approved by the Chief Privacy Officer and recorded in the data use register (POL-04 4.5). The GRC team owns the inventory. **Gap:** procurement and SaaS change management do not yet block AI features without an inventory ID; this is due 2026-11-30 (POAM-019).

**Policies that apply:**
- POL-01 4.3: a new AI feature that uses student data is a material change that triggers a risk assessment update.
- POL-04 4.3: FAFSA data and federal tax information, including ISIR-derived fields, must not be copied to analytics, marketing, or AI systems.
- POL-04 4.5: new uses of student data for AI need Chief Privacy Officer approval and a data use register entry.
- POL-04 4.10: no Restricted data in an AI tool unless the committee approved the use case and the contract prohibits training on company data.
- POL-05 4.6: only tools on the approved AI tools list (STD-05.3).
- POL-05 4.8: AI scores about applicants or students may be used only to prioritize supportive contact, never as the sole basis for a decision about admission, aid, academic standing, or discipline, and never to discourage enrollment or limit a service.

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier use case; annual re-review of every use case; a re-review after any model refresh that adds or changes inputs.

**Why 6 use cases lack review.** AI-002, AI-010, and AI-012 arrived as features inside the CRM, SIS, and LMS and were switched on through tenant settings. AI-014 and AI-016 are Low-tier tools that teams started using before asking for the fast-track review. AI-013 is a proposed HR feature, correctly held for review. The committee set review dates for all six (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FERPA, 34 CFR Part 99 (N61-R01) | Yes, for every use case with education records | Advisors and staff may use AI outputs as school officials with a legitimate educational interest (99.31(a)(1)(i)(A)), limited by reasonable methods (99.31(a)(1)(ii)). AI vendors are school officials only if they are under the College's direct control for use of the records (99.31(a)(1)(i)(B)). The FERPA annual notice does not yet describe AI vendors as school officials (P03 G-048; POAM-021) |
| HEA section 483 limits on FAFSA data (FSA Handbook) | Yes, for AI-003 and AI-011 | FAFSA data may be used only for the application, award, and administration of aid. ISIR-derived fields in the data platform must be removed (P03 G-059; POAM-004) |
| FTC Safeguards Rule, 16 CFR Part 314 (N61-R02) | Yes, for vendors that touch customer information | AI vendors are service providers under 314.4(f); a new AI use of customer information is a material change for the risk assessment (314.4(b)(2)) |
| Federal civil rights laws for recipients of federal financial assistance: Title VI, Title IX, Section 504, Age Discrimination Act | Yes | Title IV participation brings these laws into play. Federal disparate-impact enforcement has been deprioritized (EO 14281, see `00_universal-framework/cross-sector/`), but the company tests outcomes by group anyway because unequal treatment of applicants and students is the harm it wants to avoid, and state ADMT laws apply from 2027-01-01 |
| Colorado SB26-189 (C.R.S. 6-1-1701 to -1709, as reenacted) | From 2027-01-01 | Signed 2026-05-14. Covers deployers doing business in Colorado whose covered ADMT materially influences consequential decisions, including education and employment, for decisions made on or after 2027-01-01. The signed act has no small-business exemption. The online division enrolls Colorado residents. The act lists a FERPA-related carve-out; counsel is confirming how it applies to the College (P03 G-079). Attorney general rules are due by 2027-01-01 and have not been confirmed as adopted |
| California CPPA ADMT regulations (Cal. Code Regs. tit. 11, sec. 7200 et seq.) | From 2027-01-01 | CCPA businesses using ADMT for significant decisions, including education and employment, must comply by 2027-01-01 (pre-use notice, opt-out with exceptions, access rights, risk assessment). The company is a for-profit business with California online students; counsel is confirming how the CCPA's exemptions apply to its GLBA and FERPA data (P03 G-080) |
| Texas Responsible AI Governance Act (HB 149) | Yes (campuses in Texas) | Effective 2026-01-01. Intent-based prohibitions apply to all deployers (for example, AI developed with intent to unlawfully discriminate). Its disclosure duties fall on government agencies and health care service providers, not on the College. The AI policy already prohibits the intended uses it bans |
| Utah AI Policy Act (as amended) | Yes, for generative assistants used by Utah residents | Generative AI in consumer transactions must disclose when clearly asked; disclosure at the outset is a safe harbor. AI-001 and AI-008 disclose at the start of every conversation |
| State AI employment rules (for example, Illinois HB 3773; California Civil Rights Council ADS regulations) | Possibly, for AI-013 | Adjunct faculty applicants live in many states. Counsel confirms which rules apply before AI-013 is enabled; it is not enabled today |
| FTC Act Section 5 | Yes | Accuracy of AI-assisted claims to prospective students (AI-001) and of vendor claims the company relies on |
| ED AI grant priority (91 FR 18774) and ED Dear Colleague Letter on AI and grant funds (July 22, 2025) | No | Both concern ED grant funds. No ED discretionary grant funds pay for these use cases. Their responsible-use principles are used as guidance only |
| Federal preemption efforts (EO 14365; FTC proposed AI-accuracy policy statement) | Watch only | The executive order does not itself preempt any state law, and the FTC statement is proposed only. The company plans to comply with the state laws as enacted |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person (here, education or employment) or able to affect physical safety.

| ID | Use case | Tier | Status | Committee review | Consequential decision category |
|---|---|---|---|---|---|
| AI-001 | Generative AI virtual assistant answering prospective students' program, cost, and admissions questions on the website and in the CRM chat | Medium | In production | Reviewed 2025-11-18; re-checked 2026-08-25 | None (answers questions; hands off to an enrollment advisor; no scoring) |
| AI-002 | Admissions inquiry and applicant scoring | High | In production (enabled 2026-03-02 through CRM tenant configuration) | Not reviewed before enablement; interim decision 2026-08-25 (section 9); full review due 2026-12-15 (POAM-019) | Education (who receives advisor contact and how fast) |
| AI-003 | Student-success risk scoring | Medium | In production (all students; about 1,700 advisors) | Reviewed 2025-10-21; 2026-01 model refresh added ISIR-derived features without re-review; re-reviewed 2026-08-25 | None directly (routes supportive outreach); becomes Education if used for admission, aid, standing, or placement |
| AI-004 | Online proctoring behavior flagging: flags possible misconduct in webcam-proctored exams for instructor review | High | In production (about 410,000 proctored exams a year) | Reviewed 2026-02-17 | Education (academic integrity outcomes) |
| AI-005 | Generative AI teaching assistant inside the LMS that answers course questions from approved course materials | Medium | Pilot (40 College courses; not offered to SL-2 partners) | Reviewed 2026-05-12 | None (learning support; does not grade) |
| AI-006 | Application fraud scoring that flags likely synthetic identities ("ghost students") in online applications for identity verification | High | In production (1.8% of 2026 online applications flagged) | Reviewed 2026-06-23 | Education (enrollment and Title IV aid can be held pending identity verification) |
| AI-007 | Financial aid document processing: extracts and classifies fields from uploaded verification documents for aid staff | Medium | In production | Reviewed 2025-09-30 | None (staff verify every extracted field before packaging) |
| AI-008 | Student support center virtual agent and agent-assist for 24x7 technical and account help, including SL-2 partner students | Medium | In production | Reviewed 2026-01-27 | None (no account changes; escalates to staff) |
| AI-009 | Enterprise generative AI assistant for workforce productivity (drafting, summarizing, search) | Medium | In production (about 9,000 licensed users) | Reviewed 2025-12-09 | None |
| AI-010 | Transfer credit evaluation suggestions that match incoming transcripts to College course equivalencies | High | Pilot (2 evaluator teams since 2026-06) | Not reviewed (intake received 2026-07-20; review due 2026-11-30; required before expansion) | Education (credits awarded affect time and cost to degree) |
| AI-011 | Enrollment marketing audience modeling for digital advertising | Medium | In production | Reviewed 2025-11-18; re-review due after ISIR fields are removed (2026-11-30) | None (advertising reach; no decision about an applicant) |
| AI-012 | AI writing-detection score shown to faculty in the LMS for submitted assignments | High | In production (faculty-visible; being switched off) | Not reviewed (decision 2026-08-25 to switch off; no review needed unless re-enabled) | Education (academic integrity outcomes) while scores are visible |
| AI-013 | Resume screening and ranking for adjunct faculty and staff recruiting | High | Proposed (feature not enabled) | Not reviewed (review due 2026-11-30; required before any use) | Employment |
| AI-014 | Generative AI drafting of course outlines, quiz items, and media scripts by instructional designers (College and SL-2) | Low | In production (instructional design team) | Not reviewed (fast-track review by the committee chair due 2026-11-30) | None |
| AI-015 | SOC alert triage assistant that summarizes and prioritizes alerts | Low | In production | Reviewed 2026-03-10 | None |
| AI-016 | Coding assistant for company software engineers (student portal, SL-1 portal, integration code) | Low | Pilot (60 engineers) | Not reviewed (fast-track review by the committee chair due 2026-11-30) | None |

**Tiering notes:**
- **AI-003 stays Medium** because the score routes supportive outreach only and an advisor decides every contact. It re-tiers to High if it is used in any decision about admission, aid, academic standing, probation, dismissal, or placement, or if it triggers automatic holds or messages.
- **AI-004 is High** because proctoring flags feed academic integrity outcomes that affect grades and standing, even though staff review every flag.
- **AI-006 is High** because a flag can hold enrollment and Title IV aid until the applicant verifies identity.
- **AI-010 is High** because evaluators accept about 92% of its suggestions, which makes it a substantial factor in the credits a student receives.
- **AI-009 is Medium rather than Low** because Restricted data is allowed in its approved tenant.

## 5. State ADMT readiness (from 2027-01-01)
The duties below are summarized from the cross-sector file for Colorado SB26-189 (deployer duties) and the California CPPA ADMT rules. Counsel confirms the final scope after the Colorado attorney general's rules are adopted.

| Duty | Colorado SB26-189 | California ADMT | Readiness today | Plan |
|---|---|---|---|---|
| Notice before or at the point of use | Yes | Pre-use notice | Not ready: no applicant notice for AI-002; no student notice for AI-003 or AI-004 | Notices for AI-002, AI-003, and AI-004 drafted with counsel by 2026-12-15 |
| Explanation after an adverse outcome | Yes | Access rights to information about the ADMT | Not ready: AI-002 gives no reason codes | Vendor reason codes requested; explanation letter template by 2026-12-15 |
| Access and correction of data | Yes | Access rights | Partly ready: FERPA access and amendment processes cover students, not inquiries | Extend the request process to inquiries and applicants |
| Meaningful human review or reconsideration | Yes | Opt-out, with exceptions such as a human appeal | Partly ready: human review exists for AI-004 and AI-006; no appeal path for AI-002 | Appeal path for AI-002 by 2026-12-15 (POAM-019) |
| Risk assessment and records | 3-year records | Risk assessment | Partly ready: this assessment; records retention for AI decisions not set | Add AI decision records to the retention schedule (POAM-010) |

**Fallback:** if a High-tier use case is not ready by 2026-12-31, it is switched off for Colorado and California residents, or for everyone if the systems cannot separate them, until it is.

## 6. MEASURE: portfolio testing gaps
| Gap | Use cases | Plan |
|---|---|---|
| No local fairness test before production | AI-002 | Full local test by 2026-12-15 (section 7.5) |
| Fairness last tested on 2025 data, before the ISIR-derived features were added | AI-003 | Retest after retraining, by 2027-01-31 |
| Local test found a face-detection disparity; mitigation added but not yet retested | AI-004 | Retest by 2027-01-31 |
| Age 50+ flag-rate ratio of 1.31, above the 1.25 threshold | AI-006 | Review the device and network signals; retest by 2027-01-31 |
| No group analysis of generative assistant answers | AI-001, AI-005, AI-008 | Add language and disability-accommodation views to transcript sampling by 2027-03-31 |
| No testing before pilot | AI-010 | Pre-expansion test by prior institution type before committee review |

**Data used for fairness tests.** Race and ethnicity come from the self-reported fields collected for federal IPEDS reporting. They are used only for testing, never as model inputs, and the test data set is restricted to the data science team and deleted after each test cycle. Inquiries do not report race, so AI-002 inquiry-level tests use age band and home ZIP code characteristics, and applicant-level tests use the self-reported fields.

## 7. Full assessment: AI-002 admissions scoring and AI-003 student-success risk scoring
### 7.1 MAP
| Item | AI-002 admissions inquiry and applicant scoring | AI-003 student-success risk scoring |
|---|---|---|
| Purpose and intended use | Order enrollment advisors' work so likely enrollees are contacted first | Identify enrolled students who may withdraw or fail so an advisor can offer help (tutoring, schedule changes, emergency aid referral) |
| Users / operators | 2,100 enrollment advisors; enrollment marketing operations (configuration) | About 1,700 academic and student success advisors; the data science team (model owner) |
| Affected people | About 1.6 million inquirers a year and all applicants, including Colorado and California residents | About 285,000 enrolled students |
| Data | **Inputs:** inquiry source, program of interest, engagement, home ZIP code, age band, prior education, military affiliation, employer sponsorship, device type. **Training:** the vendor's pooled model across its clients, calibrated on 3 years of College inquiries. **Output:** a 0-100 score; until 2026-08-26, scores under 20 went to automated email only | **Inputs:** LMS logins and submissions, grades, credits, transfer credits, account holds, age, modality, program, and four ISIR-derived fields (Pell eligibility, aid index band, dependency status, first-generation status). **Training:** 4 years of College outcomes. **Output:** weekly score, a band, and the top 3 factors shown in the advising tool |
| Build or buy | Configure: a CRM vendor feature (SYS-06); the vendor's SOC 2 report covers the CRM | Build: company model on the Cloud provider B machine learning platform (SYS-07); model changes go through committee review and change control (P04 CM-3 row) |
| Not intended | Admission decisions (staff decide against published criteria; the score is not shown on the admission decision screen); aid; pricing | Admission, aid, academic standing, probation, dismissal, grades, or placement; any automated action on a student |

### 7.2 Applicable rules for these two use cases
Section 3 applies. The points that matter most:
- **AI-002:** inquirers are not yet students, so FERPA does not cover inquiry data until a student is in attendance. The vendor contract lets the vendor use de-identified College inquiry data to improve its pooled model; matriculated students' data must be excluded under FERPA direct control (99.31(a)(1)(i)(B)). Colorado SB26-189 and the California ADMT rules are the main new duties.
- **AI-003:** advisors see scores as school officials, but today every advisor can see every student's score, which is broader than reasonable methods allow (99.31(a)(1)(ii); P07 AC-6; POAM-003). The ISIR-derived inputs break the HEA section 483 limit (G-059).

### 7.3 Risk tier
- **AI-002: High.** Ranking inquiries and applicants decides who gets an advisor's time, and routing low scores to email only removed human contact altogether. That is a substantial factor in access to education.
- **AI-003: Medium** (section 4), with the escalation triggers listed there.

### 7.4 MEASURE
**AI-002** (local test on inquiries and applications from 2026-03-02 to 2026-07-31: 655,000 scored inquiries; 118,000 applications)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Area under the curve for enrollment within 90 days of 0.70 or higher on College data | 0.71 locally (vendor stated 0.78 on pooled data) | **Yes**, narrowly |
| Safe | No applicant is denied human contact because of the score | 7.4% of applicants were routed to email only with no advisor call until 2026-08-26 | **No** |
| Secure and resilient | Vendor SOC 2 reviewed; AI features changed only through change control | SOC 2 reviewed (P03 G-032); feature switched on without change control (P04 CM-7 row) | Partial |
| Accountable and transparent | Named owner; committee review; applicant notice | Owner named 2026-08; no review; no notice | **No** |
| Explainable and interpretable | Reason codes for each score | Score only; vendor offers reason codes in a higher license tier | **No** |
| Privacy-enhanced | No matriculated student data in the pooled model; data minimized | Contract silent on matriculated data; inputs do not include aid data | Partial |
| Fair, with harmful bias managed | Share of applicants in the email-only band, by group, as a ratio to the reference group (threshold 0.8 to 1.25) | Black applicants 1.47 (white reference); Hispanic applicants 1.18; age 50+ 1.36 (age 25 to 34 reference); women 0.97 (men reference) | **No.** Two disparities flagged |

**Bias finding (AI-002).** The disparities trace mainly to home ZIP code and device type, which act as proxies for race and income, and to email engagement, which is lower among older inquirers. The test is preliminary (vendor reason codes were not available), but the ratios are large enough to stop email-only routing at once.

**AI-003** (spring 2026 session: 271,000 scored students)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | High band against actual withdrawal or a failing grade: recall of 60% or more and precision of 35% or more | Recall 64%; precision 38% | **Yes** |
| Safe | Sample of 100 advisor notes for any use of the score to discourage enrollment or limit services (POL-05 4.8) | 2 of 100 notes suggested the student "consider pausing enrollment" and cited the score | **No** |
| Secure and resilient | Model registry and change control; committee re-review after input changes | Registry in place; January 2026 refresh added features without re-review | Partial |
| Accountable and transparent | Named owner; student notice; FERPA annual notice describes AI vendors and uses | Owner named; no student notice; FERPA notice silent (POAM-021) | **No** |
| Explainable and interpretable | Advisors see the top 3 factors and can explain them | Available; 18 of 20 interviewed advisors described the factors correctly | Yes |
| Privacy-enhanced | No FAFSA-derived inputs; scores visible only to a student's assigned advisors | Four ISIR-derived inputs; all advisors can see all scores | **No** |
| Fair, with harmful bias managed | Flag-rate ratio 0.8 to 1.25; false positive rate difference of 10 points or less; recall within 10 points of overall | Black students 1.42 flag-rate ratio (white reference); Pell recipients 1.58 (non-recipients reference); online students' false positive rate 19% vs 12% on campus (7 points, within threshold); recall within 6 points for all groups | **No.** Two disparities flagged |

**Bias finding (AI-003).** The Pell and race disparities trace mainly to the ISIR-derived fields, which must be removed anyway, and to LMS login counts, which penalize online students who work in longer, less frequent sessions.

### 7.5 Bias testing plan (both use cases)
| Element | Plan |
|---|---|
| Groups compared | Race and ethnicity (self-reported, IPEDS fields); sex; age band (under 25, 25 to 34, 35 to 49, 50 and older); modality (online, campus); Pell status for AI-003 outcomes only (not as an input); state of residence for AI-002 |
| Metrics | (1) Flag-rate ratio (AI-002: share in the lowest band; AI-003: share in the High band). (2) False positive rate difference (AI-003). (3) Recall by group (AI-003). (4) Advisor contact within 48 hours, as a ratio by group (AI-002) |
| Thresholds | Flag-rate ratio between 0.8 and 1.25; false positive rate difference of 10 points or less; recall within 10 points of overall; contact-rate ratio of 0.9 or more. Any breach needs a documented review by the committee |
| Small groups | Report counts with every rate; pool groups under 100 across sessions before a pass or fail decision; never publish results for groups under 10 |
| Frequency and owner | Before production or expansion, after every model or input change, and each session (AI-003) or quarter (AI-002). Run by the data science team; reviewed by the committee and the Chief Compliance Officer |
| Action on failure | Remove or replace the proxy input and retest; recalibrate thresholds by group only if counsel agrees it is lawful; switch off if two consecutive tests fail |

### 7.6 MANAGE
**Human-in-the-loop design:**
- AI-002: every inquiry gets an advisor contact attempt within 2 business days regardless of score (in place since 2026-08-26). The score may only order the queue. Advisors may contact any inquiry at any time. Applicants can ask for human review of how they were handled through the appeal path due 2026-12-15.
- AI-003: the score is a prompt for outreach, never a decision. Advisors choose whether and how to reach out, record overrides, and may contact any student. Outreach must offer help and never discourage enrollment or limit a service (POL-05 4.8). Advisor retraining on this rule by 2026-10-31.

**Transparency:**
- Applicant notice on inquiry forms and the application, explaining that a model helps order advisor follow-up, what it uses, and how to ask for human review (by 2026-12-15).
- Student notice in the portal and catalog for AI-003 and AI-004, and the FERPA annual notice updated to describe AI vendors as school officials (POAM-021).

**Monitoring:**
- AI-002: weekly contact-within-48-hours rate by group; quarterly fairness test; KRI for R-014.
- AI-003: session-end validity and fairness report; monthly sample of 100 advisor notes; KRI for R-015.
- Both feed the quarterly ER-08 report to the board risk committee.

**Incident handling:** misuse of a score (for example, discouraging enrollment) is a policy violation handled under the sanctions procedure (PRC-01.1). A vendor security incident, or exposure of student data through an AI system, follows the P08 runbook and the vendor's contract notice terms. A fairness threshold breach in production is logged as an AI incident and reviewed by the committee within 30 days.

**Decommissioning:**
- AI-002: switched off if the fairness thresholds are not met by 2026-12-31, if the vendor will not exclude matriculated students' data from its pooled model, or if two consecutive quarterly tests fail.
- AI-003: switched off if retraining without ISIR-derived fields is not complete by 2026-11-30, or if two consecutive sessions fail the validity or fairness thresholds. Stored scores are then deleted with a certificate.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier use case has quarterly performance and fairness metrics (inventory column `monitoring`) reported to the committee; drift or threshold breaches trigger re-review.
- **Generative AI (NIST AI 600-1):** AI-001, AI-005, AI-008, AI-009, AI-014, and AI-016 are generative. Controls address confabulation (answers grounded in approved sources, with citations for AI-005 and AI-008), information integrity (prohibited-claims checks for AI-001), data privacy (no training on company data; Restricted data only in the approved tenant), and human review of everything published.
- **Third parties:** AI vendors that handle student data are tier-1 in the vendor program. Contracts require school-official and direct-control terms, no training on company data, Safeguards Rule terms, and notice of material model changes (POL-01 4.8).
- **SL-2 partners:** no AI use case touches partner students' data without the partner's written agreement; AI-008 is disclosed in the partner agreements, and AI-005 is not offered to partners.
- **Decommissioning:** use cases are retired if they fail monitoring thresholds twice, if the vendor changes data-use terms, or if a state law duty cannot be met; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the AI governance committee's recommendation of 2026-08-25:
1. **AI-002: approved to continue with conditions.** Email-only routing stopped 2026-08-26; ZIP code and device type removed as inputs by 2026-10-31; local fairness test, applicant notice, and appeal path by 2026-12-15 (POAM-019); exclusion of matriculated students' data from the vendor's pooled model by contract amendment by 2026-12-31. If the thresholds are not met by 2026-12-31, scoring is switched off before 2027-01-01.
2. **AI-003: approved to continue with conditions.** Retrain without ISIR-derived fields and login counts by 2026-11-30 (POAM-004); scores visible only to assigned advisors with the advisor role redesign (POAM-003); student notice by 2026-12-15; retest by 2027-01-31 (POAM-019).
3. **AI-010, AI-014, AI-016:** may continue in current scope until review by 2026-11-30; AI-010 may not expand.
4. **AI-012:** the score is barred from misconduct decisions (Provost directive, 2026-08-31) and its display is switched off by 2026-10-15 (R-043).
5. **AI-013:** stays disabled until committee review, counsel's state law check, and an adverse impact analysis are complete.
6. **AI-004 and AI-006:** retests by 2027-01-31; **AI-011:** re-review after the ISIR-derived fields are removed.
7. **Intake block:** procurement and SaaS change management require an inventory ID before any AI feature is switched on, by 2026-11-30 (POAM-019).

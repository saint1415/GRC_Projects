# AI Risk Assessment: Student-Success Early Alert and Admissions Scoring

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (private career college) |
| Tier / Vertical | Small / Educational Services |
| AI use cases | **AI-001:** student-success early-alert risk scoring, piloted in 2 programs since the May 2026 term (full assessment). **AI-002:** admissions applicant scoring in the CRM, available but not approved (screening assessment) |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook. AI 600-1 is not used because neither use case is generative |
| Assessor / date | Director of Student Success with the Director of Institutional Effectiveness, the Registrar, and the IT Director, 2026-08-18 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner:** Director of Student Success for AI-001; Director of Admissions for AI-002. The Director of Institutional Effectiveness configures the AI-001 model and runs the bias tests.
- **Decision authority, scaled to a 60-person college.** There is no AI committee. The Campus President approves Medium-tier use cases. High-tier use cases also need the Board chair, consistent with the risk acceptance rules in POL-01 4.4.
- **Review cadence:** the owners, the Registrar, and the IT Director review each AI use case every term. Any new AI use is a material change that triggers a risk assessment update (POL-01 4.3).
- **Policies that apply:**
  - POL-04 4.5: FAFSA data and federal tax information may not be used as model inputs.
  - POL-04 4.10: no Restricted data in AI tools unless the tool is approved and the vendor may not train on college data.
  - POL-05 4.8: AI-001 scores may be used only by pilot advisors, and AI-002 stays turned off.
  - POL-02 4.2: advisors see only their assigned students.
- **Approved-tools list:** kept by the IT Director. Today it lists only AI-001, for the pilot programs. No general-purpose generative AI tool is approved for Restricted data.
- **Inventory:** the Director of Institutional Effectiveness keeps `ai-use-case-inventory.csv` and checks each CRM and SIS release for newly enabled AI features (P04 CM-7 row).

## 2. MAP (AI-001 early-alert risk scoring)
| Item | Description |
|---|---|
| Purpose and intended use | Identify students who may withdraw or fail a course early enough for an advisor to offer help (tutoring, schedule changes, emergency aid referral, career services). The goal is better retention and completion |
| Users / operators | 2 pilot advisors; the Director of Student Success; the Director of Institutional Effectiveness (configuration) |
| Affected people | 214 students in the 2 pilot programs (patient care technician, on campus; IT support, online). If expanded, all about 900 students |
| Data (inputs, training, outputs) | **Inputs, refreshed nightly from the reporting database:** LMS logins and assignment submissions over the last 14 days, attendance, midterm grades, prior-term GPA, credits attempted, account holds, age, home ZIP code, and two FAFSA-derived fields: Pell eligibility and first-generation status. **Training:** the vendor's base model plus 3 years of the college's historical outcomes. **Outputs:** a 0-100 score, a band (High, Medium, Low), and the top 3 contributing factors, shown to advisors in the SIS |
| Build or buy | Buy and configure: the SIS vendor's student-success analytics module (inside SYS-01, covered by the SIS SOC 2 report for Security, P09). The college chooses the inputs and the band thresholds |
| Not intended | Admission, financial aid, academic standing, probation, dismissal, grades, or program placement decisions. No automated action is taken on a student. Any such use requires re-assessment as High tier |

**Applicable laws and rules (AI-001):**
| Rule | Applies? | Why |
|---|---|---|
| FERPA, 34 CFR Part 99 (N61-R01) | **Yes** | Scores are derived from education records. Advisors may use them as school officials with a legitimate educational interest (99.31(a)(1)(i)(A)), but only for their assigned students (99.31(a)(1)(ii)). Today all advisors see every student's score (R-008). The vendor is a school official only if it is under the college's direct control for use of the records (99.31(a)(1)(i)(B)). **The contract does not stop the vendor from using college records to improve its models** (P03 G-052) |
| HEA sec. 483 limits on FAFSA data (FSA Handbook Vol. 2 Ch. 7) | **Yes** | FAFSA data may be used only for the application, award, and administration of aid (P03 G-058). **Pell eligibility and first-generation status come from the ISIR and must be removed as model inputs** (R-022, POAM-025) |
| FTC Safeguards Rule, 16 CFR Part 314 (N61-R02) | **Yes** | The module reads customer information (account holds and aid fields), so the vendor is a service provider under 314.4(f) and the pilot is a material change for the risk assessment (314.4(b)(2)) |
| Federal civil rights laws for recipients of federal financial assistance: Title VI (42 U.S.C. 2000d), Title IX (20 U.S.C. 1681), Section 504 (29 U.S.C. 794), Age Discrimination Act (42 U.S.C. 6101 et seq.) | **Yes** | Title IV participation brings these laws into play. A tool that leads to different treatment by race, color, national origin, sex, disability, or age creates legal and fairness risk. Federal disparate-impact enforcement has been deprioritized (EO 14281, see `00_universal/cross-sector/`), but the college tests outcomes by group anyway because unequal treatment of students is the harm it wants to avoid |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. The procurement file keeps the claims the college relied on |
| ED AI grant priority (91 FR 18774) and ED Dear Colleague Letter on AI and grant funds (July 22, 2025) | No | Both concern ED grant funds. The pilot uses no ED grant funds. Their responsible-use principles are used as guidance only |
| Colorado SB26-189 (ADMT in education decisions) | No | The college does business only in Florida, and online programs are offered only to Florida residents. The act is also not effective until 2027-01-01. State AI law is otherwise out of scope by decision (see `../scenario-facts.md`) |

## 3. Risk tier
**AI-001: Medium** (repository rubric, `00_universal/projects/P10_ai-governance/README.md`).
- **Why not High:** the score is not a substantial factor in a consequential decision about a student's access to education. It routes supportive outreach only. An advisor decides whether and how to contact the student, and no service is withheld based on the score.
- **Why not Low:** it uses education records and aid data about identifiable students, affects how advisor time is spent, and could reinforce past inequities in who gets help.
- **Escalation triggers (re-tier to High and re-assess):**
  - use in any decision on admission, aid, academic standing, probation, dismissal, or program placement;
  - automatic holds, messages, or enrollment actions based on the score;
  - expansion beyond the 2 pilot programs without passing the fairness tests in section 4;
  - adding inputs about disability, health, or immigration status.

**AI-002: High.** Applicant scoring that ranks applicants for outreach or follow-up can decide who gets the admissions representatives' attention. That makes it a substantial factor in access to education, a consequential decision category in the rubric.

## 4. MEASURE (AI-001, May 2026 term pilot)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Compare the High band with actual outcomes (withdrawal or a failing course grade) at the end of the term. Thresholds: recall of at least 60% and precision of at least 35% | 214 students; 46 flagged High; 31 had an adverse outcome, 19 of them flagged. Recall 61%, precision 41% | **Yes**, narrowly |
| Safe | Scores lead only to supportive outreach. Review 30 advisor notes for any use of the score to discourage enrollment or limit services | 2 of 30 notes suggested the student "consider pausing enrollment" and cited the score | **No** |
| Secure and resilient | Vendor SOC 2 (Security) covers the module; SSO with MFA for advisors; score visibility limited to pilot advisors | SOC 2 reviewed (P09); SSO with MFA in place; **all 6 advisors and the admissions team can see scores** | Partial |
| Accountable and transparent | Named owner; students told that an early-alert model is used, what it uses, and how to ask questions; FERPA annual notice reflects the vendor as a school official | Owner named 2026-08; **no student notice**; FERPA notice silent on the vendor | **No** |
| Explainable and interpretable | Advisors see the top 3 contributing factors for each score and can explain them to the student | Available in the module; the 2 pilot advisors described the factors correctly in interviews | Yes |
| Privacy-enhanced | No FAFSA-derived inputs; the vendor contract prohibits training on college records; scores kept only for the term plus 1 year | **Pell eligibility and first-generation status are inputs**; no training prohibition in the contract; no retention rule | **No** |
| Fair, with harmful bias managed | See the bias testing plan below | Black students were flagged at 1.6 times the rate of white students, with a false positive rate of 24% vs 11%. Online students' false positive rate was 22% vs 12% on campus | **No.** Two disparities flagged |

**Bias finding.** The disparities trace mainly to three inputs:
- **Home ZIP code** acts as a proxy for race and income.
- **Pell eligibility** is a FAFSA-derived field that must be removed anyway under the HEA limits.
- **LMS login frequency** penalizes online students who work in longer, less frequent sessions.

The pilot groups are small (fewer than 40 students in several groups), so these results are signals for action, not settled estimates. They are still large enough that the model must not be expanded.

### Bias testing plan
| Element | Plan |
|---|---|
| Groups compared | Race and ethnicity (self-reported in the SIS for IPEDS reporting), sex, age band (under 25, 25 and older), and modality (online, on campus). Disability is not tested from records; complaints are routed to the Director of Student Success |
| Metrics | (1) Flag-rate ratio: each group's High-band rate divided by the reference group's rate. (2) False positive rate difference: students flagged High who had no adverse outcome. (3) Recall by group, so that no group is under-served |
| Thresholds | Flag-rate ratio between 0.8 and 1.25; false positive rate difference of 10 percentage points or less; recall within 10 points of the overall rate. Any breach is a flag that requires a documented review |
| Small groups | Report counts with every rate. Groups under 30 students are pooled across terms (up to 3) before a pass or fail decision. Results are never published for groups under 10 |
| Frequency and owner | Before any expansion, after every model or input change, and at the end of every term. Run by the Director of Institutional Effectiveness, reviewed by the Director of Student Success and the Registrar |
| Action on failure | Remove or replace the proxy input, recalibrate the band thresholds by group only if counsel agrees it is lawful, and retest. Keep the model in pilot until two consecutive terms pass |

## 5. MANAGE
**Human-in-the-loop design:**
- The score is a prompt for outreach, never a decision.
- An advisor reviews the student's record and the top factors, then chooses whether and how to reach out.
- Outreach must offer help. It must never discourage enrollment or limit a service.
- Advisors may override the band. They must record their reason in the SIS advising note, and a Medium or Low student can always be contacted.
- The written human review rule is added to the advising procedure by 2026-09-30.

**Transparency to students:**
- A plain-language notice in the student portal and the student handbook explaining that an early-alert model is used, the kinds of data it uses, that it never decides grades, aid, or enrollment, and whom to contact.
- The FERPA annual notice lists the vendor as a school official (P03 G-048).

**Monitoring:**
- End-of-term validity and fairness report (section 4), tracked in the risk register as R-020.
- Monthly spot check of 10 advisor notes for prohibited uses.
- Student complaints go to the Director of Student Success and are reviewed each term.

**Incident handling:**
- A misuse of a score (for example, discouraging enrollment) is handled as a policy violation (POL-01 4.10) and reviewed by the Director of Student Success.
- A vendor security incident follows P08 and the contract's 72-hour notice terms.

**Decommissioning (stop the pilot and turn the module off):**
- The vendor will not agree by 2026-10-31 to stop using college records to train its models.
- Disparities remain above the thresholds after two terms of remediation.
- Validity falls below the thresholds for two consecutive terms.
- Any use of the score in an adverse decision about a student.

When the module is turned off, the vendor must delete stored scores, and the deletion must be confirmed in writing.

## 6. Decision
**AI-001: Approve with conditions.** Campus President, 2026-08-21. The pilot may continue in the 2 programs **only if** these conditions are met by the dates shown:
1. Pell eligibility and first-generation status are removed as inputs and purged from the reporting database (POAM-025), by 2026-10-31.
2. Home ZIP code is removed as an input, and LMS activity is measured by assignment submissions rather than login counts, by 2026-10-31. The fairness tests are then re-run on the May 2026 term data before the next term's scores are used.
3. A contract amendment prohibits the vendor from using college records to train or improve its models and limits use to college purposes (P03 G-052), by 2026-10-31.
4. Scores are visible only to the pilot advisors for their assigned students, by 2026-09-30.
5. The written human review rule and advisor retraining on prohibited uses are in place by 2026-09-30.
6. The student notice is published by 2026-11-30.

Expansion beyond the 2 programs requires two consecutive terms that pass both the validity and the fairness thresholds, and Campus President approval.

**AI-002: Not approved.** Campus President and Board chair, 2026-08-21. The CRM applicant scoring feature stays disabled, and the IT Director checks it after each CRM release (P01 R-021, avoided). Any future request needs a full High-tier assessment first:
- vendor model documentation;
- pre-deployment bias testing on past applicant data;
- applicant notice;
- a rule that no applicant is deprioritized without human review.

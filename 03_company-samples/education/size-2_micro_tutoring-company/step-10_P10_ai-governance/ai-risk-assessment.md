# AI Risk Assessment: Student-Progress Risk Scoring (AI Progress Insights)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (K-12 tutoring and learning center) |
| Tier / Vertical | Micro / Educational Services |
| AI use case | AI-001: the tutoring platform's AI progress insights module, which scores each student's risk of falling behind and recommends a number of sessions per week. Switched on by the vendor in its May 2026 release; used by the Director of Tutoring from 2026-05-18 to 2026-08-28 |
| Registry default adapted | The vertical default is "AI admissions and student-success risk scoring." A tutoring company makes no admissions decisions, so the assessment covers the student-success scoring it actually uses (see `../00_company-facts.md` section 5) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Playbook |
| Assessor / date | Center Director (Information Security Coordinator) with the Director of Tutoring, 2026-08-20 |
| Decision | Owner, 2026-08-28 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the Director of Tutoring, who uses the scores. **Decision authority:** the Owner.
- **Policies that apply:**
  - POL-02 A.6: no written assurances, no children's data. This covers new features a vendor switches on.
  - POL-04 4.5: no disclosure that is not needed to provide tutoring (for example, to train a vendor's AI models) without separate parental consent.
  - POL-04 4.6: Restricted data only in approved AI tools. The approved list is empty today.
  - POL-04 4.11: a material change to what is collected or how it is used needs a new notice and, where required, new consent.
  - POL-02 C.2: no student information in public AI chatbots (AI-002).
- **Approved-tools list:** kept by the Center Director in POL-04 4.6.
- **Scale for a Micro company:** there is no AI committee. The Owner, Center Director, and Director of Tutoring review AI use at the monthly security meeting, and the Director of Tutoring reads each vendor release note for new AI features.

**How the use started.** The vendor added the module in its May 2026 release and turned it on by default. Nobody at the company approved it, assessed it, or told parents or the district. The Director of Tutoring found the scores useful and began using them for district program placement and in parents' monthly progress reports (P01 R-008, R-009; P03 G-002, G-017, G-018).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Flag students at risk of falling behind (red, yellow, green) and suggest how many sessions a week would help, so tutors can step in early |
| Users | Director of Tutoring; Lead Tutors can see the flags |
| How it was actually used | (1) District program: students flagged red were moved into the "intensive" group (3 sessions a week instead of 2). (2) Private-pay families: 31 monthly progress reports in June and July included the line "our progress system recommends 3 sessions per week"; 12 families then added sessions |
| Affected people | About 210 students scored since May 2026 (about 90 district students and about 120 private-pay students), most of them under 13, and their parents |
| Data | Inputs: practice exercise accuracy and time on task, session attendance, session count, grade level, platform assessment scores, and, for district students, the district's assessment scores from the roster. Outputs: flag color, risk score, recommended sessions per week |
| Build or buy | Buy: vendor feature inside the tutoring platform. The model is the vendor's; the company cannot see its design or training data |
| Not intended | Deciding whether a student stays in the district program; diagnosing learning disabilities; any use outside tutoring |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| COPPA Rule, 16 CFR Part 312 (N61-R03) | **Yes** | The module processes children's personal information collected through the platform. Turning it on was a material change in use that needed direct notice to parents (312.4(b)) and consent (312.5(a)(1)). The vendor's terms allow de-identified data to improve its products; in the 2025 final rule the FTC states that disclosing children's personal information to train or otherwise develop AI is **not** integral to the service and needs separate verifiable parental consent (312.5(a)(2); 90 FR 16918). Outputs are children's information subject to the retention rule (312.10), and the vendor must give written security assurances (312.8(c)) |
| FERPA through the district contract (N61-R01) | **Yes, for district students** | The company may use program students' education records only for the purpose the district disclosed them for (34 CFR 99.33(a)(2)) and must stay under the district's direct control (99.31(a)(1)(i)(B)). Scoring district students with a vendor AI feature, and letting the vendor use the data, was never approved by the district |
| Fla. Stat. 501.171 | Yes (security and breach) | Scores and inputs are stored with students' names; reasonable security measures apply, and any breach follows P08 |
| FTC Act Section 5 | Indirectly | Telling parents that "our progress system recommends" more paid sessions is a claim about the tool. It must be truthful and not misleading, including about the company's financial interest |
| ED AI grant priority (91 FR 18774) and ED Dear Colleague Letter on AI and grant funds (July 22, 2025) | No | Both concern ED grant funds; the company receives none. Their responsible-use principles are used as guidance only |
| Colorado SB26-189 (ADMT in education decisions) | No | The company serves Florida families only, and the act is not effective until 2027-01-01 |
| Federal civil rights laws for recipients of federal financial assistance | Not directly | The company receives no federal financial assistance. It tests outcomes for students with accommodation notes anyway, because unequal treatment of children who already need support is the harm it most wants to avoid |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why High:** for district students, the flag was the main input to program placement, so the AI was a substantial factor in an education decision about a child: how much tutoring the child receives. For private-pay families, the recommendation shaped what parents bought.
- **Why not Medium:** a human made each placement, but in practice the Director of Tutoring followed the flag in 34 of 36 placement changes and recorded no other reason.

**What would allow re-tiering to Medium:** placement decided on documented tutor judgment, with the flag as one input among several; no use in sales messages to parents; and a passing fairness test.

## 4. MEASURE
The Director of Tutoring and the Center Director compared flags from May and June with the students' July platform assessments for 120 students with enough data (2026-08-20).

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Of students flagged red, at least 70% should score below grade-level benchmark in July; of students not flagged, no more than 10% should | Red: 21 of 38 (55%). Not flagged: 9 of 82 (11%) | **No** |
| Safe | No student's services reduced or ended because of a flag | None reduced or ended; flags only added sessions | Yes |
| Secure and resilient | Feature covered by the vendor's SOC 2 report; access limited to staff | Released after the report period; untested by the auditor. Lead Tutors and Director of Tutoring only | Partial |
| Accountable and transparent | Parents and the district told that AI is used and how; recommendations labeled as AI-generated | No notice to parents or the district; progress reports presented the recommendation as the company's own | **No** |
| Explainable and interpretable | Staff can see which inputs drove a flag | The platform shows the top two factors for each flag | Yes |
| Privacy-enhanced | Signed addendum barring model training; inputs limited to what tutoring needs; outputs deleted under POL-04 4.9 | No addendum; vendor terms allow de-identified data for product improvement; district assessment scores used as inputs without district approval | **No** |
| Fair, with harmful bias managed | Compare red-flag rates for students with and without accommodation notes, among students with the same July outcome; flag a gap over 10 percentage points | Students with accommodation notes: 13 of 29 flagged red (45%); without: 25 of 91 (27%). Among the 90 students who were at benchmark in July, 7 of 18 with notes had been flagged red versus 10 of 72 without (39% vs 14%) | **No (flagged)** |

**Bias finding.** The model appears to over-flag students with accommodation notes, most likely because time on task and attendance weigh heavily and those students often take longer and miss more sessions for therapy appointments. The sample is small, but the gap is large. For district students, an over-flag meant more tutoring, which is not harmful in itself; for private-pay families, it meant a recommendation to buy more sessions.

## 5. MANAGE
**Data protection:**
- Module off from 2026-08-28. It may restart only after a data processing addendum is signed that bars any use of the company's data, including de-identified data, to train or improve models, requires deletion on request, flows down to the vendor's subprocessors, and gives written security assurances (312.8(c); POAM-007).
- District students are excluded unless the district approves in writing (99.33(a)(2)).
- District assessment scores are never used as model inputs.
- Flags and scores are deleted with the student record under POL-04 4.9.

**Notice and consent (COPPA):**
- A direct notice of the change goes to every parent before restart, describing the scoring, its inputs, and how to opt out (312.4(b)).
- No separate consent is needed only if the addendum is signed, because then no non-integral disclosure is made. If the vendor will not sign, the module stays off.
- The online notice (P03 G-013) describes the feature.

**Human in the loop:**
- The flag is a prompt for a tutor's review, never a decision. The Director of Tutoring records a reason based on the tutor's judgment for every placement change.
- No student may be moved out of the district program, or have services reduced, because of a flag.
- Progress reports may say "the tutoring team recommends." Any mention of the AI tool must say it is an automated estimate, and recommendations to buy more sessions must come from the tutor, not the tool.

**Monitoring:**
- Monthly: compare last month's flags with outcomes for a sample of 20 students; log results against P01 R-009.
- Quarterly: red-flag rates for students with and without accommodation notes; stop use if the gap at equal outcomes exceeds 10 percentage points.
- Parent complaints about AI use go to the Center Director.

**Incident handling:** a vendor security incident affecting AI data is handled under POL-03 and the P08 runbook, including the district's 48-hour notice for program students.

**Decommissioning:** if the vendor will not sign the addendum by 2026-12-31, the Director of Tutoring asks the vendor to turn the module off permanently for the company's tenant and to confirm in writing that the company's data was deleted from any model-improvement datasets.

## 6. Decision
**Approve with conditions.** Owner, 2026-08-28.

The module stays off from 2026-08-28. It may restart, for private-pay students only, when all of these are met:
1. The data processing addendum is signed with the terms in section 5 (target 2026-10-31; R-008).
2. Parents have received the direct notice of the change, and the online notice describes the feature.
3. The written human review rule is in place, and no flag is used in sales messages.
4. A re-test on new data shows the accommodation-note gap at equal outcomes is 10 percentage points or less, or the vendor removes or reweights the time-on-task and attendance inputs.
5. The Director of Tutoring and the Lead Tutors complete a short briefing on these rules.

Use for district students requires, in addition, the district's written approval. Until then, district placement uses tutor judgment and the district's own assessments only.

**Related actions.**
- The 12 families who added sessions after an AI-based recommendation receive a note from the Director of Tutoring explaining the recommendation and offering to return to their previous schedule. Due 2026-09-30.
- AI-002 (public chatbots) and AI-003 (the platform's homework helper chatbot) are covered in the inventory. AI-003 stays off; turning it on would need its own assessment because it would talk directly with children.

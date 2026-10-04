# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed private, for-profit college) |
| Tier / Vertical | Mid-Market / Educational Services |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. AI-001 and AI-002 are the registry's "AI admissions and student-success risk scoring" use case |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for AI-003 and AI-004 |
| Assessors / date | Provost and Chief Academic Officer (academic), Director of Institutional Research (bias testing), vCISO and Information Security Manager (security), Chief Compliance Officer and General Counsel (privacy and legal), 2026-08-24 to 2026-09-11 |
| Decision | Chief Information Officer and Provost, 2026-09-17; High-tier decisions approved by the President and CEO |

## 1. Summary
All five tools were adopted by departments without a security, privacy, or bias review (gap 9). None is out of control, but each needs conditions:
- **AI-001, admissions scoring:** decides whom admissions calls first, and it pushes older applicants and applicants from lower-income ZIP codes down the queue.
- **AI-002, early alert:** uses FAFSA-derived fields, which the HEA does not allow for this purpose.
- **AI-003, the website and portal assistant:** gave wrong aid and transfer-credit answers, and in testing its signed-in mode showed one student another student's balance.
- **AI-004, the AI tutor:** has no contract, and the vendor uses student work to improve its models.
- **AI-005, proctoring flags:** flags students with accommodations and Black students more often, and some flags reached the integrity office without faculty review.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Admissions applicant scoring | High | Approve with conditions |
| AI-002 | Student-success early alert | Medium | Approve with conditions |
| AI-003 | Website and portal assistant | Medium | Conditional: signed-in mode stays off; public mode with conditions by 2026-11-30, or switch off |
| AI-004 | LMS AI tutor (pilot) | Medium | Conditional: contract by 2026-12-31 or switch off; no expansion |
| AI-005 | Online proctoring AI flags | High | Approve with conditions |

Tiers: 2 High, 3 Medium, 0 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Provost and Chief Academic Officer, supported by the vCISO. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.12 and 4.13: no FAFSA-derived data in AI models; AI tools must be approved before use.
  - POL-04 4.5 and 4.10: no Restricted data in unapproved AI tools; contracts must forbid training on college data and require deletion.
  - POL-05 4.9: approved tools only; a person reviews outputs and makes the final decision about any applicant or student.
  - STD-05 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Information Security Manager on the intranet. Today it lists AI-001 to AI-005 with their conditions. No general-purpose generative AI tool is approved for Restricted data.
- **Inventory:** the GRC analyst keeps `ai-use-case-inventory.csv` and checks each SaaS release note for newly enabled AI features (P02 CM-7).

### 2.1 Proposed lightweight AI governance process
A mid-market college does not need a large AI committee. It needs a short, reliable gate and a monthly rhythm that reuse existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature turned on in an existing tool, submits a one-page intake: purpose, users, people affected, data, vendor, decisions influenced | Requesting business owner | 15 minutes |
| 2. Triage | The Information Security Manager assigns a provisional tier with the rubric and checks the purchasing gate (no purchase or card payment without approval, POL-01 4.9) | Information Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, FERPA and contract terms (school official, no training, deletion), HEA data check, and an academic or business reviewer. **High:** full MAP and MEASURE assessment like this one, with a pre-deployment bias test and counsel's review of state AI laws | Information Security Manager; Chief Compliance Officer; Director of Institutional Research; business reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Information Security Manager. Medium: the **AI review group** (Provost, vCISO, Chief Compliance Officer, Director of Institutional Research), meeting monthly for 30 minutes. High: the AI review group recommends, the CIO and Provost decide, and the President and CEO approves | As listed | Monthly |
| 5. Monitor | Owner reports the agreed metrics monthly (Medium) or monthly with a term-end deep dive (High); incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type, new population, a complaint pattern, or a new state law taking effect | AI review group | Annual |

The new material-change trigger in POL-01 4.3 also sends every new AI use into the Safeguards Rule risk assessment (16 CFR 314.4(b)(2)). **Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. Re-tier triggers are in section 3.

## 3. MAP
| Item | AI-001 Admissions scoring | AI-002 Early alert | AI-003 Assistant | AI-004 AI tutor | AI-005 Proctoring flags |
|---|---|---|---|---|---|
| Purpose | Set the call order for about 4,000 online inquiries a month | Flag online students at risk of withdrawing or failing so advisors reach out | Answer common questions on the website and portal | Explain concepts and comment on drafts | Flag possible misconduct in recorded online exams |
| Users | 70 admissions staff | 45 advisors | Public and students | About 1,100 students in 40 sections | Faculty; academic integrity office |
| Affected people | Prospective students | About 3,500 online students | Prospective and current students | Pilot students | About 18,000 exam takers a year |
| Data | Inquiry data incl. ZIP code, device type, age | Education records; ISIR-derived fields (to remove) | Questions; SIS balance, holds, aid status (signed-in) | Prompts and drafts | Video, audio, ID images, accommodations |
| Build or buy | Buy (CRM feature) | Build (Institutional Research) | Buy (card purchase) | Buy (card purchase) | Buy |
| Generative AI? | No | No | Yes | Yes | No |
| Influences a consequential decision? | **Yes**: who gets timely contact, a substantial factor in access to education | No (outreach only) | No (information), but misstatements can mislead | No (feedback only) | **Yes**: misconduct referrals |
| Re-tier triggers | Any use in admission decisions, aid, or scholarships | Use in admission, aid, standing, or placement; automated holds or messages | Binding answers on admission or aid; any automated account action | Use in grading | Automatic referral or sanction |

**Applicable laws and rules (all five unless noted):**
| Rule | Applies? | Why |
|---|---|---|
| FERPA, 34 CFR Part 99 (N61-R01) | **Yes** (AI-002 to AI-005; AI-001 once applicants enroll) | Vendors that receive education records must be school officials under the college's direct control, using records only for the outsourced function (99.31(a)(1)(i)(B), 99.33(a)). AI-003's signed-in mode must authenticate the student before disclosing records (99.31(c)). AI-004's vendor terms allow model training on student work, which fails the direct-control test |
| HEA sec. 483 limits on FAFSA data (FSA Handbook Vol. 2 Ch. 7) | **Yes** (AI-002) | FAFSA data may be used only for the application, award, and administration of aid. Pell eligibility, the Student Aid Index band, and first-generation status from the ISIR must be removed as AI-002 inputs (R-011, POAM-018) |
| FTC Safeguards Rule, 16 CFR Part 314 (N61-R02) | **Yes** (AI-001, AI-002, AI-003) | These tools touch customer information, so their vendors are service providers under 314.4(f), and each tool is a material change for the risk assessment (314.4(b)(2)) |
| Misrepresentation rules for Title IV institutions, 34 CFR 668.71-668.73 | **Yes** (AI-003; AI-001 call scripts) | A misrepresentation includes any false, erroneous, or misleading statement to a prospective student or student, including on the website or in any other communication, about the program (for example, transfer of credits, 668.72(b)) or financial charges and aid (668.73). An assistant that answers on the college's behalf is such a communication (verified text, eCFR 2026-09-23) |
| FTC Act Section 5 | **Yes** | The college is a for-profit company within FTC jurisdiction; its own statements (AI-003) and the vendors' accuracy claims are covered |
| Federal civil rights laws for recipients of federal financial assistance: Title VI (42 U.S.C. 2000d), Title IX (20 U.S.C. 1681), Section 504 (29 U.S.C. 794), Age Discrimination Act (42 U.S.C. 6101 et seq.) | **Yes** | Title IV participation brings these laws into play. A tool that leads to different treatment by race, color, national origin, sex, disability, or age creates legal and fairness risk. Federal disparate-impact enforcement has been deprioritized (EO 14281, see `00_universal-framework/cross-sector/`), but the college tests outcomes by group because unequal treatment of students is the harm it wants to avoid |
| Colorado SB26-189 (automated decision-making technology) | **Possibly** (AI-001, AI-005), from 2027-01-01 | The act covers ADMT that materially influences consequential decisions, including education, for deployers doing business in Colorado, with no small-business exemption in the signed text. About 110 online students live in Colorado. Counsel is reviewing scope, including how the act treats FERPA-covered institutions, by 2026-12-15 (R-052). Not treated as a current obligation |
| California CPPA ADMT regulations (11 CCR 7200 et seq.) | **Unconfirmed** | They apply to CCPA "businesses" using ADMT for significant decisions, including education, with compliance by 2027-01-01. About 240 online students live in California. Whether the college meets the CCPA business definition, and which exemptions apply to its data, has **not been determined**; counsel is reviewing |
| ED AI grant priority (91 FR 18774) and ED Dear Colleague Letter on AI and grant funds (July 22, 2025) | No | Both concern ED grant funds; none of these tools uses ED grant funds. Their responsible-use principles are used as guidance only |
| COPPA, HIPAA | No | No children under 13; the college is not a covered entity |

## 4. Risk tier
- **AI-001: High.** The score sets who gets timely contact. In 2026 spring data, 31% of the lowest-scored decile received no human contact within 7 days. That makes the score a substantial factor in access to education, a consequential decision category in the rubric.
- **AI-005: High.** Flags start academic misconduct referrals, which can lead to failing grades or dismissal.
- **AI-002: Medium.** It routes supportive outreach only; an advisor decides, and no service is withheld. It would be High if used for any admission, aid, standing, or placement decision.
- **AI-003: Medium.** It interacts directly with prospective and current students and speaks for the college, but staff make every decision. Its misstatements carry legal risk (668.71), which the conditions address.
- **AI-004: Medium.** It processes education records and interacts with students, but makes no decision about them.

## 5. MEASURE (by use case)
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result | Pass? |
|---|---|---|---|---|---|
| AI-001 | Fair, harmful bias managed | Ratio of each group's share of top-3-decile scores to the reference group's (race and ethnicity where self-reported, sex, age band, ZIP code income quintile); about 23,000 inquiries, January to June 2026 | Between 0.8 and 1.25 | Black 0.72, Hispanic 0.81, age 40 and over 0.78, lowest-income ZIP quintile 0.59; sex within range | **No** |
| AI-001 | Valid and reliable | Calibration of score to actual enrollment | AUC at least 0.65; calibration error under 5 points | AUC 0.71; calibration error 3 points | Yes |
| AI-001 | Accountable and transparent | Notice to inquirers that a model sets contact order; vendor model documentation | Both in place | Neither | **No** |
| AI-001 | Explainable | Top features visible to admissions managers | Available | Available: ZIP code and device type are among the top 5 features | Yes (and shows the proxy problem) |
| AI-002 | Valid and reliable | High band versus actual withdrawal or failing grade, spring 2026 online terms (about 3,300 students) | Recall at least 60%; precision at least 35% | 520 flagged; 330 of 610 adverse outcomes caught: recall 54%, precision 63% | **No** (recall) |
| AI-002 | Fair, harmful bias managed | Flag-rate ratio and false positive rate difference by race and ethnicity, sex, age band | Ratio 0.8-1.25; false positive difference 10 points or less | Black students flagged at 1.5 times the rate of white students; false positive rate 21% vs 9% | **No** |
| AI-002 | Privacy-enhanced | No FAFSA-derived inputs | None | 3 ISIR-derived inputs | **No** |
| AI-003 | Valid and reliable (AI 600-1: confabulation) | 60 scripted questions on admissions, aid, billing, transfer credit | Material errors under 2% | 7 of 60 wrong (5 aid, including refund timing and Pell eligibility; 2 transfer credit) | **No** |
| AI-003 | Secure and resilient; privacy-enhanced (AI 600-1: information security, data privacy) | Prompt-injection and cross-student tests in signed-in mode | 0 disclosures in 50 attempts | Returned another student's balance when given that student's ID (2026-07-22); signed-in mode suspended | **No** |
| AI-003 | Accountable and transparent | AI disclosure banner; handoff to staff | Both | Neither at the time of testing | **No** |
| AI-004 | Privacy-enhanced | Contract forbids training on student work; deletion at contract end | Both | Vendor keeps prompts 2 years and uses them to improve models; no contract | **No** |
| AI-004 | Valid and reliable (AI 600-1: confabulation) | Faculty review of 100 tutor responses | Factual errors under 5% | 4 errors (math explanations) | Yes |
| AI-004 | Safe (academic integrity) | 50 attempts to get a full essay written | 0 complete essays | 3 produced full paragraphs on request | Partial |
| AI-005 | Fair, harmful bias managed | Flag-rate ratio by accommodation status and by race and ethnicity (self-reported SIS data linked by Institutional Research), spring 2026 (about 9,200 exams) | Ratio 0.8-1.25 | Students with accommodations 2.3; "face not detected" flags for Black students 1.9 times the rate for white students | **No** |
| AI-005 | Accountable and transparent | Faculty review of the recording before any referral | 100% | 27 of 30 sampled referrals (90%) | **No** |
| AI-005 | Valid and reliable | Share of 2025-26 referrals (412) where the integrity office found a violation | Tracked; review if under 50% | 39% found a violation (61% did not) | **No** (review triggered) |

### 5.1 Bias testing plan (AI-001, AI-002, AI-005)
| Element | Plan |
|---|---|
| Groups compared | Race and ethnicity (self-reported for IPEDS reporting), sex, age band (under 25, 25-39, 40 and over), and, by use case: ZIP code income quintile (AI-001), modality and Pell status as an outcome check only, never as an input (AI-002), and accommodation status (AI-005). Disability is tested only through accommodation status, with Disability Services' approval |
| Metrics | (1) Flag-rate or top-decile ratio against the reference group; (2) false positive rate difference; (3) recall by group, so no group is under-served (AI-002); (4) contact within 2 business days by group (AI-001) |
| Thresholds | Ratio between 0.8 and 1.25; false positive rate difference 10 points or less; recall within 10 points of the overall rate. Any breach requires a documented review and remediation |
| Small groups | Report counts with every rate; pool up to 3 terms for groups under 30; never publish results for groups under 10 |
| Data protection | Analysis runs in the data warehouse by Institutional Research as school officials; results are aggregated; no demographic data is sent to vendors |
| Frequency and owner | Before deployment, after every model or input change, and at the end of every term (AI-002, AI-005) or quarter (AI-001). Run by the Director of Institutional Research; reviewed by the AI review group |
| Action on failure | Remove or replace proxy inputs; adjust thresholds only if counsel confirms the method is lawful; strengthen human review; keep the tool in its conditional state until 2 consecutive periods pass |

## 6. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the score orders the queue, but every inquiry gets a human contact within 2 business days regardless of score, and scores never decide admission, aid, or scholarships. Managers can reorder the queue.
- **AI-002:** a prompt for outreach only. Advisors see only their assigned students, may override the band with a recorded reason, and may never use the score to discourage enrollment.
- **AI-003:** aid, admissions, and transfer-credit answers must quote and link the official page and offer a staff handoff; the assistant takes no account actions.
- **AI-004:** feedback only; faculty grade all work; students are told when the tool is on in a course.
- **AI-005:** a flag is never an accusation. Faculty must review the recording before referring, the integrity office decides with the student heard, and students can ask for a live-proctored alternative.

**Monitoring:** owners report the section 5 metrics monthly to the AI review group; High-tier items also get a term-end review. Results feed the risk register (P01 R-031 to R-035).

**Incident handling:**
- A security or privacy incident at an AI vendor follows P08 and the contract terms.
- A cross-student disclosure by AI-003 is handled as an unauthorized disclosure: FERPA disclosure record (99.32) and the P08 notification decisions.
- A misleading answer by AI-003 on aid or credits is corrected with each affected student, and the Chief Compliance Officer decides whether it needs wider correction.

**Decommissioning criteria:**
- AI-001: stop scoring if ratios stay outside the thresholds after the proxy inputs are removed, or if counsel finds a state ADMT law applies and its duties are not met by its effective date.
- AI-003 and AI-004: switch off if the contract and fixes are not in place by their dates.
- AI-005: stop automated flags (keep recording only) if accommodation and race ratios stay outside thresholds after 2 terms of remediation.
- Any tool: stop if the vendor changes data-use terms or the model changes without notice. On decommissioning, the vendor must delete college data and confirm in writing.

## 7. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | Minimum contact rule live (2026-10-15); remove ZIP code and device type (2026-11-15); re-test bias (2026-12-31); inquiry-form notice and vendor model documentation (2026-12-31); counsel's Colorado and California review (2026-12-15) | CIO and Provost, 2026-09-17; approved by the President and CEO |
| AI-002 | **Approve with conditions** | Remove ISIR-derived inputs and ZIP code (2026-10-31, POAM-018); retrain and re-test validity and fairness on the next term; student notice in the portal (2026-11-30); advisors see assigned students only (2026-12-31) | CIO and Provost, 2026-09-17 |
| AI-003 | **Conditional** | Signed-in mode stays off until a contract with FERPA, security, and no-training terms is signed, retrieval is limited by the integration (not the prompt) to the signed-in student, and 50 cross-student attempts produce 0 disclosures. Public mode: disclosure banner, quoted and linked answers on aid and credits, staff handoff, and a monthly 50-conversation accuracy sample under 2% material errors, all by 2026-11-30, or switch off | CIO and Provost, 2026-09-17 |
| AI-004 | **Conditional** | Contract with FERPA school-official, no-training, 30-day deletion, and 72-hour incident terms by 2026-12-31, or switch off; student notice in each pilot course; no expansion before a faculty evaluation in spring 2027 | Provost, 2026-09-17 |
| AI-005 | **Approve with conditions** | Faculty review of every recording before referral (Provost memo 2026-09-20); accommodation profiles applied automatically (2026-12-31); vendor face-detection performance data across skin tones and lighting (2026-12-31); quarterly flag-rate monitoring; recordings kept 1 term; live-proctored alternative on request | CIO and Provost, 2026-09-17; approved by the President and CEO |

The conditions are tracked as POAM-025 in P07 and in the risk register (P01 R-031 to R-035, R-052). The AI review group holds its first monthly meeting on 2026-10-06.

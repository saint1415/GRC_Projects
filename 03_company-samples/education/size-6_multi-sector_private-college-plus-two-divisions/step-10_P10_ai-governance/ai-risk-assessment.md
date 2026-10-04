# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Higher Education, Education Software, Student Health, corporate) |
| Tier / Vertical | Multi-Sector / Educational Services (focus division: Higher Education) |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the regulator-specific rules for the priority use cases. These are the college's admissions applicant scoring (AI-001) and student-success risk scoring (AI-002), which split the registry default; Education Software's K-12 AI tutoring assistant (AI-004) and its analytics products sold to schools (AI-005, AI-006); and Student Health's clinic AI tools (AI-007 to AI-009) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1) for generative use cases, and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27. Presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (11 use cases: 3 High, 7 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list each quarter |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, college provost, Education Software chief product officer, Student Health chief medical officer. The director of institutional research advises on testing. Approves High-tier use cases and the approved tools list |
| Division AI owners | The business owner named for each use case in the inventory. Owners run monitoring and report results each quarter |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage); approved tools list with the council (POL-05) |
| Group Chief Privacy Officer | Use of education records, children's data, and PHI; FAFSA data limits; vendor no-training terms |
| Group internal audit | Adds High-tier AI controls to the annual assessment from 2027 |

**Roles that overlap and how that is handled.** The owner of each use case also runs its monitoring. To compensate, the director of institutional research runs fairness tests for college use cases, and the Group Chief Privacy Officer's team reviews results for the other divisions. Group internal audit, which is independent of all owners, starts testing High-tier controls in 2027.

### 1.2 Group AI Standard (adopted 2026; anchored in POL-01 4.12)
1. **Register before use.** Every AI use that touches Restricted data, is offered to children, or makes or supports decisions about applicants, students, patients, or customers' students is entered in the inventory before deployment or material change (POL-01 4.12).
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`), plus one group rule: **any AI that children or K-12 students use directly is High tier**, whatever its decision role. High tier requires council approval, a pre-deployment impact assessment, bias and safety testing, notice to affected people, and quarterly monitoring reports.
3. **Data rules.**
   - FAFSA-derived data must never be a model input (POL-04 4.6; HEA sec. 483).
   - Children's data is used only under district authorization for the school's purpose (POL-04 4.7).
   - Restricted data goes only into approved tools whose vendors are barred from training on it (POL-04 4.10).
4. **Human review rule.** AI scores and summaries about people are prompts for human judgment, not decisions. Nobody may use a score to discourage enrollment, limit a service, or start an integrity case (POL-05 4.6).
5. **Change gate.** A new model, new provider, new feature that changes how student or child data is processed, or new decision role triggers re-assessment before release. Education Software runs this gate in its supplement (POAM-014).
6. **Products sold to schools.** Education Software gives every customer, including the college, intended-use statements, prohibited uses, data categories, limitations, and human review instructions for each AI feature. This also meets the Colorado SB26-189 developer duties from 2027-01-01.
7. **Regulator overlays** in each division supplement (P06):
   - civil rights laws, FERPA, and Title IV limits for the college;
   - COPPA, district contracts, and SOC 2 commitments for Education Software;
   - HIPAA, FERPA treatment records, Section 1557, and recording consent for Student Health.

**Where the program fell short in 2026.** The standard was adopted after admissions scoring (2025), proctoring flags, and the AI tutor (2026-01) were already live (P01 GR-04, High). Admissions scoring has never been bias tested and applicants get no notice (scenario gap 5). The tutor launched without a children's privacy review, a SOC 2 description update, or district contract updates (scenario gap 6). Both are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Admissions applicant scoring (CRM vendor) | Higher Education | High | In production since 2025; conditions |
| AI-002 | Student-success risk scoring | Higher Education | Medium | In production; conditions |
| AI-003 | Online proctoring flags and identity verification | Higher Education | Medium | In production; conditions |
| AI-004 | K-12 AI tutoring assistant (generative) | Education Software | High | Pilot in 140 districts; no new districts |
| AI-005 | District Platform early warning indicators | Education Software | Medium | In production; developer documentation due |
| AI-006 | Campus Platform student-success analytics | Education Software | Medium | In production; developer documentation due |
| AI-007 | Clinic AI scribe (generative) | Student Health | Medium | Pilot; no expansion |
| AI-008 | Counseling triage chatbot (generative) | Student Health | High | Proposed; not approved |
| AI-009 | EHR clinical decision support tools | Student Health | Medium | In production; inventory due |
| AI-010 | Enterprise generative AI assistant | Group | Medium | Approved pilot (3,000 users) |
| AI-011 | Engineer coding assistant | Education Software | Low | Approved |

**Developer and deployer roles inside the group.** Education Software develops AI-005 and AI-006 and sells them to schools. The college uses AI-006 to deliver its own student-success scores (AI-002), so it is a deployer of its sister division's product. It gets the same developer documentation as any external customer.

**Federal grant guidance.** The Department of Education's supplemental priority on AI (91 FR 18774) and its Dear Colleague Letter on AI and grant funds (July 22, 2025) concern grant-funded uses. No Department of Education grant funds pay for these use cases, so both are used as guidance only.

### 2.1 Admissions applicant scoring (AI-001)
**What it does.** The CRM vendor's model scores each inquiry and applicant from 0 to 100 for predicted likelihood to enroll, and sorts them into bands:
- **High and Medium bands:** a call from an admissions representative within 2 business days.
- **Low band:** automated email only, unless the applicant calls in.

About 380,000 applications went through the model in the 2025-26 cycle. Inputs include prior education, program, start term, age, home ZIP code, and communications activity. The model never decides admission, but it decides who gets human help to complete an application.

| Rule | Applies? | What it means here |
|---|---|---|
| Title VI (42 U.S.C. 2000d), Title IX (20 U.S.C. 1681), Section 504 (29 U.S.C. 794), Age Discrimination Act (42 U.S.C. 6101 et seq.) | **Yes** | Title IV participation makes the college a recipient of federal financial assistance. A tool that gives applicants less help by race, sex, disability, or age creates legal and fairness risk. Federal disparate-impact enforcement has been deprioritized (EO 14281; see `00_universal-framework/cross-sector/`), but the group tests outcomes anyway because unequal access to admission is the harm it wants to avoid |
| Colorado SB26-189 (C.R.S. 6-1-1701 to -1709 as reenacted), effective 2027-01-01 | **Yes, for Colorado applicants** (counsel's conservative reading) | Online programs enroll Colorado residents, and admissions is a consequential decision about access to education. Deployer duties: point-of-interaction notice, explanation after an adverse outcome, rights to correct data and to meaningful human review or reconsideration, and 3-year records. No size exemption. The law is under litigation and federal preemption efforts, and AG rules are due by 2027-01-01 |
| California CPPA ADMT rules (11 CCR 7200 et seq.; N51-R03) | **Under counsel review** | The college is a for-profit business with California online students, so the CCPA likely applies. Counsel will decide by 2026-11-30 whether outreach scoring is ADMT used for a significant decision about education (compliance for existing uses by 2027-01-01). This was first raised in this assessment, after P03 fieldwork. It will be added to the next regulation-by-division matrix |
| FTC Safeguards Rule (N61-R02, 16 CFR 314.4(f)) | **Yes** | The CRM holds applicant financial information, so the vendor is overseen as a service provider (P09 VR-03) |
| FERPA (N61-R01) | **Not yet** | Applicants are not "students" until they attend (34 CFR 99.3). Their records become education records if they enroll |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. The procurement file keeps the claims the college relied on |

### 2.2 Student-success risk scoring (AI-002)
| Rule | What it means here |
|---|---|
| FERPA, 34 CFR 99.31(a)(1)(ii) | Advisors may see scores only for students on their caseload. Warehouse analysts building the model need an approved project (POAM-005) |
| HEA sec. 483 (FSA Handbook Vol. 2 Ch. 7; POL-04 4.6) | **Pell eligibility and other FAFSA-derived fields are model inputs today and must be removed.** They are being restricted to the financial aid role by 2026-11-30 (POAM-007; P03 G-061) |
| 45 CFR 164.502(a); 34 CFR 99.33(a) | **Clinic visit counts from the utilization extract were model features until 2026-08-07.** They included nonstudent PHI and contract-college student records (scenario gap 2). The features have been removed, the tables are being purged (POAM-006), and any future health-related input is prohibited without council approval |
| Civil rights laws (as in 2.1) | Scores route outreach, not decisions, but unequal flagging can lead to unequal treatment |
| Colorado SB26-189 | Not covered as designed, because outreach is not a consequential decision. It would be covered if scores were used for admission, aid, standing, or placement |

### 2.3 K-12 AI tutoring assistant (AI-004)
| Rule or commitment | What it means here |
|---|---|
| 16 CFR 312.5(a)(1) | Consent is needed for any material change in how children's information is collected, used, or disclosed. Education Software relies on district authorization for the school's educational purpose under existing FTC guidance (P03 ES-G11). **31 of the 140 pilot districts signed contracts before the tutor existed**, so their authorization may not cover it |
| 16 CFR 312.5(a)(2) | Separate consent is required for disclosure to third parties unless the disclosure is integral to the service. The model provider acts as a service provider with zero retention and no training, so its role is integral. Any secondary use by the provider would change this |
| 16 CFR 312.8(b)(2), (b)(4), and (c) | The tutor's risks must be in the annual risk assessment (not done before launch, ES-G04). Safeguards must be tested (no red-team or safety testing, ES-G06). Written assurances are needed from the model provider (met, ES-G08) |
| 16 CFR 312.10 | Tutor conversation logs need a stated purpose and deletion timeframe in the written retention policy. Today they have none |
| FERPA (as a school official for districts) and state student privacy laws (each state where districts are located) | Transcripts are education records kept for districts. Use is limited to the district's purposes (99.33(a)), and state laws and district contracts may add limits |
| SOC 2 commitments (P09) | The tutor and model provider must appear in the system description for the period ending 2027-06-30 (CC2.3, CC3.4, CC8.1, CC9.2) |
| FTC Act Section 5 (N51-R01) | Marketing calls the tutor "safe for every grade" with no testing evidence. The claim is withdrawn until testing is complete (ES-G19) |
| Colorado SB26-189 | Not covered while the tutor only tutors. Using its outputs for grading or placement would require re-assessment |

### 2.4 Analytics products sold to schools (AI-005, AI-006)
- **Colorado SB26-189 developer duties** apply to Colorado customers from 2027-01-01. Developers must give documentation of intended uses, training data categories, limitations, and human review instructions, and must give notice of material updates. Neither package exists yet (P03 ES-G21, Not met).
- **Product guidance** says nothing about prohibited uses, such as using early warning indicators for discipline or placement (P01 ES-016).
- **FTC Act Section 5:** accuracy claims in sales materials must be substantiated.
- **FERPA:** the models train on de-identified, aggregated data only (P03 ES-G13, Met).

### 2.5 Student Health clinic AI (AI-007 to AI-009)
| Rule | Use cases | What it means here |
|---|---|---|
| State recording consent laws | AI-007 | In all-party consent states, recording may start only after every party consents. Florida, Fla. Stat. 934.03(2)(d), is the worked example. Today consent is asked by script but not captured in a required field (P03 SH-G30) |
| HIPAA (nonstudent patients) and FERPA (student patients' treatment records) | AI-007, AI-009 | The scribe vendor has a BAA with no-training terms (SH-G13). Records of student patients are the institutions' treatment or education records, not PHI. Counsel must confirm that the vendor contract also carries school-official and redisclosure terms for them |
| 45 CFR 92.210 (N62-R07) | AI-009; AI-007 if suggestion features are enabled; AI-008 if used to support clinical decisions | The urgent care sites accept Medicaid, so Student Health must make reasonable efforts to identify decision support tools that use race, color, national origin, sex, age, or disability as inputs, and mitigate the risk. 45 CFR 92.4 defines these tools to include non-automated ones. No inventory exists (SH-G29) |
| Colorado SB26-189 | All | Carve-out for HIPAA covered entities, except for employment decisions. Student Health also has no Colorado sites |

## 3. Risk tiers (repository rubric plus the group children rule)
- **High:**
  - AI-001: a substantial factor in access to education, because it decides who gets human help to apply.
  - AI-004: children use it directly (group rule), and harmful content is a child safety risk.
  - AI-008: talks with students who may be in crisis and would shape access to counseling, a health care decision.
- **Medium:** AI-002, AI-003, AI-005, AI-006, AI-007, AI-009, AI-010. A person makes the final decision, but outputs influence decisions about people or enter their records. AI-005 and AI-006 are Medium for the group as developer; customers that use them in consequential decisions must treat them as High.
- **Low:** AI-011.

**Re-tier triggers:**
- any use of AI-002 or AI-005/AI-006 outputs for admission, aid, standing, discipline, or placement;
- proctoring flags that start integrity cases without faculty review (AI-003);
- tutor outputs used for grading or placement (AI-004 re-assessment);
- scribe suggestion features (AI-007 to High);
- any predictive tool found in the EHR inventory (AI-009, tier set per tool).

## 4. MEASURE
Results come from monitoring, testing, and reviews between 2026-05 and 2026-08.

### 4.1 Admissions applicant scoring (AI-001)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Local validation of bands against enrollment outcomes | Not done. The vendor validated on pooled data from its customers only | **No** (due 2026-11-15) |
| Safe (human help) | Share of Low-band applicants who received any call from a representative (sample of 200) | 0 of 200 | **No**. Low band means no human contact |
| Accountable and transparent | Applicant notice that a scoring model sets outreach; Colorado and California readiness | No notice; readiness not started | **No** |
| Explainable and interpretable | Representatives see the top 3 factors; the vendor discloses the full feature list | Top factors shown; full feature list not disclosed | Partial |
| Privacy-enhanced | Contract bars the vendor from training on college applicant data; no FAFSA data in inputs | Contract silent on training; no FAFSA data | Partial |
| Secure and resilient | Vendor SOC 2; SSO with MFA | Reviewed (P09 VR-03); MFA in place | Yes |
| Fair, with harmful bias managed | **Preliminary screen** (2026-08-20, 2025-26 applications): Low-band rate ratio against the reference group | Age 25 and older: 39% vs 22% under 25 (ratio 1.77). Black applicants: 36% vs 27% for white applicants (1.33). Hispanic applicants: 31% vs 27% (1.15). Online-program applicants: 33% vs 24% on campus (1.38) | **Flagged** (3 of 4 outside 0.8 to 1.25) |

The preliminary screen counts placements only. The formal test due 2026-11-15 adds outcome-based metrics, so the council can see whether Low-band applicants who were not contacted enrolled at lower rates than similar applicants who were. Age and home ZIP code are the likely drivers, because older and online applicants respond to email less often.

### 4.2 Student-success risk scoring (AI-002), spring 2026 term
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | High band against actual outcomes (withdrawal or a failing grade). Thresholds: recall at least 60%, precision at least 35% | About 260,000 students scored. Recall 63%, precision 37% | **Yes**, narrowly |
| Safe | Review of 120 advisor notes for use of the score to discourage enrollment or limit services | 5 notes cited the score when suggesting the student "pause enrollment" | **No** |
| Privacy-enhanced | No FAFSA-derived or health inputs | Pell eligibility and other FAFSA-derived fields still inputs; clinic visit counts used until 2026-08-07 | **No** |
| Accountable and transparent | Student notice; FERPA annual notice names outsourced school officials | No student notice; annual notice silent (POAM-021) | **No** |
| Explainable and interpretable | Advisors see the top 3 factors and can explain them | Yes in 18 of 20 advisor interviews | Yes |
| Secure and resilient | Score access limited to the caseload; warehouse roles | All advisors see all scores; warehouse roles too broad (POAM-005) | Partial |
| Fair, with harmful bias managed | Flag-rate ratio; false positive rate difference | Black students flagged at 1.41 times the rate of white students. Online students' false positive rate 24% vs 12% on campus. Age bands within thresholds (ratio 0.94) | **Flagged** (2 disparities) |

The disparities trace mainly to three inputs:
- **Pell eligibility** is a proxy for income, and it must be removed anyway under HEA sec. 483.
- **Home ZIP code** is a proxy for race and income.
- **LMS login frequency** penalizes online students who work in longer, less frequent sessions.

### 4.3 Online proctoring (AI-003), spring 2026 term
| Metric | Result | Pass? |
|---|---|---|
| Flag rate overall; share of reviewed flags that faculty confirmed as misconduct | 6.2% of about 1.9 million sessions flagged; 8% of reviewed flags confirmed | Yes (information only) |
| Flag rate for students with approved testing accommodations vs others (Section 504); flag if the ratio is above 1.25 | 11.8% vs 6.0% (ratio 1.97) | **Flagged** |
| Integrity cases from flags with a documented faculty review of the video (target 100%; sample of 40) | 37 of 40 | **No** |
| Identity verification accuracy by student group (vendor data) | Overall first-attempt failure 3.1%; vendor has not supplied group-level data | **No** |
| Video and image deletion verified each term (HE-013) | Retention set to 1 term; deletion not yet verified | Partial |

### 4.4 K-12 AI tutoring assistant (AI-004), using AI 600-1 risk areas
Post-launch sampling ran 2026-05 to 2026-07 (3,000 conversations, 1,200 of them from grades 3 to 5).

| AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Dangerous, violent, or hateful content; obscene, degrading, or abusive content | Age-inappropriate responses in sampled grade 3 to 5 conversations (target 0) | 3 of 1,200 | **No** |
| Confabulation | Teacher review of 500 math and reading explanations: factual or calculation errors (target under 2%) | 4.2% | **No** |
| Data privacy | Conversations containing a child's full name with a home address or phone number; input redaction; retention period for transcripts (312.10) | 1.1% of sampled conversations; no redaction; no retention period stated | **No** |
| Information security | Red-team test for prompt injection and data leakage | Not done (POAM-013) | **No** |
| Value chain and component integration | Model provider in the SOC 2 description; subprocessor notice; provider attestation | None of the three | **No** |
| Harmful bias and homogenization | Response quality for English learners and by grade band | Not measured | **No** |
| Human-AI configuration | Students told they are using AI; teacher dashboards; district off switch | In place | Yes |

### 4.5 Analytics products (AI-005, AI-006) and clinic AI (AI-007, AI-009)
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-005, AI-006 | Developer documentation package (intended uses, data, limitations, human review) for each customer | Not prepared | **No** |
| AI-005, AI-006 | Subgroup performance (recall and false positive rate by grade band, sex, and race) published to customers | Validated each release on de-identified pooled data; no subgroup results shared | Partial |
| AI-007 | Critical errors (drug, dose, allergy, laterality) reaching a signed note (target 0; 1,500 notes sampled) | 2 found, both corrected before signing | Yes |
| AI-007 | Recorded visits with consent captured (target 100%) | 88% | **No** |
| AI-009 | Share of EHR decision support tools inventoried with inputs reviewed (92.210) | 0% (inventory not started) | **No** |

### 4.6 Bias testing plan (applies to AI-001, AI-002, AI-003, AI-005, AI-006)
| Element | Plan |
|---|---|
| Groups compared | Race and ethnicity (self-reported for IPEDS), sex, age band (under 25, 25 and older), modality (online, on campus), Pell status for reporting only (never as an input), and approved testing accommodations for AI-003. For AI-005 and AI-006, the groups available in de-identified customer data |
| Metrics | (1) Adverse-band rate ratio against the reference group (Low band for AI-001, High band for AI-002, flag rate for AI-003). (2) False positive rate difference. (3) Recall by group, so no group is under-served. (4) For AI-001, enrollment rate by band and group |
| Thresholds | Rate ratio between 0.8 and 1.25; false positive rate difference of 10 percentage points or less; recall within 10 points of the overall rate. Any breach is a flag that needs a documented review and an owner decision |
| Small groups | Report counts with every rate. Pool groups under 100 across terms or cycles before a pass or fail decision. Never publish results for groups under 10 |
| Frequency and owner | Before deployment, after every model or input change, and every term (each admissions cycle for AI-001). The director of institutional research runs the college tests; the Education Software data science lead runs the product tests; the Group Chief Privacy Officer's team reviews both |
| Action on failure | Remove or replace proxy inputs. Change band rules only if counsel agrees the change is lawful. Retest before wider use. A High-tier model that fails twice in a row goes back to the council |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** from 2026-12-15, no applicant may be placed in email-only outreach without a representative reviewing the application. Every applicant gets at least one human contact attempt, and representatives can override the band without justification. The score never affects an admission decision.
- **AI-002:** the score is a prompt for supportive outreach only. Advisors see scores only for their caseload. Overrides are recorded in the advising note, and the monthly note review covers prohibited uses.
- **AI-003:** faculty review the flag and the video before opening any integrity case. Students with accommodations are reviewed with the accommodation record in view. Students can contest a flag.
- **AI-004:** teachers see conversations, and districts can turn the feature off per school. Responses are filtered by grade band. The tutor never grades or places students.
- **AI-007:** clinicians review, edit, and sign every note. Recording cannot start until the consent field is completed.

**Monitoring:**
- Monthly metrics go to the division owners.
- A quarterly High-tier report goes to the council and the board risk committee.
- These metrics feed P01 risks GR-04, HE-008, HE-009, HE-029, ES-003, ES-004, ES-012, ES-016, SH-012, SH-013, and SH-018.

**Incident handling:** AI failures follow POL-03 and P08 if they harm a student, child, or patient, disclose protected data, or breach customer commitments. A model provider incident follows the Education Software customer notice path (72 hours under standard contracts, or shorter where district terms require). Misuse of a score is a policy violation under POL-01 4.7.

**Decommissioning:**
- Each use case has an off switch and a fallback already covered by the BIA (P05), for example manual outreach lists, advising from rosters and grade reports, live proctoring, standard tutoring content, and standard documentation.
- Stop criteria:
  - a vendor refuses no-training terms;
  - disparities stay above the thresholds after two cycles of remediation;
  - any use of a score in an adverse decision without human review;
  - for AI-004, a confirmed harmful response to a child after the test program is complete.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 admissions scoring | **Continue with conditions** (council, 2026-08-27; board risk committee informed 2026-09-15) | Formal bias test by 2026-11-15. Applicant notice and human review rule by 2026-12-15. Colorado deployer readiness (notice, adverse-outcome explanation, correction and human review process, 3-year records) by 2026-12-31 (POAM-022). Contract amendment barring training on college data, with model documentation, by 2026-12-31. Counsel decision on the CPPA ADMT rules by 2026-11-30. No new scoring uses until all conditions are met |
| AI-002 student-success scoring | **Continue with conditions** | FAFSA-derived inputs removed by 2026-11-30 (POAM-007). Clinic features permanently excluded; purge certified by 2026-10-31 (POAM-006). Caseload-only visibility and human review rule in the advising procedure by 2026-12-31. Home ZIP code removed and LMS activity measured by submissions, then fairness tests re-run before spring 2027 scores are used. Student notice and updated FERPA notice by 2026-12-31 (POAM-021) |
| AI-003 proctoring | **Continue with conditions** | Written faculty review rule by 2026-12-31. Accommodation-aware review and flag-rate monitoring each term. Vendor's identity verification accuracy data by student group requested at the 2027 renewal. Deletion verified each term (HE-013). All by 2027-03-31 |
| AI-004 AI tutor | **Continue in authorized pilot districts only; no new districts** | Subprocessor notices by 2026-10-31 and written authorization from the 31 districts with older contracts by 2026-11-30, with the tutor turned off where authorization is not received (POAM-014). "Safe for every grade" claim withdrawn by 2026-10-31. Test plan by 2026-11-15; red-team, content safety, and accuracy tests complete by 2026-12-31 (POAM-013). Input redaction for names and contact details, and a transcript retention period in the written policy (312.10), by 2026-12-31. Model provider attestation by 2026-12-31 (ES-012). SOC 2 description updated for the period ending 2027-06-30 |
| AI-005, AI-006 analytics products | **Continue** | Developer documentation packages with intended uses and prohibited uses (including discipline and placement) sent to all customers, the college included, by 2026-12-31, ahead of the Colorado effective date (ES-G21, ES-016). Subgroup performance results in the package from 2027 |
| AI-007 AI scribe | **Continue the pilot; no expansion** | Consent field mandatory before recording by 2026-12-31 (SH-012). Counsel confirms FERPA school-official and redisclosure terms in the vendor contract for student patients' records by 2026-11-30. Suggestion features stay off |
| AI-008 counseling chatbot | **Not approved** (P01 SH-013, avoided) | Any future proposal needs a full High-tier assessment, a clinical safety design for crisis messages that routes students to a person, and counseling leadership approval |
| AI-009 EHR decision support | **Continue** | Inventory and input review under 45 CFR 92.210 by 2027-03-31 (SH-018), with any predictive tool tiered individually |
| AI-010, AI-011 | **Approved** | Standard monitoring. AI-010 is prohibited for admissions, aid, advising, integrity, and clinical decisions |

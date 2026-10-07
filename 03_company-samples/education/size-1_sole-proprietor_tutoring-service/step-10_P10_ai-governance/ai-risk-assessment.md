# AI Use Assessment: Consumer AI Assistant for Student Scoring and Progress Reports (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (tutoring and educational support service) |
| Tier / Vertical | Sole Proprietorship / Educational Services |
| AI use case | AI-001: a free consumer AI assistant (SYS-09) used since March 2026 to rate each student's "support level", recommend SAT boot camp starting levels, and draft parent progress reports. Adapted from the registry default ("AI admissions and student-success risk scoring"): a tutor has no admissions, and this is the equivalent scoring use |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 for generative AI risks |
| Assessor and decision | Owner-tutor, 2026-07-24; decision 2026-07-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
For 31 students in the spring term the owner pasted first names, grades, assessment and portal assignment scores, and accommodations (for example "504 plan, extended time, ADHD") into the assistant and asked it to rate each student's support level (low, medium, high). In June 2026 it recommended starting levels for 12 SAT boot camp students, and in May 2026 it drafted about 45 parent progress reports. The account is a free personal one: the terms allow the vendor to use prompts to improve its models, and chat history was on. No parent was told or asked.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| COPPA Rule, 16 CFR 312.5(a)(2) and 312.8(c) (N61-R03) | **Yes** | Portal assignment scores are information collected online from children. Giving them to a vendor that may use them for its own purposes is a disclosure to a third party, which needs separate parental consent and written security assurances. Neither existed |
| Fla. Stat. 501.171(2) | **Yes** | Disability and diagnosis information with names must be protected by reasonable measures. Whether the pasting is itself a "breach" under 501.171 is a question for counsel (the owner entered it on purpose; no outsider accessed it) |
| FTC Act Section 5 | **Yes** | The enrollment agreement tells families their information is used to teach their child; using it to feed a vendor's models is a practice families could not expect |
| Colorado SB26-189 (education decisions) | No | It applies to consequential decisions affecting Colorado consumers from 2027-01-01; the business serves only Florida families |
| FERPA | No | No Department of Education funds (34 CFR 99.1) |

## 3. Risk tier (repository rubric)
**AI-001: High.** The output was a substantial factor in an education decision about a child: the owner kept 27 of 31 support levels and all 12 boot camp placements as the assistant gave them. Disability information was an input. **AI-002 (de-identified drafting only): Medium.** It shapes what parents read, but the owner makes every judgment and writes every score.

## 4. Measure (tests on 2026-07-16)
| Characteristic | Test | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Owner re-placed the 12 boot camp students with the publisher's diagnostic rubric | 3 of 12 placements differed by one level | No |
| Accountable and transparent | Could the owner explain each support level to a parent? | Not for 9 of 31; the assistant gave no reasons that tied to the scores | No |
| Fair, with harmful bias managed | Compare high-support ratings for students with and without IEP or 504 plans at similar scores | 7 of 9 students with plans rated high support, against 8 of 22 without; the groups are too small to measure, but disability was an input and may have pushed ratings up | No |
| Privacy-enhanced | Data minimization and vendor terms | Names, scores, and accommodations sent to a vendor that may train on them | No |
| Safe; secure and resilient | Account security | Personal account with a password only | No |
| Explainable (drafts) | Owner checked 10 drafted progress reports against session notes | 2 had a wrong score; the owner had caught 1 before sending | Partly |

## 5. Data-sharing rules and human review (Govern and Manage)
1. No student name, initials, school, score tied to a student, accommodation, or portal content goes into any AI tool (POL-01 9.5).
2. AI may be used only on a business plan whose terms bar training on customer data and give written security assurances, and only for wording.
3. **Support levels and placements are decided by the owner** from the diagnostic rubric and session observations. Accommodations are applied as the plan says, never used to predict a level.
4. Every AI-drafted report is rewritten and signed by the owner, who adds names and scores only after drafting and checks every number against the session notes. A wrong score in a sent report stops AI drafting until the cause is understood.
5. An incident with an AI vendor (data exposure, unexpected retention) is handled under P08.

## 6. Decision (approved 2026-07-31)
**AI-001: Reject and retire** (paused 2026-07-13). By 2026-08-14 (P01 R-006, POAM-005):
1. Delete the chat history, turn off model-improvement use, and send the vendor a written deletion request; keep the reply.
2. Ask counsel whether the disclosure requires notice under Florida law, and tell the affected families in the new direct notice what was shared and what was done about it.
3. Re-place any boot camp student whose rubric level differs, and tell those families.

**AI-002: Approve with conditions** (rules 1, 2, and 4 above). Re-run this assessment before any new AI use or a change of vendor.

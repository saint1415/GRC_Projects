# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Class II regional freight railroad, north and central Florida) |
| Tier / Vertical | Mid-Market / Transportation Systems |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. Anchor case: AI-001 track and equipment defect detection (computer vision) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook, with the Generative AI Profile (NIST AI 600-1) for AI-004 and AI-005 |
| Assessors / date | vCISO and Cybersecurity Manager (security), Chief Engineer and Chief Mechanical Officer (safety and FRA rules), HR Director and General Counsel (employment law), Director of Safety, Security, and Hazmat (SSI), 2026-08-24 to 2026-09-10 |
| Decision | Chief Operating Officer, 2026-09-15; High-tier decisions noted by the CEO |

## 1. Summary
Four of the five tools (AI-001, AI-002, AI-003, AI-005) were adopted by departments without a security, legal, or safety review, and there is no AI use standard (gap 12). AI-004 was bought by IT with enterprise terms. None of the tools makes a safety decision on its own today, but three need conditions before they can stay in use or grow:
- **AI-001 defect detection:** recall is below target in low light and on jointed rail, inspectors check flagged spots first, and the vendor contract is silent on reuse of company imagery.
- **AI-003 applicant screening:** ranked about 2,400 applicants with no adverse impact analysis. A preliminary check found a selection-rate ratio below four-fifths, so ranking was switched off on 2026-09-01.
- **AI-005 shipper chatbot:** reads car data, including hazmat flags, with no testing for cross-customer leakage.

| ID | Use case | Risk tier | Generative? | Decision |
|---|---|---|---|---|
| AI-001 | Track and equipment defect detection (computer vision) | High | No | Approve with conditions; branch line expansion on hold |
| AI-002 | Locomotive predictive maintenance analytics | Medium | No | Approve with conditions |
| AI-003 | Applicant screening (ranking) in the applicant tracking system | High | No | Ranking stays off until conditions are met |
| AI-004 | Enterprise generative AI assistant | Medium | Yes | Approve; expand to all office users with public tools blocked |
| AI-005 | Shipper portal chatbot | Medium | Yes | Approve with conditions by 2026-12-31, or switch off |

Tiers: 2 High, 3 Medium, 0 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** vCISO, with the Chief Engineer as the safety lead. Each use case has a business owner (inventory).
- **Policies (approved 2026-09-15, effective 2026-10-01):**
  - POL-01 4.15: AI tools approved before use; no AI output replaces an inspection or decision that an FRA rule assigns to a qualified person.
  - POL-04 4.11: no Restricted data, SSI, or infrastructure imagery in unapproved AI tools.
  - POL-05 4.8: approved-AI list by data class; human review of outputs.
  - STD-05 AI use standard: due 2026-12-31 (POAM-021).
- **Approved-AI list:** kept by the Cybersecurity Manager on the intranet, with the data classes each tool may receive. Today it lists AI-001, AI-002, AI-004, and AI-005 with their conditions. AI-003 ranking is listed as paused. Public generative AI tools are not approved for any company data and will be blocked at the DNS filter when AI-004 reaches all office users (P01 R-044).

### 2.1 Lightweight AI governance process
A mid-market railroad does not need a standing AI committee. It needs a short gate before purchase and a monthly rhythm, reusing existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature turned on in an existing tool (the way AI-003 arrived), submits a one-page intake: purpose, users, data, vendor, decisions affected, link to any FRA-regulated task | Business owner | 15 minutes |
| 2. Triage | Provisional tier with the repository rubric; purchasing gate (no purchase order or feature activation without approval, POL-01 4.12) | Cybersecurity Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, data terms (no training on company data, deletion, incident notice), and a business reviewer. **High:** full MAP and MEASURE assessment like this one, with a bias or performance plan; safety review by the Chief Engineer or Chief Mechanical Officer for anything touching inspection or train operations; employment law review by General Counsel for anything touching hiring | Cybersecurity Manager; General Counsel; safety reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Cybersecurity Manager. Medium: the **AI review group** (vCISO, Chief Engineer, General Counsel), 30 minutes a month. High: the AI review group recommends; the COO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owner reports the agreed metrics monthly (High) or quarterly (Medium); AI incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model version change, new data type, new territory or population, or a safety event | AI review group | Annual |

**Vendor features.** Most AI at this company arrives as a feature inside a product the company already buys (AI-003 is the example). STD-03 now requires vendors to give notice before turning on AI features that process company data, and IT checks new release notes monthly for them.

## 3. MAP
| Item | AI-001 Defect detection | AI-002 Predictive maintenance | AI-003 Applicant screening | AI-004 Enterprise assistant | AI-005 Shipper chatbot |
|---|---|---|---|---|---|
| Purpose | Find suspected track and car defects sooner and point inspectors to them | Predict component failures so locomotives go to the shop before they fail on the road | Rank applicants against the posting | Draft, summarize, and search documents | Answer shippers' car status and service questions |
| Users | 14 qualified track inspectors; 6 mechanical inspectors at the portals; the Chief Engineer | Mechanical supervisors and planners | 4 recruiters | 120 office users (all office users by 2027-03-31) | Shipper staff (about 310 shippers) |
| Affected people | Crews, roadway workers, and the public at 312 crossings; incidental images of people | Crews (locomotive condition) | About 2,400 applicants (2026-02 to 2026-08) | Indirect | Shipper staff |
| Data | Track, bridge, signal, and car imagery; GPS; inspector decisions | Locomotive telemetry and fault codes | Resumes and application answers | Internal and Restricted documents | Shipper's own car data, including hazmat flags |
| Build or buy | Buy (inference in the company cloud) | Buy (vendor cloud; gateway on 52 locomotives) | Buy (SaaS feature) | Buy (enterprise agreement) | Buy (SaaS) |
| Main laws and rules | 49 CFR 213.233, 213.7, 215.13; part 1520 | 49 CFR 229.21, 229.23; SD III.B.2.b for the gateway | Title VII; 29 CFR part 1607; ADA; Fla. Stat. 760.10 | 49 CFR 1520.9 | FTC Act Section 5; 49 CFR 1520.9; contracts |

**Laws considered and not applicable:**
- **State AI laws such as Colorado SB26-189:** the company operates and hires only in Florida, and this assessment did not identify a Florida statute specific to AI that applies to these uses. Florida-specific AI law was not researched beyond the employment statute above.
- **FRA automated track inspection rules:** none apply as long as AI-001 only supplements the required visual inspection. Any reduction in visual inspection frequency would need FRA relief under 49 CFR part 211 (waiver petitions are decided under 211.41). The company is not seeking one.

### 3.1 AI-001: the inspection rules (anchor case)
49 CFR 213.233(b) requires each track inspection to be made "on foot or by traversing the track in a vehicle at a speed that allows the person making the inspection to visually inspect the track structure," and allows that "mechanical, electrical, and other track inspection devices may be used to supplement visual inspection." The cameras on the hi-rail vehicles are such a device. **They may only supplement the inspector's visual inspection, and only a person designated under 213.7 decides on remedial action.**

At the portals, car flags are extra information for the mechanical inspectors. The pre-departure inspection of cars placed in a train (49 CFR 215.13) is unchanged.

**Imagery as sensitive information.** Detailed images of bridges, signal equipment, and PIH tank cars in yards are Restricted under POL-04, and could become SSI if they reveal security measures. Until 2026-09 the vendor's service account could read every bucket in the corporate workloads account, including file services backups that hold SSI (P04 finding 3; P01 R-041). It is now limited to the inference bucket.

### 3.2 AI-003: employment law
- **Title VII** prohibits employment practices that cause a disparate impact on the basis of race, color, religion, sex, or national origin unless the employer shows the practice is job related and consistent with business necessity (42 U.S.C. 2000e-2(k)). A ranking tool used to decide whom recruiters call first is a selection procedure.
- **Uniform Guidelines on Employee Selection Procedures (29 CFR part 1607)** call for records that show the impact of selection procedures (1607.4(A)) and state the four-fifths rule: a selection rate for any race, sex, or ethnic group that is less than four-fifths (80%) of the rate for the group with the highest rate will generally be regarded as evidence of adverse impact (1607.4(D)). Smaller differences can matter with large samples, and larger differences may not with small samples.
- **ADA:** using selection criteria that screen out or tend to screen out individuals with disabilities is discrimination unless the criteria are job related and consistent with business necessity (42 U.S.C. 12112(b)(6)). Gaps in work history, which the ranking appears to penalize, can be a proxy for disability.
- **Florida Civil Rights Act (Fla. Stat. 760.10):** the state law on unlawful employment practices applies in parallel.

**Preliminary check (2026-08-27).** For conductor trainee postings (1,120 applicants), the share ranked in the top tier was 24% for men and 17.8% for women who self-identified, a ratio of 0.74, below four-fifths. Race and ethnicity groups were too small for a reliable comparison at that stage. The HR Director switched ranking off on 2026-09-01. The full analysis, covering all postings and the stage at which recruiters actually called applicants, is due 2026-11-30 (POAM-021).

## 4. Risk tiers and MEASURE
### 4.1 AI-001 defect detection: High
**Tier rationale:** the rubric puts in the High tier any AI that "can affect physical safety or critical infrastructure operations." A missed broken joint bar can derail a train carrying PIH cars. The risk is manageable because the model decides nothing. The main danger is **automation bias**: inspectors trust the model and look less carefully where it shows nothing (P01 R-042).

Data: 112 hi-rail runs on the Jacksonville and Central Subdivisions, 2026-03 to 2026-07, compared with the inspectors' own findings on the same runs; portal flags compared with mechanical inspection records for the same cars.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Recall against inspector findings; target 90% or more overall and 95% or more for joint bar and rail defects | 214 of 243 defects detected (88%). Joint bar and rail: 66 of 71 (93%) | **No.** Below target on both; acceptable only because the model supplements inspection |
| Valid and reliable | Precision (flags confirmed as defects) | 214 of 690 flags confirmed (31%) | Noted. Low precision drives alert fatigue |
| Safe | No inspection skipped or shortened; inspection records still show visual inspection | Frequencies unchanged; 5 of 14 inspectors said they "check the flagged spots first" | **Partial.** Automation bias risk |
| Secure and resilient | Inference in the company account; vendor access through a restricted service account; images encrypted; model updates through change control | Service account restricted 2026-09; change control for model versions added (P04) | **Partial** until the contract is amended |
| Accountable and transparent | Every flag has an inspector decision recorded; model version logged | Decisions recorded for 96% of flags; model version logged since 2026-09 | **Partial** |
| Explainable and interpretable | Inspector sees the image crop, defect class, and confidence | Available in the review app | Yes |
| Privacy-enhanced | Faces and license plates blurred at ingestion; images kept 1 year; no vendor reuse without consent | Blurring and 1-year retention from 2026-10 (P04); contract silent on reuse | **No** until the contract is amended |
| Fair, with harmful bias managed | Performance parity across operating conditions: (a) CTC main line vs branch lines; (b) daylight vs low light; (c) jointed rail vs continuous welded rail; (d) dry vs wet; (e) heavy vegetation vs clear. Flag any condition more than 5 percentage points below overall recall | Low light 79%; jointed rail 84%; branch lines **not tested** (lighter, jointed rail; more vegetation) | **No.** Low light and jointed rail flagged |

**Fairness in this context.** AI-001 makes no decisions about people, so fairness means performing equally well across the conditions it meets. A model trained mostly on main line imagery does worse on the lighter, jointed rail of the branch lines. That is why expansion to the branch lines is on hold.

### 4.2 AI-002 predictive maintenance: Medium
**Tier rationale:** it influences maintenance planning, but mechanical supervisors decide all shop work and the daily and periodic FRA inspections (49 CFR 229.21, 229.23) are unchanged. Its failure mode, a missed early warning, leaves the company where it was without the tool. **Re-tier to High** if anyone proposes using it to defer a repair or to set an inspection interval. The model is not used for the 184-day periodic inspection interval in 229.23(b), which depends on the locomotive's own onboard condition monitoring equipment.
- Valid and reliable: of 41 alerts in 2026 H1, 29 led to a confirmed component problem (71%); 6 road failures had no prior alert. Monitored quarterly.
- Secure and resilient: the telemetry gateway on 52 locomotives sends data to the vendor cloud and is described by the vendor as read-only, separate from the PTC apparatus (P01 R-046). **Not yet confirmed in writing** and not in the OT inventory.

### 4.3 AI-003 applicant screening: High
**Tier rationale:** it is a substantial factor in an employment decision, a consequential-decision category in the rubric. Measures: selection-rate comparisons by sex, race, and ethnicity at each stage (ranked top tier, called, interviewed, offered), using the four-fifths rule as the first screen and a statistical significance test where groups are large enough; a review of which resume features drive the ranking, including employment gaps and location; and the vendor's validation evidence for the specific job families. Result so far: section 3.2.

### 4.4 AI-004 enterprise assistant: Medium
**Tier rationale:** internal productivity use, but SSI and Restricted data could be entered, and it is generative. AI 600-1 risks that apply: **Information Security** and **Data Privacy** (company documents in prompts; addressed by enterprise terms with no training on company data, company-controlled retention, and SSO with MFA); **Confabulation** (invented facts in drafts; addressed by human review before any external use); **Human-AI Configuration** (over-reliance; addressed in training); **Value Chain and Component Integration** (the vendor's model provider; covered by the vendor's SOC 2 and contract). SSI remains prohibited in AI-004 until the Director of Safety, Security, and Hazmat approves a configuration that keeps SSI inside the restricted library's access controls.

### 4.5 AI-005 shipper chatbot: Medium
**Tier rationale:** it interacts directly with customers, but a person handles any decision. AI 600-1 risks that apply: **Information Security** (prompt injection to reach another shipper's data), **Confabulation** (wrong car status or wrong hazmat information), and **Data Privacy**. A 50-prompt cross-customer test has not been run (P01 R-045). Hazmat questions must go to staff, never to the model.

## 5. MANAGE
**Human-in-the-loop rules (written, signed by the business owner):**
- **AI-001:** the model only adds findings. Inspectors perform and record every required visual inspection as before. Every track flag is reviewed by a qualified inspector within 24 hours, or before the next train where the flag is a joint bar or rail defect. The inspector decides remedial action under part 213; the model never sets or clears a slow order. Portal car flags go to a mechanical inspector before the train departs. Training says plainly that **"no flag" does not mean "no defect."**
- **AI-002:** alerts create a work order for a supervisor's decision; no alert closes or defers a defect.
- **AI-003:** ranking off. If reinstated, recruiters must review applicants in date order, not rank order, until the full analysis shows no adverse impact; quarterly selection-rate review thereafter.
- **AI-004:** human review of every output used outside the team; no SSI.
- **AI-005:** AI disclosure at the start of each chat; hand-off to staff for hazmat, RSSM, billing disputes, and any request to change an order.

**Monitoring:**
| Use case | Metric | Frequency | Owner |
|---|---|---|---|
| AI-001 | Recall and precision by condition; flag review within 24 hours; model version | Monthly; quarterly report to the AI review group | Chief Engineer |
| AI-002 | Alert precision; road failures without a prior alert | Quarterly | Chief Mechanical Officer |
| AI-003 | Selection rates by group at each stage | Quarterly (if reinstated) | HR Director |
| AI-004 | Data loss prevention events; user feedback on errors | Quarterly | vCISO |
| AI-005 | Transcript sample of 50 a month for wrong or cross-customer answers | Monthly | Director of Customer Service and Car Management |

**Incident handling.** A security incident affecting any AI service or its data follows the P08 runbooks. A model failure (for example a vendor update that drops AI-001 recall) is handled by pausing the model; inspections and maintenance continue unchanged. Any defect missed by AI-001 that leads to an FRA-reportable accident is investigated as part of the part 225 process.

**Decommissioning criteria:**
- AI-001: stop and require deletion of vendor-held data if the contract amendment is not signed by 2026-10-31, or if monthly recall on joint bar and rail defects falls below 90% for 2 months in a row.
- AI-003: retire the ranking feature if the full analysis shows adverse impact that the vendor cannot correct and validate.
- AI-005: switch off if the conditions below are not met by 2026-12-31, or on any confirmed cross-customer disclosure.

## 6. Decision
Chief Operating Officer, 2026-09-15 (High-tier decisions noted by the CEO the same day).

**AI-001: Approve with conditions.** Use continues on the Jacksonville and Central Subdivisions and the 2 portals only if, by 2026-10-31:
1. a contract amendment bars any vendor use of company imagery for training or other purposes without written consent, requires deletion on request and at contract end, and requires security incident notice within 24 hours (P01 R-041);
2. the written human-in-the-loop rule above is signed by the Chief Engineer and briefed to all 14 inspectors (P01 R-042);
3. face and license plate blurring and 1-year retention are in force (P04), and model version changes go through change control with a regression test against the defect validation set.
**Expansion to the branch lines** needs a 3-month shadow test there with recall of at least 90% overall, at least 95% for joint bar and rail defects, and no condition more than 5 percentage points below overall, including low light and jointed rail.

**AI-002: Approve with conditions.** Written confirmation from the vendor of the gateway's one-way design and its addition to the OT inventory by 2027-03-31 (P01 R-046); re-tier trigger as in section 4.2.

**AI-003: Ranking stays off.** Reinstatement only after the full adverse impact analysis (due 2026-11-30), General Counsel's review, the vendor's job-related validation evidence, and the AI review group's recommendation to the COO.

**AI-004: Approve.** Expand to all office users by 2027-03-31 and block public generative AI tools at the same time (P01 R-044).

**AI-005: Approve with conditions** by 2026-12-31: the 50-prompt cross-customer test passed with no disclosure; hazmat and RSSM questions routed to staff; no-training terms in the vendor contract.

**Program condition:** STD-05 issued by 2026-12-31, including the vendor AI feature notice term (POAM-021).

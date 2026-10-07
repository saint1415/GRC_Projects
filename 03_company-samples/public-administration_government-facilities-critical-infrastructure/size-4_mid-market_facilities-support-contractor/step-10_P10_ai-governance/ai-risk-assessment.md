# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed facilities support contractor operating government buildings) |
| Tier / Vertical | Mid-Market / Government Services and Facilities |
| Scope | Portfolio of 6 AI use cases (AI-001 to AI-006), inventory in `ai-use-case-inventory.csv`. The registry use case, facial recognition for facility access, is AI-001 and AI-002 |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-005 |
| Assessors / date | Security Systems Manager and Security Manager (security), General Counsel (legal), HR Director (AI-006), Controls Engineering Manager (AI-004), chaired by the vCISO, 2026-08-24 to 2026-09-10 |
| Decision | Chief Operating Officer, 2026-09-15; High-tier decisions noted by the CEO |

## 1. Summary
Three of the six uses (AI-001, AI-003, AI-006) went live as features of products the company already used, switched on at a customer's request or by a department, without a security, privacy, or fairness review (gap 11). AI-002 is a County A request. AI-004 and AI-005 were bought deliberately.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Face verification (1:1) at the County A government center | High | Approve with conditions; no new enrollments until met |
| AI-002 | Face identification (1:N) of the public in County A lobbies | High | Not approved; the company will not operate it |
| AI-003 | Video analytics (intrusion and loitering) at 4 state sites | Medium | Approve with conditions |
| AI-004 | BAS fault detection analytics (advisory) | Medium | Approve; autonomous mode stays disabled |
| AI-005 | Enterprise generative AI assistant (pilot) | Low | Approve the pilot with conditions |
| AI-006 | Candidate ranking in the HR suite | High | Suspend until an adverse impact test passes |

Tiers: 3 High, 2 Medium, 1 Low.

**Who decides what.** For AI-001 to AI-003 the **customer** owns the building, the access control system, and the decision to use the feature. The **company** configures and operates it, holds the data in tenants it administers, and can refuse to operate a use it considers unsafe or unlawful. This assessment is the company's decision on whether and how it will operate each one. AI-004 to AI-006 are the company's own decisions.

## 2. GOVERN
- **Accountable owner for the AI program:** vCISO, who chairs the AI review group. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.17: no AI tool or AI feature may be used or switched on without approval.
  - POL-04 4.9: no Restricted data in unapproved AI tools; face templates deleted within 30 days after withdrawal or departure.
  - POL-05 4.11: approved tools only; human review of outputs; no AI or biometric features in customer systems without an approved assessment.
  - STD-05 AI use standard: due 2026-12-31 (POAM-021).
- **Approved-tools list:** kept by the Security Manager on the intranet. Today it lists AI-001 (County A government center employee entrances only, enrolled volunteers only), AI-003 (4 state sites), AI-004 (advisory mode), and the AI-005 enterprise assistant for pilot users.

### 2.1 Lightweight AI governance process
A mid-market company does not need a standing AI committee with a large charter. It needs a short, reliable gate and a monthly rhythm, using existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any request to use an AI tool, or to switch on an AI feature in a company or customer system, gets a one-page intake: purpose, users, people affected, data, vendor, decisions affected | Requesting business owner or program manager | 15 minutes |
| 2. Triage | Provisional tier with the P10 rubric; purchasing and change gate (no purchase order or feature change without approval) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy, and contract terms (no training on company or customer data, deletion, incident notice) plus an accuracy check. **High:** full MAP and MEASURE assessment like this one, with a bias and performance plan and legal review | Security Manager; General Counsel; business reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (vCISO, Security Manager, General Counsel, HR Director when people are affected), monthly for 30 minutes. High: the AI review group recommends, the COO decides and informs the CEO. For customer systems, the customer's written request comes first | As listed | Monthly |
| 5. Monitor | Owner reports agreed metrics monthly (Medium) or monthly with a quarterly deep dive (High); incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type, expansion to a new site or population, or a complaint | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. It is defined by this repository, not by a regulation.

## 3. MAP
| Item | AI-001 Face verification | AI-002 Face identification | AI-003 Video analytics | AI-004 BAS fault analytics | AI-005 Generative assistant | AI-006 Candidate ranking |
|---|---|---|---|---|---|---|
| Purpose | Stop badge sharing and lost-badge misuse at employee entrances | Alert guards when a watch-listed person enters a lobby | Detect people in restricted zones after hours | Recommend fixes for faulty equipment and wasted energy | Draft documents faster | Order applicants for recruiters |
| Users | Security Systems Manager and technicians (configuration); county guards (fallback) | County guards (proposed) | ROC operators | Controls engineers | 40 pilot staff | 3 recruiters |
| Affected people | 1,150 enrolled county employees; employees who decline | Every lobby visitor | People near 4 state buildings after hours, including the public | None directly | People named in drafts | About 2,400 applicants a year |
| Data | Face templates, enrollment photos, match scores | Face images of the public, watch list | Video metadata, alert clips | BAS trend data | Internal documents | Resumes, application answers |
| Build or buy | Configure a vendor feature | Buy (proposed) | Configure a vendor feature | Buy | Buy | Configure a vendor feature |
| Not intended | Identifying anyone without a badge; use on the public; police use; discipline without human review | n/a | Identity matching; automatic dispatch; tracking individuals | Automatic setpoint changes | Restricted data; final decisions | Automatic rejection |

**Applicable laws and rules:**
| Rule | Use cases | How it applies |
|---|---|---|
| Fla. Stat. 501.171 | AI-001, AI-002 | Personal information includes "an individual's biometric data as defined in s. 501.702" with a name (501.171(1)(g)1.a.(VI)). Section 501.702 defines biometric data as data generated by automatic measurements of biological characteristics used to identify a person, and excludes "physical or digital photographs; video or audio recordings or data generated from video or audio recordings". Whether templates computed from the readers' camera images fall within that exclusion is **unsettled; counsel to confirm**. The company treats the templates as biometric data either way. As a third-party agent it must take reasonable security measures (501.171(2)), notify County A within 10 days of a breach determination (501.171(6)(a)), and dispose of records securely (501.171(8)) |
| Fla. Stat. 119.071(5)(g) and 119.0701 | AI-001, AI-002 | The public records exemption for biometric identification information covers only friction ridge detail, fingerprints, palm prints, and footprints (verified 2026-10-07). **It does not name face templates.** Whether another exemption (for example the security system plan exemption in 119.071(3)(a)) protects them is for the County A attorney. As a contractor, the company keeps exempt records confidential and routes requests to the county's custodian (119.0701) |
| Fla. Stat. 119.071(3)(a) | AI-003 | Camera layouts and analytics zones are security system plan information; handled as Restricted (POL-04 4.3) |
| FTC Act Section 5 | AI-001 to AI-006 | Applies to accuracy and privacy claims the vendors and the company make. Government customers are outside FTC jurisdiction; vendors and the company are not |
| Title VII and 29 CFR 1607.4(D) | AI-006 | Employment selection procedures with adverse impact must be justified. The Uniform Guidelines treat a selection rate for any race, sex, or ethnic group below four-fifths of the highest group's rate as generally regarded as evidence of adverse impact (a rule of thumb; small samples and statistical significance matter). Florida employment law reviewed by counsel |
| Customer contracts | AI-001 to AI-004 | County A addendum (cardholder data protection, 24-hour notice); CT-S exhibit; CT-K contract |
| Colorado SB26-189 and other state AI laws | All | Not applicable: the company does business only in Florida. Recheck before any out-of-state contract |
| Federal rules for the GSA buildings | None | GSA's access control uses PIV cards (FIPS 201) and is GSA's system. The company will not propose face recognition or video analytics at the federal buildings |

## 4. Risk tiers
- **AI-001 High:** controls physical access to a government facility (critical infrastructure physical security), processes biometric data, and repeated false rejections affect employees' access to their workplace. The rubric's High tier covers AI that "can affect physical safety or critical infrastructure operations."
- **AI-002 High:** would identify members of the public seeking essential government services, with a much higher chance of misidentification in a 1:N search and no review or appeal design.
- **AI-003 Medium:** no identity matching and no automatic action; a human verifies every alert. **Re-tier triggers:** linking alerts to identity, automatic lock-downs, or alerts sent straight to police.
- **AI-004 Medium:** influences maintenance decisions; a technician makes every change through change control. **Re-tier trigger:** enabling autonomous setpoint changes (would be High, because it would affect critical infrastructure operations, P01 R-036).
- **AI-005 Low:** internal productivity with human review and no Restricted data. **Re-tier trigger:** use with Restricted data or for decisions about people.
- **AI-006 High:** a substantial factor in an employment decision (which applicants recruiters look at first).

**Minimum controls for High:** human review before action; pre-deployment bias testing; impact assessment (this document); notice to affected people; ongoing monitoring.

## 5. MEASURE (by use case)
### 5.1 AI-001 face verification (measurement period 2026-07-01 to 2026-08-31)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | False non-match rate (FNMR): genuine employees rejected per attempt. Target 2% or less | 61,400 attempts; FNMR 2.1% | **No** (slightly above target) |
| Valid and reliable | False match rate (FMR): impostor accepted. Target 0 accepts in a 2,000-attempt local impostor test | Not tested locally; vendor laboratory data only | **Not measured** |
| Safe | No one refused entry on a face result alone; fallback works | Badge plus PIN fallback worked for all 1,290 rejections; average delay 35 seconds | Yes |
| Secure and resilient | Templates encrypted; module covered by the vendor's SOC 2; administrator MFA | Administrator MFA in place; **module outside the vendor SOC 2 scope** (P09) | **Partial** |
| Accountable and transparent | Written notice and signed consent before enrollment; signage at the entrances | County email notice only; signed consent for 410 of 1,150; no signage | **No** |
| Explainable and interpretable | Guards see the match score and the enrolled photo when a match fails | Yes | Yes |
| Privacy-enhanced | Templates deleted within 30 days after withdrawal or departure; no vendor training on templates | Retention was indefinite; 64 templates belonged to departed employees; no contract term on training | **No** |
| Fair, with harmful bias managed | FNMR by group (plan below) | Disparities flagged | **No** |

**Bias testing plan.** Face matching accuracy can differ by demographic group; NIST's face recognition vendor test report on demographic effects (NISTIR 8280, December 2019) documented such differentials across many algorithms.
- **Metric:** FNMR per group at the operating threshold, from real attempts; FMR per group from a controlled impostor test with volunteer pairs.
- **Groups compared:** age band (under 40, 40-59, 60 and over), sex, self-reported race and ethnicity (voluntary, collected by the County A HR office and reported to the company only in aggregate), and people wearing eyeglasses or head coverings.
- **Thresholds:** each group's FNMR at or below 1.5 times the overall FNMR and at or below 3%; zero false accepts in each group's impostor test. Groups with fewer than 30 people are reported but not scored.
- **Frequency:** before any expansion, then quarterly while in use, and after any vendor model update.

**Results (712 of 1,150 enrolled employees gave voluntary demographic data):**
| Group | FNMR | Ratio to overall (2.1%) | Result |
|---|---|---|---|
| Age 60 and over | 3.6% | 1.7 | **Flagged** |
| Black employees | 3.2% | 1.5 | **Flagged** (at the ratio limit and above 3%) |
| Wearing head coverings (32 people) | 4.4% | 2.1 | **Flagged** |
| Other groups | 1.4% to 2.4% | 0.7 to 1.1 | Pass |

**Bias finding.** Older employees, Black employees, and people wearing head coverings are rejected more often. Because the badge-plus-PIN fallback always works, the harm is delay and repeated friction, not denied entry, but it falls unevenly on these groups. The vendor must provide its model's demographic performance data and tuning options. Lowering the match threshold to cut rejections would raise the false match rate, so it may not be done without a new impostor test.

### 5.2 AI-003 video analytics (2026-02-01 to 2026-08-31)
- **Precision:** 4,860 alerts; 12 were real intrusions; most others were animals, cleaning crews, and shadows. ROC operators spent about 40 hours a month clearing alerts. **Fails** the target of at least 25% actionable alerts after tuning.
- **Detection:** a walk test of 20 staged after-hours entries detected 19. **Passes** (target 90%).
- **Fairness and privacy:** no identity matching. Loitering zones included two public sidewalks where people shelter at night, which drew 31% of loitering alerts; this risks repeated calls about the same unhoused people. **Fails** the condition that analytics zones stay on state property.
- **Security:** module outside the vendor SOC 2 scope (P09). **Partial.**

### 5.3 AI-004 BAS fault analytics
- **Validity:** technicians confirmed 78% of a sample of 100 fault recommendations as real faults. Target 70%. **Passes.**
- **Safety:** autonomous mode is disabled by configuration and checked monthly; every change goes through the CMMS change process. **Passes.**

### 5.4 AI-005 generative assistant (AI 600-1 risks)
- **Confabulation:** staff must verify any fact, citation, or figure before use; spot checks of 30 drafts found 4 with invented references, all caught before sending. **Acceptable with review.**
- **Information security and data privacy:** enterprise terms bar training on company data; a data loss rule blocks pasting text marked CUI or Restricted; public chatbots blocked on managed devices from 2026-10-31. **Partial until the block is live.**

### 5.5 AI-006 candidate ranking (2026-03-01 to 2026-08-31)
- **Adverse impact (four-fifths rule of thumb, 29 CFR 1607.4(D)):** 1,140 applicants for technician and trades roles; selection rate to interview by sex and by race and ethnicity from voluntary self-identification. Women's selection rate was 0.71 of men's; Hispanic applicants' rate was 0.84 of the highest group's. The result for women is **below four-fifths**, and the sample is large enough to treat it as a signal.
- **Validity:** the vendor could not show that the ranking predicts job performance for these roles.
- **Decision driver:** the ranking is suspended; recruiters review every application in date order until the vendor provides validation and a retest passes.

## 6. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the badge is always required. A failed match falls back to badge plus PIN or the guard desk; no one is refused entry by the algorithm alone. Face match results are never used for discipline or given to police without a human review of the event by County A.
- **AI-003:** every alert is verified on live video by a ROC operator before any dispatch or call; no automatic lock-downs.
- **AI-004:** recommendations only; changes through the CMMS with second-person approval (STD-04).
- **AI-005:** a person reviews and owns every output.
- **AI-006:** no ranking; recruiters review all applicants. If reinstated, no applicant may be rejected without a recruiter's review.

**Data handling:** face templates and analytics clips are Restricted data (POL-04). Template retention is 30 days after withdrawal or departure, checked monthly against the County A departure list. Vendor amendment: no training on templates or video, encryption at rest, per-person deletion, 24-hour incident notice, and inclusion of both modules in the SOC 2 scope.

**Monitoring:** monthly FNMR and alert precision reports; quarterly bias report for AI-001 to the County A facilities director; quarterly adverse impact check for AI-006 if reinstated; all tracked in the risk register (R-013, R-034, R-035).

**Incident handling:** a template or video breach follows P08 `ir-runbook.md` and the Fla. Stat. 501.171(6)(a) third-party agent notice (10 days after determination; the 24-hour contract notice comes first).

**Decommissioning:** stop AI-001 and delete all templates if the vendor has not signed the data terms by 2026-10-31, if a flagged group's FNMR does not improve by the next quarterly report, or if the County A attorney concludes the templates would be disclosable public records. Retire AI-006 if the vendor cannot validate the model by 2027-03-31.

## 7. Decisions
**AI-001: approve with conditions.** COO, 2026-09-15. Use may continue at the 2 entrances for currently enrolled employees, with **no new enrollments**, only if these are met by 2026-10-31:
1. Vendor contract amendment: no training on templates, encryption, per-person deletion, 24-hour incident notice, and the module in the SOC 2 scope (or a separate attestation).
2. Signed consent and signage; templates deleted for anyone who does not sign, and the 64 templates of departed employees deleted at once.
3. Template retention set to 30 days after withdrawal or departure.
4. Written opinion from the County A attorney on the public records status of the templates.
5. Local impostor test (2,000 attempts) completed and the vendor's demographic performance data received.

Expansion requires a new assessment and two consecutive quarterly reports with no flagged group.

**AI-002: not approved.** The company will not configure or operate 1:N identification of the public (P01 R-014, treatment Avoid). The COO's letter to County A, due 2026-09-30, explains why: it moves from verifying consenting employees to identifying people using county services, it carries a higher misidentification risk, and it has no review or appeal design. The company would re-assess only on a written county request that includes the county attorney's legal review and a human review and appeal process.

**AI-003: approve with conditions.** Remove the two public-sidewalk loitering zones by 2026-10-15; tune to at least 25% actionable alerts by 2026-12-31; the module in the vendor SOC 2 scope; no identity linkage.

**AI-004: approve.** Advisory mode only; monthly check that autonomous mode is disabled. Any request to enable it returns to the AI review group as a High-tier assessment.

**AI-005: approve the pilot.** Block public chatbots on managed devices by 2026-10-31; keep the data loss rule; decide on company-wide rollout by 2026-12-31.

**AI-006: suspend.** The HR Director switches the ranking off by 2026-09-30. Reinstatement needs the vendor's validation evidence and an adverse impact retest at or above four-fifths for every group with enough applicants, reviewed by General Counsel.

All conditions are tracked in POAM-021.

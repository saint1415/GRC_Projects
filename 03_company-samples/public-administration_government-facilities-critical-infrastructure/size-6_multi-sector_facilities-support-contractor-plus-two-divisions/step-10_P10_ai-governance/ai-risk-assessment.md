# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Government Facilities Support, Construction and Renovation, Janitorial and Security Services, corporate) |
| Tier / Vertical | Multi-Sector / Government Services and Facilities |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the regulator- and customer-specific rules for the priority use cases: face verification for facility access (AI-001, the registry use case) and the declined 1:N identification (AI-002), video analytics in the monitoring center (AI-003), closed-loop HVAC optimization (AI-004), applicant screening (AI-005), and the CUI exposure through estimating and generative tools (AI-006 to AI-008) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (NIST AI 600-1) for AI-007 and AI-008, and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27; presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 5 High, 3 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly; P01 GR-04 is a High group risk |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group General Counsel, Group HR director, Group building technology director, and one delegate per division president (Facilities Support security systems director, Construction CUI program manager, Janitorial and Security talent director). Approves High-tier use cases, the approved-tools list, and declines |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring and report metrics monthly |
| Group CISO | AI security standard (model and vendor access to OT, prompt injection, data leakage); owns AI-008 and AI-009 |
| Group General Counsel | State law reviews (biometric, recording consent, automated decision laws) and customer contract terms |
| Group internal audit | Includes High-tier AI controls in the 2027 assessment plan |

### 1.2 Group AI Standard (adopted 2026-03, under POL-01 4.13)
1. **Register before use.** Every AI use case that controls building equipment or physical access, processes biometric, workforce, customer, or government data, or supports decisions about people is registered and tiered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, bias or safety testing, notice to affected people, and quarterly monitoring reports.
3. **Customers decide on their buildings and people.** For AI in a customer's building (AI-001, AI-003, AI-004), the customer decides whether to use it; the group decides whether it will operate it, and can decline (AI-002).
4. **Bounded control.** No AI may write to building equipment or door controllers except within hard limits enforced in the controller, with a human-operated rollback.
5. **Data rules.** No CUI in any AI service (POL-04 4.3); no Restricted data in a tool not approved for it (POL-04 4.9); vendors sign no-training and deletion terms.
6. **Change gate.** A new model, vendor, site, data source, or decision role triggers re-assessment before release.
7. **Approved tools only** for workforce generative AI (POL-05 4.7).

**Where the program fell short.** The standard was adopted in March 2026, after face verification (AI-001, live 2026-01) and video analytics (AI-003) were already running, the applicant screening module (AI-005) had been switched on without a bias audit, and an estimating tool had sent CUI drawings to an unauthorized cloud AI service (AI-006) (scenario gap 11). Those use cases were assessed retroactively and are under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Face verification (1:1) at 3 county government centers | Facilities Support | High | In production with conditions; no new sites |
| AI-002 | Face identification (1:N) of the public in lobbies | Facilities Support; Janitorial and Security | High | **Not approved** |
| AI-003 | Video analytics in the central monitoring station | Janitorial and Security | High | In production; per-site testing due |
| AI-004 | Fault detection (advisory) and closed-loop HVAC optimization (pilot) | Facilities Support | High | Advisory in production; pilot capped at 6 sites |
| AI-005 | Applicant screening and interview scheduling | Janitorial and Security | High | In production with conditions before 2027-01-01 |
| AI-006 | Estimating and quantity takeoff assistant | Construction | Medium | Non-CUI use only |
| AI-007 | Generative drafting of officer incident reports | Janitorial and Security | Medium | In production with conditions |
| AI-008 | Enterprise generative AI assistant | Group | Medium | Pilot (3,000 users) |
| AI-009 | Meeting transcription for internal meetings | Group | Low | Approved |

### 2.1 Face verification for facility access (AI-001): the registry use case
| Item | Description |
|---|---|
| Purpose and intended use | Stop badge sharing and lost-badge misuse at employee entrances. The reader checks that the face matches the template of the badge presented. It never identifies anyone without a badge |
| Users / operators | Facilities Support security systems technicians (configuration); county security staff at the guard desks (fallback) |
| Affected people | 1,150 enrolled county employees at 3 Florida county government centers; employees who decline; visitors are not enrolled |
| Data | Enrollment photo converted by the vendor to a face template; badge ID; match score; access events |
| Build or buy | Buy: the access control SaaS vendor's face verification module. The vendor's SOC 2 report does not cover the module (P02 SA-9; P09 CC9.2) |
| Not intended | Identifying the public, police use, or use as the sole basis for discipline. Prohibited in the configuration and in the letters to the counties |

| Rule | Applies? | What it means |
|---|---|---|
| Florida breach law (worked example): Fla. Stat. 501.171(1)(g)1.a.(VI) and 501.702 | **Treated as applying** | Personal information includes biometric data as defined in 501.702: automatic measurements of biological characteristics used to identify a person, excluding photographs and data generated from video recordings. Templates are computed from live camera captures, so whether they are "biometric data" is unsettled. Counsel to confirm; the group treats them as biometric data either way. As a third-party agent the group must use reasonable security (501.171(2)) and notify the county within 10 days of a breach determination (501.171(6)(a)) |
| Florida public records (worked example): Fla. Stat. 119.0701 | Yes | Templates held for a county may be public records. Whether an exemption protects them is for each county attorney. The group routes any request to the county's custodian |
| FTC Act Section 5 | Indirectly | Applies to the vendor's and the group's accuracy and privacy claims. The FTC's December 2023 order against a national pharmacy chain over facial recognition without reasonable safeguards shows what the FTC expects: accuracy and bias testing, notice, deletion, and vendor oversight |
| County contract terms | Yes | Cardholder data protection and 24-hour incident notice apply to templates |
| Colorado SB26-189 (effective 2027-01-01) | Not today | It covers technology that materially influences consequential decisions, including employment and essential government services. All 3 sites are in Florida. Any proposal at a Colorado customer would need a new assessment |
| Federal buildings | Not in scope | Agencies use PIV credentials in their own systems. The group will not propose face recognition at federal buildings |

### 2.2 Declined: face identification of the public (AI-002)
A county and a commercial monitoring customer asked the group to scan lobby visitors against watch lists. This changes the purpose from verifying a consenting employee to identifying unknown members of the public, including people seeking essential government services, with a much higher chance of misidentification in a 1:N search and no review or appeal design. **The council declined it** (P01 JS-014, Avoid). The group would re-assess only on a written request that includes the customer's legal review, a human review and appeal process, and a public notice plan.

### 2.3 Video analytics (AI-003) and closed-loop HVAC optimization (AI-004): safety and critical infrastructure
| Rule or commitment | Use case | Implication |
|---|---|---|
| Monitoring contracts (alarm handling times in minutes) | AI-003 | Ranking must never delay review of a real alarm beyond the contract time. Analytics flag people and vehicles; face recognition is switched off by configuration and contract |
| Texas TRAIGA (Tex. Bus. & Com. Code chs. 551-554, effective 2026-01-01) | AI-003 | ROC-2 is in Texas. TRAIGA's prohibitions are intent-based (for example AI developed with intent to unlawfully discriminate) and do not fit this use; disclosure duties fall on Texas government agencies, not on the group. Counsel re-checks if face recognition is ever proposed |
| County contract terms; building codes and life-safety design | AI-004 | Life-safety functions are hardwired and outside the IBOP (P02 section 6). The optimizer writes only setpoints and schedules, within limits enforced in the controllers |
| NIST SP 800-82 Rev. 3 | AI-004 | The vendor platform is an OT connection: it reaches the supervisory servers through the IBOP with a write-capable service account limited to the 6 pilot sites |

### 2.4 Applicant screening (AI-005): employment
| Rule | Implication |
|---|---|
| Colorado SB26-189 (C.R.S. 6-1-1701 to -1709 as reenacted, effective 2027-01-01) | Janitorial and Security hires in Colorado. As a deployer of technology that materially influences employment decisions, the division must give applicants notice at the point of interaction, explain adverse outcomes, offer correction and meaningful human review, and keep records for 3 years. The signed act has no small-business exemption. Enforcement is by the Colorado attorney general; federal preemption efforts (EO 14365) continue, so counsel re-checks status before 2027-01-01 (P03 JS-G36; POAM-029) |
| Title VII (42 U.S.C. 2000e-2(k)) and the Uniform Guidelines (29 CFR 1607.4(D)) | Disparate impact applies to any selection procedure. The four-fifths rule is the federal agencies' benchmark: a selection rate for a race, sex, or ethnic group below 80% of the highest group's rate is generally regarded as evidence of adverse impact |
| Age Discrimination in Employment Act (29 U.S.C. 621-634) | Applicants 40 and older are protected; the division tests age bands with the same ratio as a screening benchmark |
| NYC Local Law 144 (N56-R08) | Not applicable: no hiring in New York City |

### 2.5 CUI and generative tools (AI-006, AI-007, AI-008)
| Rule | Use case | Implication |
|---|---|---|
| DFARS 252.204-7012(b)(2)(ii)(D) (N23-R03) | AI-006, AI-008 | CUI may be stored or processed in a cloud service only if it meets FedRAMP Moderate equivalent requirements. The estimating service does not. Uploads of labeled CUI are blocked since 2026-09-01 |
| DFARS 252.204-7012(a), (c) | AI-006 | Copying CUI to an unauthorized system can be a "compromise" and therefore a cyber incident. The uploads were found on 2026-07-14 during the P03 data mapping; the Construction CUI program manager reported them through DIBNet on 2026-07-16, within 72 hours |
| Customer contracts; public records (Fla. Stat. 119.0701 worked example) | AI-007 | Incident reports for public customers can become public records and evidence; an invented detail is a serious harm (P01 JS-016) |
| State recording consent (Fla. Stat. 934.03(2)(d) worked example: all parties must consent) | AI-007, AI-009 | Officers may dictate their own notes but may not record other people's conversations to feed the tool. Meeting transcription starts only after all participants are notified and consent |

## 3. Risk tiers (repository rubric)
- **High:** AI-001 and AI-002 (physical access to government facilities and biometric data; AI-002 also identifies people seeking government services), AI-003 and AI-004 (can affect physical safety or critical infrastructure operations), AI-005 (substantial factor in employment decisions).
- **Medium:** AI-006 (business decisions on bids; the issue is data handling), AI-007 (outputs enter reports about people, but the officer attests), AI-008 (workforce generative assistant).
- **Low:** AI-009 (internal productivity, no decisions about individuals).

**Re-tier or re-assess triggers:** any new site or entrance for AI-001; enabling any face feature in AI-003; expanding the AI-004 pilot beyond 6 sites or letting it write schedules; letting AI-005 reject applicants without recruiter review; any customer-facing use of AI-007 drafts without officer attestation.

## 4. MEASURE
Results are from monitoring, pilots, and tests between 2026-05 and 2026-08.

### 4.1 Face verification (AI-001)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | False non-match rate (FNMR): genuine employees rejected per attempt; target 2% or less | 61,400 attempts; FNMR 1.9% | Yes |
| Valid and reliable | False match rate: impostor test of 3,000 attempts at one site (2026-07); target 0 accepts | 0 false accepts | Yes |
| Safe | No one refused entry on a face result alone; fallback works | Badge plus PIN fallback worked for all rejections; average delay 35 seconds | Yes |
| Secure and resilient | Template encryption; administrator MFA; vendor assurance for the module | Encrypted; MFA in place; module outside the vendor's SOC 2; standing global administrator role can reach the tenants (POAM-011) | **Partial** |
| Accountable and transparent | Signed consent before enrollment; signage at entrances | Signed consent at 2 of 3 sites; the third relied on an email notice; signage at all 3 | **No** |
| Explainable and interpretable | Guards see the match score and enrolled photo when a match fails | In place | Yes |
| Privacy-enhanced | Templates deleted within 30 days after withdrawal or departure (POL-04 4.7); no vendor training on templates | Retention was indefinite until 2026-08; 64 departed employees' templates found and deleted; no-training term not yet in the contract | **No** |
| Fair, with harmful bias managed | FNMR by group (plan below) | Age 60 and over flagged | **No** |

**Bias testing plan (AI-001).**
- **Metric:** FNMR per group at the operating threshold from real attempts; false match rate per group from controlled impostor tests with volunteer pairs.
- **Groups compared:** age band (under 40, 40 to 59, 60 and over), sex, self-reported race and ethnicity (voluntary, collected by each county's HR office and reported to the group only in aggregate), and people wearing eyeglasses or head coverings.
- **Thresholds:** each group's FNMR at or below 1.5 times the overall FNMR and at or below 3%; zero false accepts in each group's impostor test. Groups with fewer than 15 people are reported but not scored.
- **Frequency:** before any expansion, quarterly while in use, and after any vendor model update.
- **Basis:** NIST's face recognition evaluations (NISTIR 8280, December 2019) documented demographic differentials across algorithms, so a vendor's overall accuracy figure is not enough.

| Group (812 of 1,150 enrollees gave voluntary data) | FNMR | Ratio to overall (1.9%) | Result |
|---|---|---|---|
| Age 60 and over | 3.2% | 1.7 | **Flagged** |
| Wearing head coverings (12 people) | 4.6% | 2.4 | Reported, not scored |
| All other groups | 1.4% to 2.6% | 0.7 to 1.4 | Pass |

The harm is delay and repeated friction at the door, not denied entry, because the badge-plus-PIN lane always works. It still falls unevenly on older employees and is not acceptable for expansion. Lowering the match threshold would raise the false match rate, so it may not be changed without a new impostor test.

### 4.2 Applicant screening (AI-005)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Fair, with harmful bias managed | Impact ratio for "advanced to interview" by sex and race or ethnicity (voluntary self-identification), 2026 Q2 (about 18,200 applications); flag below 0.80 (29 CFR 1607.4(D)) | Sex 0.93; race and ethnicity groups 0.84 to 0.97 | Yes |
| Fair, with harmful bias managed | Same ratio by age band (40 and older) | Applicants 55 and older 0.71 | **Flagged** |
| Accountable and transparent | Applicant notice; adverse-outcome explanation; human review on request; vendor documentation of intended use, training data categories, and limitations | None in place; vendor documentation requested 2026-08 | **No** |
| Valid and reliable | Recruiter agreement with low rankings in a blind sample of 300 | 81% agreement; 19% of low-ranked applicants judged qualified | **No** (target 90%) |
| Privacy-enhanced | Data minimization; no consumer report data in the model | Screening answers only; no consumer reports | Yes |

### 4.3 Video analytics (AI-003) and HVAC optimization (AI-004)
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-003 | Missed detections in walk tests at 12 sites (48 tests); target 0 | 2 missed (4%), both at night with poor lighting | **No** |
| AI-003 | Low-ranked alarms reviewed within the contract handling time | 93%; median review 6 minutes for low rank versus 1 minute for high rank | **No** (target 100%) |
| AI-003 | False alerts per operator hour | Down 38% since go-live | Yes |
| AI-004 | Setpoint writes within controller hard limits (pilot) | 100% within limits; limits were set by the vendor, not the group | **Partial** |
| AI-004 | Comfort and safety events | 2 comfort complaints (supply air at the upper limit in occupied hours); no safety events | Yes |
| AI-004 | Rollback switch tested at the ROC | Not yet tested | **No** |

### 4.4 Generative and estimating tools (AI-006 to AI-008), using AI 600-1 risk areas
| AI 600-1 risk | Use case | Test / metric | Result | Pass? |
|---|---|---|---|---|
| Confabulation | AI-007 | Supervisor sample of 400 drafts: details not in the officer's notes; target 0 reaching a signed report | 9 drafts (2.3%) added details; 1 reached a signed report before review | **No** |
| Data privacy | AI-006 | CUI deletion confirmed by the service | Requested; not yet confirmed | **No** |
| Information security | AI-008 | Upload block for CUI and Restricted labels; prompt-injection test of connected document sources | Block tested; prompt-injection test not done | **Partial** |
| Human-AI configuration | AI-007 | Drafts labeled; officer attestation before submission | Label in place; attestation added 2026-09 | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the badge is always required; a failed match falls back to badge plus PIN or the guard desk. Results are never used for discipline or reported to police without a county review of the event and video.
- **AI-003:** operators review every flagged event before dispatch or a police call. Every alarm, whatever its rank, must be reviewed within the contract handling time; supervisors get an alert when one is not.
- **AI-004:** advisory recommendations need engineer approval. Pilot writes stay inside group-set hard limits in the controllers; ROC operators can return a site to its approved schedule with one action.
- **AI-005:** recruiters review every low-ranked application before rejection; applicants can ask for human review.
- **AI-007:** officers review, edit, and attest every report; supervisors sample 5% weekly.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-04, GR-18, FS-005, FS-006, CN-012, JS-004, JS-005, JS-014, and JS-016.

**Incident handling:** AI failures that affect building safety, disclose biometric or applicant data, or expose CUI follow POL-03 and P08. A template breach triggers the customer contract notice (24 hours) and the third-party agent notice (Florida worked example: 10 days after determination).

**Decommissioning:** each use case has an off switch and a fallback the BIA already covers (P05): badge-only entry (AI-001), manual alarm handling (AI-003), approved schedules (AI-004), recruiter-only screening (AI-005), manual takeoff (AI-006), and officer-written reports (AI-007). AI-001 is stopped and all templates deleted if the conditions below are not met by 2026-12-31.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 face verification | **Approve with conditions** (council, 2026-08-27; board risk committee informed 2026-09-15) | Signed consent at the third site, or delete its templates, by 2026-10-31; vendor amendment (no training on templates, per-person deletion, 24-hour incident notice) and module assurance (bridge letter or SOC 2 coverage) by 2026-12-31; 30-day deletion verified monthly against county departure lists; vendor tuning plan for the age 60 and over disparity; written opinion from each county attorney on public records status. No new sites or entrances until two consecutive quarterly reports have no flagged group |
| AI-002 face identification of the public | **Reject** | Letters to the county and the commercial customer sent 2026-09-10. Re-assess only on the written conditions in section 2.2 |
| AI-003 video analytics | **Continue with conditions** | Supervisor alert for any alarm not reviewed within the contract time by 2026-10-31; per-site walk testing with lighting fixes by 2027-03-31; analytics vendor review and ticketed rule changes (P09 CC8.1, CC9.2) |
| AI-004 HVAC optimization | **Continue advisory; cap the pilot at 6 sites** | Group-set hard limits loaded into the pilot controllers and the rollback switch tested by 2026-12-31; no expansion before 2027-03-31; council re-assessment, and an SSP integrity rating review (P02 section 6), before any expansion |
| AI-005 applicant screening | **Continue with conditions** | Independent bias audit including age bands and vendor documentation by 2026-11-30; applicant notice, adverse-outcome explanation, human review on request, and 3-year records live by 2026-12-31 for all applicants, not only Colorado (POAM-029); recruiter review of every low ranking continues |
| AI-006 estimating assistant | **Continue for non-CUI drawings only** | Vendor deletion confirmation for all CUI uploads and an approved alternative inside SYS-C2 by 2026-12-31 (P01 CN-012; POAM-019) |
| AI-007 incident report drafting | **Continue with conditions** | Officer attestation (in place 2026-09) and 5% weekly supervisor sampling; confabulation rate below 1% in the 2026 Q4 sample, or the feature is switched off |
| AI-008 enterprise assistant | **Continue the pilot** | Prompt-injection test of connected sources before any expansion beyond 3,000 users; prohibited for decisions about people |
| AI-009 meeting transcription | **Approved** | Internal meetings only, with all-party notice and consent |

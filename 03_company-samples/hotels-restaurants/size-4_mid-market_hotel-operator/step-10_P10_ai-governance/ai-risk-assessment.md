# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Florida hotel owner and operator: 2 independent resorts and 4 franchised select-service hotels) |
| Tier / Vertical | Mid-Market / Accommodation and Food Services |
| Scope | Portfolio of 6 AI use cases (AI-001 to AI-006), inventory in `ai-use-case-inventory.csv`. The registry default for this vertical (revenue-management pricing and a guest chatbot) is kept as AI-001 and AI-002 and widened, because a mid-market operator runs several AI tools (`../00_company-facts.md` section 5) |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-002 and AI-006 |
| Assessors / date | General Counsel (legal and privacy), vCISO and Security Manager (security), HR Director (AI-004), with each business owner, 2026-08-24 to 2026-09-04 |
| Decision | Chief Operating Officer, 2026-09-15 (AI-004, the High-tier use case, noted by the CEO); Medium and Low decisions by the AI review group the same day |

## 1. Summary
Five of the six tools (AI-001 to AI-005) went live without a security, privacy, or legal review (gap 11 in the company facts). None is out of control, but four have problems that need dated conditions:
- **AI-001, pricing:** publishes resort rates automatically with no floor, ceiling, or emergency rule. A back-test of a 2025 declared state of emergency showed rates 41% above the 30-day average at Resort 2 (Fla. Stat. 501.160). The contract lets the vendor pool the company's non-public data into a shared benchmark.
- **AI-002, chatbot:** quotes nightly rates without the $40 resort fee (16 CFR 464.2) and keeps transcripts, 61 of them with card numbers, indefinitely.
- **AI-003, call recording and scoring:** transferred and outbound calls are recorded without an announcement (Fla. Stat. 934.03(2)(d)), and recordings and transcripts hold spoken card numbers and security codes.
- **AI-004, applicant screening:** automatically declined about 3,100 applicants in 12 months with no adverse impact testing. One job family falls below the four-fifths rule of thumb. Automatic declines were switched off on 2026-09-15.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Revenue-management pricing | Medium (High during a declared emergency) | Approve with conditions |
| AI-002 | Guest chatbot | Medium | Approve with conditions |
| AI-003 | CRO call recording, transcription, and quality scoring | Medium | Approve with conditions |
| AI-004 | Applicant screening | **High** | Conditional: automatic declines stay off; conditions by 2026-12-31 or retire |
| AI-005 | CCTV video analytics | Medium | Approve with conditions; facial recognition locked |
| AI-006 | Enterprise generative AI assistant | Low | Approve (corporate users); hotel rollout after the mailbox purge |

Tiers: 1 High, 4 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** the General Counsel, who chairs the AI review group, supported by the vCISO. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.12: every price display (including chatbot answers and phone scripts) shows the total price including mandatory fees.
  - POL-01 4.13: AI tools that use guest, card, or employee data, set prices, or affect hiring must be approved before use.
  - POL-04 4.8: no Restricted or Confidential data in unapproved AI tools; contracts must forbid training on company data and set retention.
  - POL-05 4.10 and 4.11: approved tools only; review outputs; recording announcement on every recorded call; pause before card details.
  - STD-05 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Security Manager on the intranet. Public generative AI sites have been blocked on company devices since 2026-09 (P01 R-038).

### 2.1 Lightweight AI governance process
A mid-market hotel company does not need a standing AI committee with a large charter. It needs a short gate before tools go live and a monthly rhythm. The process reuses existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature switched on in an existing tool, submits a one-page intake: purpose, users, data, vendor, decisions affected, prices or people affected | Requesting business owner | 15 minutes |
| 2. Triage | Provisional tier using the repository rubric; purchasing gate (no purchase order or feature activation without approval) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy (contract terms, retention, no training), legal (fee rule, recording consent, pricing law), and a business reviewer. **High:** full MAP and MEASURE assessment like this one, including bias testing and counsel review | Security Manager; General Counsel; HR Director or business reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (General Counsel, vCISO, Security Manager, HR Director, and the owner), 30 minutes monthly. High: the review group recommends, the COO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owners report the section 4 metrics monthly; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data, new hotel or channel (for example the REIT-managed hotels from 2027-01-01), a declared state of emergency, or a complaint | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. It is defined by this repository, not by a regulation. Re-tier triggers are listed for each use case in section 3.

## 3. MAP
| Item | AI-001 Pricing | AI-002 Chatbot | AI-003 Call scoring | AI-004 Screening | AI-005 Video analytics | AI-006 Assistant |
|---|---|---|---|---|---|---|
| Purpose | Forecast demand and set daily rates | Answer questions, quote rates, link to booking | Record, transcribe, and score CRO calls | Rank applications for hourly roles | Alert security to after-hours intrusion and left objects | Draft and summarize for corporate staff |
| Users | Director of Revenue Management | Website and text visitors; marketing staff | CRO supervisors; 22 agents | 6 recruiters; hiring managers | Resort security officers | 120 corporate users |
| Affected people | Every booking guest | About 9,000 conversations a month | About 900 callers a day; CRO agents | About 9,500 applicants a year | Guests, visitors, staff on camera | None directly |
| Data | Aggregated stays (plus guest names today) | Contact details; transcripts | Audio and transcripts with card data | Applications; scores | Video; alert snapshots | Email and files the user can reach |
| Build or buy | Buy | Buy plus integration | Buy | Buy | Buy | Buy |
| Generative AI? | No | Yes | Speech-to-text only | No | No | Yes |
| Acts on its own? | **Yes (resort rates)** | Yes (answers) | No (scores reviewed) | **Yes until 2026-09-15** | No (alerts) | No |
| Re-tier triggers | Declared emergency (High for its duration); personalized pricing; any data sharing with competitors | Payments or booking changes in chat; marketing use of transcripts | Scores used for discipline or termination | n/a (already High) | Facial recognition; analytics replacing patrols | Use with guest data outside corporate |

### 3.1 Laws and rules considered
| Rule | Use cases | Applies? | Why |
|---|---|---|---|
| FTC Rule on Unfair or Deceptive Fees, 16 CFR 464.2 and 464.3 (90 FR 2066, rule text at 2166; effective 2025-05-12) | AI-001, AI-002 | **Yes** | Short-term lodging is covered (464.1). Every offer or display of a price must show the total price, including the mandatory $40 resort fee, more prominently than other pricing (464.2(a)-(b)). The chatbot quotes the base rate: 0 of 20 sampled rate answers included the fee (**fails**; P03 G-092). AI-001's channel feeds already carry the fee as mandatory (P03 G-091). Fees must not be misrepresented (464.3) |
| FTC Act Section 5, 15 U.S.C. 45(a) and (n) (N72-R02) | All | **Yes** | Chatbot answers and AI-generated content are the company's representations. The privacy notice does not mention the chatbot, call analytics, or pooled pricing data (P03 G-090) |
| Fla. Stat. 501.160 (unconscionable prices during a declared state of emergency) | AI-001 | **Yes** | After the Governor declares a state of emergency, renting or offering a dwelling unit "necessary for habitation or use as a direct result of the emergency" at an unconscionable price in the declared area is unlawful. A gross disparity from the average price in the 30 days before the declaration is prima facie evidence, unless explained by added costs or market trends (501.160(1)(b), (2)(b)). The statute does not name hotels expressly; the company treats its room rates as covered, which is the cautious reading |
| Sherman Act Section 1, 15 U.S.C. 1 (algorithmic pricing) | AI-001 | **Litigation risk** | In *Cornish-Adebiyi v. Caesars Entertainment, Inc.*, No. 24-3006 (3d Cir. July 29, 2026), the court revived claims that casino-hotels fed non-public data into a shared pricing algorithm. In *Gibson v. Cendyn Group, LLC*, No. 24-3576 (9th Cir. Aug. 15, 2025), the court affirmed dismissal where hotels only licensed the same software. Neither binds Florida federal courts, but the **pooled benchmarking clause** is the fact pattern the Third Circuit found plausible. The company opts out (P01 R-023, avoided) |
| Fla. Stat. 934.03(2)(d) (interception with all parties' prior consent) | AI-003 | **Yes** | Recording and transcribing calls is lawful when all parties have given prior consent. The main-line greeting announces recording; transferred and outbound calls do not (P01 R-035) |
| PCI DSS v4.0.1 3.2.1, 3.3.1, 3.3.1.2, 4.2.2 (N72-R01) | AI-002, AI-003, AI-006 | **Yes** | Card numbers typed into chat and spoken in recorded calls are stored; security codes must not be kept after authorization |
| Fla. Stat. 501.171 (N72-R04) | AI-002, AI-003, AI-005 | **Yes** | Transcripts and recordings hold personal information (a name with a card number and security code). The chatbot and contact center vendors are third-party agents that must report breaches within 10 days (501.171(6)(a)) |
| Title VII, 42 U.S.C. 2000e-2(k)(1)(A); ADA, 42 U.S.C. 12112(b)(6); Uniform Guidelines, 29 CFR 1607.4 | AI-004 | **Yes** | A selection practice that causes a disparate impact by race, color, religion, sex, or national origin is unlawful unless shown to be job related and consistent with business necessity. Selection criteria that screen out people with disabilities must also be job related and consistent with business necessity. Under 29 CFR 1607.4(D), a selection rate below four-fifths of the highest group's rate is generally regarded as evidence of adverse impact. Federal enforcement priorities have shifted (EO 14281), but the statutory liability is unchanged |
| Fla. Stat. 501.702 biometric data definition (through 501.171(1)(g)1.a.(VI)) | AI-005 | **Unsettled** | 501.702 defines biometric data as automatic measurements of biological characteristics used to identify a person, and excludes photographs, video or audio recordings, and data generated from them. Whether face templates computed from camera video would be biometric data is unsettled; counsel to confirm. The company will treat them as biometric data, which is one more reason facial recognition stays disabled |
| State AI laws (for example Colorado SB26-189) | AI-004 | **No** | The company hires and operates only in Florida; this assessment did not identify a Florida AI-specific statute for these uses |
| Illinois BIPA (N72-R05) | AI-005 | **No** | No Illinois operations or employees |
| FTC proposed AI accuracy policy statement (July 2026) | AI-002 | **Watch only** | Proposed, not final |

### 3.2 AI-001 and Florida's price gouging law
Hurricane season runs June to November, and both resorts are on the coast. A declared emergency brings evacuees and recovery crews to inland hotels and stops bookings at coastal ones, which is exactly when an automated pricing model sees a demand spike. **The fix is an emergency mode:**
1. When the Governor declares a state of emergency covering any county with a company hotel, the Director of Revenue Management switches that hotel's rates to emergency mode within 4 hours of the declaration.
2. Emergency mode caps every published rate at or below the average for the same room type in the 30 days before the declaration. Any increase needs written approval from the General Manager and the CFO with a cost reason (501.160(1)(b) allows increases attributable to added costs or market trends).
3. The $40 resort fee is reviewed for the declared period (amenities may be closed).
4. The mode stays on until the price gouging prohibition period ends (60 days under the initial declaration unless extended by executive order, 501.160(2)).
5. **Until the vendor setting is live (due 2026-10-31),** automatic publishing is switched off by hand for any declared county.

## 4. MEASURE (by use case)
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (2026-08 sample) | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | 14-day occupancy forecast error, back-test June 2025 to July 2026 | Under 10% | 7.9% | Yes |
| AI-001 | Safe (emergency pricing) | Back-test of the 2025 declared emergency: published rates against the 30-day pre-declaration average | No increase without approval | Resort 2: 41% above the average for 3 nights | **No** |
| AI-001 | Valid and reliable | Published rates outside a floor and ceiling | None | No floor or ceiling exists | **No** |
| AI-001 | Fair, with harmful bias managed | Same room and dates quoted from 5 locations, 3 device types, logged-in and anonymous, English and Spanish pages | Identical apart from disclosed member rates | 60 quotes; no unexplained differences | Yes |
| AI-001 | Privacy-enhanced; competition safeguards | Only aggregated data to the vendor; no pooling of non-public data | Both | Guest names in the extract; pooling on by default | **No** |
| AI-002 | Valid and reliable | Monthly 50-question test set (policies, amenities, hours) | 95% correct | 89% (pet fee and cancellation window wrong) | **No** |
| AI-002 | Valid and reliable (fee rule) | Rate answers that state the total price including the $40 resort fee first | 100% | 0 of 20 | **No** |
| AI-002 | Safe | Accessibility, medical, and hurricane questions handed to staff | 100% | 8 of 12 | **No** |
| AI-002 | Secure and resilient | Prompt-injection attempts to reveal other guests' data or system instructions | No data exposed | No guest data exposed (integration reads availability and rates only); system instructions partly revealed | Partial |
| AI-002 | Accountable and transparent | Discloses it is an AI assistant and offers a human | Both | Both | Yes |
| AI-002 | Privacy-enhanced | Card numbers masked on entry; transcripts kept 90 days | Both | No masking; indefinite retention; 61 transcripts with card numbers | **No** |
| AI-002 | Fair, with harmful bias managed | Same 50 questions in English and Spanish | Spanish within 5 points of English | English 89%, Spanish 80% | **No** |
| AI-003 | Accountable and transparent | Recording announcement on every call path (40 test calls) | 100% | 20 of 20 main-line calls; 0 of 10 transfers from front desks; 0 of 10 outbound callbacks | **No** |
| AI-003 | Privacy-enhanced | Card numbers and security codes absent from recordings and transcripts | 0% | 13 of 60 recordings (about 22%); the transcription redaction feature is off | **No** |
| AI-003 | Valid and reliable | Supervisor rescoring of 40 calls against the AI score | 90% agreement within 1 point | 86% | Partial |
| AI-003 | Fair, with harmful bias managed | Score difference between English and Spanish calls for the same supervisor-rated quality | No more than 5 points | Spanish calls scored 7 points lower on average for the same supervisor rating | **No** |
| AI-004 | Fair, with harmful bias managed | Advance-to-interview rate by sex and by race and ethnicity (voluntary self-identification, 58% of applicants), per job family, 12 months to 2026-06-30 | Each group at least four-fifths of the highest group (29 CFR 1607.4(D)) | Sex: 0.94 overall. Race and ethnicity: 0.78 for one group in the front desk agent family; others 0.83 or higher | **No** (1 family) |
| AI-004 | Fair, with harmful bias managed | Features that may screen out people with disabilities | None without job-related justification | Model penalizes employment gaps longer than 6 months | **No** |
| AI-004 | Accountable and transparent | Applicants told AI is used and how to request an accommodation | Notice on every posting | No notice | **No** |
| AI-004 | Valid and reliable | Recruiter review of 100 low-scored applications | Under 5% judged qualified | 11% judged qualified | **No** |
| AI-005 | Valid and reliable, safe | 20 staged after-hours walk tests at pools and back-of-house doors | 95% detected | 18 of 20 (90%) | Partial |
| AI-005 | Valid and reliable | False alerts a night at Resort 1 | Under 10 | About 35 | **No** (alert fatigue) |
| AI-005 | Privacy-enhanced | Facial recognition disabled and locked against change | Locked | Disabled but any administrator can enable it | Partial |
| AI-005 | Fair, with harmful bias managed | Loitering alerts acted on without officer review | 0 | No record of officer review for 3 of 20 sampled alerts | Partial |
| AI-006 | Secure and resilient; privacy-enhanced | Tenant boundary, no training on company data, Restricted data reachable through search | Contract terms; no card data reachable | Terms in place; card forms in mailboxes are searchable until purged | Partial |
| All | Explainable and interpretable | Users can see why an output was produced (rate drivers, answer source, score rubric, screening factors, alert clip) | Available | Available for AI-001, AI-002, AI-003, AI-005; AI-004 shows only an overall score | Partial |

**Bias and fairness plan (ongoing):**
- **AI-001:** repeat the 60-quote location, device, and language test each quarter and after any vendor model update. Any unexplained price difference between groups is a stop-and-investigate event.
- **AI-002:** English and Spanish test sets monthly. Spanish replies carry a human handoff offer until the gap is 5 points or less for 2 months in a row.
- **AI-003:** monthly comparison of AI and supervisor scores by call language. Until the gap is 5 points or less, Spanish-call scores are excluded from the incentive calculation.
- **AI-004:** quarterly adverse impact analysis by job family, sex, and race and ethnicity with the four-fifths rule of thumb and a statistical significance check; any family below four-fifths triggers a review of the model's factors with counsel before the tool is used for that family again.
- **AI-005:** monthly review of a sample of 20 acted-on alerts for officer review records.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** automatic publishing only within a floor, a ceiling, and a 10% daily change limit; anything outside needs the Director of Revenue Management's approval; emergency mode as in section 3.2. Hotels 3 to 6 already have a human step (recommendations entered by hand in the brand system).
- **AI-002:** staff take over booking changes, complaints, accessibility, medical, and hurricane questions; staff review 50 transcripts a week.
- **AI-003:** supervisors review every score before use; agents can dispute; scores are never the sole basis for discipline.
- **AI-004:** no automatic declines; a recruiter reviews every low-scored application; the employment-gap feature is removed; applicants are told AI is used and how to ask for an accommodation.
- **AI-005:** officers review the clip before acting; no guest is approached or removed on an alert alone; facial recognition locked by the vendor setting and the change log reviewed monthly.
- **AI-006:** users review every output; use limited to corporate users until mailboxes are clean.

**Price display (16 CFR Part 464):** the chatbot integration adds the $40 resort fee to every nightly rate at the resorts and states the total first; the CRO script states the total first (POAM-018). The Vice President of Sales and Marketing checks 20 chatbot rate answers and 20 CRO test calls each month.

**Data protection:**
- AI-002: card-number detection and masking in chat with a reply that points guests to the booking engine; purge the 61 transcripts; 90-day retention and no-training terms in the contract.
- AI-003: announcement on every call path; pause-and-resume recording (POAM-013); transcription redaction switched on; purge of recordings and transcripts with card data.
- AI-001: remove guest names from the extract; opt out of pooled benchmarking with written confirmation that past pooled data will not be used further.

**Monitoring:** owners report the section 4 metrics monthly to the AI review group. AI-004 also gets a quarterly deep dive reported to the COO. Results feed the risk register (P01 R-022, R-023, R-033 to R-038).

**Incident handling:**
- A wrong price published at scale, a fee-rule failure, or a chatbot or recording data exposure is logged under POL-03. Card data exposure follows `ir-runbook.md` (P08).
- A complaint of discrimination about AI-004 goes to the HR Director and the General Counsel.
- A security incident at an AI vendor follows P08 and the third-party agent duty in Fla. Stat. 501.171(6)(a).

**Decommissioning criteria:**
- AI-001: switch to manual rates (P05 BP-11 tolerates 72 hours) if emergency mode is not live by 2026-10-31 or the vendor will not remove the pooling clause.
- AI-002: turn off rate quoting (keep FAQ answers) if the total price fix is not live by 2026-10-15; switch the chatbot off if masking is not live by 2026-10-31.
- AI-003: stop transcription and scoring (keep recording with announcements) if all call paths are not announced by 2026-11-30.
- AI-004: retire the screening module if the adverse impact review, feature removal, and notice are not complete by 2026-12-31, or if any job family stays below four-fifths after remediation.
- Any tool: stop if the vendor changes data-use terms or the model changes without notice.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | Floor, ceiling, and change limits; emergency mode tested with the Director of Revenue Management and the CFO; pooling switched off; guest names removed (all by 2026-10-31); manual switch-off for any declared county until then | AI review group, 2026-09-15 |
| AI-002 | **Approve with conditions** | Total price first in every rate answer (2026-10-15); masking, purge, 90-day retention, and contract amendment (2026-10-31); hurricane, accessibility, and medical handoff (2026-10-15); Spanish handoff offer until the gap closes | AI review group, 2026-09-15 |
| AI-003 | **Approve with conditions** | Announcement on every call path (2026-11-30); transcription redaction on and purge (2026-12-31, with POAM-013); Spanish-call scores excluded from the incentive until the gap closes | AI review group, 2026-09-15 |
| AI-004 | **Conditional** | Automatic declines stay off (done 2026-09-15); adverse impact review of the front desk agent family with counsel; employment-gap feature removed; applicant notice and accommodation path (all by 2026-12-31) or retire | COO, 2026-09-15; noted by the CEO |
| AI-005 | **Approve with conditions** | Facial recognition locked with change alerts (2026-10-31); officer review record for every acted-on alert; tuning to cut false alerts below 10 a night (2026-12-31); any future facial recognition proposal needs a High-tier assessment and counsel's biometric analysis | AI review group, 2026-09-15 |
| AI-006 | **Approve** | Corporate users only until the mailbox purge is complete (POAM-013); then extend to hotel managers | Security Manager, 2026-09-15 |

The conditions are tracked as POAM-019 in P07 and in the risk register (P01 R-022, R-023, R-033 to R-038). STD-05 (due 2026-12-31) turns the process in section 2.1 into a standard. The AI review group holds its first monthly meeting on 2026-10-13. Before the REIT-managed hotels start on 2027-01-01, the group re-reviews AI-001 and AI-002 for those hotels (re-review trigger).

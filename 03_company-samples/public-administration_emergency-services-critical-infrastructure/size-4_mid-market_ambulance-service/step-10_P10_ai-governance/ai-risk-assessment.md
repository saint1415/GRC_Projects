# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (licensed private ambulance service; PE-backed) |
| Tier / Vertical | Mid-Market / Emergency Services |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv` |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-001, AI-002, AI-003, and AI-005 |
| Assessors / dates | Medical Director (clinical), vCISO and Security Manager (security), Compliance and Privacy Officer (privacy and legal), Director of Revenue Cycle (billing compliance), 2026-08-24 to 2026-09-04 |
| Decision | Chief Operating Officer with the Medical Director, 2026-09-16; High-tier decisions noted by the CEO |

## 1. Summary
Four of the five tools went live without a security, privacy, or compliance review (gap 9). AI-001 and AI-003 were switched on as vendor features, AI-002 by the clinical team, and AI-004 by the data analysts. Only AI-005 came through purchasing. Two of the four need immediate limits:
- **AI-003, billing coding assistance,** coded about 35% of claims straight through with no human review, and a 200-claim audit found it chose the wrong level of service on 9% of them. That is a Medicare overpayment and client trust issue.
- **AI-001, call triage,** is in advisory mode, but its critical-keyword alerts are much weaker on Spanish-language calls and its upgrade prompts are less accurate for older patients. Section 1557 requires the company to identify and mitigate that risk.

| ID | Use case | Risk tier | 92.210 in scope? | Decision |
|---|---|---|---|---|
| AI-001 | AI-assisted emergency call triage | High | **Yes** | Continue advisory mode for English-language calls only, with conditions |
| AI-002 | ePCR narrative drafting | Medium | No (documentation only) | Continue the pilot with conditions; no expansion until 2027 |
| AI-003 | Billing coding assistance | High | No (not clinical decision support) | Continue only with 100% coder review; look-back review; straight-through coding ends by 2026-10-01 |
| AI-004 | Demand forecasting and unit posting | High | No (operational, not patient care) | Continue with minimum coverage rules and monthly equity monitoring |
| AI-005 | Enterprise generative AI assistant | Low | No | Continue the pilot; no PHI until reassessed |

Tiers: 3 High, 1 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Medical Director for clinical and dispatch uses, supported by the vCISO for security and the Director of Revenue Cycle for billing uses. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.13: AI tools and AI features must pass the AI governance gate before use.
  - POL-01 4.9: turning on a vendor feature that sends PHI is a new PHI flow and needs a BAA review.
  - POL-04 4.8: no Restricted data in AI tools without approval and a BAA with a no-training term.
  - POL-05 4.8: approved tools only; people remain responsible for AI-assisted dispatch priorities, records, and claims.
  - STD-05 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Security Manager on the intranet. Today it lists AI-001 to AI-005 with their conditions. Public chatbots are blocked for PHI and caller information.

### 2.1 Lightweight AI governance process
A mid-market company does not need a standing AI committee with a large charter. It needs a short, reliable gate and a monthly rhythm. The process reuses existing roles and meetings.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or wanting to turn on an AI feature in an existing system (CAD, ePCR, billing), submits a one-page intake: purpose, users, data, vendor, decisions affected | Requesting business owner | 15 minutes |
| 2. Triage | The Security Manager assigns a provisional tier with the P10 rubric and checks the purchasing and feature gate (POL-01 4.9) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy (BAA, no-training term, retention), and a clinical or billing reviewer. **High:** full MAP and MEASURE assessment like this one, including a bias and performance plan, a 92.210 input-variable check where relevant, and a go-live gate | Security Manager; Compliance and Privacy Officer; Medical Director or Director of Revenue Cycle | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (Medical Director, vCISO, Compliance and Privacy Officer, Director of Revenue Cycle), meeting monthly for 45 minutes. High: the AI review group recommends, and the COO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owner reports the agreed metrics monthly; incidents go to P08; clinical safety events go to the Medical Director's quality review | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model or vendor version change, new data type, new language or population, or a safety or billing event | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. Re-tier triggers are listed for each use case in section 5.

## 3. MAP
| Item | AI-001 Call triage | AI-002 Narrative drafting | AI-003 Coding assistance | AI-004 Posting | AI-005 Assistant |
|---|---|---|---|---|---|
| Purpose | Faster recognition of time-critical calls (cardiac arrest, stroke) | Save crew documentation time | Speed up coding and reduce backlog | Reduce response times by positioning idle units | Draft letters, procedures, summaries |
| Users | 44 telecommunicators and 8 supervisors | 60 paramedics (pilot) | 14 coders for company and client claims | 8 communications supervisors | 40 administrative staff |
| Affected people | Callers and patients on about 320 County A calls and about 180 request-line calls a day | About 90 patients a day in the pilot | About 740 claims a business day (all company claims and the claims of 2 of the 4 clients) | Residents of both counties' service areas | None directly |
| Data | Live audio, transcripts (ePHI) | Structured care fields (ePHI) | Narratives, trip data, codes (ePHI, including client PHI) | De-identified incident history | Internal documents only |
| Build or buy | Buy (CAD vendor cloud service) | Configure (ePCR feature) | Configure (billing platform module) | Build (company model) | Buy (enterprise service) |
| Generative AI? | Yes (transcription and language model classifier) | Yes | Yes (language model classifier) | No (statistical forecasting) | Yes |
| Not intended | Automatic dispatch; lowering a priority; pre-arrival instructions; relay-service calls | Adding care not entered by the crew | Releasing a claim without coder approval | Moving units without a supervisor | Any PHI, caller, or client data |

**Applicable laws and rules:**
| Rule | Applies to | Why |
|---|---|---|
| HIPAA Privacy and Security Rules | AI-001, AI-002, AI-003, AI-005 | Each vendor receives or could receive PHI for the company, so each is a business associate for that service. The CAD vendor's BAA covers remote support only, so **AI-001 needs a BAA amendment** before audio keeps flowing (due 2026-10-31). AI-003 also processes client PHI, so the billing vendor's client addendum must cover the AI module |
| Section 1557, 45 CFR 92.210 | AI-001 | The company receives federal financial assistance through Florida Medicaid. A patient care decision support tool is "any automated or non-automated tool ... used by a covered entity to support clinical decision-making" (45 CFR 92.4). Assigning response priority by symptom acuity supports a clinical decision. The tool does not take race or age as declared inputs, but its accuracy varies by language (a national origin factor) and by patient age. The company applies the 92.210(b) identification duty and the 92.210(c) mitigation duty |
| Fla. Stat. 934.03(2)(g) | AI-001 | The statute allows an employee of an ambulance service licensed under Fla. Stat. 401.25 to intercept and record incoming wire communications, but limits recording on designated 911 numbers and published nonemergency numbers to those staffed by trained dispatchers at public safety answering points. Counsel must confirm which company lines fall within the paragraph, including callers transferred from the County A PSAP. A "calls are recorded" greeting on request lines is added as a safeguard |
| 42 CFR 401.305 | AI-003 | A person that has received a Medicare overpayment must report and return it by the later of 60 days after identification or the cost report due date (401.305(b)(1)). The deadline is suspended while a timely, good-faith investigation of related overpayments runs, for up to 180 days (401.305(b)(3)). "Identified" uses the "knowingly" standard of 31 U.S.C. 3729(b)(1)(A) (401.305(a)(2)). For client claims, the client received the payment, so the company tells each affected client what it finds |
| 42 CFR 410.40 and 410.41(c) | AI-003 | Level of service and medical necessity must match the documentation; certification statements and origin and destination codes must be correct |
| Fla. Stat. 401.30(1) | AI-002 | Licensees must keep accurate records of emergency calls |
| County agreements (contracts) | AI-004 | Response-time standards apply in every zone; the model must not trade one zone's compliance for another's |
| FTC Act Section 5 | AI-001, AI-003 | Applies to the vendors' accuracy claims; the company keeps the claims it relied on in the procurement file |
| FDA device rules | AI-001 | Whether the product is a regulated medical device is the vendor's question as manufacturer. The company requested the vendor's written regulatory position |

**Laws considered and not applicable:**
- **State AI laws such as Colorado SB26-189:** the company operates only in Florida. This assessment did not identify a Florida AI-specific statute that applies to these uses; Florida AI law was not researched beyond the statutes listed above.
- **45 CFR 92.210 for AI-003 and AI-004:** coding assistance supports billing, not clinical decisions, and posting supports operations, not care of a specific patient. Both are still monitored for disparities (sections 4.3 and 4.4).

## 4. MEASURE
### 4.1 AI-001 call triage (High)
**Data.** A 90-day shadow period (2026-02-01 to 2026-04-30) logged suggestions without showing them. Advisory mode started 2026-05-01. The **reference standard** is the Medical Director's review of each sampled call against the acuity found at patient contact (from the ePCR). The Medical Director reviewed a stratified sample of 2,400 calls from both periods; 610 were time-critical (reference Priority 1).

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Under-triage: share of time-critical calls where the AI suggested Priority 2 or 3. Threshold: 2% or less, and no worse than telecommunicators using the protocol | AI 3.1% (19 of 610); telecommunicators 1.5% (9 of 610) | **No** (upgrade-only design contains the harm) |
| Valid and reliable | Over-triage: share of non-critical calls the AI suggested as Priority 1. Threshold: 25% or less | 17% | Yes |
| Safe | Critical keyword alert sensitivity ("not breathing", "unconscious", "no pulse"). Threshold: 98% or more | English 97%; Spanish 84% | **No** |
| Safe | Time from call answer to recognition of cardiac arrest, advisory mode versus before | Median 61 seconds versus 74 seconds (English calls) | Yes (benefit observed) |
| Safe | Automation bias: dismissed upgrade prompts later found time-critical | 3 of 412 dismissed prompts sampled | Monitor (training added) |
| Secure and resilient | BAA covering the AI service; vendor SOC 2 covering it; alert if the transcript stream fails | No BAA amendment; vendor SOC 2 excludes the AI service; failure alert exists | **No** |
| Accountable and transparent | Callers told calls are recorded; suggestions logged with model version; telecommunicator decisions logged by named account | Logging complete at consoles; no recorded greeting on request lines | Partial |
| Explainable and interpretable | Telecommunicator can see which transcript words drove each prompt | Shown in the advisory panel | Yes |
| Privacy-enhanced | No training on company data; audio deleted within 7 days | Training not excluded; 30-day retention under the order form | **No** |
| Fair, with harmful bias managed | Under-triage by caller language (English, Spanish, Haitian Creole) and by patient age (75 and over vs under 75). Flag if a group exceeds the English or under-75 rate by more than 2 percentage points; groups with fewer than 50 time-critical calls are reported as insufficient data | English 2.6% (13 of 502); Spanish 5.5% (5 of 91); Haitian Creole 1 of 17 (insufficient data); 75 and over 4.6% (11 of 240) vs under 75 2.2% (8 of 370) | **No.** Spanish and age disparities flagged |

**Bias finding.** The tool performs worse for Spanish-speaking callers and for calls about patients 75 and over, which matters in a Florida service area. Most of the gap traces to transcription errors and to callers describing an older relative's symptoms indirectly. The Haitian Creole sample is too small to measure. Under 45 CFR 92.210(c), the company's mitigation is: (1) the upgrade-only design, so the AI can never lower a telecommunicator's priority; (2) limiting advisory mode to English-language calls from 2026-09-16, with Spanish calls returning to shadow mode until keyword sensitivity reaches 98%; (3) keeping the EMD protocol as the decision of record; and (4) asking the vendor for accuracy data by language and age.

### 4.2 AI-002 narrative drafting (Medium)
| Test | Result | Pass? |
|---|---|---|
| Sample of 30 drafted narratives compared with structured fields and the crew's account | 4 of 30 contained a statement not supported by the structured fields (for example "patient denies chest pain" when no such question was documented) | **No** (threshold 0 unsupported clinical statements) |
| Share of drafts signed without any edit | 70% | **No** (signals automation bias) |
| Vendor confirmation of no training on customer data | Requested; not yet received | Pending |

### 4.3 AI-003 coding assistance (High)
| Test | Result | Pass? |
|---|---|---|
| Certified coder audit of 200 straight-through claims (2026-07) | Level of service disagreed on 18 (9%): 14 coded higher than the documentation supports (for example ALS1 emergency instead of BLS emergency), 4 coded lower | **No** (threshold 2% or less) |
| Diagnosis code agreement | 89% | **No** (threshold 95%) |
| Error rate by payer and by client | Higher on Medicaid claims (12%) than on commercial claims (6%); similar across the 2 clients in scope | Flagged for the look-back |
| Change control for model and rule updates | 2 vendor model updates and 6 rule changes in 10 months without company approval or testing | **No** |

**Overpayment exposure.** About 52,000 claims were coded straight through between 2025-11-01 and 2026-09-16, for the company and 2 clients. The look-back review by an outside coding auditor is the company's timely, good-faith investigation under 42 CFR 401.305(b)(3). Overpayments it confirms are reported and returned within the 401.305 deadlines. Findings on client claims go to the affected client in writing, because the client received those payments.

### 4.4 AI-004 posting (High)
| Test | Result | Pass? |
|---|---|---|
| Response-time compliance by zone, against each zone's own standard, before (2025) and after (2026 to date) the model | Overall compliance rose from 90.4% to 91.6%. Two zones with the highest share of residents aged 65 and over fell from 91% to 88% and 89% | **No** (threshold: no zone falls more than 1 point) |
| Supervisor override rate | 14% of recommendations overridden; reasons logged in 60% | Partial |
| Model change control | Retrained monthly by analysts without approval | **No** |

**Equity finding.** The model optimizes overall compliance, so it moves units away from lower-volume zones whose calls are often for older residents. People set minimum coverage rules per zone from 2026-10-15, and a monthly response-time equity report by zone goes to the Director of Communications and the counties.

### 4.5 AI-005 assistant (Low)
Checklist review passed: enterprise agreement with a BAA and a no-training term, single sign-on with MFA, data retention of 30 days, PHI prohibited during the pilot, and user acknowledgment of POL-05 4.8.

## 5. MANAGE
| ID | Conditions (owner, due) | Monitoring | Re-tier or re-review triggers | Stop criteria |
|---|---|---|---|---|
| AI-001 | BAA amendment with no-training, no-secondary-use, and 7-day audio deletion (Compliance and Privacy Officer, 2026-10-31); English-only advisory mode from 2026-09-16 (Director of Communications); recorded greeting and counsel's view on 934.03(2)(g) (Compliance and Privacy Officer, 2026-11-30); automation bias training for all telecommunicators (Director of Communications, 2026-11-30); vendor SOC 2 coverage of the AI service at the next report | Monthly under-triage and keyword sensitivity by language and age, reviewed by the Medical Director; weekly sample of 20 dismissed prompts | Any vendor model update (30 days back to shadow mode); adding the backup center or County B calls; any new language | Under-triage above 2% in a monthly report (return to shadow mode); BAA amendment not signed by 2026-10-31 (switch off and delete stored audio) |
| AI-002 | Attestation checkbox at signing; vendor no-training confirmation; monthly sample of 30 narratives (Director of Clinical Services, 2026-12-31) | Unsupported-statement rate; unedited-signature rate | Any treatment suggestions added by the vendor (re-tier to High) | Any unsupported statement in a monthly sample after 2026-12-31 (disable the feature) |
| AI-003 | Straight-through coding ends by 2026-10-01; 100% coder review; look-back review complete by 2026-12-31; vendor model and rule changes need company approval and a test set; written notice of findings to the 2 affected clients (Director of Revenue Cycle) | Monthly audit of 100 coded claims; error rates by payer and client | Any vendor model update; adding the other 2 clients | Level-of-service error above 2% for 2 consecutive months (disable suggestions) |
| AI-004 | Minimum coverage rules per zone from 2026-10-15; retraining only after approval by the Director of Communications; override reasons required (Director of Communications) | Monthly equity report by zone shared with both counties | New data sources; any change to the objective function | Any zone below its contract standard for 2 consecutive months because of model-driven moves |
| AI-005 | PHI prohibited during the pilot; reassess before any PHI use (Security Manager, 2027-03-31) | Quarterly usage review | Any request to use PHI or client data | Vendor changes its no-training term |

**Human-in-the-loop design for AI-001.** The telecommunicator runs the EMD protocol on every call and sets the priority; that is the decision of record. The AI may show an upgrade prompt ("possible cardiac arrest; consider Priority 1") and keyword alerts. It never shows a lower priority, and it never dispatches. Telecommunicators can dismiss any prompt with one click; dismissals are logged by named account and sampled weekly. If the transcript stream fails, the panel says so plainly, and the telecommunicator continues with the protocol.

**Incident handling.** A call where AI output may have contributed to a delay is a clinical incident: Medical Director review, plus P08 escalation if data or security is involved. A coding error pattern found by the monthly audit goes to the Director of Revenue Cycle and the Compliance and Privacy Officer for the overpayment process. A vendor security incident follows P08 and the BAA notice terms.

**Decommissioning.** For each tool: switch off the feature, confirm in writing that the vendor deleted company and client data (or return it under the BAA), remove integrations and credentials, and record the decision in the inventory.

## 6. Decision
Approved by the Chief Operating Officer with the Medical Director on 2026-09-16, with the conditions in section 5; the CEO was informed of the 3 High-tier decisions the same day. Tracked as POAM-022 in P07 and as P01 R-015 to R-020. The AI review group re-reviews AI-001 and AI-003 on 2026-12-15, after the first full quarter of monitoring under the new conditions.

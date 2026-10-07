# AI Governance Risk Assessment: Enterprise AI Portfolio and AI-Assisted Emergency Call Triage

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded private ambulance provider; FL, GA, AL, SC, TN) |
| Tier / Vertical | Enterprise / Emergency Services |
| Scope | Enterprise AI portfolio (9 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, AI-assisted emergency call triage, in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1); repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Medical Officer), meeting of 2026-08-19; GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-10 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 9 |
| Risk tier | High 4, Medium 4, Low 1 |
| Status | In production 7, Pilot 2 |
| Committee review complete | 5 of 9 |
| Not yet reviewed | 4: AI-003, AI-005, AI-006, AI-009 (all due 2026-11-30) |
| Patient care decision support tools identified under 45 CFR 92.210 | 1 AI tool (AI-001), plus the emergency medical dispatch protocol software, which is not AI but is a decision support tool that uses patient age as an input (section 5) |
| High-tier tools without local bias testing | 2 (AI-006, AI-009) |

**Main findings:** 4 use cases are running (or piloting) without committee review, including two High-tier tools: the SL-2 fraud detection model (AI-006) and the recruiting chatbot (AI-009, free-text screening now switched off). AI call triage under-triages time-critical calls more often than dispatchers do and performs worse for Spanish-language calls and for patients 75 and over, so it stays in shadow mode. The 92.210 inventory does not yet cover non-AI decision support tools such as the dispatch protocol software.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risks ER-08 (responsible use of AI) and ER-05 (public and patient safety) in P01, which the board risk committee reviews quarterly.

**Members:** Chief Medical Officer (chair); Medical Director for Communications; Chief Privacy Officer; CISO; Chief Compliance Officer; General Counsel's delegate; Chief Human Resources Officer (for workforce and HR tools); Vice President, Communications Centers; President, Managed Transportation; the data science lead; and a field paramedic representative. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Local validation and bias testing on the company's own data; 92.210 review where clinical; impact assessment; human review design; notice to affected people; monitoring plan |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.6; STD-05.3). Since 2026-03, procurement and change management block AI features without an inventory ID. The GRC team owns the inventory.

**Policies:** POL-04 4.8 (no Restricted data in AI tools without committee approval and a BAA with no-training terms); POL-05 4.6 (approved tools only); POL-01 4.8 (no BAA, no PHI); POL-01 4.13 (dispatch configuration changes, which covers any AI-driven change to response plans); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier tool; annual re-review of every use case.

**Why 4 use cases lack review.** AI-003 and AI-005 arrived as vendor feature releases before the intake block existed; AI-006 was built by the SL-2 analytics team as a "rules upgrade"; AI-009 came with a recruiting platform renewal. The committee set review dates for all four (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| HIPAA Privacy and Security Rules | Yes, for every use case with PHI | Vendors that handle PHI are business associates; BAAs with no-training and deletion terms are required (POL-04 4.8). For AI-001, the CAD vendor's BAA was amended on 2026-07-30 to cover the AI service |
| Section 1557, 45 CFR 92.210 | Yes | The company receives federal financial assistance (Medicaid) and operates health programs. It must not discriminate through patient care decision support tools, must make reasonable efforts to identify tools that use race, color, national origin, sex, age, or disability as inputs, and must make reasonable efforts to mitigate the risk. 45 CFR 92.4 covers automated and non-automated tools used to support clinical decision-making (section 5) |
| State call recording laws | Yes, for AI-001 and AI-005 | AI-001 transcribes recorded dispatch lines. Florida worked example: Fla. Stat. 934.03(2)(g) lets employees of a licensed ambulance service record incoming calls, with limits for 911 and published nonemergency numbers. Counsel's 2026-03 memo maps the Florida lines; the review of Tennessee lines and out-of-state callers is open (P03 G-101) |
| County agreements | Yes, for AI-001 and AI-002 | Response-time standards; counties expect notice before any change to how calls are prioritized |
| FTC Act Section 5 | Indirectly | Accuracy of vendor AI claims the company relies on; keep the claims in the procurement file |
| FDA device requirements | Vendor question | Whether the call triage module is regulated device software is the vendor's determination as manufacturer; the company requested the vendor's written position (received 2026-06: the vendor states it is not a device in its current advisory configuration) |
| Federal equal employment opportunity laws | Yes, for AI-009 (and AI-005 if used for employment decisions) | Title VII disparate-impact liability remains by statute even though federal enforcement guidance was withdrawn; counsel reviews adverse impact before free-text screening returns |
| State Medicaid broker contracts | Yes, for AI-006 | Contracts govern how trips may be questioned and how provider payments may be held |
| State AI laws (Colorado SB26-189, Texas TRAIGA) | No | The company does not do business in Colorado or Texas. The five operating states were not found to have a comprehensive AI statute in the cross-sector file; counsel monitors |
| NIST AI RMF Critical Infrastructure Profile | Guidance only | NIST released a concept note on 2026-04-07; the committee tracks it for dispatch use cases |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision (here, health care, government services, or employment) or able to affect physical safety.

| ID | Use case | Tier | Status | Committee review | 92.210 tool |
|---|---|---|---|---|---|
| AI-001 | AI-assisted emergency call triage | High | Pilot (shadow mode at RCC-1 and RCC-2) | Reviewed 2026-03-18; re-reviewed 2026-08-19 | Yes |
| AI-002 | Demand forecasting and dynamic unit posting | High | In production (RCC-1 to RCC-3) | Reviewed 2025-11-12 | No (resource deployment) |
| AI-003 | ePCR narrative drafting | Medium | Pilot (120 paramedics) | Not reviewed (due 2026-11-30) | No (documentation only) |
| AI-004 | Coding and level-of-service suggestions | Medium | In production | Reviewed 2026-01-21 | No |
| AI-005 | Contact center speech analytics and agent quality scoring (SL-2) | Medium | In production | Not reviewed (due 2026-11-30) | No |
| AI-006 | Trip and network provider fraud detection (SL-2) | High | In production | Not reviewed (due 2026-11-30) | No (not clinical) |
| AI-007 | Fleet predictive maintenance | Low | In production | Reviewed 2025-10-08 | No |
| AI-008 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-02-11 | No |
| AI-009 | Recruiting chatbot | High | In production (knock-out questions only) | Not reviewed (due 2026-11-30) | No |

**Tiering notes:** AI-002 is High because posting decisions change response times across whole zones, even though no individual patient is scored. AI-006 is High because a flag can delay a Medicaid member's trip or hold a small provider's payment. AI-003 stays Medium because the crew edits and signs every narrative; enabling treatment suggestions would re-tier it to High. AI-005 would become High if scores were used for discipline or pay.

## 5. Section 1557 (45 CFR 92.210) duties
| Duty | What the company does | Status |
|---|---|---|
| (a) Do not discriminate through patient care decision support tools | Committee review of AI tools; Medical Director oversight of the dispatch protocol | Partially met: AI-001 language and age gaps found in shadow mode; protocol review not documented |
| (b) Identify tools with race, color, national origin, sex, age, or disability inputs (ongoing) | AI inventory records protected-characteristic inputs. To add by 2026-11-30: the emergency medical dispatch protocol software (uses patient age as an input for some complaint types), CAD response plans that vary by patient age, and other non-automated tools | Partially met: AI tools identified; non-AI and non-automated tools not yet inventoried |
| (c) Make reasonable efforts to mitigate the risk of discrimination for each identified tool | AI-001: upgrade-only design, exclusion of non-English calls from any advisory use, and the protocol as the decision of record. Protocol software: Medical Director review of age-based determinants against clinical evidence (to be documented) | Partially met: mitigation documented for AI-001 only |

These rows match P03 G-106 to G-108 and POAM-020.

## 6. MEASURE: portfolio testing gaps
| Tool | Metric | Groups compared | Threshold for action | Status |
|---|---|---|---|---|
| AI-001 call triage | Under-triage of time-critical calls; keyword alert sensitivity | Caller language; patient age band | Any group more than 2 points worse than English or under-75 | Done in shadow mode (section 7) |
| AI-002 unit posting | Response-time compliance | County zone, including rural and lower-income zones | Any zone more than 5 points below its county standard for 2 months | Monitoring monthly |
| AI-006 fraud detection | Flag rate and overturn rate | Member county; provider size | Overturn rate above 50% or flag-rate ratio above 1.25 for any group | Not started (due with the review) |
| AI-009 recruiting chatbot | Pass-through rate | Self-identified sex and race where provided; age band | Adverse impact ratio below 0.8 | Not started (free-text screening disabled until done) |

## 7. Full assessment: AI-001 AI-assisted emergency call triage
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Transcribe calls to dispatch in real time and suggest a call type, a response priority (Priority 1 emergent, 2 urgent, 3 non-urgent), and alerts for critical keywords (for example, "not breathing"). The goal is faster recognition of time-critical calls such as cardiac arrest and stroke |
| Users / operators | Dispatchers at RCC-1 and RCC-2 (none see output during shadow mode) |
| Affected people | Callers and patients on about 2,900 calls a day at the two pilot centers, including transferred 911 callers; crews sent at the suggested priority |
| Data | Inputs: live call audio from the telephony platform (ePHI). Outputs: transcript, suggested call type and priority, keyword alerts (ePHI). BAA amendment (2026-07-30): no training on company data, no secondary use, audio deleted within 7 days |
| Build or buy | Buy: CAD vendor's cloud AI service integrated with the enterprise CAD |
| Not intended | Automatic dispatch; lowering a priority the dispatcher set; pre-arrival medical instructions; calls through relay services (excluded by configuration); RCC-3 and RCC-4. Enabling any of these requires re-assessment |

### 7.2 Risk tier
**High.** The AI would be a factor in a health care decision about a person (how fast an ambulance responds), and an error can affect physical safety. Even as an advisory tool, a missed critical keyword or a low suggested priority could anchor a busy dispatcher.

### 7.3 MEASURE (shadow mode, 2026-04-06 to 2026-07-31)
The **reference standard** is the clinical quality team's review of each call against the acuity found at patient contact (from the ePCR), overseen by the Medical Director for Communications. 6,400 calls were reviewed; 1,310 were time-critical (reference Priority 1).

| Trustworthy characteristic | Test / metric | Result (shadow mode) | Pass? |
|---|---|---|---|
| Valid and reliable | Under-triage: share of time-critical calls where the AI suggested Priority 2 or 3. Threshold: 2% or less, and no worse than dispatchers using the protocol | AI 3.1% (41 of 1,310); dispatchers 1.2% (16 of 1,310) | **No** |
| Valid and reliable | Over-triage: share of non-critical calls the AI suggested as Priority 1. Threshold: 25% or less (upgrades are tolerable in an upgrade-only design) | 21% | Yes |
| Safe | Critical keyword alert sensitivity ("not breathing", "unconscious", "no pulse"). Threshold: 98% or more | English 97.6%; Spanish 88%; Haitian Creole 71% | **No** |
| Secure and resilient | BAA; named SSO with MFA for CAD users; vendor SOC 2 covering the AI service; alert if the transcript stream fails | BAA amended; CAD accounts named with MFA; vendor's 2026 SOC 2 report includes the AI service; failure alert exists | Yes |
| Accountable and transparent | Suggestions logged with model version; dispatcher decisions logged; recorded notice on request lines | Logging complete; notice plays on request lines; transferred 911 callers hear no company notice (counsel review open) | Partial |
| Explainable and interpretable | Dispatcher can see which transcript words drove each suggestion | Available in the vendor's advisory view (not yet used) | Yes |
| Privacy-enhanced | No training on company data; audio deleted within 7 days; access limited to named users | Contract terms in place; deletion confirmed in the vendor's quarterly attestation | Yes |
| Fair, with harmful bias managed | Under-triage by caller language and by patient age (75 and over vs under 75). Flag a group more than 2 percentage points worse than English or under-75; groups with fewer than 50 time-critical calls are reported as insufficient data | English 2.4% (24 of 1,000); Spanish 5.0% (13 of 260); Haitian Creole 4 of 42 (insufficient data); other languages 0 of 8 (insufficient data); 75 and over 4.6% (19 of 410) vs under 75 2.4% (22 of 900). Transcription word error rate: English 8%, Spanish 18%, Haitian Creole 33% | **No.** Language and age disparities flagged |

**Bias finding.** The tool performs worse for Spanish-speaking callers and for calls about patients 75 and over, which matters in Florida and Georgia service areas. Most of the gap traces to transcription errors, and callers often describe an older relative's symptoms indirectly. The Haitian Creole sample is too small to measure. Under 45 CFR 92.210(c), the company's mitigation is: (1) the upgrade-only design, so the AI can never lower a dispatcher's priority; (2) excluding non-English calls from any advisory use until the vendor meets the thresholds; (3) keeping the dispatcher protocol as the decision of record; and (4) requiring vendor accuracy data by language and age before any advisory use (POAM-020).

### 7.4 MANAGE
**Human-in-the-loop design (for advisory mode, if approved):**
- The dispatcher runs the emergency medical dispatch protocol on every call and sets the priority. That is the decision of record.
- The AI may display an **upgrade prompt** ("possible cardiac arrest; consider Priority 1") and keyword alerts. It never shows a lower priority, and it never dispatches.
- The dispatcher can dismiss any prompt with one click; dismissals are logged and sampled weekly.
- If the transcript stream fails, the screen says so plainly, and the dispatcher continues with the protocol.

**Go-live gate (all required before advisory mode):**
1. Under-triage of 2% or less overall and no worse than dispatchers, and no flagged language or age group with enough data, over at least 90 more days of shadow mode.
2. Keyword alert sensitivity of 98% or more in English and Spanish.
3. Vendor accuracy data by language and age (POAM-020).
4. Counsel's written view on recording and transcription of transferred 911 callers and Tennessee lines (P03 G-101).
5. Notice to the affected county PSAPs and agreement where a county agreement requires it.
6. Dispatcher training on automation bias ("the protocol decides, not the prompt").
7. Committee vote and executive risk committee approval (High tier).

**Monitoring:**
- Monthly under-triage and keyword sensitivity report by language and age group, reviewed by the Medical Director for Communications and tracked in the risk register (R-011, R-012).
- Weekly sample of 20 dismissed prompts once advisory mode starts.
- Vendor model updates trigger a 30-day return to shadow mode with re-measurement.

**Incident handling:**
- Any call where the AI output contributed to a delay is a clinical incident: Medical Director for Communications review, plus P08 escalation if data or security is involved.
- A vendor security incident follows P08 and the BAA notice terms.

**Decommissioning:**
- Stop and delete stored audio if the vendor changes its data-use terms or breaches the BAA amendment.
- Stop if the vendor cannot provide accuracy data by language by 2027-01-31.
- Return to shadow mode (from advisory) if under-triage exceeds 2% in any monthly report.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier tool has quarterly performance and fairness metrics (inventory column `monitoring`) reported to the committee; drift or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse) are logged as SOC or clinical quality events and follow P08 where security or PHI is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts require notice of material model changes and no training on company data.
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice or change data-use terms; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the committee's recommendation of 2026-08-19:
1. **AI-001:** continue shadow mode at RCC-1 and RCC-2 only; advisory mode **not approved**. Re-assessment in 2027-01 after 90 more days of shadow data and the vendor's next model update.
2. **AI-002:** approved to continue; add rural and lower-income zone reporting to the monthly review.
3. **AI-003, AI-005, AI-006:** may continue in current scope until committee review by 2026-11-30; no expansion. AI-006 flags must keep human review before any trip is questioned or payment held.
4. **AI-009:** free-text screening stays disabled until committee review and an adverse impact analysis are complete; knock-out questions limited to license and certification.
5. **92.210 inventory:** extend to the dispatch protocol software and other non-automated tools by 2026-11-30 (POAM-020).

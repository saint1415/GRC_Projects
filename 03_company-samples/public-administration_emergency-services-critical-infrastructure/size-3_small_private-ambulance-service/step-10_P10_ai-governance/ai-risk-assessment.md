# AI Risk Assessment: AI-Assisted Emergency Call Triage

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensed private ambulance service) |
| Tier / Vertical | Small / Emergency Services |
| AI use case | AI-001: AI-assisted emergency call triage (CAD vendor module), shadow-mode pilot since 2026-06-15 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | Medical Director with the Communications Center Supervisor and IT Manager, 2026-08-24 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases; AI-001 assessed here, AI-002 summarized in section 7) |

## 1. GOVERN
- **Accountable owner:** Medical Director (clinical validity). **Operational owner:** Communications Center Supervisor. **Decision authority:** majority owner, because the use case is High tier (POL-01 4.4).
- **Policies that apply:**
  - POL-04 4.7: no Restricted data in AI tools without a BAA and approval
  - POL-05 4.9: approved tools only; AI-001 in shadow mode only
  - POL-01 4.8: no BAA, no ePHI (includes AI services that receive call audio)
  - POL-01 4.4: risks that can delay an emergency response are not accepted without a treatment plan
- **How it started:** the CAD vendor offered the module at no extra cost for a pilot, and it was switched on under an order form that no one reviewed for data use (gap 13 in `../00_company-facts.md`; P01 R-013). The shadow-mode design came from the Communications Center Supervisor, which kept the AI out of live decisions from day one.
- **Approved-tools list:** kept by the IT Manager. Today it lists AI-001 in shadow mode only. AI-002 is disabled.
- **Scale for a Small company:** there is no AI committee. The Medical Director, Communications Center Supervisor, IT Manager, and COO review AI use cases quarterly.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Transcribe calls to the dispatch center in real time and suggest a call type, a response priority (Priority 1 emergent, 2 urgent, 3 non-urgent), and alerts for critical keywords (for example, "not breathing"). The goal is faster recognition of time-critical calls such as cardiac arrest and stroke |
| Users / operators | 9 dispatchers and the dispatch supervisor (none see output during shadow mode) |
| Affected people | Callers and patients on about 44 calls a day, including transferred 911 callers from the county zone; also crews sent at the suggested priority |
| Data | Inputs: live call audio from the hosted phone system (ePHI). Outputs: transcript, suggested call type and priority, keyword alerts (ePHI). The order form lets the vendor keep audio for 30 days. **Training on company data is not contractually excluded** |
| Build or buy | Buy: CAD vendor's cloud AI service integrated with CAD |
| Not intended | Automatic dispatch; lowering a priority the dispatcher set; pre-arrival medical instructions; use on calls through relay services (excluded by configuration). Enabling any of these requires re-assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| HIPAA Privacy and Security Rules | **Yes** | The AI service receives and keeps call audio with PHI for the company, so the vendor is a business associate for this service. The existing CAD vendor BAA covers remote support only. **A BAA amendment is required before any further audio flows**; the pilot started without one (R-013) |
| Section 1557, 45 CFR 92.210 | **Yes (treated as in scope)** | The company receives federal financial assistance through Florida Medicaid. A patient care decision support tool is "any automated or non-automated tool ... used by a covered entity to support clinical decision-making" (45 CFR 92.4). Assigning response priority by symptom acuity supports a clinical decision. The tool does not take race or age as declared inputs, but it processes voice and language, and its accuracy varies by language (a national origin factor) and by patient age. The company therefore applies the 92.210(b) identification duty and 92.210(c) mitigation duty |
| Fla. Stat. 934.03(2)(g) | **Yes, with a question for counsel** | The statute allows an employee of an ambulance service licensed under Fla. Stat. 401.25 to intercept and record incoming wire communications. The same paragraph limits recording on designated 911 numbers and published nonemergency numbers to those staffed at public safety answering points. Counsel must confirm which company lines fall within the paragraph, including transferred 911 callers. A recorded "calls are recorded" greeting on request lines is added as a safeguard |
| Fla. Stat. 501.171 | Yes | Call audio and transcripts contain personal information, including medical information |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. Keep the marketing claims the company relied on in the procurement file |
| FDA device rules | Not determined | Whether the product is a regulated medical device is the vendor's question as manufacturer. Request its written regulatory position |
| State AI laws (for example, Colorado SB26-189, Texas TRAIGA) | No | The company operates only in Florida. State-specific AI analysis beyond the cross-sector file is out of scope |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why High:** the AI would be a factor in a health care decision about a person (how fast an ambulance responds), and an error can affect physical safety. Even as an advisory tool, a missed critical keyword or a low suggested priority could anchor a busy dispatcher.

**Minimum controls for High:** human review before action, pre-deployment bias testing, an impact assessment (this document), notice to affected people, and ongoing monitoring. None of these was in place when the module was switched on; shadow mode is what kept the risk contained.

## 4. MEASURE
Shadow mode ran from 2026-06-15 to 2026-08-15. The AI's suggestions were logged but not shown. The **reference standard** is the Medical Director's review of each call against the acuity found at patient contact (from the ePCR). 1,020 calls were reviewed; 214 were time-critical (reference Priority 1).

| Trustworthy characteristic | Test / metric | Result (shadow mode) | Pass? |
|---|---|---|---|
| Valid and reliable | Under-triage: share of time-critical calls where the AI suggested Priority 2 or 3. Threshold: 2% or less, and no worse than dispatchers using the protocol | AI 4.2% (9 of 214); dispatchers 1.4% (3 of 214) | **No** |
| Valid and reliable | Over-triage: share of non-critical calls the AI suggested as Priority 1. Threshold: 25% or less (upgrades are tolerable in an upgrade-only design) | 18% | Yes |
| Safe | Critical keyword alert sensitivity ("not breathing", "unconscious", "no pulse"). Threshold: 98% or more | 96% in English; 81% in Spanish | **No** |
| Secure and resilient | BAA; SSO with MFA for CAD users; vendor SOC 2 covering the AI service; alert if the transcript stream fails | No BAA amendment; CAD not federated; vendor SOC 2 does not yet cover the AI service; failure alert exists | **No** |
| Accountable and transparent | Callers told calls are recorded; suggestions logged with model version; dispatcher decisions logged | Logging complete; no recorded greeting on request lines | Partial |
| Explainable and interpretable | Dispatcher can see which transcript words drove each suggestion | Available in the vendor's advisory view (not yet used) | Yes |
| Privacy-enhanced | No training on company data; audio deleted within 7 days; access limited to named users | Training not excluded; 30-day retention; shared CAD accounts | **No** |
| Fair, with harmful bias managed | Under-triage by caller language (English, Spanish, Haitian Creole) and by patient age (75 and over vs under 75). Flag if a group exceeds the English or under-75 rate by more than 2 percentage points; groups with fewer than 50 time-critical calls are reported as insufficient data | English 2.8% (5 of 176); Spanish 9.1% (3 of 33); Haitian Creole 1 of 5 (insufficient data); 75 and over 5.7% (5 of 88) vs under 75 3.2% (4 of 126). Transcription word error rate: English 9%, Spanish 21%, Haitian Creole 38% | **No.** Language and age disparities flagged |

**Bias finding.** The tool performs worse for Spanish-speaking callers and for calls about patients 75 and over, which matters in a Florida service area. Most of the gap traces to transcription errors, and elderly callers often describe a spouse's symptoms indirectly. The Spanish sample is small (33 time-critical calls), and the Haitian Creole sample is too small to measure. The vendor must supply accuracy data by language and age before any advisory use. Under 45 CFR 92.210(c), the company's mitigation is: (1) the upgrade-only design, so the AI can never lower a dispatcher's priority; (2) excluding non-English calls from advisory mode until the vendor meets the thresholds; and (3) keeping the dispatcher protocol as the decision of record.

## 5. MANAGE
**Human-in-the-loop design (for advisory mode, if approved):**
- The dispatcher runs the emergency medical dispatch protocol on every call and sets the priority. That is the decision of record.
- The AI may display an **upgrade prompt** ("possible cardiac arrest; consider Priority 1") and keyword alerts. It never shows a lower priority, and it never dispatches.
- The dispatcher can dismiss any prompt with one click; dismissals are logged and sampled weekly.
- If the transcript stream fails, the screen says so plainly, and the dispatcher continues with the protocol.

**Go-live gate (all required before advisory mode):**
1. BAA amendment with no-training, no-secondary-use, and 7-day audio deletion terms (POAM-011).
2. Under-triage of 2% or less overall, and no flagged language or age group with enough data, over at least 60 more days of shadow mode.
3. Keyword alert sensitivity of 98% or more in English and Spanish.
4. Counsel's written view on Fla. Stat. 934.03(2)(g) line coverage, and the recorded greeting in place.
5. Named CAD accounts (POAM-003), so every dismissal is attributable.
6. Dispatcher training on automation bias ("the protocol decides, not the prompt").
7. Medical Director sign-off and majority owner approval.

**Monitoring:**
- Monthly under-triage and keyword sensitivity report by language and age group, reviewed by the Medical Director and tracked in the risk register (R-014).
- Weekly sample of 20 dismissed prompts.
- Vendor model updates trigger a 30-day return to shadow mode.

**Incident handling:**
- Any call where the AI output contributed to a delay is a clinical incident: Medical Director review plus P08 escalation if data or security is involved.
- A vendor security incident follows P08 and the BAA notice terms.

**Decommissioning:**
- Stop and delete stored audio if the BAA amendment is not executed by 2026-10-15.
- Stop if the vendor changes its data-use terms or cannot provide accuracy data by language.
- Stop advisory mode (return to shadow) if under-triage exceeds 2% in any monthly report.

## 6. Decision
**Continue shadow mode only; advisory mode not approved.** Majority owner and Medical Director, 2026-09-04. Conditions for continuing even shadow mode, due 2026-10-15:
1. The BAA amendment is executed (POAM-011). If not, the module is switched off.
2. The vendor confirms in writing that company audio is not used for training and states its FDA regulatory position.
3. Calls through relay services and calls in languages other than English and Spanish stay excluded.

Re-assessment is scheduled for 2026-12-15, after 60 more days of shadow data.

## 7. Other inventory items
- **AI-002 (ePCR narrative drafting): Medium tier, proposed, disabled.** Before enabling: confirm the ePCR BAA covers the feature with no training on company data; require crew review and edit of every narrative; sample 10 narratives per month for accuracy against the structured fields. Accurate records are a state licensure duty (Fla. Stat. 401.30(1)).
- **AI-003 (public chatbots): prohibited for PHI and caller information** under POL-05 4.9.

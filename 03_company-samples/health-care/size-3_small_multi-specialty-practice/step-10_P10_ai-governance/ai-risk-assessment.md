# AI Risk Assessment: Ambient Clinical Documentation (AI Scribe)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (multi-specialty physician practice) |
| Tier / Vertical | Small / Health Care and Social Assistance |
| AI use case | AI-001: ambient clinical documentation (AI scribe) pilot, 3 providers since June 2026 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | Medical Director (Privacy Officer) with the IT Manager, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases), built from the accounts payable list, the identity provider app list, the EHR configuration and a staff survey (EV-020, EV-031, EV-005). How many staff use public chatbots was not established (intake open request) |

## 1. GOVERN
- **Accountable owner:** Medical Director. **Decision authority:** Practice Administrator (Medium tier). Majority owner if re-tiered High.
- **Policies that apply:**
  - POL-04 4.7: no Restricted data in AI tools without a BAA and approval
  - POL-05 4.8: approved tools only
  - POL-01 4.8: no BAA, no ePHI
- **Approved-tools list:** kept by the IT Manager. Today it lists only the AI scribe, and only for enrolled pilot providers.
- **Scale for a Small practice:** there is no AI committee. The Medical Director, IT Manager, and Practice Administrator review AI use cases quarterly.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Record the patient-provider conversation, transcribe it, and generate a draft visit note that the provider edits and signs. The goal is to cut after-hours charting time |
| Users / operators | 3 enrolled providers (primary care 2, cardiology 1) |
| Affected people | Patients whose visits are recorded (about 45 per day in the pilot); also the providers |
| Data | Inputs: visit audio (ePHI). Outputs: a transcript and draft note (ePHI). The vendor states audio is deleted after the note is signed. **Training on practice data is not yet contractually excluded** |
| Build or buy | Buy: vendor SaaS integrated with the EHR by copy-paste (no API integration yet) |
| Not intended | Diagnosis suggestions, orders, billing codes, or patient-facing output. These features are **disabled**. Enabling any of them requires re-assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| HIPAA Privacy and Security Rules | **Yes** | The vendor creates, receives, and maintains ePHI for the practice, so it is a business associate. **A BAA is required before any ePHI flows.** The pilot began before the BAA was signed (risk R-012), which is a compliance gap to close now |
| Florida Security of Communications Act, Fla. Stat. 934.03 | **Yes** | Recording an oral communication is lawful when *all parties* have given prior consent (934.03(2)(d)). Patients must consent before recording starts |
| Section 1557, 45 CFR 92.210 | **Not today** for AI-001 | The rule covers tools "used ... to support clinical decision-making" (45 CFR 92.4). The scribe drafts documentation with suggestion features disabled. **AI-002 (EHR alerts) is in scope**, because it supports clinical decisions using age and sex as inputs |
| ONC HTI-1 decision support interventions | No (not directly) | These duties fall on certified health IT developers, not the practice |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy and privacy claims. Keep the marketing claims the practice relied on in the procurement file |
| State AI laws (e.g., Colorado SB26-189, Texas TRAIGA) | No | The practice operates only in Florida. State-specific AI analysis is otherwise out of scope by decision (see `../00_company-facts.md`) |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why not High:** the scribe does not make decisions and is not "a substantial factor" in one. A licensed provider reviews, edits, and signs every note.

**Why not Low:** it processes ePHI, interacts with patients (recording), and its errors enter the legal medical record and can influence later care.

**Escalation triggers (re-tier to High and re-assess):**
- enabling diagnosis, order, or coding suggestions
- automatic note filing without provider signature
- expanding to behavioral health visits
- use with minors without a guardian-consent process

## 4. MEASURE
| Trustworthy characteristic | Test / metric | Result (pilot, June-August 2026) | Pass? |
|---|---|---|---|
| Valid and reliable | Monthly sample: 10 notes per provider compared with the transcript. Critical errors (wrong medication, dose, laterality, allergy) must be 0; minor errors under 5% of notes | 90 notes: 1 critical error (wrong laterality, caught at signing); minor errors 7% | **No.** Critical-error threshold missed |
| Safe | Provider signature required; errors caught before signing | 100% of notes signed by the provider; the critical error was caught | Yes |
| Secure and resilient | Vendor SOC 2 Type 2 (Security); SSO with MFA; access limited to enrolled providers | SOC 2 received; SSO pending (local vendor accounts with MFA) | Partial |
| Accountable and transparent | Patients told before recording; notes labeled as AI-assisted in the EHR | Verbal notice given; consent not documented | **No** |
| Explainable and interpretable | Provider can view the transcript beside the draft to verify each statement | Available in vendor app | Yes |
| Privacy-enhanced | BAA signed; no training on practice data; audio deleted within 7 days | BAA under review; training opt-out not in contract; deletion stated in vendor documentation only | **No** |
| Fair, with harmful bias managed | Compare minor-error rates for (a) visits in English with patients whose first language is not English, and (b) patients 75+ versus under 75. Flag if a group's rate exceeds the baseline by more than 5 percentage points | Non-native English speakers: 13% vs 5% baseline | **No.** Disparity flagged |

**Bias finding.** Error rates are higher for patients whose first language is not English, which matters in a Florida patient population. Providers must take extra review care on these visits. The vendor must supply accuracy data by language. Spanish-language visits are excluded from the pilot until the vendor demonstrates Spanish accuracy.

## 5. MANAGE
**Human-in-the-loop design:**
- The scribe produces a draft only.
- The provider must review the whole note against their memory and the transcript, edit it, and sign it.
- An attestation checkbox is added to the signing workflow: "I reviewed this AI-assisted note for accuracy."
- The provider can turn off recording at any time, and must turn it off for sensitive discussions the patient does not want recorded.

**Consent:**
- Front desk staff give a written notice at check-in.
- The provider asks for verbal consent before recording starts, and the consent is documented in the note.
- Declining has no effect on care.

**Monitoring:**
- Monthly 10-note sampling per provider, tracked in the risk register (R-028).
- Quarterly error-rate report by language and age group.
- Patient complaints are routed to the Privacy Officer.

**Incident handling:**
- A critical documentation error is corrected through the EHR amendment process and reviewed by the Medical Director.
- A vendor security incident follows P08 and the BAA notice terms.

**Decommissioning:**
- Stop and export if the BAA is not executed by 2026-10-15.
- Stop and export if critical errors persist two months in a row.
- Stop and export if the vendor changes its data-use terms.

## 6. Decision
**Approve with conditions.** Practice Administrator, 2026-08-31. The pilot may continue for the 3 enrolled providers **only if** these conditions are met by 2026-10-15:
1. The BAA is executed, including a no-training and no-secondary-use clause and 7-day audio deletion (POAM-010).
2. Written patient notice and documented verbal consent are in use at both clinics (Fla. Stat. 934.03).
3. The provider attestation checkbox is live.
4. Spanish-language visits stay excluded until the vendor provides accuracy data.

Expansion beyond 3 providers requires two consecutive months with zero critical errors and no unresolved bias flag.

**Related action for AI-002.** Review the EHR alert rules that use age or sex as inputs, as required by 45 CFR 92.210(b), and document the mitigation (92.210(c)). Due 2026-11-30.

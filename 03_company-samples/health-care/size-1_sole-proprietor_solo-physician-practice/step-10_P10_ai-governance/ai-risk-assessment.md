# AI Use Assessment: Consumer AI Scribe App (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (solo primary care physician practice) |
| Tier / Vertical | Sole Proprietorship / Health Care and Social Assistance |
| AI use case | AI-001: consumer AI scribe app on the owner's phone (SYS-07). Trial 2026-07-06 to 2026-07-17, about 96 recorded visits; paused 2026-07-20 |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; AI 600-1 for generative AI risks |
| Assessor and decision | Physician-owner, 2026-08-25; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases), built at intake from the phone's app store history and the app itself, the bank and card statements, the EHR decision support settings, and the BAA folder (EV-026, EV-014, EV-025, EV-013). With no staff, there was no survey to run. Not established: what the vendor still holds from the trial recordings, and whether it used them for training. The deletion request in section 6 is the first step to find out |

## 1. What it does (Map)
The app records the patient visit on the phone (EV-026), sends the audio to the app vendor's cloud, and returns a draft note that the owner copies into the EHR. Inputs and outputs are ePHI. It is a consumer product: the owner accepted click-through terms, and the vendor offers **no BAA**. The terms allow the vendor to keep recordings and use them to improve its service (EV-027). Patients were **not asked for consent** before recording (EV-028).

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| HIPAA Privacy and Security Rules | **Yes** | A vendor that receives and keeps PHI for the practice is a business associate. No BAA means each recording was a disclosure the Privacy Rule does not permit (164.308(b)(1); N62-R02) |
| HIPAA Breach Notification Rule | **Yes, to assess** | An impermissible disclosure is presumed a breach unless a documented four-factor risk assessment shows a low probability of compromise (45 CFR 164.402) |
| Fla. Stat. 934.03 | **Yes** | Recording an oral communication is lawful only when all parties have given prior consent (934.03(2)(d)). No patient was asked |
| Section 1557, 45 CFR 92.210 | Not for AI-001 | The scribe drafts documentation; it does not support clinical decisions (45 CFR 92.4). It does apply to the EHR reminders (AI-002), which use age and sex as inputs |

## 3. Risk screen (repository rubric)
**Tier: Medium** if used as designed: it touches patients and ePHI, but the physician reviews and signs every note and it makes no decisions. The tier does not matter yet, because **no tier allows PHI to go to a vendor without a BAA** (POL-01 6.1).

## 4. Data-sharing rules (Govern)
1. No PHI (audio, text, or images) goes to any AI tool without a signed BAA and a written P10 assessment (POL-01 9.5).
2. The BAA must bar use of practice data for model training or any purpose other than serving the practice, and must set a deletion period for audio.
3. No recording starts without each patient's prior consent, documented in the chart; a patient who declines gets the same care.

## 5. Human review of outputs (Measure and Manage)
For any future approved scribe: the physician reads the whole draft against memory and the transcript before signing; checks medications, doses, allergies, and laterality every time; and samples 5 signed notes a month against the transcript. A critical error (wrong drug, dose, side, or allergy) stops use until the vendor explains it. No accuracy testing was done during the trial.

## 6. Decision: stop (approved 2026-08-31)
**Do not resume the app.** Then, by 2026-09-30 (P01 R-009):
1. Delete the app and its recordings from the phone; send the vendor a written deletion request and keep the reply.
2. With counsel, complete and document the four-factor breach risk assessment for the trial visits. If a breach cannot be ruled out, follow the P08 notification matrix.
3. Ask counsel how to address the recordings made without consent under Fla. Stat. 934.03.
4. Consider a scribe **only** when a HIPAA-eligible tool is available with a BAA, no-training terms, and a consent workflow, and re-run this assessment first.

**Related action (AI-002):** by 2026-11-30, list the EHR reminder rules that use age or sex as inputs and document the reasonable steps taken to identify and mitigate discrimination risk, as 45 CFR 92.210 requires.

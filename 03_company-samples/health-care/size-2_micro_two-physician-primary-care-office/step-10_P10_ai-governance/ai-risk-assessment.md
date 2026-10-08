# AI Risk Assessment: Ambient Clinical Documentation (AI Scribe)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (primary care office, two physicians) |
| Tier / Vertical | Micro / Health Care and Social Assistance |
| AI use case | AI-001: AI scribe pilot, one physician (the associate physician), since 2026-06-01 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | Office Manager (Privacy and Security Officer) with the associate physician, 2026-08-25 |
| Decision | Owner physician, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases), built from the card statements and vendor invoices, the AI scribe vendor documents, the EHR configuration and a staff survey (EV-022, EV-023, EV-039, EV-036). How many staff use public chatbots, and what they enter, was not established (intake open request) |

## 1. GOVERN
- **Accountable owner:** the associate physician, who runs the pilot. **Decision authority:** the owner physician.
- **Policies that apply:**
  - POL-02 A.5: no BAA, no ePHI. This covers pilots and free trials.
  - POL-04 4.6: Restricted data only in approved AI tools; the AI scribe is approved only after its BAA and the conditions in section 6.
  - POL-02 C.2: no ePHI in public AI chatbots (AI-003).
- **Approved-tools list:** kept by the Office Manager in POL-04 4.6. It has one entry, the AI scribe, for the associate physician only.
- **Scale for a Micro practice:** there is no AI committee. The owner physician, associate physician, and Office Manager review AI use at the monthly security meeting.

**How the pilot started.** The associate physician signed up for the vendor's trial on 2026-06-01 and began recording visits (EV-023). The BAA was sent for review but not signed. That broke the "no BAA, no ePHI" rule that the practice has now written down (P01 R-011; P03 164.308(b)(1)).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Record the patient-physician conversation on a practice tablet, transcribe it, and draft a visit note that the physician edits and signs. The goal is to cut after-hours charting |
| Users | The associate physician only |
| Affected people | Patients whose visits are recorded (about 15 to 20 a day on pilot days), family members or companions in the room, and the physician |
| Data | Inputs: visit audio (ePHI, including companions' voices). Outputs: transcript and draft note (ePHI). The vendor's documentation says audio is deleted after the note is finalized. **The vendor's standard terms allow use of de-identified data to improve its models; no contract term excludes this yet** |
| Build or buy | Buy: vendor SaaS. Notes move to the EHR by copy and paste (no EHR integration) |
| Not intended | Diagnosis suggestions, orders, billing codes, patient-facing summaries. These features are **turned off**. Turning any on requires a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| HIPAA Privacy and Security Rules | **Yes** | The vendor creates, receives, and maintains ePHI for the practice, so it is a business associate. A BAA is required **before** any ePHI flows (45 CFR 164.308(b)(1); 164.314(a)). The pilot ran for three months without one |
| Florida Security of Communications Act, Fla. Stat. 934.03 | **Yes** | Recording an oral communication is lawful when **all parties** have given prior consent (934.03(2)(d)). "All parties" includes a spouse or interpreter in the room, not only the patient |
| Section 1557, 45 CFR 92.210 | **Not for AI-001 today** | A patient care decision support tool is any automated or non-automated tool used to support clinical decision-making (45 CFR 92.4). With suggestion features off, the scribe drafts documentation; it does not support clinical decisions. **AI-002 (EHR reminders) is in scope**, because it uses age and sex as inputs. The practice has an ongoing duty to make reasonable efforts to identify such tools and to mitigate discrimination risk |
| FDA device rules | Not assessed as applying | The vendor markets the scribe as documentation software, not a medical device. Recheck if clinical suggestion features are enabled |
| State AI laws in other states | No | The practice operates only in Florida |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why not High:** the scribe does not make, and is not a substantial factor in, a decision about a patient. The physician reviews, edits, and signs every note.
- **Why not Low:** it processes ePHI, records patients, and its errors can enter the legal medical record and shape later care.

**Re-tier to High and reassess if:** diagnosis, order, or coding suggestions are turned on; notes file without a physician signature; use expands to behavioral health visits or to minors without a guardian-consent step; or the second physician joins without the section 6 conditions.

## 4. MEASURE
The Office Manager and the associate physician compared 20 signed notes (10 from June, 10 from July) with their transcripts on 2026-08-20.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Critical errors (wrong medication, dose, side of body, allergy) must be 0; minor errors under 10% of notes | 1 critical error (a medication dose, caught at signing); minor errors in 3 of 20 notes (15%) | **No** |
| Safe | Every note signed by the physician; errors caught before signing | 20 of 20 signed; the critical error was corrected before signing | Yes |
| Secure and resilient | Vendor SOC 2 Type 2 (Security); MFA on the vendor account; recordings only on the practice tablet | SOC 2 report received, not yet reviewed; MFA on; app on the practice tablet only | Partial |
| Accountable and transparent | Patients told before recording; notes marked as AI-assisted | Verbal mention only; no written notice; consent not recorded; notes not marked | **No** |
| Explainable and interpretable | Physician can view the transcript next to the draft | Available in the vendor app | Yes |
| Privacy-enhanced | BAA signed; no model training on practice data; audio deleted within 7 days | No BAA; training use allowed by standard terms; deletion in documentation only | **No** |
| Fair, with harmful bias managed | Compare minor-error rates for visits held partly or fully in Spanish versus English; flag a gap over 10 percentage points | Spanish or mixed-language visits: 2 of 6 notes with errors (33%); English: 1 of 14 (7%). Sample is small, but the gap is flagged | **No (flagged)** |

**Bias finding.** Many of the practice's patients speak Spanish at home. Error rates look higher for Spanish or mixed-language visits. The sample is too small to be sure, so the practice treats it as a real risk until the vendor provides accuracy data by language. Until then, Spanish-language visits are excluded from the pilot.

## 5. MANAGE
**Data protection:**
- No recording until the BAA is signed. The BAA or addendum must: prohibit use of practice data for model training or any purpose other than providing the service, including in de-identified form; delete audio within 7 days; require breach and security incident notice (164.314(a)(2)(i); the practice will ask for 24 hours); and flow down to the vendor's subcontractors.
- Recording only on the practice tablet with the vendor app; never on a personal phone.
- The vendor account is added to the monthly account reconciliation (POL-02 B.5).

**Consent (Fla. Stat. 934.03(2)(d)):**
- A written notice at check-in explains the scribe and that declining has no effect on care.
- Before starting, the physician asks everyone in the room and records their consent in the note ("Patient and companion consented to AI-assisted documentation").
- The physician stops recording on request, and for any sensitive topic a patient does not want recorded.

**Human in the loop:**
- The scribe produces a draft only. The physician reviews the whole note against the transcript and their memory, corrects it, and signs it.
- An attestation line is added to the note template: "I reviewed this AI-assisted note for accuracy."

**Monitoring:**
- Monthly: 10 notes compared with transcripts; results logged against P01 R-022.
- Quarterly: error rate by visit language.
- Patient complaints about recording go to the Office Manager as Privacy Officer.

**Incident handling:** a critical documentation error that reaches a signed note is corrected through the EHR amendment process and reviewed by the owner physician. A vendor security incident is handled under POL-03 and the P08 runbook.

**Decommissioning:** stop and export notes if the BAA is not signed by 2026-09-30, if critical errors appear in two months in a row after restart, or if the vendor changes its data-use terms. Ask the vendor to confirm deletion of all practice audio and transcripts.

## 6. Decision
**Approve with conditions.** Owner physician, 2026-08-31.

Recording stops on 2026-08-31 and may restart for the associate physician only when all of these are met:
1. The BAA is signed with the terms in section 5 (target 2026-09-30; R-011).
2. Written notice at check-in and documented all-party consent are in use (R-012).
3. The attestation line is in the note template.
4. The associate physician and front desk complete a short consent and privacy training (POAM-007).
5. Spanish-language visits stay excluded until the vendor provides accuracy data by language.

Expansion to the owner physician requires two consecutive months with zero critical errors, no open bias flag, and a SOC 2 review of the vendor.

**Related action for AI-002.** The owner physician reviews the EHR reminder rules that use age or sex as inputs, documents whether any could lead to discrimination, and records the mitigation, as 45 CFR 92.210 requires. Due 2026-11-30.

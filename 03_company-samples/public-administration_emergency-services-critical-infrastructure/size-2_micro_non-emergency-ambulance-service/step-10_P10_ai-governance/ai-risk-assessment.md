# AI Risk Assessment: AI Intake Assistant for Trip Requests

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensed BLS ambulance service, non-emergency transport only) |
| Tier / Vertical | Micro / Emergency Services |
| AI use case | AI-001: AI intake assistant in the operations platform (SYS-09). Transcribes recorded trip-request calls, pre-fills the trip request, suggests a level of service and a medical necessity checklist, and flags possible emergencies for redirection to 911. Advisory use by the Scheduler-Dispatcher since 2026-06-01 |
| Why this use case | The registry use case is AI-assisted emergency call triage. This company takes no 911 calls, so the closest real use is triage of its request line: callers sometimes describe an emergency, and the assistant is meant to catch those and to sort routine requests |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | Office Manager (Privacy and Security Officer) with the Medical Director and the Scheduler-Dispatcher, 2026-08-28 |
| Decision | Owner with the Medical Director, 2026-09-04 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the Medical Director (clinical validity of the emergency flag and the level-of-service suggestion). **Operational owner:** the Scheduler-Dispatcher, the only user. **Decision authority:** the Owner, because the use case is High tier (POL-02 A.3).
- **Policies that apply:**
  - POL-02 A.5: no BAA, no ePHI. This covers AI features added to an existing service.
  - POL-04 4.6: Restricted data only in approved AI tools; the assistant is approved only under the conditions in section 6.
  - POL-02 C.2: no patient information in public AI chatbots (AI-003).
  - POL-03 4.6: any caller who describes an emergency is told to dial 911, whatever any system says.
- **Approved-tools list:** kept by the Office Manager in POL-04 4.6. It has one entry, AI-001, for the Scheduler-Dispatcher only.
- **Scale for a Micro company:** there is no AI committee. The Owner, the Medical Director, and the Office Manager review AI use at the monthly security meeting.

**How the pilot started.** The platform vendor offered the feature at no extra cost in May 2026. The Owner accepted the in-app feature terms on 2026-05-28, and the Scheduler-Dispatcher began using it on 2026-06-01. Nobody read the terms, which allow the vendor to use transcripts to improve its models, and nobody confirmed that the platform BAA covers the AI subprocessor (P01 R-013; P03 164.308(b)(1)). Unlike a shadow-mode pilot, the suggestions were visible from day one.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Speed up intake and reduce errors: transcribe each recorded request call, pre-fill patient, pickup, and destination fields, suggest a level of service (BLS stretcher, or "ambulance may not be medically necessary"), list the certification statement the trip will need, and show a red "possible emergency: advise caller to dial 911" flag when the caller describes emergency symptoms |
| Users | The Scheduler-Dispatcher only |
| Affected people | Patients and callers on about 15 request calls a day (facility staff, family members, patients), including Spanish-speaking callers; crews sent on the trips |
| Data | Inputs: call audio from the hosted phone system (ePHI), caller number. Outputs: transcript, pre-filled trip request, suggested level of service, PCS checklist, emergency flag (ePHI). The feature terms let the vendor keep audio and transcripts 90 days and use them "to improve the service" |
| Build or buy | Buy: platform vendor feature using a cloud speech-to-text and language model subprocessor |
| Not intended | Deciding whether to send an ambulance; clearing a caller as "not an emergency"; denying a transport; billing decisions. Any of these would require a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| HIPAA Privacy and Security Rules (C-EMERGENCY-R04) | **Yes** | The vendor and its AI subprocessor receive and keep call audio with PHI for the company. The platform BAA must cover the feature and require subcontractor terms (45 CFR 164.308(b)(1); 164.314(a)(2)(iii)). Use of transcripts to improve the vendor's models is not a use the company has permitted |
| Section 1557, 45 CFR 92.210 | **Yes (treated as in scope)** | The company receives federal financial assistance through Florida Medicaid. A patient care decision support tool is any automated or non-automated tool used to support clinical decision-making (45 CFR 92.4). Flagging emergency symptoms and suggesting whether an ambulance is needed support clinical decisions. The tool does not take race or national origin as declared inputs, but it processes voice and language, and the patient's age is captured in the request. The company therefore applies the ongoing duty to make reasonable efforts to identify such tools and to mitigate discrimination risk |
| Fla. Stat. 934.03 | **Yes** | The assistant depends on recorded calls. The company does not staff a public safety answering point, so it relies on all-party prior consent (934.03(2)(d)) through a recorded announcement on every request line, added 2026-08-25. Counsel is to confirm the announcement wording (P01 R-024) |
| Medicare ambulance rules | Indirectly | A suggestion that an ambulance "may not be medically necessary" touches the coverage standard in 42 CFR 410.40(e)(1). The decision belongs to the patient's clinicians and the certification statement, not the assistant |
| Fla. Stat. 501.171 | Yes | Transcripts contain medical information and insurance numbers |
| FDA device rules | Not determined | Whether the product is a regulated medical device is the vendor's question as manufacturer. Request its written position |
| State AI laws in other states | No | The company operates only in Florida |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why High:** the assistant can affect physical safety. A missed emergency flag on a call from a facility about a patient with chest pain could anchor a busy scheduler into booking a routine pickup instead of telling the caller to dial 911. A wrong "not medically necessary" suggestion could steer a bed-confined patient away from the transport they need. Both are health care decisions about a person.

**Minimum controls for High:** human review before action, pre-deployment bias testing, an impact assessment (this document), notice to affected people, and ongoing monitoring. None was in place on 2026-06-01. The only thing that limited harm was the Scheduler-Dispatcher's own judgment and the Medical Director's 911 redirect card at the desk.

## 4. MEASURE
The Medical Director and the Office Manager reviewed calls from 2026-06-01 to 2026-08-14 (1,150 calls processed). The **reference standard** is the Medical Director's review of each sampled call against the recording and, where a trip ran, the patient care report. Every call the assistant or the Scheduler-Dispatcher marked as a possible emergency was reviewed, plus a random sample of 200 other calls.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Emergency flag sensitivity: share of calls that described an emergency that the assistant flagged. Threshold: 95% or more | 11 of 14 (79%). The Scheduler-Dispatcher redirected all 14 callers to 911 | **No** |
| Valid and reliable | False flags: share of non-emergency calls flagged. Threshold: 10% or less | 46 of 1,136 (4%) | Yes |
| Safe | Level-of-service suggestion: share of "ambulance may not be medically necessary" suggestions the Medical Director judged wrong. Threshold: 5% or less | 6 of 18 such suggestions in the sample were wrong (33%), mostly bed-confined patients described as "able to sit up a little" | **No** |
| Secure and resilient | BAA coverage of the AI subprocessor; MFA on the platform; vendor SOC 2 covering the feature | Coverage unconfirmed; no platform MFA; feature not in the SOC 2 period | **No** |
| Accountable and transparent | Callers told calls are recorded; suggestions logged with model version; the Scheduler-Dispatcher's decision logged | Announcement since 2026-08-25 only; suggestions logged; decisions logged under the shared dispatch account | **No** |
| Explainable and interpretable | The Scheduler-Dispatcher can see the transcript words behind each suggestion | Available in the request screen | Yes |
| Privacy-enhanced | No training on company data; audio deleted within 30 days; access limited to named users | Training use allowed; 90-day retention; shared account | **No** |
| Fair, with harmful bias managed | Emergency flag sensitivity and the "not medically necessary" rate by caller language (English, Spanish), and by patient age (75 and over vs under 75). Flag a gap of more than 5 percentage points; groups with fewer than 30 calls are reported as insufficient data, but a gap that large is still flagged for follow-up | Emergency flag: English 10 of 11; Spanish 1 of 3 (insufficient data, but 2 of 3 missed). "Not medically necessary" rate: English 14 of 171 sampled calls (8%); Spanish 4 of 29 (14%; insufficient data); 75 and over 12 of 112 (11%) vs under 75 6 of 88 (7%). Transcription word error rate: English 8%, Spanish 19% | **No (flagged).** Language gaps flagged despite small samples; age gap (4 points) under the threshold and watched |

**Bias finding.** The assistant misses more emergency descriptions from Spanish-speaking callers and suggests "not medically necessary" more often for them. Older patients also see the suggestion more often, though the gap is under the threshold. Most of the gap traces to transcription errors and to indirect descriptions ("she can't really get up"). The samples are small, so the company treats the gap as real until the vendor provides accuracy data by language and age. Under 45 CFR 92.210, the mitigation is: (1) the emergency flag can only add a 911 reminder and can never clear one; (2) the level-of-service suggestion is hidden; and (3) Spanish-language calls get no AI suggestions until the vendor meets the thresholds.

## 5. MANAGE
**Human-in-the-loop design (from 2026-09-08):**
- The Scheduler-Dispatcher asks the Medical Director's redirect questions on every call and decides whether to tell the caller to dial 911. That is the decision of record. The red flag is an extra prompt only; the absence of a flag means nothing.
- The level-of-service suggestion and the "not medically necessary" text are switched off (the vendor confirmed both can be hidden per user). Level of service is decided from the facility's information and the certification statement.
- Pre-filled fields (name, addresses, times) stay on; the Scheduler-Dispatcher checks each one against the caller before saving.
- Any disagreement between the Scheduler-Dispatcher and the flag is logged with one click and reviewed monthly.

**Data protection:**
- By 2026-10-15 the vendor must confirm in writing that the platform BAA covers the AI feature and its subprocessor, that company audio and transcripts are not used to train or improve models, including in de-identified form, and that they are deleted within 30 days. If not, the feature is switched off and the vendor is asked to confirm deletion.
- The recorded announcement plays on every request line, including after-hours forwarding.
- The feature is used only under a named account with MFA (POAM-002, POAM-003).

**Monitoring:**
- Monthly: the Medical Director reviews every flagged call, every logged disagreement, and 20 random calls, with results tracked against P01 R-014.
- Quarterly: flag sensitivity and false flag rate by language and age group.
- Vendor model updates: the Office Manager asks the vendor for release notes; a major model change triggers a fresh 30-day review before relying on the flag.

**Incident handling:** a call where the assistant's output contributed to a delay is a clinical incident for the Medical Director's quality review (Fla. Stat. 401.265(2)). A vendor security incident is handled under POL-03 and the P08 runbook.

**Decommissioning:** switch the feature off if the BAA confirmation is not received by 2026-10-15, if the vendor changes its data-use terms, or if the emergency flag misses 2 emergencies in any month. Ask the vendor to confirm deletion of all company audio and transcripts.

## 6. Decision
**Continue with conditions; level-of-service suggestions off.** Owner with the Medical Director, 2026-09-04.

Use continues from 2026-09-08 only in the restricted form in section 5, and only while all of these hold:
1. The vendor confirms BAA coverage, no-training terms, and 30-day deletion by 2026-10-15 (R-013; POAM-011).
2. The recorded announcement plays on every request line, and counsel confirms its wording by 2026-10-31 (R-024).
3. The Scheduler-Dispatcher completes the AI intake and recording training (POAM-006).
4. Spanish-language calls get no AI suggestions until the vendor provides accuracy data by language that meets the thresholds.
5. Named accounts with MFA replace the shared dispatch account by 2026-10-31.

Turning the level-of-service suggestion back on requires 90 days of monitoring with emergency flag sensitivity of 95% or more, no flagged language or age gap, a wrong "not medically necessary" rate of 5% or less, and a new decision by the Owner and the Medical Director. Re-assessment is scheduled for 2026-12-15.

## 7. Other inventory items
- **AI-002 (billing company's coding and denial prediction): Medium tier, in production at the billing company.** The billing company's coders review every suggested code and the company's Office Manager works every denial. Before the next contract renewal, confirm the billing BAA covers the feature with no training on company data, and ask for the billing company's accuracy checks.
- **AI-003 (public chatbots): prohibited for patient information** under POL-02 C.2 and POL-04 4.6.

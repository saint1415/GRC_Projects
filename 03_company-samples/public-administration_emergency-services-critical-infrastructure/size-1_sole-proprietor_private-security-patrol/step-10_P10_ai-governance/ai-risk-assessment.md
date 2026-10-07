# AI Use Assessment: Patrol App AI Report Assistant (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (unarmed private security patrol, licensed Class "B" agency) |
| Tier / Vertical | Sole Proprietorship / Emergency Services |
| AI use case | AI-001: the patrol app's AI report assistant (part of SYS-01). Turned on 2026-05-04; about 140 reports drafted by 2026-08-12. This is the one-person version of the registry's "AI-assisted emergency call triage": it triages **incident alerts to clients**, not 911 calls |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; AI 600-1 for generative AI risks |
| Assessor and decision | Owner, 2026-08-24; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (1 use case) |

## 1. What it does (Map)
On patrol, the owner records a voice note in the app. The app sends the audio to a third-party AI model provider, which returns a transcript, a drafted incident report, an incident type, and a **priority**. Until this assessment, an "Immediate" priority sent the client an alert at once, and a "Routine" one waited for the 6:30 a.m. daily report. Inputs and outputs can name people and include descriptions, vehicle details, and sometimes ID numbers or injury notes. The AI provider is carved out of the vendor's SOC 2 report (P09). The vendor's AI terms let it use customer content to improve its features unless the admin opts out; the owner opted out on 2026-08-12. The AI provider keeps prompts for 30 days.

**What went wrong.** On 2026-07-19 at about 1:40 a.m. the owner dictated a note about water coming from under a unit door at the self-storage facility. The assistant labeled it "Maintenance, Routine", so no alert went out. The manager learned of it from the daily report and arrived at about 7:15 a.m.; the contents of 3 units were water-damaged. The owner had assumed the app alerts on any water event.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| Fla. Stat. 493.6119(4) | **Yes** | No licensee may "willfully make a false statement or report" to a client or the department. An AI error is not willful, but a report the owner submits without reading is the owner's report |
| Fla. Stat. 493.6118(1)(e) | **Yes** | Information acquired in licensed work goes to the vendor and its AI provider. Use for the vendor's own purposes, before the opt-out, risks being an "unauthorized release" |
| Fla. Stat. 501.171(2), (6)(a) | **Yes** | Reasonable measures for personal information in voice notes; the vendor and AI provider are third-party agents with a 10-day breach notice duty |
| Client agreements | **Yes** | Confidentiality, and notice of incidents affecting the client (P03 G-019, G-020) |
| AI-specific laws | **No** | The business operates only in Florida. Florida's Digital Bill of Rights reaches only controllers above $1 billion in global gross annual revenue (Fla. Stat. 501.702); the business has about $180,000. No state AI law in the cross-sector file reaches a Florida-only patrol |

## 3. Risk screen (repository rubric)
**Tier: High.** As configured, the priority label could **affect physical safety**: it decided whether a client heard about a fire, flood, or intrusion at night or the next morning, and the near miss shows the harm is real. Drafting alone, with the owner setting every priority, would be **Medium** (it shapes reports clients rely on, but the owner makes every decision).

**Generative AI risks (AI 600-1) that matter here:** confabulation (invented or wrong details in a report, such as a plate number or a time), data privacy (personal information in voice notes sent to a provider outside the vendor's audit), and information integrity (reports used later as evidence).

## 4. Data-sharing rules (Govern)
1. Training on customer content stays off; the owner checks the setting after every app update (POL-01 9.5).
2. Voice notes must not include ID numbers, alarm or gate codes, or medical details beyond what the report needs. ID numbers are typed into the report's ID field, not dictated.
3. No other AI tool may receive Restricted data without its own P10 assessment.
4. Ask the vendor where voice notes are processed and kept, and whether the AI provider has an independent report (P09 follow-up, due 2026-10-31).

## 5. Human review of outputs (Measure and Manage)
- **Priority is the owner's decision.** The owner changed the app setting so the AI priority is only a suggestion and every report needs the owner to choose a priority before it can be submitted (done 2026-08-24).
- **Urgent events go by phone.** Fire, water, intrusion, injury, and police events are phoned to the client at once, whatever the app shows (POL-01 9.5).
- **Every draft is read in full** against the voice note before submitting, checking names, times, places, plate numbers, and what the owner actually did. Corrections after submission are dated addenda (POL-01 8.5).
- **Monthly sample:** the owner compares 5 submitted reports with their voice notes and records any AI error by type. Two errors that change meaning in one month, or any missed urgent event, stop use of the assistant until the vendor explains them.
- **Bias check:** descriptions of people in drafts are compared with the voice note in the monthly sample, so the tool does not add race, age, or other descriptors the owner did not say.

## 6. Decision: continue with conditions (approved 2026-08-31)
**Keep the assistant for drafting only.** Conditions, tracked as P01 R-008:
1. Owner-chosen priority on every report and phone calls for urgent events (in place 2026-08-31).
2. Training opt-out on (2026-08-12) and dictation rules in section 4.
3. Monthly sample review from September 2026; first result recorded by 2026-10-05.
4. Tell the self-storage client in writing what changed after the 2026-07-19 event.
5. Re-run this assessment before using any new AI feature (for example automatic alerts or video analysis), and at the August 2027 review.

# AI Use Assessment: Consumer Generative AI Chatbot (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent community pharmacy) |
| Tier / Vertical | Sole Proprietorship / Healthcare and Public Health |
| AI use case | AI-001: a consumer generative AI chatbot on a free personal account (SYS-08), used on the counter desktop and the phone from 2026-03-02. About 60 conversations: about 35 drafting counseling sheets, about 15 checking compounding calculations or formulations, about 10 drug information questions. Patient details pasted in 6 conversations. PHI and calculation use stopped 2026-08-07 |
| Why this use case | The registry default (a sepsis prediction model) needs an inpatient setting. This chatbot is the one third-party AI tool the owner actually uses |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 for generative AI risks (confabulation, data privacy) |
| Assessor and decision | Pharmacist-owner, chat history reviewed 2026-08-12; decision 2026-09-04 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
The owner types a question; the vendor's general-purpose language model returns text. It is a consumer product: the owner accepted click-through terms, the free plan offers **no BAA**, and the account setting that lets the vendor use chats to improve its models was **on**. The history review on 2026-08-12 found patient names or initials, ages, drugs, and doses in 6 conversations (allergies in 2). In one compounding conversation the chatbot converted a percentage strength to milligrams incorrectly; the owner caught it against the master formulation record before compounding. That is the generative AI risk NIST AI 600-1 calls confabulation: a fluent, confident, wrong answer.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| HIPAA Privacy and Security Rules | **Yes** | A vendor that receives and keeps PHI for the pharmacy is a business associate. With no BAA, each conversation with patient details was a disclosure the Privacy Rule does not permit (164.308(b)(1)) |
| HIPAA Breach Notification Rule | **Yes, to assess** | An impermissible disclosure is presumed a breach unless a documented four-factor risk assessment shows a low probability of compromise (45 CFR 164.402). Six individuals at most, so any notice would be individual notice plus the annual HHS log |
| Section 1557, 45 CFR 92.210 (parent vertical ID N62-R07) | **Yes for AI-002; for AI-001 only as it was used** | A patient care decision support tool is any automated or non-automated tool used to support clinical decision-making (45 CFR 92.4). Using the chatbot to check doses and formulations brought it within that definition; drafting general counseling text does not. The PMS DUR alerts (AI-002) are such a tool and use age and sex as inputs, so the pharmacy must identify them and make reasonable efforts to mitigate discrimination risk (92.210(b)-(c)) |
| FDA device rules | Not for the pharmacy | The pharmacy does not market software; the chatbot vendor does not claim a medical purpose |
| State AI laws | No | The pharmacy operates only in Florida, and no Florida statute specific to pharmacy AI use was identified for this review |

## 3. Risk screen (repository rubric)
- **As it was used: High.** Calculation and dose checks can affect patient safety, the rubric's trigger for High, and the tool had no validation, no BAA, and no review rule.
- **As restricted: Medium.** Counseling sheets reach patients (direct interaction with customers), but the pharmacist reviews every sheet and makes every decision.
No tier allows PHI to go to a vendor without a BAA (POL-01 6.1).

## 4. Data-sharing rules (Govern)
1. No patient name, initials, date of birth, age with a drug, prescription number, or any other patient detail goes into any AI tool unless a BAA and a written P10 assessment are in place (POL-01 9.5).
2. The model-training setting stays off, and chat history is deleted at the end of each month.
3. Any future AI tool that will see PHI needs a BAA that bars training on pharmacy data and sets a deletion period, and this assessment must be repeated first.

## 5. Human review of outputs (Measure and Manage)
- **No AI for calculations, doses, or formulations.** Every compounding calculation is checked against the master formulation record and a standard compounding reference, and high-risk compounds get a second calculation on paper (P01 R-010).
- **Counseling sheets:** the pharmacist checks every statement against the drug reference and the product labeling, removes anything not supported, and keeps the approved sheet in the file suite as a template; the chatbot is not asked again for a drug that already has an approved sheet.
- **Monitoring:** at each monthly review (POL-01 7.7) the owner scans the month's chat history for patient details before deleting it, and records the result.
- **What is not measured:** no accuracy or bias testing is planned for AI-001, because its outputs no longer inform clinical decisions. If that changes, the tool goes back to High and needs testing first.

## 6. Decision: restrict (approved 2026-09-04)
**Continue only for drafting general counseling text, with no patient details and no calculations.** Then, by 2026-09-30 (P01 R-009):
1. Turn off the training setting (done 2026-08-12) and delete the chat history after exporting the 6 conversations for counsel.
2. With counsel, complete and document the four-factor breach risk assessment for the 6 conversations. If a breach cannot be ruled out, follow the P08 notification matrix.
3. Tell the relief pharmacist the rule in POL-01 9.5 at the P08 walkthrough.

**Related action (AI-002):** by 2026-11-30, list the PMS DUR rules that use age, sex, or pregnancy status as inputs (from the vendor's knowledge base documentation), document why each input is clinically appropriate, and record the reasonable steps taken to identify and mitigate discrimination risk, as 45 CFR 92.210 requires.

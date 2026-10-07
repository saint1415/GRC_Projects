# AI Risk Assessment: PMS Controlled Substance Risk Score

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent community pharmacy) |
| Tier / Vertical | Micro / Healthcare and Public Health |
| AI use case | AI-001: controlled substance risk score (SYS-09), a machine-learning feature of the PMS switched on by the vendor's May 2026 release |
| Adapted from | The registry default, "clinical decision support (sepsis prediction) model", which needs an inpatient setting a pharmacy does not have. Like a sepsis model, the risk score is a vendor-built predictive score that supports a clinical decision, so the same questions apply: validity, bias, Section 1557, and human judgment (`../00_company-facts.md` section 5) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook. AI 600-1 is not used: the score is a predictive model, not generative AI |
| Assessor / dates | Staff Pharmacist (clinical lead) with the Store Manager (Privacy and Security Officer), 2026-08-17 to 2026-08-19 |
| Decision | Pharmacist-owner, 2026-08-28 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the Staff Pharmacist, as clinical lead for the score. **Decision authority:** the pharmacist-owner, who is also the DEA registrant contact.
- **Policies that apply:**
  - POL-04 4.6: Restricted data only in approved AI tools; any AI or decision support feature the PMS vendor switches on must be reviewed before staff rely on it. The risk score is the only approved entry, for pharmacists only, under the conditions in section 6.
  - POL-02 A.2: a PMS release with new clinical features is a major change that triggers a risk analysis update.
  - POL-02 C.2: no ePHI in public AI chatbots (AI-003).
- **Approved-tools list:** kept by the Store Manager in POL-04 4.6.
- **Scale for a Micro pharmacy:** there is no AI committee. The pharmacist-owner, the Staff Pharmacist, and the Store Manager review AI use at the monthly security meeting.

**How the score went live.** The vendor's May 2026 release added the score and switched it on for every customer by default. The release notes went to the Store Manager's email and were not read. From then until this review, every user, including technicians and the front-store clerk, saw a colored flag (Low, Elevated, High) on each incoming controlled substance prescription. Two technicians told the review that they had told patients their prescription was "flagged by the system" and would need extra checks (P01 R-019).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Help the pharmacist decide how closely to review an incoming controlled substance prescription, as part of the pharmacist's corresponding responsibility to dispense only prescriptions issued for a legitimate medical purpose (21 CFR 1306.04(a)) |
| Users | Intended: the two pharmacists. Actual until 2026-08-19: all PMS users |
| Affected people | About 6 to 7 controlled substance prescriptions a business day (about 12% of about 55); patients with chronic pain, ADHD, anxiety, or sleep disorders; their prescribers |
| Inputs (vendor documentation) | Patient age and sex; number of prescribers and pharmacies in the PMS history; morphine milligram equivalents; early refill history; payment type (cash or insurance); distance between the patient's address and the prescriber |
| Output | A score from 0 to 100 shown as Low, Elevated, or High, with the top three contributing factors |
| Data | All inputs come from the pharmacy's own PMS data (ePHI). The score does not use the state PDMP. The vendor's documentation says the model was trained on de-identified dispensing data from its customer base; the PMS BAA permits de-identification, and it is not clear whether this pharmacy's data was used |
| Build or buy | Buy: a feature of the PMS, run in the vendor's platform under the existing PMS BAA |
| Not intended | Refusing a prescription because of the score alone; telling patients about the score; replacing the PDMP consultation required by Fla. Stat. 893.055(8) |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Section 1557, 45 CFR 92.210 | **Yes** | The pharmacy is a Medicaid provider. A patient care decision support tool is any automated or non-automated tool used to support clinical decision-making (45 CFR 92.4); the decision to dispense a controlled substance is a clinical decision. The score uses age and sex as inputs, so the pharmacy must make reasonable efforts to identify that use (92.210(b), done by this review) and to mitigate the risk of discrimination (92.210(c), section 5) |
| DEA corresponding responsibility, 21 CFR 1306.04(a) | **Yes** | Responsibility for proper dispensing rests on the pharmacist who fills the prescription. A vendor score cannot carry that responsibility; the pharmacist's own documented judgment must |
| Florida PDMP consultation, Fla. Stat. 893.055(8) | **Yes** | The pharmacist must still consult the PDMP before dispensing a controlled substance to a patient aged 16 or older. The score is not a substitute |
| HIPAA Privacy and Security Rules | **Yes** | The score runs on ePHI in the PMS under the existing BAA. Open question: whether the vendor uses the pharmacy's data, even de-identified, to train the model |
| HIPAA Security Rule risk analysis, 45 CFR 164.308(a)(1)(ii)(A) | **Yes** | The release changed how ePHI is used and displayed; it is now in P01 (R-019) |
| ONC certification criteria for decision support interventions, 45 CFR 170.315(b)(11) | Not to the pharmacy | Duties fall on developers of certified health IT. The pharmacy has asked whether the PMS is certified and, if so, for the source attribute information |
| FDA device rules | Not assessed | The pharmacy is not the manufacturer. The vendor markets the score as a workflow feature |
| State AI laws in other states | No | The pharmacy operates only in Florida |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- The score can be a **substantial factor in a health care decision**: whether a patient receives a controlled substance today, gets a delay while the prescriber is called, or is refused. Before this review, staff were acting on it without a pharmacist's judgment.
- An unjustified refusal or delay can harm a patient (untreated pain, withdrawal, interrupted ADHD treatment), and a missed warning can contribute to misuse.

High tier requires human review before action, bias testing, an impact assessment (this document), notice to affected people where appropriate, and ongoing monitoring. Section 6 sets these as conditions.

## 4. MEASURE
The Staff Pharmacist pulled every controlled substance prescription processed from 2026-06-01 to 2026-07-31 (342 prescriptions) and compared the flag with the pharmacists' own documented assessment and the outcome.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Of prescriptions flagged High, the share the reviewing pharmacist independently judged to need extra steps; target at least 70% | 41 flagged High (12%); the pharmacist agreed on 22 (54%). Pharmacists judged 34 of the 342 to need extra steps; 3 of those were flagged Low | **No** |
| Safe | No refusal or delay based on the flag alone; every refusal documented with the pharmacist's reasons | 3 refusals and 5 delays; all 3 refusals had documented reasons beyond the flag. 2 delays were started by a technician because of the flag before a pharmacist saw the prescription | **No** |
| Secure and resilient | Runs in the vendor platform under SOC 2; score cannot be changed by users | SOC 2 Type 2 covers the platform; the May release is one of the questions in P09 | Partial |
| Accountable and transparent | Vendor documents inputs, training data, validation, and known limits; pharmacy knows who sees the score | Inputs and factors documented; no validation or subgroup performance data provided; every user could see the score | **No** |
| Explainable and interpretable | Top contributing factors shown with each score | Shown; pharmacists found them useful | Yes |
| Privacy-enhanced | No use of the pharmacy's data for training without agreement; score visible only to those who need it | Training data use unclear; score visible to all roles until 2026-08-19 | **No** |
| Fair, with harmful bias managed | Compare High-flag rates by sex, age group, and payment type; flag any group whose rate is more than twice the rate of the comparison group, then check whether pharmacist-judged concern differs the same way | By sex: women 9%, men 15%. By age: under 30 years 24%, 65 and older 5%. By payment: cash 31%, insured 10%. Pharmacist-judged concern by payment: cash 18%, insured 9% | **No (flagged)** |

**Bias finding.** The flag rate for cash-paying patients was about three times the rate for insured patients, while the pharmacists' own concern was about twice as high, so the score appears to amplify the difference. Payment type and distance can stand in for income and, in this neighborhood, for national origin, which Section 1557 protects. The age difference is larger than the pharmacists' own judgment supports for patients under 30. The sample is small (342 prescriptions), so the pharmacy treats these as real risks until the vendor supplies subgroup performance data. Sex is a direct input, and the vendor has not explained why it is needed.

## 5. MANAGE
**Mitigation under 45 CFR 92.210(c):**
- The score is shown to the pharmacist role only (vendor setting changed 2026-08-19). Technicians and the clerk no longer see it.
- A flag is a prompt to look, never a reason by itself. The pharmacist decides using the prescription, the PDMP, the patient's history, and, when needed, a call to the prescriber, and documents the reasons for any delay or refusal in the prescription record.
- Pharmacists give extra attention to the groups flagged in section 4 before acting on a High flag for a cash-paying or younger patient.
- The vendor has been asked in writing to explain the sex and payment type inputs, provide subgroup performance data, and offer a version without them.

**Data protection:**
- Ask the vendor to confirm in writing whether the pharmacy's data is used to train or improve the model, even de-identified, and to stop if the pharmacy objects; add the answer to the BAA file.
- The score stays inside the PMS; no export.

**Human in the loop:**
- The pharmacist reviews every controlled substance prescription, consults the PDMP as Florida requires, and makes the dispensing decision. The score never blocks a prescription automatically.
- Staff never tell a patient about the score. If a pharmacist delays or refuses, the reason given is the pharmacist's professional judgment.

**Monitoring:**
- Quarterly: the Staff Pharmacist repeats the section 4 tables (agreement rate, flag rates by sex, age group, and payment type) and logs the results against P01 R-019.
- After each PMS release: check whether the score, its inputs, or its display changed (POL-04 4.6).
- Patient complaints about delays or refusals go to the Store Manager as Privacy Officer and are reviewed by the pharmacist-owner.

**Incident handling:** a refusal or delay later found to be wrong is reviewed by the pharmacist-owner, the patient is contacted, and the case is logged under POL-03. A vendor security incident is handled under POL-03 and the P08 runbook.

**Decommissioning:** ask the vendor to switch the score off for the pharmacy if the agreement rate stays below 70% for two quarters, if the bias flags are not explained or fixed by 2027-03-31, or if the vendor will not confirm its training data use.

## 6. Decision
**Approve with conditions.** Pharmacist-owner, 2026-08-28.

The score may stay on, for pharmacists only, with these conditions:
1. Pharmacist-only display (done 2026-08-19); staff briefed not to mention the score to patients (done 2026-08-21).
2. Pharmacists document their own reasons for every delay or refusal; the flag alone is never a reason.
3. The vendor answers the questions on the sex and payment type inputs, subgroup performance, training data use, and whether the May 2026 release followed its change approval process, by 2026-10-31 (R-019).
4. Quarterly bias and agreement checks, the first by 2026-10-31.
5. The 45 CFR 92.210 review is extended to the PMS drug utilization review alerts that use age and sex (AI-002) by 2026-11-30.

**Re-tier or reassess if:** the vendor adds automatic blocking, starts using PDMP data, changes the inputs, or the agreement rate or bias checks fail two quarters in a row.

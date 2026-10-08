# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed multi-specialty physician group with an ASC and an imaging center) |
| Tier / Vertical | Mid-Market / Health Care and Social Assistance |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`, built from the accounts payable vendor master, the identity provider app list, the EHR and PACS configuration and a department heads survey (EV-035, EV-050, EV-007, EV-052). How many staff use public generative AI sites, and what they enter, was not established (intake open request); R-025 treats it as unknown |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-001, AI-004, and AI-005 |
| Assessors / date | Chief Medical Officer (clinical), vCISO and Security Manager (security), Compliance and Privacy Officer (privacy and legal), 2026-08-24 to 2026-09-10 |
| Decision | Chief Operating Officer and Chief Medical Officer, 2026-09-15; High-tier decisions noted by the CEO |

## 1. Summary
Four of the five tools (AI-001, AI-003, AI-004, AI-005) were adopted by departments without a security or privacy review (EV-037, EV-050). AI-002 came with the EHR. None of the tools is out of control, but three need conditions before they grow:
- **AI-001, the AI scribe:** has no reliable recording-consent process. That is a Florida law issue (Fla. Stat. 934.03).
- **AI-004, prior authorization:** submits 70% of requests with no human review.
- **AI-005, the chatbot:** receives PHI with no BAA.

AI-002 and AI-003 are patient care decision support tools under 45 CFR 92.210. The required review found 1 alert rule that used race as an input.

| ID | Use case | Risk tier | 92.210 in scope? | Decision |
|---|---|---|---|---|
| AI-001 | Ambient clinical documentation (AI scribe) | Medium | No, while suggestion features stay disabled | Approve with conditions; expansion paused |
| AI-002 | EHR clinical decision support alerts | Medium | **Yes** | Approve with conditions |
| AI-003 | Imaging triage (FDA-cleared) | High | **Yes** | Approve with conditions |
| AI-004 | Prior-authorization automation | High | No (not clinical decision support) | Approve with conditions; human approval required |
| AI-005 | Website chatbot | Medium | No | Conditional: BAA and redesign by 2026-11-30, or switch off |

Tiers: 2 High, 3 Medium, 0 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Chief Medical Officer, supported by the vCISO. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.13: AI tools must be approved before use.
  - POL-04 4.8: no Restricted data in unapproved AI tools; BAA with a no-training clause.
  - POL-05 4.8 and 4.9: approved tools only; human review of outputs; all-party recording consent.
  - STD-05 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Security Manager on the intranet. Today it lists AI-001 to AI-005 with their conditions and an enterprise generative AI assistant under BAA (pilot).

### 2.1 Proposed lightweight AI governance process
A mid-market company does not need a standing AI committee with a large charter. It needs a short, reliable gate and a monthly rhythm. The process below reuses existing roles and meetings.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool (or an AI feature turned on in an existing tool) submits a one-page intake: purpose, users, data, vendor, decisions affected | Requesting business owner | 15 minutes |
| 2. Triage | The Security Manager assigns a provisional tier with the P10 rubric and checks the purchasing gate (no PO without approval, POL-01 4.9) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist only. **Medium:** security, privacy (BAA, no-training clause, retention), and a clinical or business reviewer. **High:** full MAP and MEASURE assessment like this one, including a bias and performance plan and a 92.210 input-variable check where relevant | Security Manager; Compliance and Privacy Officer; CMO or business reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (CMO, vCISO, Compliance and Privacy Officer), meeting monthly for 30 minutes. High: the AI review group recommends, and the COO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owner reports the agreed metrics monthly (Medium) or monthly with a quarterly deep dive (High); incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type, expansion to a new population, or a safety event | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. **Re-tier triggers** are listed for each use case in section 4.

## 3. MAP
| Item | AI-001 Scribe | AI-002 EHR alerts | AI-003 Imaging triage | AI-004 Prior auth | AI-005 Chatbot |
|---|---|---|---|---|---|
| Purpose | Draft visit notes from recorded conversations | Remind providers of screening, interactions, dosing, risk | Prioritize suspected hemorrhage and pulmonary embolism studies on the reading worklist | Complete and submit payer authorization requests | Answer scheduling and general questions; take appointment requests |
| Users | 40 providers | All 90 providers | 6 radiologists (plus teleradiology overnight) | 18 CBO authorization staff | Website visitors |
| Affected people | Patients recorded (about 700 visits a day); providers | All patients | About 70 CT studies a day | About 350 requests a day | Patients and prospective patients |
| Data | Visit audio; transcripts; notes | EHR data including age and sex | CT images and DICOM metadata | Notes, diagnoses, codes | Names, dates of birth, phone numbers, free-text reasons |
| Build or buy | Buy (SaaS) | Buy (EHR configuration) | Buy (FDA-cleared software) | Buy (automation platform with a large language model) | Buy (SaaS) |
| Generative AI? | Yes | No (rules and vendor scores) | No (classification model) | Yes | Yes |
| Applicable laws | HIPAA (BA); Fla. Stat. 934.03 | 45 CFR 92.210 | 45 CFR 92.210; FDA labeling; 21 CFR 803 | HIPAA (BA); accuracy of payer submissions | HIPAA (BA required); FTC Act Section 5 |

**Laws considered and not applicable:**
- **State AI laws such as Colorado SB26-189:** the company operates only in Florida, and this assessment did not identify a Florida AI-specific statute applying to these uses. Florida-specific AI law was not researched beyond the recording statute.
- **42 CFR 422.101(c)(1)(i):** this governs how Medicare Advantage organizations make medical necessity determinations. It binds the payer, not the company's submissions under AI-004. It is still relevant context, because payers must base decisions on the enrollee's clinical records, which AI-004 summarizes.
- **ONC HTI-1 decision support transparency duties:** these fall on certified health IT developers (the EHR vendor), not the company. The company should use the source attributes the vendor publishes for AI-002 predictive scores in its review.

### 3.1 AI-001: recording consent under Florida law
Fla. Stat. 934.03(2)(d) makes interception of an oral communication lawful when **all parties** have given prior consent. An ambient scribe records the patient, the provider, and anyone else in the room (family members, interpreters, students).

**Findings:**
- The assessment sampled 30 scribe-assisted notes from 10 providers (2026-08). Consent was documented in 19 of 30.
- In 4 of 30, a third person was present with no record of that person's consent.
- No written notice was given at check-in.
- **Behavioral health visits:** 3 providers used the scribe for these visits, which the vendor's contract does not exclude.

**Required process (condition 1):**
1. Written notice at check-in and on the patient portal that some visits use an AI scribe, and that patients may decline without any effect on their care.
2. A verbal consent script before recording starts, covering every person in the room.
3. A required EHR field, "AI scribe consent obtained from all present: yes / declined", that blocks the scribe from starting if it is not completed.
4. Recording stops if anyone objects or a new person enters the room without consenting.
5. The Compliance and Privacy Officer audits 30 notes a month until 2 consecutive months reach 100% documented consent.
6. The scribe is not used in behavioral health visits until the CMO approves a specific protocol.

Legal counsel reviewed and approved this process on 2026-09-09.

### 3.2 AI-002 and AI-003: Section 1557 (45 CFR 92.210)
Section 92.210 prohibits discrimination through patient care decision support tools (92.210(a)). It creates an ongoing duty to make reasonable efforts to **identify** tools that use input variables measuring race, color, national origin, sex, age, or disability (92.210(b)), and to **mitigate** the risk of discrimination for each tool identified (92.210(c)). A patient care decision support tool is any automated or non-automated tool used to support clinical decision-making (45 CFR 92.4). Both AI-002 and AI-003 support clinical decisions, so both are in scope.

**AI-002 review (completed 2026-09-04 by the CMO with 3 specialty leads):**
| Input variable | Rules using it | Assessment | Mitigation |
|---|---|---|---|
| Age | 64 | Clinically required (screening intervals, pediatric and geriatric dosing) and consistent with current guidelines | Documented rationale per rule; annual review |
| Sex | 23 (16 of them also use age) | Clinically required (sex-specific screening); 2 rules did not account for patients whose recorded sex differs from anatomy relevant to screening | Rules updated to use organ inventory where the EHR supports it; manual review prompt otherwise (due 2026-10-31) |
| Race | 1 | Legacy spirometry interpretation rule used race-specific reference values | **Rule retired**; the clinical committee adopted a race-neutral interpretation approach (due 2026-10-31) |
| Disability, national origin, color | 0 | Not used | None needed |

In total, 71 of 212 rules use age or sex, and 1 rule used race.

**AI-003 review (completed 2026-09-08 by the Imaging Center Director and CMO):**
- The software processes image data. Its intended use is limited to adults, and it reads age from the DICOM header to exclude patients under 18. So it uses an input variable that measures age and is identified under 92.210(b).
- **Mitigation under 92.210(c):**
  - Obtain the manufacturer's published performance data by sex and age band.
  - Monitor local performance quarterly by sex and age band (section 4).
  - Confirm that studies of patients under 18 are never deprioritized. They are simply not flagged and are read in normal order, and this was verified in a 2026-08 sample of 20 pediatric head CTs.
  - Radiologists read every study regardless of the flag.

## 4. MEASURE (by use case)
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (2026-08 sample) | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | 10 notes per provider per quarter compared with the transcript; critical errors (medication, dose, laterality, allergy) | 0 critical; minor under 5% | 120 notes: 1 critical (dose, caught at signing); minor 6% | **No** |
| AI-001 | Fair, harmful bias managed | Minor-error rate for visits with patients whose preferred language is Spanish versus English | Gap no more than 5 points | Spanish 12% vs English 5% | **No** |
| AI-001 | Accountable and transparent | Consent documented for all parties | 100% | 19 of 30 (63%) | **No** |
| AI-001 | Privacy-enhanced | BAA prohibits training on company data; audio deleted within 7 days of signing | Both contractual | BAA permits de-identified use; deletion stated only in documentation | **No** |
| AI-002 | Fair, harmful bias managed | 92.210(b) inventory of input variables; mitigation documented | 100% of rules reviewed | 212 of 212 reviewed; 1 race-based rule retired | Yes (mitigation in progress) |
| AI-002 | Valid and reliable | Alert override rate per rule (signal of poor rules) | Review any rule overridden more than 90% | 14 rules above 90% | Partial: rules under review |
| AI-003 | Valid and reliable, safe | Discordance: flagged studies not confirmed, and confirmed findings not flagged, from radiologist reports | Missed flags no more than the manufacturer's labeled performance | 2 missed flags in 1,900 studies (both read within the normal time); consistent with labeling | Yes |
| AI-003 | Fair, harmful bias managed | Missed-flag rate by sex and by age band (18-44, 45-64, 65+) | No subgroup more than 2 times the overall rate | Too few events to judge; continue quarterly | Monitor |
| AI-003 | Secure and resilient | Runs in the PACS enclave; outbound only to vendor update endpoint; model version logged | All true | All true | Yes |
| AI-004 | Valid and reliable | Monthly sample of 50 submissions compared with the chart | Material errors under 2% | 50 sampled: 3 material errors (wrong laterality, outdated imaging date, missing conservative therapy history) = 6% | **No** |
| AI-004 | Accountable and transparent | Human approval before submission for ASC and imaging cases | 100% | 30% (exceptions only) | **No** |
| AI-005 | Privacy-enhanced | BAA; no free-text clinical data | Both | No BAA; free-text field open | **No** |
| AI-005 | Safe | Test 40 scripted clinical questions for unsafe answers and nurse-line handoff | 0 unsafe; 100% handoff | 3 answers gave general medical advice without handoff | **No** |
| All | Explainable and interpretable | Users can see the source for each output (transcript, rule logic, flagged image region, extracted chart text) | Available | Available for AI-001, AI-002, AI-003, AI-004; not for AI-005 | Partial |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the provider reviews and signs every note, with an attestation checkbox. There is no automatic filing.
- **AI-002:** alerts are advisory only, with no automatic orders.
- **AI-003:** a radiologist reads every study. The flag changes order, not whether a study is read.
- **AI-004:** staff must approve every ASC and imaging submission, and every request the tool scores below its confidence threshold.
- **AI-005:** it schedules only through call-center confirmation, and it must hand off clinical questions to the nurse line.

**Monitoring:** owners report the section 4 metrics monthly to the AI review group. High-tier items (AI-003, AI-004) also get a quarterly deep dive. Results feed the risk register (P01 R-019 to R-024).

**Incident handling:**
- A security or privacy incident at an AI vendor follows P08 and the BAA terms.
- A patient-safety event involving AI-003 is reviewed by the CMO. If it reasonably suggests that the device caused or contributed to a death or serious injury, the imaging center reports under 21 CFR 803.30 (the imaging center is a device user facility) within 10 work days.
- Material AI-004 submission errors are corrected with the payer, and counsel decides whether any look-back is needed.

**Decommissioning criteria:**
- AI-001: stop if the BAA is not amended by 2026-12-31, or if critical errors continue for 2 consecutive quarters.
- AI-004: stop automated submission if material errors stay above 2% for 3 months after human approval starts.
- AI-005: switch off on 2026-11-30 if the BAA is not signed and the free-text field is not disabled.
- Any tool: stop if the vendor changes data-use terms, or the model changes without notice.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions**; no new providers until met | Consent process live (2026-11-30); BAA amended with no-training and 7-day audio deletion (2026-12-31); Spanish-language accuracy data from the vendor; no behavioral health use without a CMO protocol | COO and CMO, 2026-09-15 |
| AI-002 | **Approve with conditions** | Retire race-based rule and fix 2 sex-based rules (2026-10-31); annual 92.210 review; review of 14 high-override rules (2026-12-31) | CMO, 2026-09-15 |
| AI-003 | **Approve with conditions** | Manufacturer subgroup performance data (2026-12-31); quarterly subgroup monitoring; MDR procedure added to imaging center policy (2026-10-31) | COO and CMO, 2026-09-15; noted by the CEO |
| AI-004 | **Approve with conditions** | Human approval for ASC and imaging submissions (2026-12-31); monthly 50-case sample; payer correction process | COO, 2026-09-15; noted by the CEO |
| AI-005 | **Conditional** | BAA executed, free-text symptom field removed, AI disclosure banner, and nurse-line handoff fixed by 2026-11-30, or switch off | COO, 2026-09-15 |

The conditions are tracked as POAM-024 in P07 and in the risk register (P01 R-019 to R-025). The AI review group holds its first monthly meeting on 2026-10-06.

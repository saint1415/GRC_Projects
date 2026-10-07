# AI Risk Assessment: AI-001 Camera-Based Respiratory Rate Function

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (medical device startup) |
| Tier / Vertical | Micro / Manufacturing (NAICS 334510) |
| AI use case | AI-001: AI-enabled device software function that estimates respiratory rate from the WM-1 hub's near-infrared camera video (image analysis). **Feasibility stage**; not part of the first 510(k) |
| Framework | NIST AI RMF 1.0 (AI 100-1); Generative AI Profile (AI 600-1) for the public-tool rule (AI-002) |
| Assessors / date | Head of Engineering with the QA/RA Manager and the Firmware Engineer; completed 2026-08-26 |
| Decision | CEO, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the Head of Engineering (model development, security, and performance). **Decision authority:** the CEO.
- **Review:** there is no AI committee. The CEO, Head of Engineering, and QA/RA Manager review AI use at the monthly security meeting; the regulatory consultant joins before any design input for AI-001 is approved.
- **Policies that apply:**
  - POL-02 A.10: security requirements, threat model, SBOM, and testing for every release. The model file and its inference library are software components of the hub and belong in the SBOM.
  - POL-04 4.7: no Restricted or Confidential data in AI tools that are not approved (covers AI-002).
  - POL-04 4.1: the training video shows identifiable research participants. **The CEO classified it as Restricted on 2026-08-31.**
- **Quality system link.** Once AI-001 moves from feasibility into development, it runs under **design controls** (21 CFR 820.10(c); ISO 13485 cl. 7.3, incorporated by reference). The design history file will hold the data management plan, model description, verification and validation, and the risk management file. This assessment is an input to that file; it does not replace it.
- **Approved-tools list:** kept by the Head of Engineering (POL-04 4.7). Today it lists no generative AI tool for Confidential data.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use (proposed) | Estimate respiratory rate from near-infrared video of the patient's chest when the wearable sensor is off or disconnected, and flag a mismatch when both are available. **Adjunct only:** a nurse confirms by a manual count before acting on a camera-based value. It does not diagnose, and it does not replace the sensor |
| Users | Nurses on general wards at hospital customers |
| Affected people | Adult inpatients on general wards, and anyone else in the camera's view (visitors, staff) |
| Data: training | A licensed research dataset from a university lab: about 60 hours of video from 120 adult volunteers with chest-band reference respiratory rate. Faces are visible. The dataset documentation reports ages 19 to 45 and gives no skin tone, body size, or clinical data. No patients lying in hospital beds under blankets. **The license terms have not been reviewed for commercial use (P01 R-019)** |
| Data: production (planned) | Video is processed **on the hub** and never leaves it. Only the respiratory rate estimate and a signal quality score are sent to the cloud service. No video is stored |
| Build or buy | Build. A motion-analysis pipeline with a small neural network trained in-house, running on the hub. The model will be **locked** in any submitted version; retraining would follow a predetermined change control plan (PCCP) if the company seeks one |
| Status of the hardware | The WM-1 hub has a near-infrared camera module that is **disabled in WM-1 firmware**. Enabling it is a design change for a later product version |
| Not intended | Pediatric patients; ICU use; apnea detection or any alarm driven by the camera alone; storing or sending video |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FD&C Act device requirements and QMSR design controls (21 CFR Part 820) | **Yes** | AI-001 measures a physiological parameter to support patient monitoring, so it is a device software function needing FDA marketing authorization. The pathway will be confirmed with FDA through a pre-submission |
| FD&C Act section 524B (N31-33-R05) | **Yes** | AI-001 is software in a hub that connects to the internet; the future submission is for a cyber device. The model file must be signed and verified like firmware, and listed in the SBOM |
| FDA draft guidance, *Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations* (notice of availability 90 FR 1154, 2025-01-07) | Nonbinding **draft** | Recommends data management, model description, performance validation including subgroups, bias control, performance monitoring, and AI-specific cybersecurity. No final version was found in the Federal Register as of 2026-09-25. Recheck before the pre-submission |
| FDA guidance, *Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions* (notice 89 FR 96259, 2024-12-04) | Nonbinding final guidance | Needed only if the company wants to authorize planned model updates in advance |
| HIPAA | **Not for the company today** | The company holds no PHI. The planned production design keeps video on the hub under the hospital's control. If the company later collects patient video at the partner hospital for training, the hospital's own HIPAA rules for research disclosures apply, and the company must meet the hospital's data use terms |
| Section 1557, 45 CFR 92.210 | **Hospitals, not the company** | Hospitals that receive federal financial assistance must make reasonable efforts to identify patient care decision support tools that use inputs measuring race, color, national origin, sex, age, or disability, and mitigate discrimination risk. Video carries skin color and apparent age. The company will give hospitals subgroup performance data so they can meet this duty |
| FTC Act Section 5 | Yes | Performance claims must be truthful and substantiated, and match the validated subgroup results |
| State AI laws | No | All sales are in Florida. Colorado SB26-189 (effective 2027-01-01) carves out FDA-regulated devices, per `00_universal-framework/cross-sector/us-cross-sector-obligations.md`. Recheck if the company sells into other states |

## 3. Risk tier
**AI-001: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`). Its output informs health care decisions about a person, and a wrong respiratory rate can affect physical safety. A nurse confirms before acting, but a **falsely normal** value may never get a second look, because the tool can give false reassurance.

**AI-002 (public generative AI tools): High if Restricted or Confidential data is entered**, so prohibited for that data (POL-04 4.7; P01 R-017).
**AI-003 (coding assistant built into the repository service): Medium.** It is switched off. It could be enabled only under an enterprise contract with no training on company code, and never for signing, key-handling, or cryptographic code.

## 4. MEASURE
Results are from the feasibility prototype on held-out volunteer video (24 volunteers not used in training) and an 8-hour bench session with 4 employees lying on a hospital bed in the lab, as of 2026-08-26.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Mean absolute error against the chest-band reference no more than 2 breaths per minute, and 95% of estimates within 4 breaths per minute | Volunteers (seated, uncovered): 1.3 breaths per minute, 94% within 4. Bench (lying under a blanket): 2.9 breaths per minute, 81% within 4 | **No.** Fails in the intended position |
| Safe | "No estimate" shown when signal quality is low; no alarm from the camera alone; labeling says a normal value does not rule out deterioration | Quality score works in the prototype; labeling not drafted | Partial |
| Secure and resilient | Threats to the model (adversarial patterns, model file tampering, camera misuse) in the threat model; model signed and verified with firmware; model and inference library in the SBOM | None done yet | **No** |
| Accountable and transparent | Model card stating training data sources, demographic mix, and subgroup performance; the value is labeled as camera-derived on screen | Model card outline only; on-screen label designed | Partial |
| Explainable and interpretable | Nurse can see the signal quality score and a breathing waveform next to the value | Working in the prototype | Yes |
| Privacy-enhanced | Video processed on the hub only; no video stored or sent; training data license and consent reviewed; Restricted handling of the dataset | On-hub design yes. **Dataset stored on one engineer's laptop and a shared folder; license not reviewed** | **No** |
| Fair, with harmful bias managed | Error by skin tone, body size, age group, sex, bedding, and sleeping position (thresholds in section 5) | Cannot be measured: the dataset has no demographic labels and only young adults | **No (untestable with current data)** |

**Bias finding.** The feasibility data cannot show whether AI-001 works for the patients it is meant for: older adults, lying down, under blankets, across skin tones and body sizes. Near-infrared imaging reduces but does not remove sensitivity to skin tone, and respiratory motion is harder to see in larger patients and under bedding. Until the company has representative data, any accuracy claim is unsupported.

## 5. Bias testing plan
| Element | Plan |
|---|---|
| Groups compared | Skin tone (a recorded scale such as Fitzpatrick I-II, III-IV, V-VI), body mass index (under 25, 25-35, over 35), age (18-64, 65-79, 80 and over), sex, bedding (none, sheet, blanket), and position (supine, side, semi-upright) |
| Metrics | Mean absolute error, share within 4 breaths per minute, and rate of "no estimate" per group, with 95% confidence intervals; sensitivity for detecting respiratory rate above 24 or below 8 breaths per minute |
| Thresholds | (1) Every group meets the overall accuracy threshold in section 4. (2) No group's mean absolute error is more than 1 breath per minute worse than the overall value. (3) No group's "no estimate" rate is more than 10 percentage points above the overall rate. Failing any threshold blocks design input approval for the intended use |
| Sample size | At least 30 participants per skin tone group and per body mass index group, recruited to targets rather than by convenience |
| Data source | A new data collection with informed consent under IRB oversight, at the partner hospital or a research site. The regulatory consultant will determine whether 21 CFR Part 812 applies before it starts |
| When | Before design input approval; again in design validation; after release, quarterly from complaint data and hospital feedback |
| Mitigations if a group fails | Collect more data for that group; improve the signal model; narrow the intended use (for example, exclude a position) and state the limit in labeling |

## 6. MANAGE
**Data protection (now):**
- Move the licensed dataset off the laptop and shared folder into one access-controlled storage location limited to the 2 engineers working on AI-001, and delete other copies (by 2026-09-30).
- Counsel reviews the license and the participants' consent scope. If commercial use is not allowed, stop using the dataset and delete it, and plan the new data collection (P01 R-019).
- Keep the production design: video processed on the hub, never stored or sent.

**Human in the loop (proposed design):**
- A camera-derived value is always labeled as such and shows its signal quality.
- A nurse confirms by manual count before acting on it. The camera never raises an alarm on its own.
- When the sensor is attached, the sensor value is primary; the camera only flags a mismatch.

**Monitoring after release:** quarterly review of accuracy and "no estimate" rates by group, from hospital feedback and complaints; a drop below any threshold triggers a complaint investigation and a correction decision (P08).

**Incident handling:** model tampering or camera misuse follows the P08 runbook. A missed deterioration linked to AI-001 is a complaint and is evaluated for MDR reporting once the device is marketed.

**Decommissioning:** the function can be switched off per hub by configuration. It will be switched off if performance falls below a threshold, if the model file fails integrity verification, or if a hospital asks.

## 7. Decision
**Approve continued feasibility work with conditions.** CEO, 2026-08-31. The following must be met before any AI-001 design input is approved:
1. Dataset moved to restricted storage and other copies deleted (2026-09-30); license and consent review completed (2026-10-31).
2. A data collection protocol that meets the bias testing plan in section 5, with IRB oversight and a regulatory determination.
3. AI-specific threats added to the threat model; the model file signed with firmware and listed in the SBOM (POL-02 A.10).
4. A pre-submission request to FDA covering the intended use, the validation design, and whether to include a PCCP, after the WM-1 510(k) is submitted.
5. No engineering time on AI-001 that delays the WM-1 510(k) critical path (P01 R-003).

**AI-002 and AI-003.** Public AI tools stay prohibited for Restricted and Confidential data (POL-04 4.7). The repository coding assistant stays off until an enterprise contract with a no-training term is signed and the Head of Engineering adds it to the approved list; target decision 2026-12-31.

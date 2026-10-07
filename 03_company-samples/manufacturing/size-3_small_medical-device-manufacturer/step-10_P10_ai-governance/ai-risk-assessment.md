# AI Risk Assessment: AI-001 Skin-Image Analysis Function and AI-002 Coding Assistant

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (connected medical device manufacturer) |
| Tier / Vertical | Small / Manufacturing (NAICS 334510) |
| AI use cases | **AI-001:** AI-enabled device software function that analyzes skin images for possible pressure injuries (in development; marketing submission planned 2027 Q3). **AI-002:** enterprise generative AI coding assistant for engineers (proposed pilot) |
| Framework | NIST AI RMF 1.0 (AI 100-1); Generative AI Profile (AI 600-1) for AI-002 |
| Assessors / date | Clinical Affairs Manager (registered nurse) with the VP Engineering, Product Security Lead, and VP QA/RA; contracted physician medical advisor for clinical review. Completed 2026-08-26 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases; AI-003 is the prohibited use of public tools) |

## 1. GOVERN
- **Accountable owners:**
  - AI-001: Clinical Affairs Manager (clinical performance and bias) and VP Engineering (model development and security).
  - AI-002: VP Engineering.
- **Decision authority** (repository rubric, scaled to a Small company):
  - High tier: the CEO, on the advice of the review group below.
  - Medium tier: the COO.
- **Review group:** there is no AI committee. The Clinical Affairs Manager, VP Engineering, VP QA/RA, Product Security Lead, and IT Manager review AI use cases each quarter. The physician medical advisor joins for AI-001.
- **Policies that apply:**
  - POL-01 4.5: security requirements, threat modeling, testing, and SBOM for every device release, including AI-001.
  - POL-04 4.9: no Restricted or Confidential data in AI tools that are not approved.
  - POL-05 4.8: approved AI tools only; no source code or PHI in public tools.
- **Quality system link.** AI-001 is device software, so its development runs under **design controls** (21 CFR 820.10(c), ISO 13485 clause 7.3). The design history file in PLM holds the data management plan, model description, verification and validation, and the risk management file. This assessment is an input to that file. It does not replace it.
- **Approved-tools list:** kept by the IT Manager and VP Engineering. Today it lists no generative AI tool. AI-002 is added for the pilot group only once its contract is signed (see section 7).

## 2. MAP: AI-001
| Item | Description |
|---|---|
| Purpose and intended use | A nurse photographs at-risk skin (sacrum, heels, hips) with a hospital-issued mobile device through the clinician portal. The AI-001 service in the device cloud flags images that show possible stage 1 or deep tissue pressure injury, which can be hard to see, especially on darker skin. A flag prompts an assessment by a wound care nurse. **Adjunct only:** it does not diagnose, stage, or replace the standard skin assessment |
| Users / operators | Bedside nurses and wound care nurses at hospital customers |
| Affected people | Hospitalized adults at risk of pressure injury. The hospitals serve a Florida population with a wide range of skin tones |
| Data: training and test | 14,200 images from 3 partner hospitals, **de-identified by the hospitals** under the HIPAA safe harbor method (45 CFR 164.514(b)(2)). Images showing faces or tattoos were excluded, because full-face and comparable images and unique identifying characteristics are identifiers. Labels come from 3 wound care nurses, with physician adjudication, using the bedside assessment as the reference standard. Skin tone was annotated on the Fitzpatrick scale: types I-II 48%, III-IV 39%, V-VI 13%. **Darker skin tones are under-represented** |
| Data: production | Photo, body site, and patient identifiers. Outputs: flag, heat map, and confidence score. All are PHI held in the device cloud for the hospital (business associate). Production images are **not** used for retraining without a new agreement with the hospital |
| Build or buy | Build. An image classification model fine-tuned from an open-source pretrained vision model. The model is **locked**: it does not learn in the field. Future retraining would follow a predetermined change control plan (PCCP) submitted with the marketing submission |
| Not intended | Staging or diagnosing wounds; use on patients under 18; use on images from personal phones; automatic documentation or orders. Any of these requires re-assessment and regulatory review |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FD&C Act device requirements and QMSR design controls (21 CFR Part 820) | **Yes** | AI-001 is a device software function and needs FDA marketing authorization before it can be sold. The pathway will be confirmed at an FDA pre-submission meeting |
| FD&C Act section 524B (N31-33-R05) | **Yes** | AI-001 includes software and connects to the internet through the device cloud, so it will be a cyber device. The submission needs the CVD plan, SBOM, and cybersecurity processes that P03 found incomplete (P01 R-010) |
| FDA draft guidance, *AI-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations* (January 2025; docket FDA-2024-D-4488) | Nonbinding **draft** | Recommends the content FDA expects: data management, model description, performance validation including subgroups, bias control, performance monitoring, and AI-specific cybersecurity. Still a draft as of 2026-09-25. Recheck before the submission |
| FDA guidance, *Marketing Submission Recommendations for a PCCP for AI-Enabled Device Software Functions* (final; Federal Register notice 2024-12-04) | Nonbinding guidance | Governs how planned model updates can be authorized in advance. Needed if the company wants to retrain without a new submission |
| HIPAA Security Rule (N62-R01) | **Yes, for production** | Production images and outputs are PHI in the device cloud. Hospitals' BAAs must cover the new service before clinical use. The de-identified training set is not PHI |
| Section 1557, 45 CFR 92.210 | **Hospitals, not the company** | Hospitals that receive federal financial assistance must make reasonable efforts to identify patient care decision support tools with inputs that measure race, color, national origin, sex, age, or disability, and to mitigate discrimination risk (92.210(b)-(c)). Skin images carry skin color. The company will give hospitals subgroup performance data so they can meet this duty |
| FTC Act Section 5 | Yes | Performance claims in marketing must be truthful and substantiated. Claims must match the validated subgroup results |
| State AI laws | No | All customers are in Florida. State-specific AI analysis is otherwise out of scope by decision (`../00_company-facts.md`) |

## 3. Risk tier
**AI-001: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`). Its output influences health care decisions about a person, and a missed injury can affect physical safety. A nurse reviews every flag, but a **false negative** may never get a second look, because the tool can give false reassurance.

**AI-002: Medium.** It makes no decisions about people and handles no PHI. It is not Low, because its output enters safety-related device software and can introduce vulnerabilities or license obligations into a cyber device. Human review and verification under design controls keep it below High.

**AI-003: prohibited.** Public tools under personal accounts would be High if source code, unfixed vulnerabilities, signing material, or PHI were entered (P01 R-028).

## 4. MEASURE: AI-001
Results are from the internal held-out test set (2,100 images) as of 2026-08-26. External validation has not started.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Sensitivity at least 85% and specificity at least 80%, with the lower 95% confidence bound for sensitivity at least 80% | Sensitivity 88%, specificity 84% overall. Internal data only | **Provisional.** External validation at 2 hospitals not in the training set is required |
| Safe | Labeling and user interface make clear that "no flag" does not rule out injury; human factors test of the workflow | Labeling drafted; human factors test not yet run | Partial |
| Secure and resilient | AI-specific threats (adversarial images, poisoned training data, model file tampering) in the threat model; model file signed and verified like firmware; model and framework in the SBOM | None of these done yet | **No** |
| Accountable and transparent | Model card and labeling state the training data sources, skin tone mix, and subgroup performance | Model card outline only | Partial |
| Explainable and interpretable | Heat map shows the region behind each flag; nurses can compare it with the photo | Working in the prototype | Yes |
| Privacy-enhanced | Training data de-identified; production PHI only under an amended BAA; no secondary use | De-identification attestation from each partner hospital on file; BAA amendment not drafted | Partial |
| Fair, with harmful bias managed | Sensitivity by Fitzpatrick group, with the thresholds in section 5 | I-II: 91%; III-IV: 88%; **V-VI: 76%** (about 80 positive cases, so the interval is wide) | **No.** Disparity flagged (P01 R-027) |

**Bias finding.** AI-001 misses more pressure injuries on the darkest skin tones. Two causes stack up:
- Early pressure injury is harder to see on darker skin, which is the very reason the tool is useful.
- Types V-VI make up only 13% of the training data.

This is the main clinical risk in the program and the reason for the conditions in section 6.

## 5. Bias testing plan (AI-001)
| Element | Plan |
|---|---|
| Groups compared | **Skin tone** (Fitzpatrick I-II, III-IV, V-VI), the primary comparison. Also sex, age (18-64, 65-79, 80 and over), body site (sacrum, heels, other), and camera model |
| Metrics | Sensitivity, specificity, positive and negative predictive value per group, with 95% confidence intervals. Annotator agreement (kappa) per skin tone group, to check that labels are as reliable on darker skin |
| Thresholds | (1) Each skin tone group's sensitivity lower 95% bound at least 80%. (2) No group's sensitivity more than 5 percentage points below the overall value. (3) No group's specificity more than 10 points below the overall value. Failing any threshold blocks design freeze |
| Sample size | At least 150 positive cases per skin tone group in the validation set. This needs about 2 more partner hospitals with a higher share of type V-VI patients. Data collection targets are set by skin tone, not only by total count |
| Reference standard | Bedside assessment by a wound care nurse, not the photo alone, so the labels do not inherit the bias the tool is meant to fix |
| When | (1) Before design freeze (due 2027-03-31). (2) In the external clinical validation. (3) After release: quarterly, from hospital-reported outcomes and complaint data |
| Mitigations if a group fails | Collect more data for that group; rebalance training; set a group-aware operating threshold only if clinically justified and documented; otherwise narrow the intended use and state the limitation in labeling |
| Records | Results go into the design history file, the model card, the labeling, and the marketing submission |

## 6. MANAGE: AI-001
**Human-in-the-loop design:**
- Every flag goes to a nurse, who performs the standard skin assessment before any action.
- The tool never writes to the chart, orders a consult, or escalates on its own.
- Nurses can dismiss a flag with a reason. Dismissal rates are monitored by skin tone group.
- The standard skin assessment schedule stays the same whether or not an image is flagged.

**Monitoring after release:**
- Quarterly performance review by skin tone group and camera model, from hospital feedback and complaint data.
- Input drift checks: skin tone mix, lighting quality, and new camera models.
- A drop below any section 5 threshold triggers a complaint investigation and a correction decision (21 CFR 803 and 806; P08).

**Incident handling:**
- Security events (adversarial inputs, model tampering, device cloud compromise) follow P08.
- A missed injury linked to AI-001 is a complaint and is evaluated for MDR reporting (21 CFR 820.35, 803.50).

**Decommissioning:** the device cloud can switch AI-001 off per hospital through a feature flag. It will be switched off if:
- postmarket performance falls below a threshold and cannot be fixed quickly;
- the model file fails integrity verification;
- a hospital's BAA amendment lapses.

### Decision (AI-001)
**Approve continued development with conditions.** CEO, 2026-09-04. The following must be met before design freeze (2027-03-31):
1. Execute the bias testing plan (section 5), including enrollment of 2 more partner hospitals to reach 150 positive cases in each skin tone group.
2. Add AI-specific threats to the threat model; sign and verify the model file; add the model and framework to the SBOM (POL-01 4.5).
3. Draft the BAA amendment for AI-001 before any production pilot.
4. Request an FDA pre-submission meeting covering the bias plan, the external validation design, and a PCCP.
5. Close the P03 section 524B roadmap items the submission depends on (P01 R-010).

## 7. AI-002: coding assistant (summary assessment)
| Function | Assessment |
|---|---|
| MAP | 10 engineers (cloud and firmware) in a 3-month pilot. Inputs: source code and comments (Confidential). No PHI, vulnerability details under embargo, or signing material may be entered |
| Risks (AI 600-1 themes) | Information security (insecure code suggestions); intellectual property (license-encumbered snippets entering firmware and the SBOM); data privacy and confidentiality (code retained or used for training by the vendor); overreliance (reduced review quality) |
| MEASURE | During the pilot, compare pull requests with and without AI assistance: static analysis findings per 1,000 lines, reviewer rejection rate, and license scan hits. Pass if AI-assisted code is no worse than the baseline |
| MANAGE | Enterprise contract with no training on company data and limited retention; SSO access; second reviewer for every merge (already required); license scanning in CI; not used for cryptographic, signing, or key-handling code. Public tools blocked on company laptops from 2026-11-30 (AI-003) |

### Decision (AI-002)
**Approve the pilot with conditions.** COO, 2026-09-04. The pilot starts 2026-11-01 only after the enterprise contract is signed with the no-training term. Expansion to all engineers needs pilot results that meet the MEASURE criteria. It is reviewed at the quarterly AI review.

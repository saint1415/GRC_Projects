# AI Risk Assessment: Facial Recognition for Facility Access

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (facilities support contractor operating government buildings) |
| Tier / Vertical | Small / Government Services and Facilities |
| AI use cases | AI-001: face verification (1:1) pilot at the county government center employee entrance, 140 enrolled county employees since June 2026. AI-002: face identification (1:N) of the public in lobbies, requested by the county, not approved |
| Framework | NIST AI RMF 1.0 (AI 100-1). AI 600-1 (Generative AI Profile) applies only to AI-003 in the inventory |
| Assessor / date | Security Systems Supervisor with the IT Manager and Contracts Manager, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Who decides what.** The **county** owns the building, the access control system, and the decision to use face recognition on its employees. The **company** configures and operates the feature, holds the templates in the tenant it administers, and can refuse to operate a use it considers unsafe or unlawful. This assessment is the company's decision on whether and how it will operate AI-001 and AI-002.
- **Accountable owner:** Security Systems Supervisor. **Decision authority:** COO (High tier). The majority owner is informed.
- **Policies that apply:**
  - POL-05 4.10: no AI or biometric features in customer systems without an approved P10 assessment. **AI-001 started before this rule and before any assessment**, which is the main governance gap (scenario-facts gap 14).
  - POL-04 4.1 and 4.9: face templates are Restricted data; deletion within 30 days after opt-out or departure.
  - POL-01 4.8: vendors must pass a security review before handling customer data.
- **Approved-tools list:** kept by the IT Manager. For customer systems it lists only AI-001, only at the county government center employee entrance, only for enrolled volunteers.
- **Scale for a Small company:** there is no AI committee. The COO, IT Manager, Security Systems Supervisor, and Contracts Manager review AI use cases quarterly, and the county's facilities director and county attorney join for AI-001.

## 2. MAP
| Item | AI-001 face verification (1:1) |
|---|---|
| Purpose and intended use | Stop badge sharing and lost-badge misuse at the employee entrance. The reader checks that the face matches the template of the badge presented |
| Users / operators | Security Systems Supervisor and 2 technicians (configuration); county guards (fallback desk) |
| Affected people | 140 enrolled county employees; county employees who decline; visitors are not affected |
| Data | Enrollment photo (converted by the vendor to a face template), badge ID, match score, and access events. **Default template retention was indefinite** |
| Build or buy | Buy: vendor SaaS feature, machine learning face matching; model not trained on county data according to the vendor, but not in the contract |
| Not intended | Identifying anyone without a badge; use on the public; use by police; use as evidence for discipline without human review. These are prohibited in the configuration and the county letter |

**AI-002 (1:N identification of the public)** would scan every lobby visitor against a watch list. It changes the purpose from verifying a known employee to identifying unknown members of the public who came to use county services. The company **declined** it (section 6).

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Fla. Stat. 501.171 | **Yes** | Personal information now includes "an individual's biometric data as defined in s. 501.702" with a name (501.171(1)(g)1.a.(VI)). Section 501.702 defines biometric data as data from automatic measurements of biological characteristics used to identify a person, and excludes physical or digital photographs and data generated from video recordings. A face template built from the enrollment capture is therefore likely biometric data; enrollment photos alone are not. Because the readers capture live camera images, counsel should confirm the templates are not caught by the video exclusion. The company treats them as personal information either way. The company, as a third-party agent, must take reasonable security measures (501.171(2)), notify the county within 10 days of a breach determination (501.171(6)), and dispose of records securely (501.171(8)) |
| Florida public records law, Fla. Stat. 119.071(5)(g) and 119.0701 | **Yes, needs county counsel** | The county's biometric exemption covers only friction ridge records, fingerprints, palm prints, and footprints. **It does not name face templates.** Whether another exemption (for example the security system plan exemption in 119.071(3)(a)) protects them is for the county attorney. As a contractor, the company must keep exempt records confidential and route requests to the county's custodian (119.0701(2)(b)) |
| FTC Act Section 5 | Indirectly | Applies to the vendor's and the company's accuracy and privacy claims (the county itself is outside FTC jurisdiction). The FTC's December 2023 order against a national pharmacy chain over facial recognition without reasonable safeguards shows what the FTC expects: testing for accuracy and bias, notice, deletion, and vendor oversight |
| County security addendum | Yes | Cardholder data protection and 24-hour incident notice apply to templates |
| Colorado SB26-189 and other state AI laws | No | The company does business only in Florida |
| Federal rules for the GSA building | Not in scope | GSA's access control uses PIV cards (FIPS 201) and is GSA's system. The company will not propose face recognition at the federal building |

## 3. Risk tier
**Tier: High** for both use cases (repository rubric, `00_universal/projects/P10_ai-governance/README.md`).

**Why High for AI-001, even as a second factor:** it controls physical access to a government facility (critical infrastructure physical security), it processes biometric data, and repeated false rejections affect employees' access to their workplace. The rubric's High tier covers AI that "can affect physical safety or critical infrastructure operations."

**Why High for AI-002:** it would identify members of the public seeking essential government services, with no human review design and a much higher chance of misidentification in 1:N search.

**Minimum controls for High:** human review before action; pre-deployment bias testing; impact assessment (this document); notice to affected people; ongoing monitoring.

## 4. MEASURE
### 4.1 Trustworthy characteristics (AI-001 pilot, June 15 to August 15, 2026)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | False non-match rate (FNMR): genuine employees rejected per attempt. Target 2% or less | 9,780 attempts; FNMR 2.4% | **No** |
| Valid and reliable | False match rate (FMR): impostor accepted. Target 0 accepts in a 2,000-attempt impostor test (upper bound about 0.15%) | Not tested locally; vendor lab data only | **Not measured** |
| Safe | No one refused entry on a face result alone; fallback works | Badge plus PIN fallback worked for all 235 rejections; average delay 40 seconds | Yes |
| Secure and resilient | Templates encrypted; vendor SOC 2 covers the module; administrator MFA | SOC 2 does not cover the module (P09); administrator MFA in place | **Partial** |
| Accountable and transparent | Written notice and signed consent before enrollment; signage at the entrance | County email notice only; no signed consent; no signage | **No** |
| Explainable and interpretable | Guards can see the match score and the enrolled photo when a match fails | Score visible; enrolled photo visible to guards | Yes |
| Privacy-enhanced | Templates deleted within 30 days after opt-out or departure; no vendor training on templates | Retention was indefinite; no contract term on training | **No** |
| Fair, with harmful bias managed | FNMR by group (plan in 4.2) | Disparity flagged (below) | **No** |

### 4.2 Bias testing plan
Face matching accuracy can differ by demographic group; NIST's face recognition evaluations (NISTIR 8280, December 2019) documented such differentials across algorithms. The plan:
- **Metric:** FNMR per group at the operating threshold, from real attempts; FMR per group from a controlled impostor test with volunteer pairs.
- **Groups compared:** age band (under 40, 40-59, 60 and over), sex, self-reported race and ethnicity (voluntary, collected by the county HR office, reported to the company only in aggregate), and people wearing eyeglasses or head coverings.
- **Thresholds:** each group's FNMR at or below 1.5 times the overall FNMR and at or below 3%; zero false accepts in each group's impostor test. Groups with fewer than 15 people are reported but not scored.
- **Frequency:** before any expansion, then quarterly while in use, and after any vendor model update.

**Pilot results (96 of 140 enrolled employees gave voluntary demographic data):**
| Group | FNMR | Ratio to overall (2.4%) | Result |
|---|---|---|---|
| Age 60 and over | 4.1% | 1.7 | **Flagged** |
| Black employees | 3.6% | 1.5 | **Flagged** (at the ratio limit, above 3%) |
| Wearing head coverings (11 people) | 5.2% | 2.2 | Reported, not scored (fewer than 15) |
| Other groups | 1.6% to 2.6% | 0.7 to 1.1 | Pass |

**Bias finding.** Older and Black employees are rejected more often. Because the badge-plus-PIN fallback always works, the harm is delay and repeated friction, not denied entry. It still falls unevenly on these groups and is not acceptable for an expansion. The vendor must provide its model's demographic performance data and tuning options. Lowering the match threshold to cut rejections would raise the false match rate, so it may not be done without a new impostor test.

## 5. MANAGE
**Human-in-the-loop design:**
- The face match is never the only factor. The badge is always required.
- A failed match falls back to badge plus PIN, or the guard desk with a visual check. No one is refused entry by the algorithm alone.
- Face match results are never used as evidence for discipline or reported to police without a human review of the event and video by the county.

**Consent and notice:**
- Written notice and a signed consent form before enrollment, stating purpose, retention, and how to withdraw.
- Signage at the entrance.
- Declining or withdrawing has no effect on employment or access; the badge-plus-PIN lane stays open.

**Data handling:**
- Templates are Restricted data (POL-04). Retention set to delete within 30 days after withdrawal or departure, verified monthly against the HR departure list.
- Contract amendment with the vendor: no training on templates, encryption at rest, per-person deletion, 24-hour incident notice.

**Monitoring:**
- Monthly FNMR report and quarterly bias report to the county facilities director, tracked in the risk register (R-013).
- Complaints go to the county HR office and the Security Systems Supervisor.

**Incident handling:** a template breach follows P08 and the 501.171 third-party agent notice (10 days after determination; 24 hours under the contract).

**Decommissioning:** stop the pilot and delete all templates if the vendor has not signed the data terms by 2026-10-31, if a flagged group's FNMR does not improve by the next quarterly report, or if the county attorney concludes the templates would be disclosable public records.

## 6. Decision
**AI-001: approve with conditions.** COO, 2026-08-31. The pilot may continue for the currently enrolled volunteers, with no new enrollments, **only if** these are met by 2026-10-31:
1. Vendor contract amendment: no training on templates, encryption, per-person deletion, 24-hour incident notice.
2. Signed consent forms and signage in place; templates deleted for anyone who does not sign.
3. Template retention set to 30 days after withdrawal or departure.
4. Written opinion from the county attorney on the public records status of the templates.
5. Local impostor test (2,000 attempts) completed and the vendor's demographic performance data received.

Expansion to other entrances or sites requires a new assessment and two consecutive quarterly reports with no flagged group.

**AI-002: not approved.** The company will not configure or operate 1:N identification of the public (P01 R-014, treatment Avoid). The COO's letter to the county, due 2026-09-30, explains why: it moves from verifying consenting employees to identifying people using county services, it carries a higher misidentification risk, and it has no review or appeal design. The company would re-assess only on a written county request that includes the county attorney's legal review and a human review and appeal process.

**AI-003:** Low tier if the approved enterprise tool is used under POL-04 and POL-05. Public chatbots are prohibited for Restricted data. Evaluation due 2026-12-31.

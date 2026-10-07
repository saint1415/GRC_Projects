# AI Use Assessment: Instrument Drift Prediction (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent radiation safety consultant) |
| Tier / Vertical | Sole Proprietorship / Nuclear Reactors, Materials, and Waste |
| AI use case | AI-001: the drift prediction feature in the calibration-tracking SaaS (SYS-08), turned on 2026-05-18. It is the registry default "predictive maintenance for non-safety plant equipment" adapted to this business: the owner maintains no plant equipment, but does maintain six portable survey instruments |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form. AI 600-1 applies only to AI-002 (generative), noted in section 6 |
| Assessor and decision | Owner-consultant, 2026-08-25; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
The calibration laboratory posts each instrument's annual calibration results to the calibration-tracking SaaS, and the owner logs the pre-use response check (reading on a check source) before each job. The vendor's model uses this history to predict when each instrument will drift out of tolerance and shows a "service soon" flag. The owner turned it on without reading the terms. Inputs include each reading's **location tag** (client site, building, and room), so the vendor now holds a log of where the owner surveyed inside Client A's plant. The feature makes no decision; the owner decides when to send an instrument for service.

**Why it matters for safety.** A survey meter that reads low can make a radiation area look safer than it is. Licensees must ensure instruments used for quantitative radiation measurements are "calibrated periodically for the radiation measured" (10 CFR 20.1501(c); Florida licensees under the Florida equivalent). The risk is not the prediction itself. It is the temptation to **trust a good prediction and skip or delay a check.**

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| CSR-A (6), Client A information | **Yes** | Room-level location tags inside Client A's protected area are Client A information; they may sit only in Client A's portal or encrypted storage under the owner's control, not with a third-party vendor |
| 10 CFR 20.1501(c) and client procedures | **Yes, through the clients** | Clients rely on the owner's instruments being calibrated; a prediction can never stand in for a calibration or a response check |
| CSIA-B (3) | No for AI-001 | No Client B security information goes to this feature. It does apply to AI-002 (section 6) |
| State AI laws on consequential decisions | No | The feature makes no decision about a person (repository rubric categories) |

## 3. Risk screen (repository rubric)
**Tier: Medium, on conditions.** The feature influences maintenance decisions that touch worker safety, but a human makes every decision and the conditions in section 5 stop it from ever lowering the level of checking. **If it were used to extend calibration intervals or skip response checks, it would be High** (it could affect physical safety), and that use is not allowed.

## 4. Data-sharing rules (Govern)
1. Remove site, building, and room tags from all readings; tag by job number only, with the job-to-site key kept on the owner's encrypted laptop (by 2026-09-30, P01 R-009).
2. Read and record the vendor's terms on data use and model training. If the vendor uses customer data to train its model, ask for an opt-out; if none, keep only instrument serial numbers and readings in the service.
3. MFA on the calibration-tracking account (POAM-001).
4. No client information of any level goes into any AI feature without the client's written agreement and a new assessment (POL-01 9.8).

## 5. Human review of outputs (Measure and Manage)
- **Never later, only sooner.** A "service soon" flag may bring a calibration or extra check forward. A "healthy" prediction never delays the annual calibration or the pre-use response check.
- **Check the model against reality.** For one year, compare each prediction with the laboratory's as-found results at calibration. If an instrument is found out of tolerance that the model called healthy, the owner records it and reviews the surveys done with that instrument since its last good check.
- **Measured so far:** 4 months of use, no instrument found out of tolerance, so accuracy is unknown. No fairness metric applies (no people are scored).
- **Stop rule:** a missed out-of-tolerance instrument, or any vendor change to data use terms, suspends the feature until reviewed.

## 6. Related use: AI-002 consumer chat assistant
On 2026-06-09 the owner pasted one paragraph of the draft 2026 Client B Part 37 review report into a consumer AI chat assistant to improve the wording. That broke CSIA-B (3) and was reported to Client B on 2026-07-22 (late, P03 G-027). Actions: chat history deleted and deletion requested from the service (2026-07-22); no client text of any level in any AI tool (POL-01 9.8); the tool may be used only for Public-level text. AI 600-1's information security and data privacy risks (inputs kept by the provider) are the reason. Client B decides whether anything more is needed for its own Part 37 records.

## 7. Decision: continue with conditions (approved 2026-08-31)
Keep AI-001 in use for scheduling extra checks only, on the conditions in sections 4 and 5, due 2026-09-30 (P01 R-009). Re-run this assessment if the vendor changes its terms or model, if a client objects, or at the July 2027 review.

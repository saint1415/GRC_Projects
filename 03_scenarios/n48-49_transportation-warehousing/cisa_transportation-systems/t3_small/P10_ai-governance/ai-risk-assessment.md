# AI Risk Assessment: Track and equipment defect detection (computer vision)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (Class III short line freight railroad) |
| Tier / Vertical | Small / Transportation Systems |
| AI use case | AI-001: track and equipment defect detection (computer vision) pilot on the North Subdivision since 2026-03 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook. AI 600-1 is not applied because the model is not generative |
| Assessor / date | Chief Engineer with the IT Manager and the Manager of Safety and Security, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner:** Chief Engineer, who also designates the qualified track inspectors (49 CFR 213.7). **Decision authority:** President and General Manager, because the use case is High tier (section 3).
- **How the pilot started:** the vendor offered a free pilot in 2026-03, and it began without an AI use policy, an approved-tools list, or a contract review (gap 15 in `../scenario-facts.md`). This assessment is the first formal review.
- **Policies that apply (approved 2026-08-31):**
  - POL-05 4.8: approved AI tools only; AI outputs supplement required inspections and never replace them
  - POL-04 4.7: no Restricted data, SSI, or infrastructure imagery in unapproved AI tools
  - POL-01 4.7: security terms in vendor contracts, including data return and deletion
- **Approved-tools list:** kept by the IT Manager. Today it lists AI-001 for the pilot only. AI-002 (public chatbots) is not approved for Restricted data or SSI.
- **Scale for a Small railroad:** there is no AI committee. The Chief Engineer, IT Manager, and Manager of Safety and Security review AI use cases quarterly and report to the President and General Manager.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Find suspected defects (broken or cracked joint bars, missing fasteners and spikes, defective ties, rail surface defects, and, at the wayside portal, visible car component defects) sooner, and point inspectors to them. The goal is more defects found between required inspections |
| Users / operators | 6 qualified track inspectors (hi-rail camera runs); 2 mechanical inspectors (portal flags); the Chief Engineer |
| Affected people | Train crews, roadway workers, and the public at 41 crossings, who rely on safe track and equipment. Employees and members of the public appear incidentally in images |
| Data (inputs, training, outputs) | Inputs: images and video with GPS and milepost. Outputs: flags with a defect class, a confidence score, and an image crop. Inspector decisions (confirm or reject) are stored. **The contract is silent on whether the vendor may keep images or use them to train its model** (P01 R-027) |
| Build or buy (vendor / model) | Buy: a licensed vendor model trained mostly on Class I main line imagery, run as an inference service in the company's cloud tenant (P04). Images are stored in the tenant |
| Not intended | Replacing any required inspection; clearing or closing a defect; setting slow orders automatically; measuring the performance of individual inspectors or other employees. Any of these requires re-assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| 49 CFR 213.233 (visual track inspections) | **Yes** | Inspections must be made "on foot or by traversing the track in a vehicle" so the person can visually inspect the track, and "mechanical, electrical, and other track inspection devices may be used to supplement visual inspection." The model is such a device. **It may only supplement the required visual inspection** |
| 49 CFR 213.7 (designated qualified persons) | **Yes** | Only designated persons inspect track and decide on remedial action. The model's output goes to them |
| 49 CFR 215.13 (pre-departure freight car inspection) | **Yes, as context** | Cars placed in a train must be inspected before departure by a designated inspector or for the Appendix D conditions. Portal flags are extra information only |
| 49 CFR 1520.9 (SSI) | **Possibly** | Imagery of security measures at facilities could become SSI if TSA marks it. Treat detailed imagery of bridges and signal equipment as Restricted (POL-04) |
| Fla. Stat. 501.171 | No | Images of people are not "personal information" under the statute as long as no names or identifiers are linked to them |
| State AI laws (for example Colorado SB26-189) | No | The railroad operates only in Florida, and the use case makes no consequential decision about a person in the listed categories. The ban on using it to evaluate inspectors keeps it out of the employment category |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal/projects/P10_ai-governance/README.md`). The rubric puts in the High tier any AI that "can affect physical safety or critical infrastructure operations." A missed broken joint bar can derail a train carrying PIH cars.

**Why the risk is manageable:** the model does not decide anything. Every required inspection is still done by a qualified person, and the model can only add findings. The main danger is **automation bias**: inspectors start trusting the model and look less carefully where it shows nothing (P01 R-026).

**Minimum High-tier controls from the rubric**, and how they are met:
- Human review before action: every flag goes to a qualified inspector (section 5).
- Pre-deployment testing: pilot testing on the North Subdivision (section 4). **Not yet done for the South Subdivision.**
- Impact assessment: this document.
- Notice to affected people: employees informed through POL-05; signs at the portal site.
- Ongoing monitoring: monthly metrics (section 5).

## 4. MEASURE
Pilot data: 38 hi-rail runs on the North Subdivision, 2026-03 to 2026-07, compared with the inspectors' own findings on the same runs.

| Trustworthy characteristic | Test / metric | Result (pilot) | Pass? |
|---|---|---|---|
| Valid and reliable | Recall on defects the inspectors found on the same runs; target 90% or more for all classes and 95% or more for joint bar and rail defects | 55 of 64 defects detected (86%). Joint bar and rail defects: 18 of 20 (90%) | **No.** Below target. Acceptable only because the model supplements inspection |
| Valid and reliable | Precision (flags confirmed as defects) | 97 of 412 flags confirmed (24%) | Noted. Low precision drives alert fatigue |
| Safe | No inspection skipped or shortened; required inspections recorded as visual | Inspection records unchanged in frequency. 2 of 6 inspectors said they "check the flagged spots first" | **Partial.** Automation bias risk |
| Secure and resilient | Inference service in the company tenant behind the VPN; vendor access through named accounts; images encrypted at rest | Tenant hosting and encryption in place; the vendor's service account has broad storage rights | **Partial** |
| Accountable and transparent | Every flag has an inspector decision recorded; model version logged | Decisions recorded for 94% of flags; model version not logged | **No** |
| Explainable and interpretable | Inspector sees the image crop and the defect class for each flag | Available in the review app | Yes |
| Privacy-enhanced | Faces and license plates blurred before storage; images kept no longer than 1 year; no vendor reuse without consent | Blurring not enabled; no retention rule; contract silent on reuse | **No** |
| Fair, with harmful bias managed | Compare recall across operating conditions: (a) North vs South Subdivision, (b) daylight vs low light, (c) jointed rail vs continuous welded rail, (d) dry vs wet, (e) heavy vegetation vs clear. Flag any condition more than 5 percentage points below the overall recall | Low light: 74% vs 86% overall. Jointed rail: 81%. South Subdivision: **not tested** (lighter rail, more vegetation) | **No.** Low-light and jointed-rail gaps flagged |

**Fairness in this context.** The model does not make decisions about people, so fairness is measured as performance parity across the conditions it will meet. A model trained on Class I main line may do worse on a short line's lighter, jointed rail and vegetated right of way. That is exactly what the pilot shows. The South Subdivision has more jointed rail, so the model must not be relied on there without testing.

## 5. MANAGE
**Human-in-the-loop design:**
- The model only adds findings. Inspectors perform and record every required visual inspection as before (49 CFR 213.233).
- Every flag is reviewed by a qualified inspector within 24 hours, or before the next train where the flag is a joint bar or rail defect. The inspector confirms or rejects it in the app.
- The inspector decides on remedial action under part 213. The model never sets or clears a slow order.
- Portal flags on cars go to a mechanical inspector before the train departs. The pre-departure inspection (215.13) is unchanged.
- Inspection training restates that "no flag" does not mean "no defect."

**Monitoring:**
- Monthly: recall and precision against inspector findings, by condition; review rate within 24 hours; model version.
- Quarterly: the review group reports to the President and General Manager and updates P01 R-026 and R-027.
- Any missed defect that leads to an FRA-reportable accident is investigated as part of the part 225 process.

**Incident handling:**
- A security incident affecting the inference service or image store follows the P08 runbook.
- A model failure (for example, a vendor update that drops recall) is handled by pausing the model. Inspections continue unchanged.

**Decommissioning:**
- Stop and delete vendor-held data if the contract terms in section 6 are not signed by 2026-10-31.
- Stop if monthly recall on joint bar and rail defects falls below 85% for two months in a row.
- Stop if the vendor changes its data-use terms without consent.

## 6. Decision
**Approve with conditions.** President and General Manager, 2026-08-31. The pilot may continue on the North Subdivision **only if** these conditions are met by 2026-10-31:
1. A contract amendment: no vendor use of company imagery for training or any other purpose without written consent; deletion on request and at contract end; security incident notice within 24 hours (POL-01 4.7; P01 R-027).
2. A written human-in-the-loop rule, signed by the Chief Engineer and briefed to all inspectors (P01 R-026).
3. Face and license plate blurring enabled; 1-year image retention; the vendor service account limited to the pilot storage.
4. Model version logging turned on.

**Expansion to the South Subdivision** requires a 3-month shadow test there with recall of at least 90% overall and no condition more than 5 percentage points below overall, including low light and jointed rail.

**Related action for AI-002.** Public chatbots stay prohibited for Restricted data and SSI (POL-05 4.8). The IT Manager will evaluate an enterprise tool with no-training terms in 2027.

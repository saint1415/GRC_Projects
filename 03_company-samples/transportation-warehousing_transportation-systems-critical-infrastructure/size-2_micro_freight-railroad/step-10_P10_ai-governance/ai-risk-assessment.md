# AI Risk Assessment: Track Defect Detection (Computer Vision)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (short line freight railroad, 16 route miles, north Florida) |
| Tier / Vertical | Micro / Transportation Systems |
| AI use case | AI-001: track defect detection (computer vision) pilot on the hi-rail truck (SYS-09), since 2026-05-04 |
| Scope note | The registry default is "track and equipment defect detection". This railroad has no wayside camera portal, so only the track part is in use. Car and locomotive inspections stay fully manual |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook. AI 600-1 is not applied because the model is not generative |
| Assessor / date | Roadmaster (business owner) with the Office Manager (Security Lead), 2026-08-25 |
| Decision | Owner and General Manager, 2026-08-31 (section 6) |
| Inventory | `ai-use-case-inventory.csv` (2 entries) |

## 1. GOVERN
- **Accountable owner:** the Roadmaster, who is also the railroad's designated qualified track inspector (49 CFR 213.7(b)). **Decision authority:** the Owner and General Manager, because the use case is High tier (section 3) and the General Manager accepts risk for the railroad (POL-02 A.3).
- **How the pilot started.** The vendor offered a pilot, and the camera kit went on the hi-rail truck on 2026-05-04. Nobody reviewed the vendor's terms and the railroad had no approved-tools list (gap 13 in `../00_company-facts.md`). This assessment is the first formal review.
- **Policies that apply (approved 2026-08-31):**
  - POL-04 4.7: approved AI tools only; the track defect detection service is approved for the hi-rail camera only, under the conditions in section 6
  - POL-02 A.5: no vendor holds company data until its terms for security, incident notice, and data return and deletion are reviewed
  - POL-02 C.2: no Restricted information in public AI chatbots (AI-002)
  - POL-04 4.5 and 4.6: the AI service goes into the inventory and through the new-vendor check
- **Approved-tools list:** kept by the Office Manager. It has one entry, AI-001, for the hi-rail camera only.
- **Scale for a Micro railroad:** there is no AI committee. The Roadmaster reports pilot results to the General Manager at the monthly security review with the Office Manager.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Point the inspector to suspected track defects (broken or cracked joint bars, missing or loose bolts and spikes, defective ties, rail surface defects) so that more defects are found and fixed between required inspections |
| How it works | The camera kit on the hi-rail truck records the track during the Roadmaster's weekly inspection run. After the run, the video uploads over the enginehouse Wi-Fi to the vendor's service, which returns flags (defect class, confidence score, image crop, and milepost) in a web portal. The Roadmaster reviews each flag and marks it confirmed or rejected |
| Users / operators | The Roadmaster (reviews flags); the Track Maintainer (drives the hi-rail truck and starts the camera) |
| Affected people | Train crews, roadway workers, and the public at the 15 grade crossings, who depend on safe track. People at crossings and on adjacent property appear incidentally in the video |
| Data (inputs, training, outputs) | Inputs: video of track, bridges, grade crossings, customer sidings (including the propane distributor's siding), with GPS and milepost. Outputs: flags and the Roadmaster's decisions. **The pilot terms say nothing about whether the vendor keeps the video or uses it to train its model** (P01 R-020) |
| Build or buy (vendor / model) | Buy: the vendor's licensed model, run in the vendor's SaaS. The vendor states the model was trained mostly on main line imagery from larger railroads |
| Not intended | Replacing or shortening any required inspection; clearing a defect or deciding remedial action; setting or removing slow orders; measuring the work of the Roadmaster or Track Maintainer. Any of these needs a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| 49 CFR 213.233 (visual track inspections); C-TRANSPORTATION-S08 | **Yes** | Each inspection is made "on foot or by traversing the track in a vehicle" at a speed that lets the inspector visually inspect the track, and "mechanical, electrical, and other track inspection devices may be used to supplement visual inspection" (213.233(b)). The model is such a device, so **it may only supplement** the weekly visual inspection that Class 1 main track requires (213.233(c)) |
| 49 CFR 213.7 (designated qualified persons); C-TRANSPORTATION-S08 | **Yes** | Only a designated person inspects track and prescribes remedial action (213.7(b)). Every flag goes to that person |
| 49 CFR part 225 (accident/incident reporting); C-TRANSPORTATION-S05 | **Yes, as context** | A missed defect that leads to a reportable accident is reported and investigated the usual way. The AI output becomes part of that record |
| 49 CFR 1520.9 (SSI); C-TRANSPORTATION-S03 | **Possibly** | Video is not SSI unless TSA marks it or it falls in an SSI category. Video of bridges and the propane siding is treated as Restricted under POL-04 to be safe |
| Fla. Stat. 501.171; C-TRANSPORTATION-S07 | No | Video of people is not "personal information" under the statute while no name or identifier is linked to it |
| State AI laws (for example Colorado SB26-189) | No | The railroad operates only in Florida, and the model makes no consequential decision about a person. The ban on using it to judge employees keeps it out of the employment category |
| NIST AI RMF Critical Infrastructure Profile | Not yet | NIST released a concept note on 2026-04-07; no profile has been issued. Track it |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`). The rubric places in the High tier any AI that "can affect physical safety or critical infrastructure operations." A missed broken joint bar can derail a train, and about 110 propane tank cars a year move over this track.

**Why the risk is manageable.** The model decides nothing. The Roadmaster still performs every required visual inspection, and the model can only add findings. The main danger is **automation bias**: the inspector begins to trust the model and looks less carefully where it shows nothing (P01 R-019, Moderate). The model is weakest exactly where inspection is hardest, on heavily vegetated sections (section 4).

**Minimum High-tier controls from the rubric**, and how they are met:
| Rubric control | Status |
|---|---|
| Human review before action | Every flag reviewed by the Roadmaster (section 5). Met in practice; written rule due 2026-10-31 |
| Pre-deployment testing (bias testing) | 12-run pilot measured against the Roadmaster's own findings (section 4). Conditions such as low light and wet rail not yet tested |
| Impact assessment | This document |
| Notice to affected people | Employees told through POL-04 4.7 and the monthly security review. Crews and roadway workers are told that "no flag" does not mean "no defect" |
| Ongoing monitoring | Monthly recall check (section 5) |

## 4. MEASURE
Pilot data: 12 weekly inspection runs over the whole line, 2026-05-04 to 2026-07-24. On each run the Roadmaster recorded defects from his own visual inspection, then compared them with the model's flags.

| Trustworthy characteristic | Test / metric | Result (pilot) | Pass? |
|---|---|---|---|
| Valid and reliable | Recall: share of the defects the Roadmaster recorded that the model also flagged. Target 90% or more | 19 of 23 (83%) | **No.** Below target. Acceptable only because the model supplements inspection |
| Valid and reliable | Precision: share of flags confirmed as defects | 31 of 141 flags (22%). Confirmed flags include repeat flags of the same defect on later runs before it was repaired | Noted. 110 false flags in 12 runs is a real review burden and can breed alert fatigue |
| Safe | Required inspections not skipped or shortened; inspection records still show visual inspection | All 12 weekly inspections were done on schedule and recorded as visual. The Roadmaster said he now looks at flagged spots first | **Partial.** Early sign of automation bias |
| Secure and resilient | Vendor service access, encryption, and incident terms | Video uploads over TLS. The portal has one account, the Roadmaster's, with a password only and no MFA. No security or incident notice terms; no vendor assurance report requested | **No** |
| Accountable and transparent | Every flag has a recorded decision; model version visible | Roadmaster decision recorded for all 141 flags. The portal does not show the model version, so a vendor update could change results unseen | **Partial** |
| Explainable and interpretable | Inspector sees why a spot was flagged | Each flag shows the image crop, defect class, and confidence score | Yes |
| Privacy-enhanced | Incidental images of people minimized; retention limited; no vendor reuse without consent | No face or license plate blurring offered in the pilot; vendor retention unknown; terms silent on reuse | **No** |
| Fair, with harmful bias managed | Recall by operating condition compared with overall recall. Conditions: (a) heavy vegetation vs clear right of way; (b) daylight vs low light; (c) dry vs wet rail; (d) plain track vs grade crossings, bridges, and turnouts. Threshold: flag any condition more than 5 percentage points below overall recall | (a) Heavy vegetation: 4 of 7 (57%); clear sections: 15 of 16 (94%); overall 83%. (b) to (d): **not tested**. All runs were in daylight and dry weather, and results were not split by location type | **No.** Vegetation gap flagged; other conditions untested |

**Fairness in this context.** The model makes no decision about people, so fairness is measured as performance parity across the conditions the model meets on this line. A model trained mostly on larger railroads' main lines can do worse on a short line's lighter rail and overgrown right of way, and the pilot shows exactly that. The sample is small (7 defects on vegetated sections), so the result is a warning, not a precise rate. Until a retest shows parity, the model's silence on a vegetated section carries no weight.

## 5. MANAGE
**Human-in-the-loop design:**
- The model only adds findings. The Roadmaster performs and records every required visual inspection as before (213.233), including on foot where vegetation blocks the view from the truck.
- The Roadmaster reviews every flag within 24 hours of the upload, and before the next train for any flag on a joint bar or the rail itself. He confirms or rejects it in the portal.
- The Roadmaster alone decides remedial action under part 213. The model never sets or clears a slow order; slow orders still go to the dispatcher by the usual route.
- On heavily vegetated sections the model's output is ignored until a retest passes (section 6).
- The Track Maintainer's driving and the Roadmaster's findings are never scored against the model.

**Monitoring:**
- Monthly (Roadmaster): recall and precision against his own findings, split by vegetated and clear sections; review time for each flag; any vendor change notice.
- At the monthly security review: the Roadmaster reports results to the General Manager; P01 R-019 and R-020 are updated.
- Any missed defect that contributes to an FRA-reportable accident is investigated as part of the part 225 process, and the pilot is paused until the investigation ends.

**Incident handling:**
- A security incident at the vendor or on the portal account follows the P08 runbook and `notification-matrix.csv`. A compromise of the portal account is a cyber attack on company infrastructure and is reported to TSA within 24 hours (1570.203).
- A model failure (for example, a vendor update that drops recall) is handled by pausing the model. Inspections continue unchanged.

**Decommissioning:**
- Stop, and ask the vendor to delete company video, if the contract terms in section 6 are not signed by 2026-10-31.
- Stop if monthly recall on clear sections falls below 85% for two months in a row.
- Stop if the vendor changes its data-use terms without written consent.

## 6. Decision
**Approve with conditions.** Owner and General Manager, 2026-08-31. The pilot may continue on the hi-rail truck **only if** these conditions are met by 2026-10-31 (P01 R-019 and R-020; P07 POAM-009):
1. **Contract terms** (POL-02 A.5): no vendor use of company video for model training or any other purpose without written consent; deletion on request and at contract end; security incident notice within 24 hours; the vendor's security assurance report or a completed questionnaire.
2. **Written human-in-the-loop rule** (section 5), signed by the Roadmaster and briefed to the Track Maintainer and the dispatchers.
3. **Access:** MFA on the portal account, or a named account with MFA if the vendor offers one; the service added to the inventory (POL-04 4.5).
4. **Data handling:** video of bridges and the propane siding treated as Restricted; a retention limit of 1 year agreed with the vendor; blurring turned on if the vendor offers it.

**Before relying on the model on vegetated sections**, a 3-month retest there must show recall within 5 percentage points of clear sections. **Before any expansion** (for example a wayside portal for car defects, or using the model to set inspection priorities), a new assessment is required.

**AI-002.** Public AI chatbots are not approved for any company information that is Restricted (POL-02 C.2; POL-04 4.7). No company account exists. The Office Manager will revisit this if a business need comes up.

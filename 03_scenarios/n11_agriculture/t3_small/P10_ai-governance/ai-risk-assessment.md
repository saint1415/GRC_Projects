# AI Risk Assessment: Computer-Vision Crop Yield Prediction

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (diversified precision-agriculture crop farm) |
| Tier / Vertical | Small / Agriculture, Forestry, Fishing and Hunting |
| AI use case | AI-001: computer-vision yield prediction from drone imagery (agronomy analytics SaaS, SYS-12), piloted on 14 acres of strawberries and 18 acres of watermelons in the 2025-26 season |
| Framework | NIST AI RMF 1.0 (AI 100-1). The model is a computer-vision model, not generative AI, so the Generative AI Profile (AI 600-1) was not applied to AI-001; it applies to AI-003 in the inventory |
| Assessor / date | Farm Manager (business owner) with the Operations and Technology Manager, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** Farm Manager. **Decision authority:** Farm Manager for Medium-tier use cases, with the majority owner and General Manager informed; the majority owner decides if a use case is re-tiered High.
- **Policies that apply:**
  - POL-04 4.9: no Restricted data in AI tools; farm imagery and yield data only to approved tools whose terms bar secondary use
  - POL-05 4.8: drone imagery must not be used to watch or evaluate individual workers
  - POL-05 4.9: approved tools only; AI yield estimates are advice and must be checked against field counts
  - POL-01 4.6: supplier checklist and security terms before connecting a new SaaS
- **Approved-tools list:** kept by the Operations and Technology Manager. Today it lists AI-001 (conditions below) and AI-002 (recommendation mode only).
- **Scale for a 15-person farm:** there is no AI committee. The Farm Manager, the Operations and Technology Manager, and the majority owner review AI use at the July risk assessment and whenever a use case changes.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Estimate weekly marketable yield per block, 1 to 3 weeks ahead, from fruit and flower counts detected in drone images. Used to plan harvest crew hours and to set weekly volume commitments to the distributor |
| Users / operators | Equipment and Drone Specialist (flies weekly missions, uploads orthomosaics); Farm Manager (planning); Sales and Farm Stand Coordinator (distributor commitments) |
| Affected people | Harvest crews, including 4 H-2A workers, whose offered hours follow the harvest plan; the distributor, which buys against the commitments; people who appear incidentally in field images |
| Data | **Inputs:** RGB and multispectral orthomosaics, block boundaries, variety and planting dates, and historical block yields (block totals from tally, never per-worker data). **Outputs:** block-level yield estimates with a confidence range and image overlays showing detected fruit. **Training:** the vendor's model was trained mainly on imagery from other growing regions; the vendor fine-tunes per customer. **The vendor's click-through terms allow it to use farm imagery and yields to improve its models (P01 R-026)** |
| Build or buy | Buy: vendor SaaS. Estimates are exported to a planning spreadsheet; there is no connection to SYS-01 or to irrigation |
| Not intended | Setting the number of H-2A workers in a job order; reducing crew hours without the Farm Manager's review; evaluating individual workers; crop insurance or USDA program reporting; driving irrigation or variable-rate application. Each of these would require re-assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| H-2A three-fourths guarantee, 20 CFR 655.122(i) | **Yes, indirectly** | The farm must offer each H-2A worker hours equal to at least three-fourths of the workdays in the contract period. A forecast cannot lower that floor. If the model over-forecasts and the farm plans too many crews, or under-forecasts and cuts hours, the guarantee and the hours-offered records in 655.122(j)(1) still govern |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. The farm keeps the marketing claims it relied on in the procurement file |
| Fla. Stat. 501.171 | Not today | Images of people in fields are not "personal information" as defined unless linked to a name and a listed data element. POL-05 4.8 keeps it that way |
| Federal crop insurance and USDA program reporting | Not used | Production is reported from buying point settlement sheets and packed-out records, not model estimates. POL-05 4.9 and the "Not intended" list keep it that way |
| State AI laws (for example Colorado SB26-189) | No | The farm operates only in Florida, and a yield estimate is not a consequential decision about a person. See `00_universal/cross-sector/us-cross-sector-obligations.md` |
| Sector AI rules for agriculture | None identified | The vertical overlay lists none |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal/projects/P10_ai-governance/README.md`).

**Why not High:** the model does not make, and is not a substantial factor in, a consequential decision about a person, and it cannot affect physical safety or critical infrastructure operations, because it has no connection to irrigation or equipment. The Farm Manager makes every crew and sales decision.

**Why not Low:** it influences business decisions that change workers' offered hours and the farm's commitments to its main buyer, and it sends farm data to a vendor under terms the farm has not negotiated.

**Escalation triggers (re-tier to High and re-assess):**
- using estimates to set the number of workers in an H-2A job order, or to cut crew hours without review
- linking estimates to irrigation schedules or variable-rate prescriptions that execute automatically
- using imagery or model output to evaluate individual workers
- using estimates in crop insurance or USDA program reports

## 4. MEASURE
Results are from the 2025-26 pilot: 22 weekly flights, December 2025 to May 2026, compared with actual block yields from tally totals and distributor receipts.

| Trustworthy characteristic | Test / metric | Result (pilot) | Pass? |
|---|---|---|---|
| Valid and reliable | Mean absolute percentage error (MAPE) of 1-week-ahead block estimates; threshold 15% | Strawberries 11%; watermelons 24% (vine canopy hides fruit) | **Strawberries yes; watermelons no** |
| Safe | No connection to irrigation, application equipment, or SYS-01; estimates cannot trigger any action | Confirmed in P04 and by the vendor's integration list | Yes |
| Secure and resilient | Imagery bucket private with time-limited links (P04); vendor account protected by SSO or MFA; vendor security evidence | Bucket confirmed private; vendor account uses a password only; no SOC 2 report from the vendor (security questionnaire requested) | **Partial** |
| Accountable and transparent | Estimates labeled "AI estimate" in the planning sheet; a decision log records each crew or sales decision that used an estimate | Label used; no decision log | **Partial** |
| Explainable and interpretable | Detection overlays let the Farm Manager spot-check counts image by image | Available and used in 18 of 22 weeks | Yes |
| Privacy-enhanced | No secondary use of farm data without opt-in; imagery retention limit; people in images not analyzed | Terms allow secondary use; imagery kept indefinitely; the vendor confirms it does not detect people | **No** |
| Fair, with harmful bias managed | Signed error (bias) by subgroup: strawberry variety (2 varieties), season stage (early, peak, late), and flight time (morning, afternoon). Flag any subgroup whose mean error differs from the overall mean error by more than 5 percentage points | Overall strawberry bias +3%. New variety (4 of 14 acres) +14%: **flagged**. Early season (December) -12%: **flagged**. Flight time within 2 points | **No.** Two subgroups flagged |

**Bias finding and why it matters to people.** The model over-estimates the newer strawberry variety and under-estimates early-season yield. Over-estimates lead to planning more crew hours than there is fruit to pick, and then cutting hours at short notice. Under-estimates lead to too few pickers and fruit left in the field. Workers bear the first effect. The farm will correct for the new variety with hand-count calibration (or exclude it) and will not use December estimates for crew planning.

**Worker-impact check (process, not model).** When a forecast change leads to fewer planned hours, the Farm Manager compares hours offered per worker across crews each week. A difference of more than 10% between crews is reviewed and corrected, and hours offered are recorded as 20 CFR 655.122(j)(1) requires.

## 5. MANAGE
**Human-in-the-loop design:**
- Estimates are advice only.
- Before any crew schedule or distributor commitment, the Farm Manager checks each block's estimate against hand counts on 3 sample plots.
- Distributor commitments are capped at 85% of the AI estimate unless hand counts confirm the full estimate.
- No crew hours are cut because of an estimate alone. Hours offered to H-2A workers never fall below the three-fourths guarantee (20 CFR 655.122(i)).
- Watermelon estimates are not used for decisions until MAPE is at or below 15% for a full season.

**Monitoring:**
- Weekly error tracking by block in season, kept with the planning sheet.
- Monthly subgroup bias check (variety, season stage, flight time).
- Model version recorded each week; the vendor must give notice of model changes (contract condition).

**Incident handling:**
- A vendor security incident or data exposure follows P08 and the supplier terms.
- A model failure (for example, an estimate more than 30% off hand counts) triggers a return to hand counts for that block and a report to the vendor.

**Decommissioning:**
- Stop and request deletion of farm data if the vendor has not signed the data terms by 2026-10-31.
- Stop if strawberry MAPE exceeds 20% for two consecutive months.
- Stop if the vendor changes the model or its data-use terms without notice.

## 6. Decision
**Approve with conditions.** Farm Manager, with the majority owner and General Manager informed, 2026-08-31. AI-001 may be used in the 2026-27 season **for strawberries only** (watermelons advisory) **only if** these conditions are met by 2026-10-31:
1. Negotiated data terms: no secondary use of farm imagery or yields without opt-in; deletion within 30 days of exit; notice of model changes (POAM-016).
2. The vendor account is placed behind the farm's single sign-on, or vendor MFA is enabled.
3. Imagery retention set to 3 seasons, and images showing people deleted when not needed (POL-05 4.8).
4. The new strawberry variety is calibrated with hand counts or excluded, and December estimates are not used for crew planning.
5. A decision log records each crew or sales decision that used an estimate.

**Related action for AI-002.** The FMIS irrigation scheduling recommendations stay in recommendation mode. Enabling automatic application would make AI-002 a High-tier use case under the rubric (it could affect physical operations) and requires a new assessment before it is switched on.

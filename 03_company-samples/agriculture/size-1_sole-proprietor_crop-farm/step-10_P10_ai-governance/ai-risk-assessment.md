# AI Use Assessment: Computer-Vision Crop Yield Prediction (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (precision-agriculture crop farm) |
| Tier / Vertical | Sole Proprietorship / Agriculture, Forestry, Fishing and Hunting |
| AI use case | AI-001: computer-vision yield prediction (SYS-08) from weekly drone flights over the 6 acres of U-pick strawberries, December 2025 to April 2026 (18 weekly flights), used to set how many reservation slots to open each weekend |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form. AI-001 is a computer-vision model, not generative AI, so NIST AI 600-1 applies only to AI-003 in the inventory |
| Assessor and decision | Owner-operator, 2026-08-25; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases), built at intake from the AI yield trial account and its terms, the SYS-01 scheduling settings, the public chatbot account, and the laptop browser history (EV-031, EV-032, EV-006, EV-033, EV-020). With no staff, there was no survey to run. Not established: whether the AI yield vendor has already used the farm's imagery and yields in its models, and what it keeps from the trial; and whether customer names or emails were ever entered in the chatbot (the history reviewed shows drafts with prices and U-pick hours). The written confirmation in section 6 is the first step to find out about the vendor |

## 1. What it does (Map)
The owner flies the drone over the strawberries each Wednesday and uploads the images to the vendor's SaaS (EV-031). The model counts ripe and nearly ripe fruit and returns an estimate of pounds ready by the weekend, by block. The owner uses the estimate to decide how many U-pick time slots to open on the booking platform. **Inputs:** RGB and multispectral images, block boundaries, variety and planting dates, and past weekend picked pounds from the farm stand scale. **Outputs:** pounds per block with a range. Customers picking in the field can appear in the images, but the model does not look for people. The trial runs on **click-through terms that let the vendor use farm images and yields to improve its models** (EV-032; P01 R-011). There is no connection to SYS-01 or the irrigation.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| FTC Act Section 5 | Indirectly | Covers the farm's own promises to customers (for example "plenty of berries this weekend") and the vendor's accuracy claims |
| Fla. Stat. 501.171 | No | Images of people are not "personal information" under 501.171(1)(g) unless linked to a name and a listed data element; POL-01 9.7 keeps it that way |
| Crop insurance and USDA reporting | Not used | Production is reported from scale and settlement records, never from model estimates (POL-01 6.6) |
| Produce Safety Rule qualified exemption | No effect | Sales records come from the booking and accounting systems, not the model |
| State AI laws on consequential decisions | No | A yield estimate is not a decision about a person; see `00_universal-framework/cross-sector/us-cross-sector-obligations.md` |
| Sector AI rules for agriculture | None identified | The vertical overlay lists none |

## 3. Risk screen (repository rubric)
**Tier: Medium.** It influences a business decision that customers feel (how many slots are offered, and whether a family drives out to a picked-over field), but the owner makes the decision and no decision is made about any person. It cannot affect physical operations. **Escalation trigger:** if forecasts were ever used to drive irrigation or fertigation automatically, or to report production, the use case would be re-tiered High and re-assessed.

## 4. Data-sharing rules (Govern)
1. Farm images and yields go only to an AI vendor whose terms bar use of farm data for its own models unless the owner opts in (POL-01 6.6).
2. The vendor account uses MFA, and images are deleted from the vendor after 3 seasons, or sooner on request.
3. No customer, W-9, or booking data is ever uploaded. Images showing identifiable people are deleted when not needed (POL-01 9.7).

## 5. Human review of outputs (Measure and Manage)
**What the trial showed.** The owner compared each weekend forecast with the pounds actually picked (farm stand scale; EV-038, 2026-08-25): across 16 weekends the mean absolute percentage error was 22%. Errors were not even: in the 5 weekends after rain or heavy cloud, the model over-forecast by 30% or more, so slots were overbooked and 2 weekends needed refunds. In clear weeks the error was 12%. The 2 weekends the U-pick was closed for cold weather are excluded.

**Rules for the 2026-27 season:**
- Before opening slots, the owner counts ripe fruit in 3 sample rows per block and compares with the forecast. If they differ by more than 20%, the owner uses the count.
- Slots are capped at 80% of the forecast until a full season shows error at or below 15%.
- After rain or heavy cloud, the forecast is advisory only.
- Weekly error is logged (forecast, picked pounds, weather). If the season error passes 25%, use stops.
- Vendor model changes must be announced; the owner re-checks error for the following 3 weekends.

## 6. Decision: approve with conditions (approved 2026-08-31)
AI-001 may continue in the 2026-27 season **only if**, by 2026-10-31 (P01 R-011; POAM-006):
1. The vendor confirms in writing that farm data is not used for its models (opt-out or amended terms). **If not, stop, export the forecasts, and request deletion of all farm data.**
2. MFA is on for the vendor account and the 3-season retention is set.
3. The human review rules in section 5 are in use from the first flight.

**Related action (AI-002):** the SYS-01 irrigation scheduling recommendations stay in recommendation mode. Turning on automatic application would let a model start and stop pumps, which the rubric rates High; it requires a new assessment first.

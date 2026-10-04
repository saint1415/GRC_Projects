# AI Risk Assessment: Computer-Vision Crop Yield Prediction

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (precision-agriculture row crop and watermelon farm) |
| Tier / Vertical | Micro / Agriculture, Forestry, Fishing and Hunting |
| AI use case | AI-001: computer-vision yield prediction from drone imagery (agronomy analytics SaaS, SYS-09), piloted on 90 acres of watermelons in the 2026 season. Cotton boll counts are proposed for fall 2026 |
| Framework | NIST AI RMF 1.0 (AI 100-1). AI-001 is a computer-vision model, not generative AI, so the Generative AI Profile (AI 600-1) was not applied to it; it is used as guidance for AI-002 in the inventory |
| Assessor / date | Office Manager (Security Coordinator) with the Irrigation and Equipment Technician (remote pilot), 2026-08-25 |
| Decision | Owner and General Manager, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner and decision authority:** the Owner and General Manager, who uses the estimates and runs the pilot. At a 7-person farm there is no AI committee. The Owner and General Manager, the Security Coordinator, and the Technician review AI use at the monthly security meeting and at the July risk assessment.
- **Policies that apply:**
  - POL-02 A.5: supplier checklist and security terms before any supplier gets farm data. This covers trials, pilots, and free tools.
  - POL-04 4.6: only approved AI tools; no Restricted information in any AI tool; Internal information (drone imagery, yields) only to a tool whose terms bar use of farm data to train or improve models for others without the farm's opt-in.
  - POL-04 4.10: drone images are for crops only, never to watch, identify, or evaluate workers or neighbors; images showing identifiable people are deleted within 30 days when not needed.
  - POL-02 C.2: no Restricted information in public AI chatbots (AI-002).
- **Approved-tools list:** kept by the Security Coordinator under POL-04 4.6. It was created on 2026-08-31. AI-001 is listed with the conditions in section 6; no public chatbot is listed.

**How the pilot started.** The Owner and General Manager signed up for the vendor's service in April 2026 under click-through terms that let the vendor use farm imagery and yield data to improve its models. Nobody reviewed the terms, and the farm had no approved-tools list (`../00_company-facts.md` section 4, item 14; P01 R-018). The policies approved on 2026-08-31 now forbid that path.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Estimate marketable watermelon yield per field, 1 to 2 weeks ahead, from fruit counts detected in drone images. Used to plan load commitments to the packer-shipper and the farm crew's harvest-support hours (BP-02, BP-08) |
| Users / operators | Irrigation and Equipment Technician (FAA Part 107 remote pilot; flies weekly missions and uploads images from the ground station tablet); Owner and General Manager (reads estimates and makes every decision) |
| Affected people | The farm crew, including the 2 H-2A workers, whose harvest-support hours follow the harvest plan; the packer-shipper, which plans trucks against committed loads; people who appear incidentally in field images, including the packer-shipper's contracted harvest crew |
| Data | **Inputs:** RGB and multispectral images, field boundaries, variety and planting dates, and past field yields taken from load records (field totals, never per-worker data). **Outputs:** field-level yield estimates with a confidence range, and image overlays showing detected fruit. **Training:** the vendor's model was trained mainly on imagery from other regions and other melon types; the vendor tunes it per customer. **Terms:** the click-through terms allow the vendor to reuse farm imagery and yields to improve its models (R-018). No Restricted data is sent |
| Build or buy | Buy: vendor SaaS. Estimates are read in the vendor's web app and copied into the harvest plan by hand. There is no connection to SYS-01, the pivots, or the variable-rate irrigation on the 2 NRCS-funded pivots |
| Not intended | Setting the number of workers in an H-2A job order; cutting crew hours without review; evaluating individual workers; crop insurance or FSA reporting; driving irrigation or variable-rate prescriptions. Each would require a new assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| H-2A three-fourths guarantee, 20 CFR 655.122(i) | **Yes, indirectly** | The farm must offer each H-2A worker employment for at least three-fourths of the workdays in the contract period. A forecast cannot lower that floor. If the model over-estimates and the farm then cuts hours, the guarantee and the hours-offered records required by 655.122(j)(1) still govern |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims, not to the farm. The farm keeps the vendor's marketing claims in the contract folder |
| Fla. Stat. 501.171 | Not today | An image of a person in a field is not "personal information" under 501.171(1)(g) unless it is linked to the person's name together with a listed data element. POL-04 4.10 keeps it that way |
| Federal crop insurance and FSA reporting | Not used | Watermelons are not insured. Peanut and cotton production is reported from buying point and gin records, not model estimates. The "Not intended" list keeps it that way for the cotton trial |
| FAA Part 107 | Yes (operations, not AI) | Governs the drone flights, not the model. The Technician holds a remote pilot certificate (14 CFR 107.12) |
| State AI laws (for example Colorado SB26-189) | No | The farm operates only in Florida, and a yield estimate is not a consequential decision about a person. See `00_universal-framework/cross-sector/us-cross-sector-obligations.md` |
| Sector AI rules for agriculture | None identified | The vertical overlay lists none |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why not High:** the model does not make, and is not a substantial factor in, a consequential decision about a person. It cannot affect physical safety or irrigation, because it has no connection to SYS-01 or the pump station. The Owner and General Manager makes every load and crew decision.

**Why not Low:** it influences business decisions that change workers' offered hours and the farm's commitments to its main buyer, and it sends farm data to a vendor under terms the farm did not negotiate.

**Escalation triggers (re-tier to High and reassess):**
- using estimates to set the number of workers in an H-2A job order, or to cut crew hours without review
- linking estimates to irrigation schedules or variable-rate prescriptions that run automatically
- using imagery or model output to evaluate individual workers
- using estimates in crop insurance or FSA reports

## 4. MEASURE
Results are from the 2026 watermelon pilot: 11 weekly flights from 2026-05-04 to 2026-07-13 over 4 watermelon fields (two seedless varieties: an established variety on 60 acres and a new variety on 30 acres). The Owner and General Manager and the Security Coordinator compared 36 field-week estimates, made 1 week ahead, with actual loads by field from the harvest log and load records (2026-08-25).

| Trustworthy characteristic | Test / metric | Result (pilot) | Pass? |
|---|---|---|---|
| Valid and reliable | Mean absolute percentage error (MAPE) of 1-week-ahead field estimates; threshold 15% | 19% overall (vine canopy hides fruit) | **No** |
| Safe | No connection to SYS-01, the pivots, or variable-rate irrigation; estimates cannot trigger any action | Confirmed in P04 and the vendor's integration list | Yes |
| Secure and resilient | Vendor account with MFA; vendor security evidence; images uploaded only from the farm ground station tablet | Account uses a password only (P04); no SOC 2 report from the vendor; uploads from the ground station only | **Partial** |
| Accountable and transparent | Estimates marked "AI estimate" in the harvest plan; a decision log records each load or crew decision that used an estimate | Estimates copied into the plan without a label; no decision log | **No** |
| Explainable and interpretable | Detection overlays let the Owner and General Manager spot-check counts image by image | Available; used in 7 of 11 weeks | Yes |
| Privacy-enhanced | No secondary use of farm data without opt-in; image retention limit; people in images not analyzed | Terms allow secondary use; images kept indefinitely; the vendor confirms it does not detect people | **No** |
| Fair, with harmful bias managed | Mean signed error (bias) by subgroup: variety (established, new) and picking stage (first pick, later picks). Flag any subgroup whose bias is outside plus or minus 10% | Overall +10%. Established variety +6% (24 estimates); **new variety +18% (12): flagged**. First pick +3% (12); **later picks +13.5% (24): flagged** | **No.** Two subgroups flagged |

**Bias finding and why it matters to people.** The model over-estimates the new variety and the later picks, when culls left after the first pick are counted as marketable fruit. Over-estimates lead the farm to commit too many loads and plan more harvest-support hours than there is fruit, then to cancel work at short notice. The crew, including the H-2A workers, bears that effect. This is the risk in P01 R-019. In the pilot one over-commitment (3 loads in late June) was corrected by phone with the packer-shipper's field buyer, and no crew hours were cut, because the Owner and General Manager checked the fields first.

**Worker-impact check (process, not model).** Each week of harvest, the Field Supervisor compares hours offered to each crew member with the harvest plan. Any week in which planned hours fall because of a forecast change is reviewed by the Owner and General Manager, and hours offered are recorded as 20 CFR 655.122(j)(1) requires.

## 5. MANAGE
**Data protection:**
- No Restricted information goes to the vendor. Past field yields are field totals from load records, never hours or names.
- Data terms (condition 1 in section 6) must bar reuse of farm imagery and yields without the farm's opt-in, require deletion within 30 days of exit, and require notice of model changes and of security incidents (POL-02 A.5).
- Vendor account behind MFA, added to the monthly account reconciliation (POL-02 B.5).
- Images uploaded only from the farm's ground station tablet. Images showing identifiable people are deleted within 30 days when not needed (POL-04 4.10).

**Human-in-the-loop design:**
- Estimates are advice only.
- Before any load commitment or crew plan, the Owner and General Manager checks each field's estimate against hand counts on 3 sample rows.
- Load commitments are capped at 85% of the AI estimate unless hand counts confirm the full estimate (R-019).
- No crew hours are cut because of an estimate alone. Hours offered to H-2A workers never fall below the three-fourths guarantee (20 CFR 655.122(i)).

**Monitoring:**
- Weekly error by field during harvest, kept with the harvest plan.
- Bias by variety and picking stage at the end of each month of harvest.
- Model version recorded each week; the vendor must give notice of model changes.

**Incident handling:**
- A vendor security incident or data exposure is handled under POL-03 and the P08 runbook, and logged by the Security Coordinator.
- A model failure (an estimate more than 30% off hand counts) means hand counts only for that field for the rest of the week, and a report to the vendor.

**Decommissioning:**
- Stop and request written deletion of farm data if the vendor has not signed the data terms by 2026-10-31 (R-018).
- Stop if MAPE exceeds 25% across the first 4 weeks of the 2027 harvest.
- Stop if the vendor changes its model or data-use terms without notice.

## 6. Decision
**Approve with conditions.** Owner and General Manager, 2026-08-31.

AI-001 may continue only if these conditions are met by 2026-10-31 (POAM-010):
1. Negotiated data terms: no reuse of farm imagery or yields without opt-in; deletion within 30 days of exit; notice of model changes and security incidents.
2. MFA on the vendor account, and the account added to the monthly reconciliation.
3. Image retention set to 3 seasons, and images showing people deleted when not needed (POL-04 4.10).
4. Estimates labeled "AI estimate" in the harvest plan, and a decision log for each load or crew decision that used one.

**Scope of use:**
- **2027 watermelon season: advisory only.** Load commitments and crew plans rest on hand counts until MAPE is at or below 15% and no subgroup is flagged for a full season. The new variety is calibrated with hand counts, and later-pick estimates are not used.
- **Fall 2026 cotton boll counts: advisory trial only**, compared with gin turnout. Not used for marketing commitments, crop insurance production reports, or crew planning.

If condition 1 is not met by 2026-10-31, the pilot ends and the farm returns to field counts, as before the pilot (P05 BP-08 workaround).

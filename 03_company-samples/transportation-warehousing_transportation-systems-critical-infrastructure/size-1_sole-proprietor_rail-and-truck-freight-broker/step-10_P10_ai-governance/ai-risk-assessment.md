# AI Use Assessment: TMS Document Capture (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight broker arranging truck and rail shipments) |
| Tier / Vertical | Sole Proprietorship / Transportation Systems |
| AI use case | AI-001: the TMS document capture feature, which reads driver-uploaded BOL and POD photos with computer vision and a language model. On since 2026-06-15; automatic approval of carrier pay on "clean" PODs from 2026-07-01 to 2026-08-17. Adapted from the registry default (track and equipment defect detection): for a broker, the "defect" to detect is the damage or shortage note on the delivery paperwork |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form |
| Assessor and decision | Owner, 2026-08-18; decision 2026-09-08 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
A driver photographs the signed BOL or POD and uploads it through the TMS carrier link. The feature reads the image, fills the BOL number and delivery fields in the load record, and flags handwritten exception notes such as "2 pallets damaged" or "short 3 cases." A beta setting would also screen freight photos for visible damage; it was never turned on. Until 2026-08-17, a load with no flag was approved for carrier pay automatically. The images show driver names and signatures, consignee names, and seal numbers. The vendor's terms allowed it to use customer documents to improve its models unless the customer opted out.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| 49 CFR 371.3(a)(3) and (b) | **Yes** | The BOL number is a required record element, kept 3 years. The trial left 4 of 60 sampled records wrong or blank (P03 G-018) |
| Largest shipper's master agreement | **Yes** | Shipper documents are confidential; sending them to train a vendor's model is a use the agreement does not allow |
| Fla. Stat. 501.171(2) | Limited | BOL and POD images rarely hold personal information as Florida defines it (a name with a Social Security, license, or account number, or location). Reasonable measures still apply to anything that does |
| AI-specific law | None identified | The profile lists no sector AI rule. The use is not a consequential decision about a person in any category the repository rubric lists |

## 3. Risk screen (repository rubric)
**Tier: Medium.** It influences business decisions (paying carriers, billing shippers, handling claims), and with automatic approval on it was making the payment decision itself. It does not decide anything about a person's employment, credit, housing, or similar matters, and it cannot affect physical safety or rail operations. Using the P01 method, R-012 rates Moderate.

**Trial results (2026-06-15 to 2026-08-14):** 412 images processed. In the owner's check of 60 sampled documents, 54 had every field right. Of 9 PODs with handwritten exception notes, the feature flagged 6 and missed 3 (recall 67%); it also flagged 2 clean PODs. The 3 missed notes led to carrier payments approved automatically before the shipper's damage or shortage claims arrived, which weakened the broker's position on those claims.

## 4. Data-sharing rules (Govern)
1. Model training on business documents stays off. The owner opted out on 2026-08-18 and keeps the vendor's confirmation (POL-01 9.4).
2. No carrier W-9s, driver licenses, or bank documents go through the feature. Only BOL and POD images.
3. The feature must be named in the vendor list (POL-01 6.1), and the next TMS SOC 2 report is checked for whether it covers the feature (P09).

## 5. Human review of outputs (Measure and Manage)
- **Before carrier pay or a shipper invoice,** the owner reads every POD image, confirms the BOL number, and checks for any handwritten note, whether flagged or not. Automatic approval stays off (turned off 2026-08-17).
- **Monthly sample:** 20 PODs compared field by field with the owner's reading. Metrics: field accuracy and exception-note recall, reported separately for notes in English and in Spanish and for low-quality images (blurred or dark), so that drivers whose paperwork is harder to read are not systematically missed.
- **Thresholds:** keep using the feature only while field accuracy stays at or above 95% in the monthly sample. Recall is not used to justify less human review: every POD is still read.
- **Stop rule:** any payment made on a document the owner did not read, or a vendor change to data use terms, suspends the feature until this assessment is rerun.

## 6. Decision: approve with conditions (2026-09-08)
Keep the feature as a typing aid, not a decision-maker: automatic approval off, human reading of every POD, training opt-out kept, and monthly sampling (P01 R-012, due 2026-09-30). Re-run this assessment before turning on the freight photo damage screening or any automatic approval.

**Related use (AI-002):** the carrier monitoring service's fraud risk score is one input to booking, never the only reason to reject a carrier. Because many carriers are owner-operators, the owner records the reason for every rejection and reviews the list each quarter to check that new carriers are not being turned away on the score alone.

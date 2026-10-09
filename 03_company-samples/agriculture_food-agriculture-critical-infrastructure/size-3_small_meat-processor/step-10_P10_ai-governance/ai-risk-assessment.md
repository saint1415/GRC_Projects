# AI Risk Assessment: AI Quality Inspection on Processing Lines

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (meat processing plant with a smoked seafood room) |
| Tier / Vertical | Small / Food and Agriculture |
| AI use case | AI-001: AI vision quality inspection on Line 3 (sliced and packaged smoked sausage, ham, deli meats, and bacon), pilot since May 2026 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook. AI 600-1 is not applied: AI-001 is not generative |
| Assessor / date | FSQA Manager with the IT Manager and the Controls Engineer, 2026-08-26 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases), built from the accounts payable list, the vendor contracts, the ERP configuration, the identity provider app list and a staff survey (EV-031, EV-032, EV-044, EV-045). How many office staff use public chatbots, and what they paste, was not established (intake open request) |

## 1. GOVERN
- **Accountable owner:** FSQA Manager (food safety outcome). **Technical owner:** Controls Engineer (edge server, line integration). **Decision authority:** majority owner, because AI-001 is High tier (POL-01 4.4 reserves High risk decisions to the owner); the General Manager runs the quarterly review.
- **Policies that apply:**
  - POL-05 4.8: approved AI tools only; no Restricted data in unapproved tools
  - POL-04 4.8: Restricted data only in approved tools
  - POL-01 4.6: any change to AI-001 that affects a CCP or an actionable process step goes through OT change control with FSQA sign-off
  - POL-02 4.5: vendor remote access only through the OT remote access gateway
- **Approved-tools list:** kept by the IT Manager. It lists AI-001 (Line 3 only, conditions in section 6) and AI-002. It does not list any public generative AI tool.
- **Scale for a Small company:** no AI committee. The FSQA Manager, IT Manager, Controls Engineer, and General Manager review AI use cases quarterly, and the majority owner signs High-tier decisions.
- **Gap at the start of the pilot:** AI-001 went live in May 2026 without a validation protocol, a written relationship to the metal detector CCP, or an AI policy (EV-024, EV-045). This assessment closes the documentation gap; sections 4 and 6 set the conditions.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Inspect every pack on Line 3 after sealing for (1) visible foreign material (plastic, film pieces, glove fragments), (2) seal and packaging defects, and (3) missing, wrong, or unreadable labels and lot codes. Suspect packs are diverted to a QA review bin |
| Users / operators | Line 3 operators and QA technicians on two shifts |
| Affected people | **Consumers**, if the system misses a hazard that other controls also miss, or if staff rely on it and reduce other checks. **Workers**, whose hands and arms appear in some images |
| Data | Inputs: product images and label images from 4 cameras; lot codes from the MES. Outputs: pass or divert decisions, defect category, confidence score. The vendor keeps sample images for model improvement (**retention and use terms not yet in the contract**) |
| Build or buy | Buy: vendor-trained models on a vendor-supplied edge server on the control network; vendor retrains in its cloud with plant images |
| Not intended | Replacing the metal detector CCP; replacing manual visual inspection; releasing product; any evaluation of individual workers; use on the seafood line (Line 4). Any of these requires re-assessment |

**How AI-001 relates to food safety controls.** The metal detector is a CCP in the HACCP plans and stays unchanged. AI-001 is **not** a CCP monitoring device and is not part of any HACCP plan. If the company ever wanted to use AI-001 as a CCP, or to reduce manual inspection because of it, that would be a change in "processing methods or systems" requiring HACCP reassessment (9 CFR 417.4(a)(3)) and validation (417.4(a)(1)). AI-001 is also outside the food defense plan today, because Line 3 makes FSIS-inspected product (see P03 section 1.3).

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FSIS HACCP (9 CFR Part 417) | **Indirectly** | Not a CCP today. Becomes directly relevant if AI-001 is used for CCP monitoring or changes the process |
| FMIA misbranding; FSIS recall notice (9 CFR 418.2) | **Yes, as a consequence** | A missed label or lot-code error that reaches commerce can be misbranding and trigger the 24-hour notice |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. The procurement file keeps the claims the company relied on (99% detection) |
| Florida recording law (Fla. Stat. 934.03) | No | It covers interception of oral communications. AI-001 captures images only; the vendor confirmed the cameras have no microphones |
| State AI and employment AI laws (e.g., Colorado SB26-189, Illinois HB 3773) | No | The company operates only in Florida, and AI-001 makes no decision about any person. **Using AI-001 images to evaluate workers is prohibited** because it would turn the system into an employment decision tool |
| 21 CFR Part 121 | No (today) | Line 3 is not in the FDA food defense plan scope. If a similar system is added to the seafood line, the food defense plan must consider it |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why High:** the rubric puts any AI that "can affect physical safety or critical infrastructure operations" in the High tier. AI-001 sits on a food safety path in a critical infrastructure sector. Its failure modes are physical: a missed foreign object, or a misbranded pack that reaches consumers.

**What keeps residual risk manageable:** AI-001 can only *divert* packs, never release them; every diverted pack is decided by a person; and the metal detector CCP and the manual visual inspection stay in place unchanged.

**Escalation triggers (re-assess before any of these):**
- reducing manual visual inspection staff or frequency on Line 3
- using AI-001 as, or in place of, CCP monitoring
- allowing AI-001 to stop or restart the line automatically
- extending to Line 4 (seafood) or other lines
- any use of images to monitor or evaluate workers

## 4. MEASURE
Pilot results cover May 25 to August 21, 2026 (Line 3, two shifts). Seeded-defect tests used certified test pieces and deliberately defective packs placed by QA on each shift.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Seeded foreign material detection of at least 95% overall and at least 90% for every product type | 96% overall (346 of 360); bacon 81% (29 of 36) | **No.** Bacon subgroup fails |
| Valid and reliable | Lot-code and label read accuracy of at least 99.5% against QA check | 99.7% | Yes |
| Valid and reliable | False divert rate of 2% or less (avoids alarm fatigue) | 3.1% overall; 5.8% in the three weeks after the July packaging film change | **No** |
| Safe | Metal detector CCP and manual inspection unchanged; every divert decided by QA | Confirmed by walkthrough and QA logs | Yes |
| Secure and resilient | Edge server isolated; vendor access through the gateway with MFA; model updates through OT change control | Edge server on the control network; vendor remote tool always on; two model updates pushed without notice | **No** |
| Accountable and transparent | Divert decisions logged with defect category and QA disposition | Logged in the vendor dashboard only, not in the records application | Partial |
| Explainable and interpretable | QA can see the image and highlighted region for each divert | Available | Yes |
| Privacy-enhanced | No audio; worker images not used for other purposes; image retention 90 days; no vendor reuse outside the service | No audio confirmed; retention and reuse terms missing from the contract | **No** |
| Fair, with harmful bias managed | Performance compared across product types, shifts (lighting), and packaging films; flag any group more than 5 percentage points worse than overall | Bacon 15 points below overall; night shift 3 points below (not flagged); new film raised false diverts | **No.** Product-type disparity flagged |

**"Bias" in a vision inspection system.** AI-001 makes no decisions about people, so fairness here means **consistent performance across the conditions the product meets**. The flagged disparity is by product: bacon's marbled fat and irregular slices look like the variation the model treats as normal, so foreign material on bacon is missed more often. A system that works well on average but poorly on one product gives false comfort exactly where it is least reliable.

**Ongoing bias and performance testing plan:**
- **Groups compared:** product type (smoked sausage, ham, deli meats, bacon), shift (day and night lighting), packaging film supplier, and label language (English-only versus bilingual private-label packs).
- **Metrics:** seeded-defect detection rate, false divert rate, and label read accuracy for each group.
- **Thresholds:** 95% detection overall and 90% for every group; false diverts of 2% or less; no group more than 5 percentage points worse than overall on any metric.
- **Frequency:** seeded tests on every shift; monthly group report to the FSQA Manager; full re-test after any model update, camera move, lighting change, or packaging change.

## 5. MANAGE
**Human-in-the-loop design:**
- AI-001 diverts; people decide. QA technicians review every diverted pack and record the disposition.
- Manual visual inspection stays at two inspectors per shift. The metal detector CCP is unchanged.
- Operators can switch AI-001 to bypass (all packs pass to manual inspection) at any time; bypass events are logged.

**Monitoring:**
- Seeded tests on every shift, logged in the records application (not just the vendor dashboard).
- Monthly performance and group report (section 4) reviewed by the FSQA Manager; results feed P01 R-022.
- Model updates are changes: the vendor must request them through OT change control, and a full re-test follows each one (POL-01 4.6).

**Security (P01 R-023):**
- Move the edge server to the OT DMZ (POAM-001).
- Vendor access only through the OT remote access gateway with named accounts and MFA (POAM-002).

**Incident handling:**
- A missed defect found downstream (customer complaint, metal detector, QA audit) is investigated under the HACCP corrective action procedure, and the FSQA Manager decides on hold, recall, and FSIS notice (9 CFR 418.2) as for any other cause.
- A security incident involving the edge server or vendor access follows P08.

**Decommissioning:**
- Switch to bypass and remove if detection falls below thresholds for two consecutive months.
- Switch to bypass and remove if the vendor will not sign data retention and reuse terms by 2026-11-30.
- On removal, the vendor must delete all plant images and confirm in writing.

## 6. Decision
**Approve with conditions.** Majority owner, on the recommendation of the General Manager and FSQA Manager, 2026-09-04. AI-001 may continue on Line 3 as a **supplemental** inspection **only if**:
1. **Bacon is excluded** (AI-001 in bypass for bacon runs) until the vendor retrains and a re-test meets the 90% subgroup threshold.
2. Manual visual inspection staffing and the metal detector CCP stay unchanged. The FSQA Manager documents that AI-001 is not part of the HACCP plans.
3. The vendor contract adds 90-day image retention, no reuse outside the service, no use for worker evaluation, and change notice for model updates, by 2026-11-30.
4. Vendor remote access is disabled except through supervised sessions until the OT remote access gateway is live (2026-10-31).
5. Seeded tests and divert dispositions are recorded in the records application from 2026-10-01.

Expansion to other lines, or any reduction in manual inspection, requires a new assessment and two consecutive months meeting all thresholds.

**AI-003 (public generative AI).** Rated Medium because staff could paste formulations, food defense content, or employee data. Prohibited for Restricted and Confidential data (POL-05 4.8). The IT Manager will evaluate an enterprise tool with data-use terms by 2027-03-31.

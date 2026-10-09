# AI Risk Assessment: AI Label and Seal Inspection Camera on Line 2

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (USDA-inspected sausage and smoked meats plant) |
| Tier / Vertical | Micro / Food and Agriculture |
| AI use case | AI-001: AI label and seal inspection camera on the Line 2 packager, pilot since 2026-06-15 (the registry's "AI quality inspection on processing lines," scaled to one vendor smart camera) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook. AI 600-1 is not applied: AI-001 is not generative |
| Assessor / date | Office Manager (security and compliance lead) with the Production Supervisor, 2026-08-25 |
| Decision | Owner, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases), built from the packaging machine purchase order and commissioning record, the intake interviews, the cold-chain dashboard settings and vendor documentation, and a staff question (EV-011, EV-035, EV-036, EV-006, EV-044, EV-043). What has been entered into public chatbots was not established (intake open request) |

## 1. GOVERN
- **Accountable owner:** the Production Supervisor (label accuracy and product release). **Technical contact:** the Maintenance and Sanitation Technician (camera, network, vendor sessions). **Decision authority:** the owner, because AI-001 is High tier and POL-02 A.3 reserves High risk decisions to the owner.
- **Policies that apply:**
  - POL-04 4.6: Restricted information only in approved AI tools; AI-001 is approved only under the conditions in section 6.
  - POL-02 B.8: vendor remote access off by default; sessions supervised and logged.
  - POL-02 B.10: label template changes, and any AI-001 model update, go through the change log with the Production Supervisor's approval and a HACCP reassessment decision.
  - POL-02 C.2: no Restricted information in public AI chatbots (AI-003).
- **Approved-tools list:** kept by the Office Manager in POL-04 4.6. It has one entry, AI-001, for Line 2 only.
- **Scale for a Micro company:** there is no AI committee. The owner, Production Supervisor, and Office Manager review AI use at the monthly security meeting.

**How the pilot started.** The camera module came with the new packaging machine in June 2026. The vendor turned it on during commissioning, with automatic image upload and automatic model updates. Nobody wrote down what it was for, how it would be checked, or what the vendor could do with the images (EV-011; EV-036). This assessment closes the documentation gap; sections 4 and 6 set the conditions.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | After sealing, check each pack for (1) seal defects and (2) label errors: the printed product name, allergen statement, and lot code must match the job loaded on the labeling PC. Failing packs are pushed to a reject bin |
| Users / operators | Production workers on Line 2; the Production Supervisor reviews rejects |
| Affected people | **Consumers**, if a mislabeled pack with a missing allergen statement gets through and staff have come to rely on the camera. **Workers**, whose gloved hands appear in some images |
| Data | Inputs: pack images and label text from one camera; the job's expected label data from the labeling PC. Outputs: pass or reject, defect type, confidence score. The vendor uploads rejected images and a sample of passed images to its cloud to retrain the model. **No retention, reuse, or change-notice terms in the purchase order** |
| Build or buy | Buy: vendor-trained models on the camera; vendor retrains in its cloud and pushes updates over the internet |
| Not intended | Replacing the Production Supervisor's first-label check at the start of each run; replacing the second-person check after a template change; releasing product; any HACCP monitoring; any evaluation of workers. Any of these requires a new assessment |

**How AI-001 relates to food safety controls.** The HACCP plans do not list label checks as CCPs, and AI-001 is not part of any plan. Label accuracy is still a legal duty: a pack with a wrong product name or a missing allergen statement is misbranded, and if it reaches commerce the plant must notify FSIS within 24 hours (9 CFR 418.2). If the company ever wanted AI-001 to replace a manual check, that would be a change in "processing methods or systems" that calls for a HACCP reassessment (9 CFR 417.4(a)(3)(i)).

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FSIS recall notice (9 CFR 418.2) and recall procedure (418.3) | **Yes, as a consequence** | A label error that reaches commerce can be misbranding and trigger the 24-hour notice |
| FSIS HACCP (9 CFR Part 417) | **Indirectly** | Not a CCP today; relevant if AI-001 changes the process or replaces a check (417.4(a)(3)) |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. The purchase file keeps the claim the company relied on ("99% label verification") |
| Florida recording law (Fla. Stat. 934.03) | No | It covers interception of oral communications. AI-001 captures images only; the vendor confirmed the camera has no microphone (EV-044) |
| State AI and employment AI laws | No | The company operates only in Florida, and AI-001 makes no decision about any person. **Using AI-001 images to evaluate workers is prohibited** by company decision |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

**Why High:** the rubric puts any AI that "can affect physical safety or critical infrastructure operations" in the High tier. AI-001 sits on a food safety path in a critical infrastructure sector. Its failure mode is physical: a pack with a missing allergen statement reaching a consumer with that allergy.

**What keeps residual risk manageable:** AI-001 can only reject packs, never release them; every reject is decided by a person; and the first-label check and second-person template check stay in place unchanged.

**Escalation triggers (re-assess before any of these):**
- dropping or reducing the first-label check or the second-person template check
- letting AI-001 stop or restart the line, or release rejected packs automatically
- extending AI-001 to other products or lines, or using it for any HACCP monitoring
- any use of images to monitor or evaluate workers

## 4. MEASURE
Pilot results cover 2026-06-15 to 2026-08-21 (EV-052). The Production Supervisor placed seeded defects on each production day: packs with a wrong label, a label missing the allergen statement, a wrong lot code, and a deliberately bad seal.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Seeded label errors (wrong product, missing allergen statement, wrong lot code) detected: at least 99% | 98.7% (148 of 150); both misses were wrong lot codes on a curved jerky pouch | **No** |
| Valid and reliable | Seeded seal defects detected: at least 95% overall and at least 90% for every product group | 94% overall (113 of 120); snack sticks 82% (23 of 28) | **No.** Snack stick subgroup fails |
| Valid and reliable | False reject rate of 2% or less (avoids staff ignoring the bin) | 3.4% overall; 6.1% in the two weeks after the 2026-07-28 film change | **No** |
| Safe | First-label check and second-person template check unchanged; every reject decided by a person | Confirmed by walkthrough and the reject log | Yes |
| Secure and resilient | Camera on the plant network; vendor access supervised; model updates only through the change log | Camera on the flat network (EV-SC-7); two model updates pushed without notice (2026-07-09 and 2026-08-04, EV-052) | **No** |
| Accountable and transparent | Rejects logged with defect type and disposition in the records app | Logged in the vendor dashboard only | Partial |
| Explainable and interpretable | Supervisor can see the image and the flagged region for each reject | Available in the vendor dashboard | Yes |
| Privacy-enhanced | No audio; worker images not used for other purposes; image retention 90 days; no vendor reuse outside the service | No audio confirmed; retention and reuse terms missing | **No** |
| Fair, with harmful bias managed | Performance compared across product groups, label stock, and packaging film; flag any group more than 5 percentage points worse than overall | Snack sticks 12 points below overall on seals; jerky pouches account for both label misses | **No.** Product-group disparity flagged |

**"Bias" in a vision inspection system.** AI-001 makes no decisions about people, so fairness here means **consistent performance across the products and packaging it sees**. Snack sticks are thin and packed tightly, so seal wrinkles look like the variation the model treats as normal. A system that works well on average but poorly on one product gives false comfort exactly where it is least reliable.

**Ongoing performance and bias testing plan:**
- **Groups compared:** product group (fresh sausage, smoked sausage, ham, jerky, snack sticks), label stock, packaging film supplier.
- **Metrics:** seeded label error detection, seeded seal defect detection, false reject rate, for each group.
- **Thresholds:** 99% label error detection; 95% seal detection overall and 90% for every group; false rejects of 2% or less; no group more than 5 percentage points worse than overall.
- **Frequency:** seeded tests every production day; a monthly group report to the Production Supervisor; a full re-test after any model update, camera move, lighting change, label stock change, or film change.

## 5. MANAGE
**Human-in-the-loop design:**
- AI-001 rejects; people decide. The Production Supervisor reviews every reject and records the disposition.
- The first-label check at the start of each run and the second-person check after any template change stay mandatory (POL-02 B.10).
- Operators can switch AI-001 to bypass at any time; bypass events are logged.

**Monitoring:**
- Seeded tests every production day, logged in the records app (not just the vendor dashboard).
- Monthly performance and group report reviewed by the Production Supervisor; results feed P01 R-017.
- Model updates are changes: automatic updates are turned off, the vendor gives notice, the update goes through the change log, and a full re-test follows.

**Security (P01 R-001, R-017):**
- Camera moves to the plant network (POAM-012), with outbound access only to the vendor's update and upload service.
- Vendor remote access only in supervised sessions (POL-02 B.8).

**Incident handling:**
- A label error found downstream (customer complaint, retail audit) is investigated as a product deviation: the Production Supervisor decides hold, recall, and FSIS notice (9 CFR 418.2) as for any other cause.
- A security incident involving the camera or vendor access follows P08.

**Decommissioning:**
- Switch to bypass and remove if detection falls below thresholds for two consecutive months.
- Switch to bypass and remove if the vendor will not sign data and change-notice terms by 2026-11-30.
- On removal, the vendor must delete all plant images and confirm in writing.

## 6. Decision
**Approve with conditions.** Owner, 2026-08-31, on the recommendation of the Production Supervisor and the Office Manager. AI-001 may continue on Line 2 as a **supplemental** check **only if**:
1. **Snack sticks are excluded** from the seal check (bypass for snack stick runs) until the vendor retrains and a re-test meets the 90% subgroup threshold.
2. The first-label check and the second-person template check stay unchanged, and the Production Supervisor records in the HACCP file that AI-001 is not part of any plan.
3. Automatic model updates are turned off from 2026-09-01; updates only after notice, through the change log, with a re-test.
4. The vendor adds 90-day image retention, no reuse outside the service, no use for worker evaluation, and change notice for model updates to the contract by 2026-11-30.
5. Seeded tests and reject dispositions are recorded in the records app from 2026-10-01.

Expansion to other lines or any reduction in manual checks requires a new assessment and two consecutive months meeting all thresholds.

**AI-002 (cold-chain anomaly alerts).** Rated Medium. It adds early warnings on top of the fixed temperature alarms, which stay in place and remain the monitoring record. The Production Supervisor reviews its alerts but never uses them instead of a threshold alarm or a manual reading.

**AI-003 (public generative AI).** Rated High if Restricted information is entered, because staff could paste formulations, label templates, or employee data. Prohibited for Restricted information (POL-04 4.6; POL-02 C.2). The Office Manager's use for drafting customer emails without Restricted information is allowed.

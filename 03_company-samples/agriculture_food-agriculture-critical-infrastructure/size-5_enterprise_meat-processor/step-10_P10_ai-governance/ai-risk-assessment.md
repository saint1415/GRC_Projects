# AI Governance Risk Assessment: Enterprise AI Portfolio and AI Quality Inspection on Processing Lines

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded further processor of meat products; FL, GA, AL, NC, TN, TX) |
| Tier / Vertical | Enterprise / Food and Agriculture |
| Scope | Enterprise AI portfolio (10 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001 AI quality inspection on processing lines in section 6 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for AI-008 and AI-009; repository risk tier rubric |
| Assessor / date | AI council (chaired by the SVP FSQA), meeting of 2026-08-26; GRC team and the data science lead prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-08 (section 8) |
| Inventory | `ai-use-case-inventory.csv` (10 use cases), built from the AI council register, intake forms and testing records (EV-068), the accounts payable vendor master (EV-043), AI vendor contract terms (EV-044), the web gateway and SSO application catalog review (EV-069), and the gap analysis review of PLT-03 inspection staffing (EV-084). Not established at intake: AI features embedded in OT equipment or vendor products that were never registered or billed separately, and workforce use of public AI tools from personal devices, which the web gateway does not see |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 10 |
| Risk tier | High 2, Medium 6, Low 2 |
| Status | In production 8, Pilot 2 |
| Council review complete | 6 of 10 |
| Not yet reviewed | 4: AI-003, AI-005, AI-007, AI-009 (all due 2026-11-30, POAM-020) |
| Use cases that touch food safety | 3: AI-001 (inspection), AI-005 (refrigeration recommendations), AI-009 (complaint intake) |
| Use cases relying only on vendor data or vendor-run tests | 3: AI-001 (at 4 of 5 plants), AI-002, AI-007 |

**Main findings:**
1. **A plant changed a food safety practice because of an AI tool.** In April 2026, PLT-03 cut manual visual inspection from two inspectors to one on 2 packaging lines after AI-001 went live, without HACCP reassessment (9 CFR 417.4(a)(3)) or council approval. No complaint or recall has been linked to the change, but it removed the safeguard that made AI-001 a Medium-consequence tool in practice (P01 R-012; POAM-021).
2. **One High-tier employment tool is piloting without review.** AI-007 ranks applicants for plant jobs at three plants, including PLT-08 in Texas, with only the vendor's adverse impact summary.
3. **AI-001 performs worse on bacon** at the two bacon plants, the same pattern the company saw in its earlier pilot.

## 2. GOVERN: AI council operating model
**Charter.** The AI council was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee reviews quarterly. Because the company's highest AI risks are physical, the council is chaired by the SVP FSQA rather than by IT.

**Members:** SVP FSQA (chair); CISO; Director of OT Security; Vice President, Engineering; Chief Human Resources Officer (for workforce tools); Deputy General Counsel, Privacy; Chief Compliance Officer; the Director of Refrigeration and Process Safety; a plant manager on rotation; and the data science lead. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Council vote, then the executive risk committee | Local validation and bias or performance testing on the company's own data; impact assessment; human review design; notice to affected people; monitoring plan; for food safety tools, a written statement of the tool's role relative to CCPs and HACCP reassessment where the process changes |
| Medium | Council vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; security and privacy review |
| Low | Council chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products or OT equipment, must be registered before use (POL-05 4.8; STD-05.3). Procurement and OT change control now block AI features without an inventory ID, and **any change to inspection staffing, a CCP, or a HACCP monitoring practice because of an AI tool needs council approval and HACCP reassessment** (POL-05 4.8, added after the PLT-03 finding; POAM-021).

**Policies:** POL-04 4.8 (no Restricted data in AI tools without council approval and no-training terms); POL-05 4.8 (approved tools only, approved purposes only, no food safety practice changes without reassessment) and 4.10 (worker images only for approved safety purposes); POL-01 4.6 (OT change control applies to model updates on plant equipment).

**Cadence:** monthly council meetings; quarterly monitoring review for every High-tier tool; annual re-review of every use case.

**Why 4 use cases lack review.** AI-003 and AI-005 entered as features of existing maintenance and refrigeration services; AI-007 arrived with a recruiting platform upgrade; AI-009 was switched on by the e-commerce vendor. All four predate the procurement block. The council set review dates for all four (section 8).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FSIS HACCP (9 CFR Part 417) | **Indirectly, for AI-001** | AI-001 is not a CCP or a HACCP monitoring device. Using it to replace or reduce an existing control is a change in "processing methods or systems" that requires reassessment (417.4(a)(3)); using it for CCP monitoring would also require validation (417.4(a)(1)) |
| FMIA misbranding; FSIS recall notice (9 CFR 418.2) | **Yes, as a consequence** | A missed label or lot-code error, or an underweight pack (AI-002), that reaches commerce can be misbranding and trigger the 24-hour notice |
| FSMA Intentional Adulteration (21 CFR Part 121) | **PLT-07 only** | AI-001 runs on PLT-07 meat lines, which are outside the Part 121 scope; any AI on the plant-based line must be screened in the food defense plan (POL-01 4.6) |
| Title VII of the Civil Rights Act | **Yes, for AI-007** | Disparate impact remains a statutory theory of liability even though EEOC enforcement priorities changed under EO 14281 |
| Texas TRAIGA (HB 149, effective 2026-01-01) | **Yes, for AI-007 at PLT-08** | Intent-based prohibitions, including AI developed with intent to unlawfully discriminate; AG enforcement with notice and cure |
| Colorado SB26-189, Illinois HB 3773, NYC Local Law 144, California ADS regulations | **No** | The company has no operations or hiring in those jurisdictions; recheck before hiring there |
| State biometric privacy laws | **Not analyzed** | AI-006 has facial recognition and individual tracking disabled; counsel must review before any change |
| FTC Act Section 5 | **Yes** | Accuracy of vendor claims the company relies on (AI-001, AI-002) and of AI-009's statements to consumers |
| OSHA PSM management of change (29 CFR 1910.119) | **Context, for AI-005** | Closed-loop setpoint control of the ammonia system would be a change to the process; advisory mode keeps people in control |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person, or able to affect physical safety or critical infrastructure operations.

| ID | Use case | Tier | Status | Council review |
|---|---|---|---|---|
| AI-001 | AI quality inspection on processing lines (14 lines, 5 plants) | High | In production; bacon lines in bypass | Reviewed 2025-11-12; re-reviewed 2026-08-26 |
| AI-002 | Slicer yield optimization within an approved thickness range | Medium | In production (6 lines) | Reviewed 2026-02-18 |
| AI-003 | Predictive maintenance alerts | Low | In production (advisory) | Not reviewed (due 2026-11-30) |
| AI-004 | Demand forecasting | Medium | In production | Reviewed 2025-12-09 |
| AI-005 | Refrigeration energy optimization (advisory) | Medium | In production at 4 sites | Not reviewed (due 2026-11-30) |
| AI-006 | Worker safety camera analytics (aggregate only) | Medium | In production (22 lines) | Reviewed 2026-05-20 |
| AI-007 | Applicant screening and interview scheduling for plant roles | High | Pilot at 3 plants | Not reviewed (due 2026-11-30) |
| AI-008 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-05-12 |
| AI-009 | Online store and consumer line chatbot | Medium | Pilot | Not reviewed (due 2026-11-30) |
| AI-010 | SOC alert triage assistant | Low | In production | Reviewed 2026-03-11 |

**Tiering notes:** AI-001 is High because it sits on a food safety path in a critical infrastructure sector. AI-005 is Medium only because it is advisory; enabling closed-loop control would make it High. AI-006 is Medium because no alert identifies a worker; enabling individual identification would make it High (employment). AI-009 is Medium, but its complaint routing is treated as a food safety control: a missed illness report is a missed early warning.

## 5. MEASURE: testing gaps and plan
| Tool | Metric | Groups compared | Threshold for action | Status |
|---|---|---|---|---|
| AI-001 | Seeded foreign material detection; false divert rate; label read accuracy | Plant; product type; shift; packaging film | Detection at least 95% overall and 90% per group; false diverts 2% or less; label reads at least 99.5% | Local testing at PLT-03 only; other plants by 2027-03-31 (POAM-020) |
| AI-002 | Pack weight accuracy; underweight rejects | Product; slicer model | Rejects no higher than before deployment | Vendor data only; local comparison by 2026-12-31 |
| AI-007 | Selection rate ratio at each stage (screen, interview, offer) | Sex; race and ethnicity where self-reported; age band; plant | Ratio below 0.8 for any group triggers review and suspension of ranking at that plant | Vendor summary only; local analysis before the 2027 hiring season (POAM-020) |
| AI-009 | Food safety complaint routing | Keywords and languages (English and Spanish) | 100% of illness, injury, and foreign-material mentions routed the same day | 96% on 200 historical complaints; Spanish phrasing missed most often |

**Data limits for AI-007:** self-reported race and ethnicity is incomplete for applicants, so the plan reports completeness and adds plant and shift as secondary views. Zip code and commute distance are model inputs that can act as proxies; the council will decide whether to remove them.

## 6. Full assessment: AI-001 AI quality inspection on processing lines
### 6.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Inspect every pack after sealing for (1) visible foreign material, (2) seal and packaging defects, and (3) missing, wrong, or unreadable labels and lot codes. Suspect packs are diverted to a QA review bin |
| Where | 14 packaging lines: PLT-01 (bacon, 3 lines), PLT-03 (deli meats, 4 lines), PLT-04 (hot dogs, 3 lines), PLT-06 (bacon, 2 lines), PLT-07 (fully cooked entrees, 2 meat lines) |
| Users / operators | Line operators and QA technicians on all shifts |
| Affected people | **Consumers**, if the system misses a hazard that other controls also miss, or if staff rely on it and reduce other checks. **Workers**, whose hands and arms appear in some images |
| Data | Inputs: product and label images; lot codes from the MES. Outputs: pass or divert, defect category, confidence score. The vendor keeps sample images for model improvement under contract terms (90-day retention, no reuse outside the service, no worker evaluation) signed 2026-01 |
| Build or buy | Buy: vendor-trained models on edge servers in each plant's OT DMZ; vendor retrains in its cloud; model updates go through OT change control |
| Not intended | Replacing metal detection, X-ray, or manual visual inspection; releasing product; any evaluation of individual workers; use on the PLT-07 plant-based line. Any of these requires re-assessment |

**How AI-001 relates to food safety controls.** Metal detection or X-ray is a CCP or prerequisite program in each plant's HACCP plans and stays unchanged. AI-001 is **not** a CCP monitoring device and is not part of any HACCP plan. Manual visual inspection is part of each plant's prerequisite program. PLT-03's reduction of manual inspection on lines 3-2 and 3-4 (2026-04-06) was therefore a change to the process made because of AI-001, without the reassessment 9 CFR 417.4(a)(3) requires.

### 6.2 Risk tier
High (section 4). Escalation triggers (re-assess before any of these):
- reducing manual visual inspection staff or frequency on any line;
- using AI-001 as, or in place of, CCP monitoring;
- allowing AI-001 to stop or restart a line automatically;
- extending to new lines or plants, or to the PLT-07 plant-based line;
- any use of images to monitor or evaluate workers.

### 6.3 MEASURE (2026-05-01 to 2026-08-21)
Seeded-defect tests used certified test pieces and deliberately defective packs placed by QA. Local tests ran on every shift at PLT-03; the other plants ran weekly seeded tests reported through the vendor dashboard.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Seeded foreign material detection of at least 95% overall and at least 90% per product type | 95.8% overall (1,226 of 1,280); bacon 84% (PLT-01 and PLT-06); deli 97%; hot dogs 96%; entrees 94% | **No.** Bacon fails |
| Valid and reliable | Label and lot-code read accuracy of at least 99.5% | 99.7% | Yes |
| Valid and reliable | False divert rate of 2% or less | 2.6% overall; 4.9% at PLT-04 after a packaging film change in July | **No** |
| Safe | Metal detection, X-ray, and manual inspection unchanged; every divert decided by QA | Manual inspection reduced on 2 PLT-03 lines since 2026-04-06; otherwise confirmed | **No** |
| Secure and resilient | Edge servers in the OT DMZ; vendor access through the OT gateway with MFA; model updates through OT change control | In place at all 5 plants; one model update in June skipped the change ticket at PLT-06 | Partial |
| Accountable and transparent | Divert decisions logged with defect category and QA disposition in the records platform | Logged at 4 plants; PLT-06 still uses the vendor dashboard only | Partial |
| Explainable and interpretable | QA can see the image and highlighted region for each divert | Available | Yes |
| Privacy-enhanced | No audio; worker images not used for other purposes; 90-day retention; no vendor reuse | Contract terms in place; quarterly vendor attestation received | Yes |
| Fair, with harmful bias managed | Performance compared across plants, products, shifts, and films; flag any group more than 5 points worse than overall | Bacon 11.8 points below overall; PLT-04 false diverts after the film change | **No.** Product-type disparity flagged |

**"Bias" in a vision inspection system.** AI-001 makes no decisions about people, so fairness here means **consistent performance across the conditions the product meets**. Bacon's marbled fat and irregular slices look like the variation the model treats as normal, so foreign material on bacon is missed more often. A system that works well on average but poorly on one product gives false comfort exactly where it is least reliable.

### 6.4 MANAGE
- **Human in the loop:** AI-001 diverts; people decide. QA technicians review every diverted pack and record the disposition.
- **Manual inspection restored:** two inspectors per line at PLT-03 from 2026-09-15; HACCP reassessment at PLT-03 by 2026-10-31 (POAM-021). No other plant may reduce inspection without council approval and reassessment.
- **Bacon:** AI-001 stays in bypass on the 5 bacon lines (all packs go to manual inspection as before) until the vendor retrains and a re-test meets the 90% threshold.
- **Monitoring:** seeded tests on every shift at every plant from 2026-10-01, logged in the records platform; monthly performance report by plant, product, shift, and film to the SVP FSQA; full re-test after any model update, camera move, lighting change, or packaging change (POL-01 4.6).
- **Security:** model updates only through OT change control; the PLT-06 skipped ticket was reviewed and closed.
- **Incident handling:** a missed defect found downstream is investigated under the HACCP corrective action procedure, and FSQA decides on hold, recall, and FSIS notice (9 CFR 418.2). A security incident involving an edge server or vendor access follows P08.
- **Decommissioning:** switch a line to bypass and remove if detection falls below thresholds for two consecutive months, or if the vendor changes data-use terms; on removal, the vendor deletes all plant images and confirms in writing.

## 7. MANAGE: portfolio controls
- **Monitoring:** each High-tier tool has monthly or quarterly metrics (inventory column `monitoring`) reported to the council; threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, missed food safety signal, bias finding, data misuse) are logged as SOC or FSQA events and follow P08 where security or product safety is involved.
- **Third parties:** AI vendors with access to plant OT or Restricted data are tier-1 in the vendor program; contracts require notice of material model changes and bar training on company data.
- **OT boundary:** AI tools on plant equipment (AI-001, AI-002, AI-005) are inventoried in the OT asset inventory and follow the OT remote access and change rules.
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice or change data-use terms; the inventory records retirement.

## 8. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the council's recommendation of 2026-08-26:
1. **AI-001:** approved to continue as a supplemental inspection with conditions: PLT-03 manual inspection restored by 2026-09-15 and reassessed by 2026-10-31; bacon lines in bypass until retrained; local seeded testing at all 5 plants by 2027-03-31; divert records in the records platform at PLT-06 by 2026-10-31.
2. **AI-007:** ranking stays advisory and recruiters must review every low-ranked application before any rejection; council review by 2026-11-30 and local selection rate analysis before the 2027 hiring season; ranking is suspended at any plant where the ratio falls below 0.8.
3. **AI-003, AI-005, AI-009:** may continue in current scope until council review by 2026-11-30; AI-005 stays advisory; AI-009 routing must reach 100% on food safety keywords in English and Spanish before the pilot expands.
4. **AI-002, AI-004, AI-006, AI-008, AI-010:** approved to continue; AI-002 local pack-weight comparison by 2026-12-31; AI-006 quarterly configuration audits continue.
5. **Policy change:** POL-05 4.8 now bars any change to inspection staffing, a CCP, or a HACCP monitoring practice because of an AI tool without council approval and HACCP reassessment.

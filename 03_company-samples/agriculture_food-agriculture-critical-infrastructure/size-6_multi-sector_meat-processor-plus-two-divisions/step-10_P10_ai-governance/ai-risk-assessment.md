# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Meat Processing, Food Distribution, Grocery Retail, corporate) |
| Tier / Vertical | Multi-Sector / Food and Agriculture |
| Scope | The group AI governance program: the Group AI Standard, the division use-case inventory, and the rules that apply to each division's use cases. Priority use case: **AI-001 AI quality inspection on processing lines** (Meat Processing). Second priority: **AI-005 store loss-prevention camera analytics** (Grocery Retail pilot) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook; NIST AI 600-1 for the generative AI assistant (AI-008) only. AI-001 is not generative |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-09-02; presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (8 use cases: 2 High, 5 Medium, 1 Low), built from AI tool discovery across procurement records, SaaS discovery, the SYS-G1 app list and the data platform model registry (EV-037), division configuration records (EV-058, EV-065, EV-077, EV-078), the use case owner refresh in 2026-08 (EV-100), and the test results in section 4 (EV-101 to EV-103). Not established: workforce use of public generative AI tools outside the enterprise assistant (intake open request) |
| Related | P01 GR-04, GR-12, GR-20, MT-013, MT-014, RT-009, RT-018; P07 POAM-015, POAM-023, POAM-026; P06 POL-01 4.12 and 4.13, POL-04 4.9, POL-05 4.7 and 4.8 |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and food safety risk; receives the High-tier list and conditions each quarter |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Food Safety and Quality Officer, Group Chief Privacy Officer, Group General Counsel, Group OT security director, and one delegate per division president. Approves High-tier use cases and the approved-tools list |
| Division AI owners | The named business owner for each use case (inventory column); run monitoring and report monthly |
| Group Chief Food Safety and Quality Officer | Final say on any AI on a food safety path: HACCP reassessment, food defense reanalysis, product holds |
| Group CISO and Group OT security director | AI security: vendor access through SYS-G5, model updates through OT change control, edge server placement, data leakage |
| Group Chief Privacy Officer | Shopper, loyalty member, employee, and driver data; privacy notices; privacy reviews before customer-facing pilots |
| Group internal audit | Adds High-tier AI controls to the 2027 assessment plan; designs and operates no AI controls |

### 1.2 Group AI Standard (adopted 2026 under POL-01 4.12)
1. **Register before use.** Every AI use case that can affect food safety, critical infrastructure operations, or decisions about people is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). **Group override:** any in-store surveillance analytics is High, because it can lead to a shopper being stopped or accused even though the rubric's consequential-decision categories do not name it.
3. **High tier needs council approval**, a pre-deployment validation and bias test, a notice plan for affected people, and quarterly monitoring reports.
4. **Food safety gate.** AI that sits on a food safety path passes OT change control with FSQA sign-off (POL-01 4.13). The sign-off records whether the change triggers a HACCP reassessment (9 CFR 417.4(a)(3)(i)) or, at Plant 6, a food defense reanalysis (21 CFR 121.157).
5. **Vendor terms** (POL-01 4.8; POL-04 4.9): no training or reuse of group data outside the service, image and video retention limits, deletion on exit, notice before model updates, and vendor access only through SYS-G5.
6. **Approved tools only** for workforce generative AI (POL-05 4.7). **Images and video** are used only for the approved purpose, never to evaluate workers or identify shoppers (POL-05 4.8).

**Where the program fell short (group gap 8).** The standard was adopted after AI-001 was already in production at three plants (since 2025) and after the AI-005 pilot started at 12 stores without a privacy review. The Food Distribution forecasting and routing tools (AI-003, AI-004) were not registered until this assessment. Each now has conditions (section 6), tracked as POAM-026.

## 2. MAP
### 2.1 Inventory summary
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | AI quality inspection on processing lines | Meat Processing | **High** | 7 lines at Plants 1, 3, and 4 in production; 2-line pilot at Plant 6 |
| AI-002 | Predictive maintenance on ammonia refrigeration compressors | Meat Processing | Medium | In production at Plants 1, 3, and 6 |
| AI-003 | Demand forecasting and replenishment | Food Distribution | Low | In production |
| AI-004 | Route optimization | Food Distribution | Medium | In production |
| AI-005 | Store loss-prevention camera analytics | Grocery Retail | **High** (group override) | Pilot at 12 stores |
| AI-006 | Personalized loyalty offers | Grocery Retail | Medium | In production |
| AI-007 | Workforce scheduling optimizer | Grocery Retail | Medium | In production at 120 stores |
| AI-008 | Enterprise generative AI assistant | Group | Medium | Pilot (1,500 users) |

### 2.2 AI-001: AI quality inspection on processing lines
| Item | Description |
|---|---|
| Purpose and intended use | Inspect every pack after sealing for (1) visible foreign material (plastic, film, glove fragments), (2) seal and packaging defects, and (3) missing, wrong, or unreadable labels and lot codes. Suspect packs are diverted to a QA review bin |
| Where | Plant 1: bacon, ham, and deli lines (3). Plant 3: cooked meats lines (2). Plant 4: case-ready tray lines (2). Plant 6 pilot since 2026-05: one deli line and one line on the plant-based protein line |
| Users / operators | Line operators and QA technicians on all shifts |
| Affected people | **Consumers**, if AI-001 misses a hazard that other controls also miss, or if staff come to rely on it. **Workers**, whose hands and arms appear in some images |
| Data | Inputs: product and label images; lot codes from MES (SYS-M3). Outputs: pass or divert, defect category, confidence score. The vendor keeps sample images to retrain models in its cloud; **retention and reuse terms are not yet in the contract** (P04) |
| Build or buy | Buy. Vendor models run on edge inference servers on each line's control network (SYS-M6); retraining happens in the vendor cloud |
| Not intended | Replacing a metal detector CCP or manual visual inspection; releasing product; stopping or restarting lines; evaluating individual workers. Any of these needs a new assessment |

**How AI-001 relates to the food safety system.** The metal detectors that are CCPs in the plant HACCP plans, and manual visual inspection, stay unchanged. AI-001 is **not** a CCP monitoring device and is not in any HACCP plan. Using it for CCP monitoring, or reducing manual inspection because of it, would be a change in "processing methods or systems" that requires a HACCP reassessment (9 CFR 417.4(a)(3)(i)) and validation (417.4(a)(1)). A label or lot-code error that AI-001 misses and that reaches commerce can be misbranding, which triggers the 24-hour FSIS notice (9 CFR 418.2) as for any other cause.

**Plant 6 and Part 121.** Plant 6 is the one FDA-registered plant, so its food defense plan is mandatory (C-FOOD-AG-R01). AI-001 is an inspection step, not an actionable process step. Its edge server, however, sits on the plant-based line's control network, which also carries the brine and CIP controls that the P03 gap analysis found were never assessed as attack paths. The council treats adding a networked, vendor-maintained server to that network as a significant change that creates a reasonable potential for a new vulnerability, so a reanalysis was due before the pilot started (121.157(b)(1), (c)(1)). This is an **author interpretation**, consistent with how P03 treats control-system access as access to the product. The reanalysis now under way for the 2025 MES upgrade (POAM-023) will include it.

**Applicable laws and rules (AI-001):**
| Rule | Applies? | Why |
|---|---|---|
| FSIS HACCP, 9 CFR 417.4(a)(1), (a)(3)(i) | **Indirectly** | Not a CCP today. Becomes direct if AI-001 is used for CCP monitoring or changes the process |
| FMIA misbranding; 9 CFR 418.2 | **Yes, as a consequence** | Missed label or lot-code errors that reach commerce |
| FSMA Intentional Adulteration, 21 CFR 121.157 (C-FOOD-AG-R01) | **Yes, Plant 6 pilot** | Reanalysis of the control network change (author interpretation above) |
| FTC Act Section 5 (N42-R01) | Indirectly | Applies to the vendor's detection claims. The procurement file keeps the claims relied on |
| State AI and employment AI laws | No | AI-001 makes no decision about any person. Using images to evaluate workers is prohibited (POL-05 4.8), because it would turn AI-001 into an employment tool |
| State recording laws | No | Images only; the vendor confirmed the cameras have no microphones |

### 2.3 AI-005: store loss-prevention camera analytics
| Item | Description |
|---|---|
| Purpose | Flag possible non-scans and concealment at self-checkout from CCTV video so asset protection staff can offer help or review the transaction |
| Data | Video of shoppers and workers at self-checkout; transaction logs. Processed in the vendor cloud; 30-day retention |
| Configuration | **Facial recognition disabled.** No identification of shoppers; no watch lists |
| Affected people | Shoppers, who may be approached; cashiers and self-checkout attendants, who appear in the video |
| Gap | The pilot started at 12 stores in 2026-04 without a privacy review, without signage, and without mention in the privacy notice (P01 RT-009; P03 RT-G66). No vendor security review under POL-01 4.8 |

| Rule | Implication |
|---|---|
| FTC Act Section 5 (N44-45-R02) | Data practices must match the privacy notice, and unfair practices that harm consumers are actionable. The FTC's December 2023 order against Rite Aid (a 5-year ban on facial recognition surveillance, with notice, deletion, an information security program, and independent assessments) is the clearest signal of what the FTC expects from AI surveillance in stores |
| State consumer privacy and biometric laws | Apply in each operating state where thresholds are met. The group treats them generically and avoids biometric identifiers altogether by prohibiting facial recognition |
| POL-05 4.8 | Video used only for the approved purpose; never to evaluate workers or identify shoppers |

### 2.4 Other use cases (rules in brief)
- **AI-002 (refrigeration):** the model reads historian exports only. PSM inspection and testing of process equipment (29 CFR 1910.119(j)(4)) continue on their own schedule; the model may move a work order earlier, never later.
- **AI-003 and AI-004 (Food Distribution):** route plans must respect hours-of-service limits (49 CFR Part 395) and pre-cool timing that supports temperature control during transport (21 CFR 1.908). Driver location data is Restricted (POL-04); in the Florida worked example a name with geolocation information is personal information under the breach law (Fla. Stat. 501.171(1)(g)1.a.(VII)).
- **AI-006 (loyalty offers):** data use must match the privacy notice (N44-45-R02). The excluded-categories list keeps the model from inferring health conditions, pregnancy, or similar sensitive traits from purchases (P01 RT-018).
- **AI-007 (scheduling):** employment discrimination laws (Title VII, the ADA, the ADEA) apply to scheduling practices whatever the tool. No operating state was found to have an AI-specific employment law; counsel rechecks yearly using the cross-sector file.
- **AI-008 (generative assistant):** NIST AI 600-1 risks (data privacy, information integrity, information security). Restricted data such as formulations and the Plant 6 food defense plan stays out (POL-04 4.9).

## 3. Risk tiers (repository rubric plus the group override)
- **High:** AI-001 (can affect physical safety in a critical infrastructure sector: a missed foreign object or a misbranded pack reaches consumers). AI-005 (group override for in-store surveillance).
- **Medium:** AI-002, AI-004, AI-006, AI-007, AI-008. People make the final decision, but outputs influence operations, customers, or workers.
- **Low:** AI-003. Internal business use with no personal data and no decisions about people.

**What keeps AI-001's residual risk manageable:** it can only divert, never release; a person decides every diverted pack; and the CCPs and manual inspection stay unchanged.

**Re-tier and re-assess triggers:**
- AI-001: reducing manual inspection; any CCP role; automatic line stop or restart; new lines, plants, or product types; any use of images about workers.
- AI-002: any write path to SYS-M4 controllers (to High).
- AI-005: enabling facial recognition (prohibited); expansion beyond 12 stores; using alerts for anything other than an offer of help.
- AI-007: use in discipline, attendance points, or hours reductions (to High).

## 4. MEASURE
### 4.1 AI-001 (seeded-defect tests and line data, 2026-05-04 to 2026-08-21; EV-101)
Seeded tests used certified test pieces and deliberately defective packs placed by QA on every shift.

| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Seeded foreign material detection: at least 95% overall and at least 90% for every product type (Plants 1, 3, 4) | 95.2% overall (800 of 840). Bacon 83.3% (100 of 120); ham 97.5% (117 of 120); deli 98.3% (118 of 120); cooked meats 98.8% (237 of 240); case-ready 95.0% (228 of 240) | **No.** Bacon fails |
| Valid and reliable | Plant 6 pilot detection (same thresholds) | Deli 96.7% (58 of 60); plant-based 86.7% (52 of 60) | **No.** Plant-based fails |
| Valid and reliable | Label and lot-code read accuracy of at least 99.5% against QA checks | 99.8% | Yes |
| Valid and reliable | False divert rate of 2% or less (prevents alarm fatigue) | 2.4% overall; 4.1% on Plant 4 case-ready lines (film glare) | **No** |
| Safe | Metal detector CCPs and manual inspection unchanged; every divert decided by QA | Confirmed by walkthroughs and QA logs at Plants 1, 3, 4, and 6 | Yes |
| Secure and resilient | Vendor access only through SYS-G5; model updates only through OT change control | Always-on vendor remote tool at Plants 1, 3, and 4 (P01 MT-014); two model updates in 2026 bypassed change control (P01 GR-20) | **No** |
| Accountable and transparent | Divert dispositions recorded in the food safety records application (SYS-M5) | Plants 1, 3, and 6: yes. Plant 4: vendor dashboard only | Partial |
| Explainable and interpretable | QA sees the image and highlighted region for each divert | Available at all lines | Yes |
| Privacy-enhanced | No audio; images not used about workers; retention and reuse limits in the contract | No audio and no worker use confirmed; contract terms missing | **No** |
| Fair, with harmful bias managed | Detection and false diverts compared across product type, plant, shift, and packaging film; flag any group more than 5 points worse than overall | Bacon 11.9 points below overall; plant-based pilot 8.5 points below; night shifts within 2 points (not flagged) | **No.** Two product disparities flagged |

**"Bias" in a vision inspection system.** AI-001 makes no decisions about people, so fairness here means **consistent performance across the conditions the product meets.** Bacon's marbled fat and irregular slices look like the normal variation the model has learned to ignore, so foreign material on bacon is missed more often. A system that works well on average but poorly on one product gives false comfort exactly where it is weakest.

**Ongoing bias and performance testing plan (AI-001):**
- **Groups compared:** product type, plant, line, shift (lighting), packaging film supplier, and label language (English-only versus bilingual private-label packs).
- **Metrics:** seeded detection rate, false divert rate, and label read accuracy per group.
- **Thresholds:** at least 95% detection overall and 90% per group; false diverts of 2% or less; no group more than 5 points worse than overall on any metric.
- **Frequency:** seeded tests every shift; monthly group report to the Division VP FSQA; full re-test after any model update, camera move, lighting change, or packaging change; quarterly summary to the council.

### 4.2 AI-005 (pilot data, 2026-04-06 to 2026-07-31, 12 stores; EV-102)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Share of alerts confirmed as a likely non-scan after video review (target of at least 50% before any expansion) | 31% | **No** |
| Safe and accountable | Share of approaches made only after video review (target 100%), from an audit of 200 approaches | 93% (186 of 200; 14 approaches without review) | **No** |
| Fair, with harmful bias managed | Alerts per 1,000 self-checkout transactions by store, compared with confirmed loss; flag a store above 1.5 times the pilot median without matching loss. The group collects no shopper demographics by design, so it uses store-level rates, approach outcomes, and complaints | 3 of 12 stores flagged; causes under review (camera angle, layout, customer mix) | **Flagged** |
| Privacy-enhanced | Facial recognition off; 30-day retention; privacy review | Off and 30-day retention confirmed; no privacy review | **No** |
| Accountable and transparent | Store signage and privacy notice describe the analytics | Neither | **No** |
| Secure and resilient | Vendor security review and contract terms (POL-01 4.8) | Not done | **No** |

### 4.3 Other use cases (summary; EV-103)
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-002 | No write path from the model to SYS-M4 (configuration review) | Read-only export confirmed at all three plants | Yes |
| AI-002 | Share of high-risk scores confirmed by a mechanic's inspection | 64% (target 50%) | Yes |
| AI-004 | Route plans exceeding hours-of-service limits before dispatcher review | 1.8% of plans; all corrected by dispatchers | Yes, with the condition in section 6 |
| AI-007 | Hours offered by store, compared across part-time workers by age band (from HR data) | Within 5 points at all stores | Yes |
| AI-008 | Data leakage test: Restricted data samples pasted by test users | Blocked by data loss prevention rules in 48 of 50 attempts | **No** (2 formulation snippets not detected) |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001** diverts; people decide. QA technicians review every diverted pack and record the disposition in SYS-M5. Manual visual inspection and the metal detector CCPs stay as they are. Operators can switch to bypass at any time, and bypass events are logged.
- **AI-005** alerts trained asset protection staff, who must review the video before any approach and may only offer checkout help. An alert never leads to detention, a ban, or a record about a named shopper.
- **AI-002, AI-004, AI-006, AI-007:** a named role approves every work order, route plan, offer rule, and schedule.

**Monitoring:** monthly metrics to division AI owners; quarterly High-tier report to the council and the board risk committee. Results feed P01 risks GR-04, MT-013, MT-014, GR-20, RT-009, and RT-018.

**Security:** AI-001 vendor access moves to SYS-G5 at Plants 1, 3, and 4 (GR-12); model updates are OT changes with FSQA sign-off and a full re-test (POL-01 4.13; POAM-015); edge servers move to the OT DMZ where the plant has one.

**Incident handling:**
- A defect AI-001 missed and found downstream (customer complaint, metal detector, QA audit) is handled under the HACCP corrective action procedure. The plant FSQA manager and the Division VP FSQA decide on holds, recall, and the 9 CFR 418.2 notice as for any other cause.
- A security incident involving edge servers, vendor access, or vendor cloud data follows the P08 runbook.
- A shopper complaint about AI-005 goes to the Group Chief Privacy Officer within 2 business days, and the store's alert history is reviewed.

**Decommissioning:**
- AI-001: switch a line to bypass if detection falls below the thresholds for two consecutive months; remove AI-001 if the vendor will not sign retention and reuse terms by 2026-11-30. On removal, the vendor deletes all plant images and confirms in writing.
- AI-005: end the pilot if confirmed-alert precision is still below 50% after retuning, or if the privacy review is not complete by 2027-01-31.
- Every use case has a manual fallback already covered in the BIA (P05): manual inspection, scheduled maintenance, buyer-built orders, dispatcher-built routes, standard offers, and manager-built schedules.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 AI quality inspection | **Approve with conditions** (council, 2026-09-02; board risk committee informed 2026-09-15) | Bacon runs in bypass until the vendor retrains and a re-test meets the 90% threshold. Plant 6 plant-based line pilot suspended until the food defense reanalysis covers the edge server (2026-12-31, POAM-023); the Plant 6 deli line pilot continues. Contract terms for image retention, no reuse, deletion, and update notice by 2026-11-30. Vendor access only through SYS-G5 and model updates only through change control by 2026-12-31. Plant 4 dispositions in SYS-M5 from 2026-10-01. Validation report by product type by 2026-12-31 (POAM-026). No reduction in manual inspection and no new lines until two consecutive months meet all thresholds |
| AI-005 camera analytics | **Continue the pilot at 12 stores with conditions; no expansion** | Approach only after video review (retraining by 2026-10-31); signage and a privacy notice update by 2026-12-31; vendor security review and contract terms by 2026-12-31; privacy review and store-level disparity analysis by 2027-01-31 (POAM-026) |
| AI-002 predictive maintenance | **Approved** | Read-only data path re-checked at every change; no effect on PSM inspection schedules |
| AI-004 route optimization | **Approved with conditions** | Hours-of-service check before dispatch; driver location data kept 13 months |
| AI-006 loyalty offers | **Approved** | Excluded-categories review by 2027-03-31 (RT-018) |
| AI-007 scheduling optimizer | **Approved with conditions** | No use for discipline; annual hours-distribution review by store |
| AI-003 forecasting | **Approved** | Standard monitoring |
| AI-008 generative assistant | **Approved for the pilot** | Data loss prevention rules updated for formulation formats before any expansion beyond 1,500 users; prohibited for food safety, food defense, and employment decisions |

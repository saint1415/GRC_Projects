# AI Governance Risk Assessment: Enterprise AI Portfolio and Track Defect Detection

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company of 64 freight railroads in 27 states) |
| Tier / Vertical | Enterprise / Transportation Systems |
| Scope | Enterprise AI portfolio (13 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, track and equipment defect detection (computer vision), in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1); repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Safety Officer), meeting of 2026-08-20; GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-08 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 13 |
| Risk tier | High 3, Medium 7, Low 3 |
| Status | In production 10, Pilot 3 |
| Committee review complete | 8 of 13 |
| Not yet reviewed | 5: AI-005, AI-007, AI-010, AI-012, AI-013 (all due 2026-12-31) |
| Safety inspection tools supplementing FRA-required inspections | 2 (AI-001, AI-002) |
| High-tier tools validated only on vendor data | 2 (AI-001, AI-002); AI-007 has no adverse impact analysis |

**Main findings:** the two safety inspection models (AI-001, AI-002) were validated on vendor data from Class I main lines, not on short line track and equipment, and the first local test of AI-001 shows lower recall on jointed and excepted track. A High-tier employment tool (AI-007) is in production without committee review, applicant notice, or an adverse impact analysis, with Colorado's law taking effect on 2027-01-01. Three pilots (AI-005, AI-012, AI-013) started through vendor features or engineering projects before the intake rule existed.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board safety, security, and risk committee reviews quarterly.

**Members:** Chief Safety Officer (chair); CISO; Vice President, Engineering; Chief Mechanical Officer; Director of Train Control Systems; Chief Human Resources Officer; General Counsel's delegate; Director of Labor Relations; the data science lead; and a Chief Risk Officer delegate. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Local validation on company data (track class, equipment, region); impact assessment; human review design; notice to affected people where law or policy requires; monitoring plan with thresholds; labor relations review where crafts are affected |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; security and privacy review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.9; STD-05.3). Since 2026-03, procurement and the change board block AI features without an inventory ID. The GRC team owns the inventory.

**Policies:** POL-04 4.9 (no SSI or Restricted data in AI tools without committee approval and no-training terms); POL-05 4.9 (approved tools only); STD-05.3 (approved AI tools list); STD-05.4 (notice to unions before deploying monitoring technology that affects represented crafts).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier tool; annual re-review of every use case.

**Why 5 use cases lack review.** AI-007 and AI-010 arrived as vendor feature releases; AI-005, AI-012, and AI-013 started as engineering or safety pilots before the intake block existed. The committee set review dates for all five (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FRA track safety standards, 49 CFR 213.233 | Yes, for AI-001 | Visual track inspections must be made by a person designated under 213.7; "mechanical, electrical, and other track inspection devices may be used to supplement visual inspection" (213.233(b)). AI-001 is used only as a supplement. Using it to replace or reduce required inspections would need FRA approval, which the company has not sought |
| FRA freight car safety standards, 49 CFR 215.13 | Yes, for AI-002 | Each freight car placed in a train must be inspected before departure; portal flags support, but do not replace, the inspection |
| Hazmat security inspection, 49 CFR 174.9 | Context for AI-002 | Security inspection of placarded hazmat cars stays a human ground-level inspection |
| TSA SD 1580/82-2022-01E | Yes, where AI connects to a Critical Cyber System | AI-005 reads exported PTC logs only; any direct connection to the PTC back office would be a change to a Critical Cyber System and would trigger a CIP amendment check (Sec. VI.B) |
| SSI, 49 CFR part 1520 | Yes | SSI must not enter AI tools without approval (POL-04 4.9); bridge and infrastructure imagery is kept Restricted |
| Colorado SB26-189 | Yes, for AI-007 from 2027-01-01 | Automated decision-making technology in consequential decisions, including employment; the company recruits in Colorado |
| Illinois Public Act 103-0804 | Yes, for AI-007 | Amends the Illinois Human Rights Act on employer use of AI; the company recruits in Illinois |
| Federal equal employment opportunity laws | Yes, for AI-007 | Adverse impact analysis before any change in use |
| FTC Act Section 5 | Indirectly, for AI-009 | Accuracy of claims the assistant makes to customers |
| Collective bargaining agreements | Yes, for AI-006 and AI-013 | Crew assignment rules and notice to unions for technology that affects represented crafts |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision (here, employment) or able to affect physical safety (here, safety inspections).

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | Track and equipment defect detection (computer vision) | High | In production (24 vehicles) | Reviewed 2025-11-12; re-reviewed 2026-08-20 |
| AI-002 | Machine vision car inspection portals | High | In production (9 portals) | Reviewed 2025-12-10 |
| AI-003 | Wayside detector alarm prioritization for maintenance | Medium | In production | Reviewed 2026-01-21 |
| AI-004 | Locomotive predictive maintenance | Medium | In production | Reviewed 2026-02-18 |
| AI-005 | PTC back office log anomaly analytics | Low | Pilot | Not reviewed (due 2026-12-31) |
| AI-006 | Crew scheduling optimization suggestions | Medium | In production | Reviewed 2026-03-18 |
| AI-007 | Applicant screening and ranking (conductor trainees) | High | In production | Not reviewed (due 2026-12-31) |
| AI-008 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-01-14 |
| AI-009 | Customer portal virtual assistant | Medium | In production | Reviewed 2026-04-15 |
| AI-010 | SOC alert triage assistant | Low | In production | Not reviewed (due 2026-12-31) |
| AI-011 | Demand forecasting for car supply | Low | In production | Reviewed 2025-10-22 |
| AI-012 | Grade crossing video analytics for near misses | Medium | Pilot (12 crossings) | Not reviewed (due 2026-12-31) |
| AI-013 | Energy management advisory for engineers | Medium | Pilot (40 locomotives) | Not reviewed (due 2026-12-31) |

**Tiering notes:** AI-001 and AI-002 are High because a missed defect could contribute to a derailment, even though humans still perform every required inspection. AI-003 stays Medium because real-time detector alarms are handled by rule without the model. AI-013 is Medium only while its automatic throttle mode stays disabled; enabling it would re-tier it to High. AI-006 is Medium because crew callers apply the agreement rules to every assignment.

## 5. Safety inspection AI: how it fits the FRA inspection duties
| Duty | What the company does | Status |
|---|---|---|
| Required visual track inspections by designated persons (213.233(a)) | Inspection frequency and staffing are set without regard to AI-001 | Met |
| Devices only supplement visual inspection (213.233(b)) | AI-001 flags go to the inspector, who confirms, records, and takes remedial action under part 213 | Met |
| Pre-departure car inspection (215.13) | AI-002 flags go to qualified inspectors; trains are not released on portal results alone | Met |
| Avoid automation bias | Inspector audits compare findings on portal-cleared and non-portal cars | Partially met: audit design approved, first results due 2027-03-31 (POAM-022) |

These rows match P03 G-105 and G-106 and POAM-022.

## 6. MEASURE: validation gap and plan
**Gap.** For AI-001 and AI-002 the only full validation evidence is the vendors' data from Class I main lines: heavy welded rail, concrete ties, and newer cars. The company's network is mostly lighter jointed rail on wood ties, much of it excepted or Class 1 and 2 track, with older cars in captive service.

**Local validation plan (POAM-022, due 2027-03-31):**
| Tool | Metric | Groups compared | Threshold for action |
|---|---|---|---|
| AI-001 track defect detection | Recall and precision on inspector-confirmed defects | Track class; rail type (jointed, welded); region; light conditions | Any group's recall below 85%, or more than 5 points below overall |
| AI-002 car inspection portals | Agreement with inspector findings; missed defects found later | Car type; car age band; portal location | Missed-defect rate above 2% for any car type |
| AI-007 applicant screening | Selection rate ratios | Sex, race and ethnicity where self-reported, age band | Ratio below 0.8 for any group triggers review and suspension |

Results go to the committee, the Vice President, Engineering, and the Chief Mechanical Officer.

## 7. Full assessment: AI-001 track and equipment defect detection
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Cameras on hi-rail vehicles capture track images during inspection runs; the model flags possible defects (broken or cracked rail, joint bar defects, missing fasteners, tie and plate conditions, vegetation fouling) for the inspector |
| Users | About 60 designated track inspectors in 3 regions; engineering managers |
| Affected people | Train crews and the public, who depend on track safety; roadway workers and members of the public who appear in images |
| Data | Inputs: track images with location and time. Outputs: flags with confidence and location. Bridge and infrastructure imagery is Restricted; faces are blurred at capture |
| Build or buy | Configure: vendor model, fine-tuned by the company data science team, deployed in a dedicated Cloud provider B account (P04) |
| Not intended | Replacing or reducing required visual inspections; deciding speed restrictions or track removal without an inspector |

### 7.2 Risk tier
High (section 4). Escalation triggers: any proposal to rely on AI-001 to change inspection frequency or method (would require FRA approval and executive risk committee review), or use of images for employee performance monitoring (prohibited without labor relations review under STD-05.4).

### 7.3 MEASURE (local test set: 420 inspector-confirmed defects and 3,100 defect-free image segments on 6 railroads, June to August 2026)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Recall on confirmed defects overall at least 90%; precision at least 60% | Recall 86%; precision 71% | **No** (recall) |
| Safe | Inspector confirms every flag; no required inspection skipped because of AI-001 | 100% of sampled runs had full visual inspection records | Yes |
| Secure and resilient | Dedicated cloud account; MFA; model release control; no connection to OT | In place (P04) | Yes |
| Accountable and transparent | Every flag and inspector decision logged; model version recorded with each flag | In place | Yes |
| Explainable and interpretable | Flag shows the image region and defect class | Available | Yes |
| Privacy-enhanced | Faces and vehicle plates blurred at capture; images kept 2 years | Blurring confirmed in a 200-image sample | Yes |
| Fair, with harmful bias managed (performance across environments) | Recall gap by track class and rail type no more than 5 points | Welded rail 91%; jointed rail on excepted and Class 1 track 68%; low light 74% | **No** |

### 7.4 MANAGE
- **Human in the loop:** inspectors review every flag and record their own findings; AI flags never close or open a defect record on their own.
- **Performance gap:** until local recall on jointed and excepted track reaches 85%, inspectors on those segments are told in the app that the model may miss defects there, and AI-001 is not offered as a reason to change inspection speed or frequency. The vendor and data science team retrain on company images by 2027-03-31.
- **Monitoring:** monthly recall on inspector-confirmed defects by track class and region; false positives per 100 miles; quarterly report to the committee.
- **Incidents:** if a derailment or accident investigation finds a defect that AI-001 imaged and did not flag, the case goes to the committee and the Chief Safety Officer within 5 business days; FRA accident reporting is unchanged (part 225).
- **Decommissioning:** stop use if recall falls below 80% for two months in a row, if the vendor changes data-use terms, or if the gap is not closed by 2027-06-30 for the affected track classes.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier tool has quarterly performance and fairness or environment metrics (inventory column `monitoring`) reported to the committee; threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse) are logged as SOC or safety events and follow P08 where security or SSI is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts require notice of material model changes and prohibit training on company data without approval.
- **Change control:** new model versions for AI-001 and AI-002 are released through the pipeline with validation results attached and committee approval (P04).
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice, change data-use terms, or lose a required approval; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the committee's recommendation of 2026-08-20:
1. **AI-001:** approved to continue as a supplement with conditions: the in-app limitation notice on jointed and excepted track by 2026-10-31; local validation and retraining by 2027-03-31 (POAM-022); no use to change inspection frequency or method.
2. **AI-002:** approved to continue; automation-bias audits and local validation due 2027-03-31 (POAM-022).
3. **AI-007:** may continue only with recruiter review of every list; adverse impact analysis by 2026-11-15, applicant notices by 2026-12-15, and the impact assessment by 2026-12-31 (POAM-024). If the Colorado requirements are not met by 2027-01-01, ranking is switched off for Colorado applicants.
4. **AI-005, AI-010, AI-012, AI-013:** may continue in current scope until committee review by 2026-12-31; no expansion. AI-013 automatic throttle mode stays disabled. AI-012 keeps face and plate blurring.
5. **Inventory:** procurement and the change board continue to block AI features without an inventory ID.

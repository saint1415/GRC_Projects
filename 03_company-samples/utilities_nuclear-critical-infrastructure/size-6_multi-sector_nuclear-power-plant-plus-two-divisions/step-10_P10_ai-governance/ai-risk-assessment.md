# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Nuclear Generation, Engineering and Radiation Services, Radioactive Waste Management, corporate) |
| Tier / Vertical | Multi-Sector / Nuclear Reactors, Materials, and Waste |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the regulator-specific rules for the priority use case, **predictive maintenance for non-safety plant equipment** (AI-001), plus the other High-tier use cases (AI-006, AI-007) and engineering generative AI (AI-002) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1) for AI-002, AI-003, and AI-009, and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-28; presented to the board risk committee 2026-09-17 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 3 High, 5 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group General Counsel, the Chief Nuclear Officer's delegate (fleet engineering director), the fleet cyber security program manager, the Engineering and Radiation Services chief engineer, and the Radioactive Waste Management processing director. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) and the rule that no AI service may connect to a CDA, an SGI system, or a Part 37 security system (POL-01 4.7) |
| Fleet cyber security program manager | Confirms that any AI data flow from station systems is outbound-only from the business DMZ replicas and never touches a CDA |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026, under POL-01 4.14)
1. **Register before use.** Every AI use case that supports maintenance, engineering, safety, security, or decisions about people is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, testing against defined metrics (bias testing where people are affected), and quarterly monitoring reports.
3. **Nuclear overlays come first.** Anything that can influence plant maintenance, plant configuration, or security is screened under 10 CFR 73.58 and, for maintenance, reviewed by the Maintenance Rule program (50.65) before use. Anything used in safety-related engineering follows the quality assurance program that the client or licensee requires (10 CFR Part 50, Appendix B).
4. **Data rules.** No SGI, CSP information, access authorization files, Part 37 information, or Part 810 controlled technology may go to any AI tool (POL-04; POL-05 4.4). Plant data reaches AI services only from the business DMZ replicas, which receive data one way from Level 3.
5. **Change gate.** A material change (new model, new vendor, new equipment scope, new decision role, or automation of an action) triggers re-assessment before release.
6. **Approved tools only** for workforce generative AI (POL-05 4.5).

**Where the program fell short in 2026.** The standard was adopted after the predictive maintenance pilot was already running. Its alerts were creating work requests automatically on equipment in Maintenance Rule scope, and it had not been screened under 73.58 or reviewed by the Maintenance Rule program (scenario gap 10). Engineers were using a generative AI assistant without a quality assurance rule. Both are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Predictive maintenance for non-safety plant equipment | Nuclear Generation | High | Pilot (Stations A and B) with conditions |
| AI-002 | Generative AI engineering assistant | Engineering and Radiation Services | Medium | Approved with restrictions |
| AI-003 | Enterprise generative AI assistant | Group | Low | Pilot (3,000 users) |
| AI-004 | SOC alert triage and anomaly scoring | Group | Medium | In production |
| AI-005 | Dosimetry anomaly flagging | Engineering and Radiation Services | Medium | In production |
| AI-006 | Outage craft staffing match | Engineering and Radiation Services | High | Proposed; not approved |
| AI-007 | Waste container imaging classifier | Radioactive Waste Management | High | Pilot (second facility) |
| AI-008 | Driver safety scoring | Radioactive Waste Management | Medium | In production |
| AI-009 | Condition report screening assist | Nuclear Generation | Medium | Proposed |

### 2.1 Priority use case: predictive maintenance (AI-001)
| Item | Description |
|---|---|
| Purpose and intended use | Detect early degradation in balance-of-plant rotating equipment and transformers so engineers can plan maintenance before failure. Intended as an **advisory** input to engineers, not a decision maker |
| Users / operators | System engineers and Maintenance Rule coordinators at Stations A and B; work planners see approved work requests only |
| Affected people | No individuals are the subject of decisions. Plant workers and the public are affected indirectly, because some monitored equipment is in Maintenance Rule scope: its failure could cause a reactor trip (50.65(b)(2)(iii)) |
| Data (inputs, training, outputs) | Inputs: about 2,400 tags of process data from the business DMZ replicas and 10 years of work order history from the WMS. Training: vendor base models tuned on fleet history. Outputs: anomaly alerts, remaining-life estimates, and (until 2026-09-15) automatically created work requests |
| Build or buy | Buy: vendor SaaS (SYS-N9). The vendor's SOC 2 report does not cover its model hosting provider (P04) |
| Deployment context | Data leaves the station only from the business DMZ replica servers, outbound to the vendor. **Nothing flows back to the replicas, and the replicas have no path to Level 3** (one-way devices). The pilot cannot change plant equipment, setpoints, or the control room |

**Regulator-specific rules for AI-001**
| Rule | What it requires | What it means for the pilot |
|---|---|---|
| 10 CFR 50.65(a)(1); (b)(2)(iii) | Monitor the performance or condition of SSCs in scope against licensee-established goals; scope includes nonsafety-related SSCs whose failure could cause a reactor scram | Alerts on scoped equipment are condition-monitoring information. The Maintenance Rule program must decide how (or whether) the model's outputs are used in monitoring against goals; the pilot cannot quietly become the monitoring method. **Gap:** not reviewed by the program before use |
| 10 CFR 50.65(a)(3) | Evaluate performance and condition monitoring activities and goals at least every refueling cycle, not to exceed 24 months | The next periodic evaluation at each station must cover how the pilot was used and whether it changed preventive maintenance |
| 10 CFR 50.65(a)(4) | Assess and manage the increase in risk before maintenance activities | Met: every pilot-generated work request passed through work control risk assessment (P03 G-061). The model does not schedule work |
| 10 CFR 73.58(b)-(c) | Assess and manage potential adverse effects on safety and security before changes, including maintenance activities and procedural changes | Automatic creation of work requests changed how maintenance is initiated. It needed a 73.58 screen. **Gap:** not screened |
| 10 CFR 73.54 (boundary) | Protect CDAs against cyber attacks | The data path is outbound-only from the business DMZ; no vendor connection reaches Level 3. The fleet cyber security program manager confirmed this boundary in 2026-08 |
| Vendor and contract | SA-9 assurance for the vendor and its model hosting provider | The vendor's SOC 2 report carves out the hosting provider; obtain the hosting provider's report or a bridge letter |

**Not applicable to AI-001:** state AI laws on consequential decisions (no decision about a person), and 10 CFR 50.55a or digital I&C licensing rules (the model is not plant equipment and does not perform a safety function). Industry and NRC discussion of AI in nuclear applications was noted, but no NRC rule specific to AI applies to this use.

### 2.2 Other High-tier and nuclear-specific use cases
| Use case | Rule | Implication |
|---|---|---|
| AI-007 waste imaging classifier | Facility license conditions and waste acceptance criteria; DOT hazmat rules for outbound shipments | A missed prohibited item could create a processing hazard or a shipping violation. The classifier may add holds but never release a package; a technician reviews every scan |
| AI-006 outage staffing match | Title VII disparate impact; state AI employment laws where candidates reside (Colorado SB26-189 applies to consequential employment decisions made on or after 2027-01-01; Illinois HB 3773 requires notice and bars zip codes as proxies; California Civil Rights Council ADS rules and CPPA ADMT rules) | The group recruits in about 30 states. Treat as High: bias audit by protected class where data allows, candidate notice, and human review before any use. Not approved |
| AI-002 engineering assistant | Client QA requirements (10 CFR Part 50, Appendix B, by contract); 73.22 (no SGI); Part 810 | No use in safety-related calculations or design documents until the QA procedure for AI is issued (POAM-024). No SGI or controlled technology in prompts |
| AI-009 CAP screening assist | 73.77(b) (CSP deficiencies recorded within 24 hours); licensee QA corrective action program | A suggestion must never delay the 24-hour record or downgrade a CSP deficiency. Only the screening committee assigns significance |

## 3. Risk tiers (repository rubric)
- **High:** AI-001 and AI-007 (can affect physical safety or critical infrastructure operations); AI-006 (substantial factor in employment decisions).
- **Medium:** AI-002, AI-004, AI-005, AI-008, AI-009. Humans make every final decision, but outputs influence engineering, security, dose, employment coaching, or corrective action priority.
- **Low:** AI-003 (internal productivity, no regulated data).

**Why AI-001 is High even though it covers non-safety equipment.** The rubric's High tier includes AI that "can affect physical safety or critical infrastructure operations." Some monitored equipment is in Maintenance Rule scope because its failure could cause a reactor trip, and the pilot was creating work requests on its own. A missed degradation, or a flood of false alerts that pulls maintenance resources away from real problems, can affect plant reliability.

**Re-tier and re-assessment triggers:** extending AI-001 to safety-related equipment or to Station C; any automation of work requests or schedule changes; using AI-002 output in safety-related work; enabling AI-009 auto-assignment.

## 4. MEASURE
Results are from pilot data and audits between 2026-03 and 2026-08.

### 4.1 Predictive maintenance (AI-001)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Back-test on 3 years of fleet history: share of recorded functional failures on monitored equipment that the model alerted at least 7 days before failure (target 70% or more) | 24 of 31 failures (77%) | Yes |
| Valid and reliable | Precision: share of alerts that engineers confirmed as real degradation (target 50% or more) | 212 of 498 alerts (43%) | **No.** Alert volume is high |
| Safe | Maintenance Rule scoped equipment: any scoped failure in the pilot period that the model missed and the existing program also missed (target 0) | 0 | Yes |
| Safe | Automation bias: share of auto-created work requests on scoped equipment that planners scheduled without an engineer's review (target 0%) | 61 of 140 (44%) before the 2026-09-15 change | **No.** Fixed by the human approval condition |
| Secure and resilient | Data flow confirmed outbound-only from the business DMZ; vendor access reviewed; vendor and hosting provider assurance | Outbound-only confirmed; hosting provider not covered by the vendor's SOC 2 report | Partial |
| Accountable and transparent | 73.58 screen and Maintenance Rule program review completed before use | Not done (scenario gap 10) | **No** |
| Explainable and interpretable | Each alert shows the tags and trends that drove it | In place | Yes |
| Privacy-enhanced | No personal information in inputs | Confirmed | Yes |
| Fair, with harmful bias managed | People are not affected directly. **Equipment-class performance check:** recall and precision by equipment class (pumps, motors, transformers) and by station; flag if any class or station is more than 15 points below the overall rate | Transformers: recall 50% (3 of 6 failures) vs 77% overall | **Flagged.** Exclude transformers from the pilot until retrained |

### 4.2 Other High-tier use cases
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-007 imaging classifier | Recall on a seeded test set of 400 packages with known prohibited items (target 98% or more, with technician review as a second check) | 386 of 400 (96.5%) | **No.** Remains a pilot with 100% technician review |
| AI-007 imaging classifier | Performance by container type (drums, liners, boxes); flag a gap of more than 3 points | Liners 91% | **Flagged** |
| AI-006 staffing match | Selection-rate comparison by sex and by age band (40 and over) on a 2025 historical test set; flag any group below 80% of the highest group's rate | Age 40 and over at 71% of the under-40 rate | **Failed.** Not approved |

### 4.3 Generative AI (AI-002, AI-003, AI-009), using AI 600-1 risk areas
| AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Confabulation | Sample of 100 AI-assisted engineering drafts reviewed by senior engineers for fabricated references or values (target 0 reaching an issued document) | 7 drafts with fabricated references, all caught before issue | Yes for issued documents; QA rule still needed |
| Information security (data leakage) | DLP hits for SGI, Part 810, or CSP markings in prompts | 3 blocked attempts (no SGI; Part 810 markings) | Controls working |
| Value chain and component integration | Enterprise tenant terms: no training on group data; data residency | Signed | Yes |
| Human-AI configuration | AI-009 suggestions labeled; committee override rate tracked | Not yet enabled | n/a |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** alerts go to the system engineer, never directly to work planning. The engineer reviews the evidence and either closes the alert or writes a work request in their own name. For Maintenance Rule scoped equipment, the Maintenance Rule coordinator is copied. Engineers can disregard any alert without justification. The model cannot change schedules, setpoints, or Maintenance Rule status.
- **AI-007:** every scan is reviewed by a technician; the classifier can only add a hold.
- **AI-002:** the engineer of record owns every output; no use in safety-related work until the QA procedure is issued.
- **AI-006:** not deployed.

**Monitoring:** monthly metrics to each division owner; quarterly High-tier report to the council and the board risk committee; P01 risks GR-08, NG-020, and ER-013.

**Incident handling:** an AI failure that affects plant equipment, a waste package, a person's employment, or regulated information follows P08 and POL-03. A missed degradation on scoped equipment is also a condition report in the station CAP. Any suspected compromise of the predictive maintenance vendor is treated as a third-party incident on the business side; it cannot reach CDAs because the data path is outbound-only.

**Decommissioning:** each use case has an off switch and a fallback that the BIA already covers (P05): time-based preventive maintenance and existing condition monitoring for AI-001 (BP-NG12, RTO 72 hours), technician-only review for AI-007, manual drafting for AI-002, and manual screening for AI-009.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 predictive maintenance | **Approve with conditions** (council, 2026-08-28; board risk committee informed 2026-09-17) | Automatic work request creation disabled (done 2026-09-15); 73.58 screen and Maintenance Rule program review by 2026-11-30; transformers excluded until retrained; precision improvement plan with a 50% target by 2027-03-31; hosting provider assurance by 2026-12-31; no expansion to Station C or safety-related equipment without a new assessment (POAM-023) |
| AI-002 engineering assistant | **Continue with restrictions** | QA procedure for AI by 2026-11-30; training by 2026-12-31; no use in safety-related calculations or design documents until then (POAM-024) |
| AI-007 imaging classifier | **Continue as a pilot at the second facility only** | 100% technician review; retrain for liners; recall target met on a new seeded test before any Florida deployment |
| AI-006 staffing match | **Reject for now** | Re-submit only with an independent bias audit, candidate notice in each state that requires it, and a human-review design |
| AI-003, AI-004, AI-005, AI-008 | **Approved** | Standard monitoring. AI-003 is prohibited for regulated information and decisions about people |
| AI-009 CAP screening assist | **Not yet approved** | Pre-deployment test on 2025 condition reports; written rule that suggestions never delay the 73.77(b) 24-hour record |

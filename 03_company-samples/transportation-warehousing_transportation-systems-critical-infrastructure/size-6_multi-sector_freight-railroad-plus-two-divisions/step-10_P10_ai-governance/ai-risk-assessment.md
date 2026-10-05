# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Freight Railroad, Transload and Wholesale, Real Estate, corporate) |
| Tier / Vertical | Multi-Sector / Transportation Systems |
| Scope | The group AI governance program (standards, inventory, council), the division use cases, the regulator-specific rules that apply to them, and a full assessment of the priority use case **AI-001, track and equipment defect detection (computer vision)** |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1) for AI-005, AI-009, and AI-010, and the AI RMF Playbook; risk tiers from the repository rubric |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27; presented to the board safety, security, and risk committee 2026-09-10 |
| Inventory | `ai-use-case-inventory.csv` (11 use cases: 3 High, 5 Medium, 3 Low; 5 reviewed by the council, 6 not yet) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board safety, security, and risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group General Counsel, Chief Safety Officer, Freight Railroad, the three division security and compliance leads, Group HR director. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (model supply chain, data leakage, prompt injection, SSI and FCI exclusion) |
| Group General Counsel | Employment, state AI, and contract questions |
| Group internal audit | Adds High-tier AI controls to the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-02 under POL-01 4.14)
1. **Register before use.** Every AI use case that supports safety inspections, train operations, pricing, employment, or lease decisions, or that touches SSI or personal information, is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier needs council approval, a pre-deployment impact assessment, validation on the group's own operating conditions, and quarterly monitoring reports.
3. **Safety rules come first.** No AI output may replace an inspection, authority, or decision that an FRA or TSA rule assigns to a qualified person or a defined process.
4. **No SSI, FCI, or Restricted data in unapproved tools** (POL-05 3.6). Vendors that process group data sign no-training and retention terms.
5. **Critical Cyber Systems.** An AI feature added to a Critical Cyber System is a change under POL-01 4.9 and may need a CIP amendment request (SD 1580/82-2022-01E VI.B.2).
6. **Change gate.** A new model, vendor, data source, or decision role triggers re-assessment before release.

**Where the program fell short in 2026.** The Standard arrived after several use cases were live. AI-001 was approved with conditions, but its validation came from Class I main lines (scenario gap 11). AI-006 and AI-009 went live in 2025 with no review, and AI-008 started a pilot in 2026-05 before council review. The council has scheduled all 6 unreviewed use cases by 2027-01-31 (P01 GR-04).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Council review |
|---|---|---|---|---|
| AI-001 | Track and equipment defect detection | Freight Railroad | High | Approved with conditions 2026-03-18 |
| AI-002 | Locomotive predictive maintenance from fault codes and sensor data | Freight Railroad | Medium | Not yet reviewed |
| AI-003 | Dispatch meet-and-pass planning assistant suggesting meets and sidings to dispatchers | Freight Railroad | High | Not yet reviewed (review before any pilot) |
| AI-004 | Crew scheduling optimization proposing crew assignments within agreement rules | Freight Railroad | Medium | Not yet reviewed |
| AI-005 | Shipper portal assistant answering car-trace and invoice questions | Freight Railroad | Low | Approved 2026-04-22 |
| AI-006 | Wholesale pricing recommendation model for bulk product quotes | Transload and Wholesale | Medium | Not yet reviewed |
| AI-007 | Demand forecasting and inventory replenishment for terminals | Transload and Wholesale | Low | Approved 2026-05-13 |
| AI-008 | Driver safety video analytics flagging risky driving events from in-cab cameras | Transload and Wholesale | High | Not yet reviewed |
| AI-009 | Lease abstraction tool extracting key terms from leases | Real Estate | Low | Not yet reviewed |
| AI-010 | Enterprise generative AI assistant for workforce productivity | Group | Medium | Approved 2026-02-24 |
| AI-011 | SOC alert triage assistant summarizing and ranking alerts | Group | Medium | Approved 2026-03-18 |

### 2.1 Rules that apply by division
| Division | Rules that shape AI use | What they mean |
|---|---|---|
| Freight Railroad | 49 CFR 213.7 and 213.233 (track); 215.11 and 215.13 (freight cars); 229.21 (locomotives); TSA directives for AI in Critical Cyber Systems | Inspections are done by designated qualified persons. 213.233(b) allows "mechanical, electrical, and other track inspection devices" to **supplement** visual inspection, not replace it. AI features in CAD or PTC are changes to Critical Cyber Systems |
| Transload and Wholesale | FTC Act Section 5 (accuracy of claims; unfair practices); state AI-in-employment laws for driver analytics; FAR 52.204-21 for FCI | Driver analytics that influence discipline need notice and human review; pricing models must not use data in ways counsel has not cleared |
| Real Estate | FTC Act Section 5 | Low-risk productivity use; leases are commercial, so housing and consumer credit AI rules do not apply |
| Group | NIST AI RMF; state laws on AI in employment where affected employees work (Illinois Public Act 103-0804, effective 2026-01-01; Colorado SB26-189 for consequential decisions on or after 2027-01-01); POL-05 data rules | The group has employees in both states. Counsel is reviewing whether AI-004 and AI-008 "materially influence" employment decisions under SB26-189 before its effective date |

## 3. AI-001: track and equipment defect detection
### 3.1 Context
- **Purpose:** find suspected track defects (broken or cracked rail, joint bar cracks, missing fasteners, tie and plate problems) and equipment defects (wheel, truck, brake, and safety appliance conditions) sooner, and point qualified inspectors to them.
- **How it works:** 24 hi-rail vehicles with camera kits record track during scheduled inspections; 8 wayside machine vision portals image passing cars. The vendor models run on cloud provider B and send alerts to inspectors' tablets with the image, location, and confidence.
- **Who is affected:** employees and the public, through the safety of train operations, especially where PIH tank cars and hosted passenger trains run.
- **Where it runs:** 9 railroads since 2025, as an advisory tool alongside the required inspections.
- **What it is not:** it is not a track inspection under 213.233 and not a pre-departure inspection under 215.13. Those are still performed and recorded by designated people.

### 3.2 Risk tier: High
AI-001 can affect physical safety and critical infrastructure operations, so it is High under the repository rubric even though it makes no decision about a person. The controls that follow from the tier: human review before action, pre-deployment validation, impact assessment, and ongoing monitoring.

### 3.3 MEASURE
| Characteristic (AI RMF) | Test or evidence | Result |
|---|---|---|
| Valid and reliable | Vendor validation on Class I main line images | **Not representative.** Short lines have lighter rail, jointed track, more vegetation, and older cars. A 2026-06 field comparison on 2 short lines found recall for broken joint bars of 71% against 93% in the vendor report |
| Safe | Inspector decides on every alert; alerts cannot close defects | Met. The concern is the reverse: inspectors trusting a quiet day. Inspection records show no reduction in walking inspections where AI-001 runs |
| Secure and resilient | Model supply chain; image store access; inference service in provider B behind group identity | Met for access; the vendor's model update process is not yet reviewed under POL-01 4.8 |
| Accountable and transparent | Alert log with model version, image, location, inspector decision | Met (P04) |
| Explainable and interpretable | Bounding boxes and defect class on every alert | Met for inspectors' needs |
| Privacy-enhanced | People in crossing images are blurred at ingest | Met |
| Fair with harmful bias managed | No decisions about people. **Performance equity across railroads** is the relevant fairness question: older, lower-traffic lines must not get worse detection | Not yet measured per railroad |

**Validation plan (POAM-023):** a short line validation set of at least 2,000 labeled images per defect class drawn from all 9 railroads, labeled by qualified inspectors; per-railroad recall and precision; thresholds: recall of at least 90% for broken rail and broken joint bars on every railroad before expansion, and a false alert rate that inspectors can work (set by the Chief Safety Officer with inspectors). Re-validate at every model version.

### 3.4 MANAGE
- **Human in the loop:** every alert goes to a qualified inspector; inspectors confirm, reject, or escalate; only inspectors record defects and remedial actions under part 213 or part 215.
- **Monitoring:** monthly per-railroad recall estimate from inspector-found defects that AI-001 missed; quarterly report to the council.
- **Incidents:** a missed defect that contributes to an accident is investigated as a safety event and, if a cyber cause is suspected, as a P08 incident.
- **Change control:** new model versions go through the group change gate and the validation plan before release.
- **Decommissioning:** if per-railroad recall falls below the threshold for two months, alerts are suspended on that railroad and inspections continue unchanged.

## 4. Other priority use cases
| ID | Main risk | Required action | Owner | Due |
|---|---|---|---|---|
| AI-003 | An optimizer in the CAD could become an unreviewed change to a Critical Cyber System | Council review and CIP amendment decision before any pilot | Director, Network Operations Center | Before pilot |
| AI-008 | Driver discipline influenced by video analytics without notice | Driver notice; human review documented; counsel decision on state laws before 2027-01-01 | Director, Fleet Operations | 2026-12-15 |
| AI-006 | Unreviewed pricing model | Council review; override monitoring | Vice President, Commercial (Transload and Wholesale) | 2027-01-31 |
| AI-004 | Crew assignments influenced by an unreviewed model | Council review; check against agreement rules and state law | Director, Crew Management | 2027-01-31 |

## 5. Decisions of the council (2026-08-27)
1. AI-001 stays in production on 9 railroads as an advisory tool; **no expansion** until the validation plan is met (POAM-023, due 2027-03-31).
2. AI-008 pilot continues on 300 trucks, but flagged events may not be used for discipline until notice and counsel review are complete.
3. AI-003 may not be piloted without council approval and a CIP amendment decision.
4. All unreviewed use cases are scheduled for review by 2027-01-31.

These decisions were presented to the board safety, security, and risk committee on 2026-09-10 with the group risk register (GR-04).

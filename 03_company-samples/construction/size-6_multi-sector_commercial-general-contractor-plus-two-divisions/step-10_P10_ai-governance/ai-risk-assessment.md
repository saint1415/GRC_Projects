# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Construction, Property, A&E, corporate) |
| Tier / Vertical | Multi-Sector / Construction |
| Scope | The group AI governance program: the Group AI Standard, the division use-case inventory, and the rules specific to each division's regulators and contracts. Priority use case: **AI-001, the AI estimating and bid assistant** (Construction, also used by A&E cost estimators). Deeper review of the four High-tier use cases (AI-002, AI-003, AI-005, AI-007) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-09-04; presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 4 High, 5 Medium, 0 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group General Counsel, Group HR director, Director of Federal Contracts Compliance, Construction VP of preconstruction, A&E chief quality officer, Property VP of building operations. Approves High-tier use cases, the approved-tools list, and the information classes each tool may receive |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring and report monthly |
| Group CISO | AI security standard (data leakage, prompt injection, vendor terms, tenant configuration) |
| Director of Federal Contracts Compliance | Decides whether a tool may receive FCI; confirms no tool receives CUI |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026, under POL-01 4.12)
1. **Register before use.** Every AI use case that touches FCI, bid pricing, personal information, or client data, or that supports decisions about people, subcontractors, designs, or building operations, is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, bias or safety testing, and quarterly monitoring reports.
3. **Information classes per tool** (POL-04 4.13). **No AI tool is approved for CUI.** A tool may receive FCI only if the Director of Federal Contracts Compliance has confirmed it is inside the CMMC Level 1 scope or approved as an external system under FAR 52.204-21(b)(1)(iii), with enterprise terms that bar training on group data.
4. **Contract and regulator overlays.** Each division supplement adds its rules: federal pricing and small business rules for Construction, licensing and responsible charge for A&E, and building safety limits for Property.
5. **Change gate.** A material change (new model, new vendor feature, new data class, new decision role) triggers re-assessment before release. Vendor features that pool data across customers are off by default.
6. **Approved tools only** for workforce generative AI (POL-05 4.8).

**Where the program fell short in 2026.** The standard was adopted after AI-001 grew from a 4-person pilot to about 725 users, after the resume screening pilot started, and after the generative design assistant was in use (scenario gap 6; P01 GR-08). P07 then found a CUI-marked specification in AI-001's tenant (POAM-025). The decisions in section 6 bring these use cases under the standard.

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | AI estimating and bid assistant | Construction (also A&E) | Medium | In production with conditions (about 725 users); expansion paused |
| AI-002 | Jobsite safety computer vision | Construction | High | Pilot at 40 jobsites |
| AI-003 | AI resume screening for craft hiring | Group HR | High | Pilot paused for rejection decisions |
| AI-004 | Generative design assistant | A&E | Medium | Approved for commercial projects |
| AI-005 | Code compliance checking assistant | A&E | High | Pilot, advisory only |
| AI-006 | Lease abstraction | Property | Medium | In production |
| AI-007 | BAS energy optimization | Property | High | In production at 8 properties |
| AI-008 | AP invoice and payment anomaly detection | Group finance | Medium | In production |
| AI-009 | Enterprise generative AI assistant | Group | Medium | Pilot (3,000 users) |

### 2.1 Priority use case: AI estimating and bid assistant (AI-001)
| Item | Description |
|---|---|
| Purpose and intended use | Speed up estimating: (1) quantity takeoff from drawings; (2) unit pricing from the group's historical cost database and the vendor's market data; (3) subcontractor bid leveling (normalizing scope, flagging exclusions, ranking bids); (4) drafting proposal narratives |
| Users / operators | About 640 Construction estimators and 85 A&E cost estimators; preconstruction leads review output |
| Affected parties | Owners (the price they pay), subcontractors (whether they are selected, including small and disadvantaged businesses), the group (fixed-price exposure on about 1,350 active projects) |
| Data | Inputs: drawings and specifications, historical costs, subcontractor bid forms. Outputs: quantities, unit prices, leveled bid tables, recommendations, draft text. Enterprise terms bar training on group data. **The vendor's pooled "market pricing" feature was still enabled in 2026-08** (P07 SA-09c.) |
| Build or buy | Buy: vendor SaaS (enterprise tenant) with a read-only connector to the group cost database |
| Not intended | Submitting bids automatically; selecting subcontractors without an estimator's documented decision; producing certified cost or pricing data without human verification; hiring, discipline, or crew assignment; structural or life-safety quantities; **any CUI** |

**Is the data FCI or CUI?** It depends on the stage and the contract.
- Public solicitation documents posted for all bidders are not FCI (FAR 52.204-21(a) excludes information provided by the Government to the public).
- Drawings and change-order packages on **awarded** federal contracts are FCI. They may be used in AI-001 only if the tool is approved as an external system for FCI (condition 1 in section 6).
- Drawings marked CUI from DoD design-build projects are **never** allowed in AI-001. P07 found one CUI-marked specification uploaded by an A&E cost estimator. It was removed and reported (POAM-025), and A&E federal uploads are now blocked.

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FAR 52.204-21(b)(1)(iii) | **Yes** for FCI | The contractor must "verify and control/limit connections to and use of external information systems" |
| DFARS 252.204-7021(d)(2) | **Yes** on DoD awards with the clause | FCI and CUI may be processed only on systems with the required CMMC status. AI-001 is outside the enclave, so it may never hold CUI, and for FCI it must be inside the Level 1 scope |
| DFARS 252.204-7012(b)(2)(ii)(D) | **Yes** (prohibition) | CUI in a cloud service requires FedRAMP Moderate or equivalent; AI-001 has neither |
| FAR 52.203-2, Certificate of Independent Price Determination | **Yes** on federal bids | The offeror certifies its prices were arrived at independently, without consultation with competitors about prices or the methods or factors used to calculate them. A feature that pools competitors' pricing puts that certification at risk |
| FAR 15.403-4 (certified cost or pricing data) | **When required** | For negotiated actions above the threshold, data must be accurate, complete, and current; AI-derived figures need traceable sources |
| FAR 52.219-8, Utilization of Small Business Concerns | **Yes** on federal jobs | Small businesses, including veteran-owned, service-disabled veteran-owned, HUBZone, small disadvantaged, and women-owned small businesses, must have the maximum practicable opportunity to participate in subcontracts. A ranking that disfavors them works against that policy |
| Sherman Act Section 1 (15 U.S.C. 1) | Indirectly | Bid rigging and price-fixing are illegal; counsel reviews any vendor feature that shares or aggregates pricing across contractors |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims; the claims the group relied on are kept in the procurement file |
| Colorado SB26-189 and other state AI laws | No | No operations in Colorado; AI-001 does not make consequential decisions about individuals |

### 2.2 Division and group use cases: regulator- and contract-specific rules
| Use case | Rules that matter | Implication |
|---|---|---|
| AI-002 jobsite safety computer vision | OSHA duties stay with the employer; employee monitoring notice (counsel; generic); collective bargaining agreements where they apply; Texas TRAIGA at Texas jobsites (intent-based prohibitions) | The tool supports, never replaces, required inspections. If used to discipline workers it becomes an employment use, which the group prohibits |
| AI-003 resume screening | Title VII disparate impact (42 U.S.C. 2000e-2(k)); ADA accommodation duties; Texas TRAIGA | EEOC's AI guidance was removed and disparate-impact enforcement is deprioritized (EO 14281), but statutory liability still exists. The group has no hiring in Colorado, Illinois, New York City, or Connecticut, so their AI employment laws do not apply today (`00_universal-framework/cross-sector/us-cross-sector-obligations.md`); revisit on entry |
| AI-004 generative design; AI-005 code compliance checking | State architecture and engineering licensing rules on responsible charge (generic; they vary by state); adopted building codes; client contracts | The licensed professional who seals the drawings is responsible for every element, whatever tool produced it. Neither tool may receive CUI |
| AI-006 lease abstraction | Lease confidentiality | Commercial tenants only; no decisions about individuals |
| AI-007 BAS energy optimization | Group building systems standard (POL-01 4.13); ventilation requirements in applicable codes (generic) | The service writes setpoints into building systems that sit on flat networks at some properties (POAM-022). It must never reach life-safety interfaces |
| AI-008 AP anomaly detection | FAR 52.232-27(c) prompt payment of subcontractors on federal jobs; POL-01 4.15 | Holds must be cleared quickly so subcontractors are paid on time; the tool supports, never replaces, the call-back rule |
| AI-009 enterprise assistant | POL-04 4.13; POL-05 4.8 | No CUI, no federal bid pricing, no Social Security numbers |

## 3. Risk tiers (repository rubric)
- **High:** AI-002 (can affect physical safety on jobsites), AI-003 (substantial factor in employment decisions), AI-005 (can affect life safety through code review), AI-007 (writes setpoints into building operations).
- **Medium:** AI-001, AI-004, AI-006, AI-008, AI-009. They influence business decisions or outputs a professional relies on, but a human makes the final decision.
- **Low:** none.

**AI-001 is Medium, not High.** It does not make, and is not a substantial factor in, a consequential decision about a person, and it does not affect physical safety: an estimator decides every quantity and every subcontractor selection, and a preconstruction lead approves every bid. It is not Low because it handles FCI and third parties' confidential pricing, influences subcontractor selection, and can lock the group into a losing fixed price.

**Tier is not the same as residual risk.** AI-007 is High tier because it acts on building operations, but P01 rates its residual risk Low (PRP-017) because ventilation and setpoint bounds limit what it can do.

**Re-tier triggers:** AI-001 used for automatic bid submission, automatic subcontract award, hiring, crew assignment, or life-safety quantities (to High); AI-004 used for structural or life-safety design (to High); AI-002 alerts used for discipline (prohibited; would add Employment); AI-007 expanded to properties without segmented networks (re-assessment).

## 4. MEASURE
Results are from monitoring between 2026-05 and 2026-08, the P07 tests, and back-tests.

### 4.1 AI estimating and bid assistant (AI-001)
Back-test on 40 completed bids (15 federal, 25 private) and live monitoring of 410 bid packages (about 3,900 subcontractor bids).

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Takeoff quantity error by trade versus the estimator's final takeoff. Threshold: within 5% for concrete, steel, and drywall; within 10% for other trades | Concrete 3%, drywall 4%, steel 5%; MEP fixture counts 13%; sitework 11%; renovation projects 12% against 4% for new construction | **No** for MEP, sitework, and renovations |
| Safe | No bid leaves without estimator verification and preconstruction lead approval | 100% of sampled bids reviewed; 3 material quantity errors caught at review | Yes |
| Secure and resilient | Vendor assurance; single sign-on and MFA; access limited to enrolled users; information classes enforced | Single sign-on with group MFA in place; vendor holds a SOC 2 Type 1 report only; one CUI-marked file found in the tenant (P07 AC-20b.) | **No** |
| Accountable and transparent | Each AI-derived figure tagged with its source (AI takeoff, cost database, vendor market data) | Tagging in 31% of sampled estimates | **No** |
| Explainable and interpretable | Estimator can see what the model counted and why it suggested a price | Takeoff overlays show counted items; market pricing suggestions do not show their basis | Partial |
| Privacy-enhanced (confidentiality) | No training on group data; deletion on request; no cross-customer pricing features | Enterprise terms bar training and set 30-day deletion; the pooled "market pricing" feature was on until 2026-08 | **No** (fixed by condition 2) |
| Fair, with harmful bias managed | Bid leveling recommendation rate for each subcontractor group divided by the rate for all others, among bids within 5% of the low price. Groups: certified small disadvantaged, women-owned, HUBZone, service-disabled veteran-owned, and first-time bidders to the group. Flag any ratio below 0.8. The heuristic is borrowed from employment selection practice; it is not a legal threshold for subcontracting | Certified small business groups 0.86 to 0.94; **first-time bidders 0.62** | **No.** Disparity flagged (P01 CON-018) |

**Bias finding.** The ranking weights a "historical performance" score. First-time bidders have no history, and the model treats missing history as poor history. Many new firms are small or disadvantaged businesses, so this works against the FAR 52.219-8 policy on federal jobs and narrows the subcontractor base. It is a data problem (missing values), not a certification-status input.

### 4.2 Other High-tier use cases
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-002 safety vision | Detection rate on 600 labeled hazard clips (target 90%); false alerts per camera per day (target under 2) | 87% detection; 3.4 false alerts; detection drops to 71% at night | **No** |
| AI-002 safety vision | Written use limitation (safety only, no discipline) and worker notice at each pilot jobsite | Limitation issued 2026-09; notices posted at 31 of 40 jobsites | **No** |
| AI-003 resume screening | Selection rate ratio by sex and by race and ethnicity (where self-identified) for applicants ranked in the top half; flag below 0.8. Also checks for proxies (zip code, gaps in work history) | Women 0.71; applicants with employment gaps over 12 months 0.64 (possible disability or caregiver proxy) | **No.** Flagged |
| AI-005 code checking | Recall against 300 known code issues seeded in test models (target 95% for egress and fire separation) | Egress 92%; fire separation 88%; accessibility 96% | **No** for egress and fire separation |
| AI-007 BAS optimization | Setpoint and ventilation excursions outside engineer-approved bounds (target 0); comfort complaints | 0 excursions; complaints down 6%; bounds held in the vendor service only, not in the controllers | Partial |

### 4.3 Medium-tier use cases
AI-004 (design options are reviewed by the architect of record; AI-generated elements labeled in 70% of sampled sets, target 100%), AI-006 (critical date accuracy 98.5%; all dates verified by lease administrators), AI-008 (flags cleared within 2 business days 94% of the time), and AI-009 (DLP blocked 46 attempts to paste Social Security numbers in the pilot). Monitoring continues at the Medium-tier cadence.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** drafts only. Estimators verify every major-trade takeoff against the drawings; MEP, sitework, and renovation takeoffs are done manually until the tool meets the thresholds for two quarters. Bid leveling is advisory, and the estimator records the reason for each subcontractor selection. The preconstruction lead signs any federal price certification only after confirming no pooled pricing was used. AI-derived figures in federal change-order pricing carry source tags (FAR 15.403-4 where applicable).
- **AI-002:** the safety manager reviews every alert; no alert is used for discipline.
- **AI-003:** recruiters review every application; the ranking may not reject anyone.
- **AI-005:** licensed reviewers complete the full code review; tool flags are a second check.
- **AI-007:** engineers can switch it off per building; it has no path to life-safety interfaces.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-08, CON-017, CON-018, CON-019, AE-005, AE-006, PRP-016, PRP-017.

**Incident handling:** an AI vendor security incident, a data-use change, or CUI or FCI found in an AI tool follows P08 and POL-03 (CUI in an AI tool is a DoD-reportable incident under POL-03 4.4). A material estimating error in a submitted bid goes to the division president and counsel before award.

**Decommissioning:** each use case has an off switch and a manual fallback that the BIA covers (P05: estimating BP-C06, safety BP-C05, building operations BP-P01). AI-001 stops for federal work if the vendor re-enables pooled pricing or cannot provide a SOC 2 Type 2 report by 2027-06-30.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 estimating and bid assistant | **Continue with conditions; expansion paused** (council, 2026-09-04; board risk committee informed 2026-09-15) | (1) No FCI uploads until the Director of Federal Contracts Compliance approves the tool as an external system under FAR 52.204-21(b)(1)(iii), by 2026-10-31; (2) pooled pricing off and counsel's written confirmation that none reached federal bids, by 2026-10-15 (POAM-019); (3) A&E federal uploads blocked and a CUI marking scan on upload (POAM-025, by 2026-11-30); (4) missing history scored as neutral and the bias check rerun, by 2026-11-30; (5) source tagging in estimates, by 2026-12-31; (6) SOC 2 Type 2 report from the vendor at renewal, by 2027-06-30 |
| AI-002 safety vision | **Continue pilot at 40 jobsites; no expansion** | Worker notices at all pilot sites by 2026-10-31; night detection fixed and detection rate at 90% before expansion; discipline use stays prohibited |
| AI-003 resume screening | **Not approved for rejection decisions** | Remove the employment-gap feature; vendor bias audit and the group's own selection-rate test with ratios at or above 0.8; accommodation process for applicants; council re-review by 2027-01-31 |
| AI-004 generative design | **Approved (commercial projects)** | Label AI-generated elements in 100% of sets and use the sealing checklist by 2026-12-31; no CUI |
| AI-005 code checking | **Continue pilot; advisory only** | Recall at 95% for egress and fire separation before any wider use; never a substitute for licensed review |
| AI-006 lease abstraction | **Approved** | 100% verification of critical dates continues |
| AI-007 BAS optimization | **Continue at 8 properties; no expansion** | Controller-level limits the service cannot override by 2027-03-31; expansion only to properties with segmented building networks (POAM-022) |
| AI-008 AP anomaly detection | **Approved** | Extend to Property AP with the move to the payment factory (POAM-031) |
| AI-009 enterprise assistant | **Approved (pilot, 3,000 users)** | Prohibited for hiring, safety, code compliance, and federal pricing decisions; no CUI |

# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Marine Terminals, Freight Trading, Port Real Estate, corporate) |
| Tier / Vertical | Multi-Sector / Transportation and Warehousing |
| Scope | The group AI governance program: the Group AI Standard, the division use-case inventory, and the regulator-specific rules for the priority use case, the berth and yard optimization service (AI-001), with the trading legal generative AI tool (AI-004) as the second assessed use case |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; the Generative AI Profile (AI 600-1) for AI-004 and AI-008. AI-001 is optimization and prediction, not generative AI |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-31 to 2026-09-04; presented to the board risk committee 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 1 High, 7 Medium, 1 Low) |
| Related risks | P01 GR-09, MT-011, FT-005; POAM-010 |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group General Counsel, Division CySO, Marine Terminals director of engineering, Freight Trading general counsel, Port Real Estate director of building technology. Approves High-tier use cases, safety cases for equipment-moving AI, and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage, vendor connections) |
| Division CySO | Decides whether an AI system is, or connects to, a critical IT or OT system under Subpart F and records it in the Cybersecurity Plan |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-06-15, under POL-01 4.14)
1. **Register before use.** Every AI use case that makes or supports operational, safety, commercial or legal decisions, or that processes Restricted data, is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, bias and fairness testing, notice to affected parties and quarterly monitoring.
3. **Safety case for equipment-moving AI.** No AI system may sequence or command cranes, ASCs, RTGs or yard equipment without a safety case approved by the director of engineering and the council (Marine Terminals supplement MT-S1).
4. **Affiliate neutrality.** AI used in berth, gate or appointment decisions must not favor the group's own divisions (POL-01 4.7; 46 U.S.C. 41106(2)).
5. **Data rules.** No SSI, CUI, FCI, personal information or counterparties' confidential terms in AI tools that are not approved for that data; approved tools must not train on group inputs (POL-04; POL-05 3.7).
6. **Change gate.** A material change (new decision role, automatic execution, new data, new vendor or model type) triggers re-assessment before release.

**Where the program fell short in 2026.** The standard was adopted after two use cases had already changed or started: automatic ASC job sequencing at T5 went live in 2026-03 without a safety case or approval, and trading legal adopted a generative AI tool with counterparties' confidential terms (scenario gap 8). Both are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Berth and yard optimization (SYS-T5) | Marine Terminals | High | Advisory with conditions; automatic ASC sequencing at T5 suspended |
| AI-002 | Gate OCR | Marine Terminals | Medium | In production |
| AI-003 | Crane and ASC predictive maintenance | Marine Terminals | Medium | In production at T1 to T6 |
| AI-004 | Generative AI contract review | Freight Trading | Medium | Suspended for counterparty documents |
| AI-005 | Commodity price and demand forecasting | Freight Trading | Medium | In production |
| AI-006 | Building energy optimization | Port Real Estate | Medium | In production |
| AI-007 | CCTV intrusion analytics | Port Real Estate | Medium | In production |
| AI-008 | Enterprise generative AI assistant | Group | Medium | Pilot (1,500 users) |
| AI-009 | SOC alert triage assistant | Group | Low | Approved |

### 2.1 AI-001 berth and yard optimization: what it does
| Item | Description |
|---|---|
| Purpose | Recommend berth windows and crane splits, yard slots that reduce rehandles, and truck appointment allocations; at T5, sequence ASC yard jobs |
| Users | About 40 vessel and yard planners and customer service staff at T1 to T6; at T5 the equipment control system received sequences directly from 2026-03 to 2026-09-25 |
| Affected parties | Carriers (berth windows), about 4,200 trucking companies and their drivers (appointments), longshore workers and staff in the yard (safety), and competing cargo owners (appointment fairness against the trading affiliate) |
| Data | Inputs: schedules, bay plans, container attributes including hazardous class and weight, yard inventory, equipment status, appointments with driver names. Outputs: plans written to a TOS staging area; at T5 also job sequences to the equipment control system |
| Build or buy | Vendor SaaS, connected through a connector in the TOS account (P04). Vendor SOC 2 report reviewed 2026-02 |
| Not intended | Labor dispatch (the hiring halls dispatch longshore workers), pricing, demurrage |

### 2.2 AI-001: regulator-specific rules
| Rule | What it requires | What it means for AI-001 |
|---|---|---|
| USCG cyber rule, 33 CFR Part 101 Subpart F (N48-49-R01) | Inventory of network-connected systems with critical systems designated (101.650(b)(3)); supply chain measures (101.650(f)(1)-(3)); IT-OT connections logged and monitored (101.650(h)(2)); the Cybersecurity Assessment analyzes all networks and the risk posed by each digital asset (101.650(e)(1)(i)) | The path from SYS-T5 to the T5 equipment control system is an IT-to-OT connection. It must be in the inventory, logged and monitored, covered by vendor notification terms, and analyzed in the T5 Cybersecurity Assessment. The CySO must decide whether SYS-T5 is itself a critical IT system (101.615). **Gap:** the 2026-03 change was not reviewed as a new connection (P07 CM-4; P02 CA-9) |
| Shipping Act, 46 U.S.C. 41106(2) | A marine terminal operator may not give any undue or unreasonable preference or advantage, or impose any undue or unreasonable prejudice or disadvantage, with respect to any person | Berth and appointment recommendations must be explainable on operational grounds. **Gap:** the appointment module treats the reserved slots for the trading affiliate's truckers at T3 and T5 as fixed inputs, so the model carries the preference forward (scenario gap 1; P03 G-070) |
| OSHA marine terminal standards, 29 CFR part 1917 | Safe cargo handling and equipment operation at marine terminals remain the employer's responsibility | An unsafe sequence or stack plan is a workplace hazard whoever proposed it. Automatic execution needs a documented safety case |
| FTC Act Section 5 | Truthful claims | The vendor's accuracy and safety claims relied on in procurement are kept on file; the group makes no AI claims to customers |
| State AI laws (Colorado SB26-189; CPPA ADMT rules) | Consequential decisions about individuals | Not applicable: AI-001 makes no decisions about individuals' employment, credit, housing, insurance, education, health care or government services, and the group has no Colorado or California operations |

### 2.3 AI-004 generative AI contract review: rules and commitments
| Rule or commitment | Implication |
|---|---|
| Counterparty confidentiality clauses in purchase and sale contracts | Uploading counterparties' terms to a service that may retain or use them can breach those clauses. The vendor's standard terms allow use of inputs to improve the service |
| FAR 52.204-21 and 32 CFR 170.19(b) | DoD order terms are FCI; any system that processes FCI must be inside the CMMC Level 1 scope. The tool is not |
| FTC Act Section 5 | Covers the vendor's privacy and accuracy claims; keep them on file |
| POL-04 and POL-05 3.7 | Restricted data only in approved tools that do not train on inputs |

## 3. Risk tiers (repository rubric)
- **High:** AI-001, because it **can affect physical safety or critical infrastructure operations** (rubric). This holds even in advisory mode: in the pilot at other terminals planners caught unsafe recommendations, and at T5 no human was in the loop for ASC sequencing.
- **Medium:** AI-002 to AI-008. Humans make the final decision, but outputs influence operations, commercial decisions or security responses, or the tool handles Restricted data.
- **Low:** AI-009.

**Re-tier and re-assess triggers:** any automatic execution on equipment (AI-001 at any terminal); AI-003 changing required inspection intervals (to High); face recognition in AI-007 (council approval and a privacy review); use of any model for longshore labor decisions (employment).

## 4. MEASURE
Results are from monitoring and reviews between 2026-05 and 2026-08.

### 4.1 AI-001 berth and yard optimization
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Berth plans feasible as issued (tide, draft, crane availability) at least 98% of calls at T1 to T6 | 96.4% (about 690 calls) | **No** |
| Safe (advisory terminals) | Hard-constraint violations in recommendations (hazardous segregation, stack weight and height, reefer plugs) | 11 violations in 4 months, all caught by planners | **No.** Planner vigilance is the only control |
| Safe (T5 automatic sequencing) | Sequences rejected by the equipment control system's safety interlocks; near-miss reports in the ASC block | 37 interlock rejections and 2 near-miss reports (a yard tractor handover conflict at an ASC transfer zone and an ASC stopped by its proximity sensor) since 2026-03; no injuries | **No.** No safety case; interlocks were the last line |
| Secure and resilient | Connector scoped to needed fields; vendor notification terms; IT-OT path logged | Connector key reads all TOS data; vendor contract has no notification clause; the T5 path is logged but was never reviewed | **No** |
| Accountable and transparent | Every approval or override recorded with the planner and a reason | Approvals recorded; overrides recorded without reasons at 4 of 6 terminals | Partial |
| Explainable and interpretable | Planners can see why a window or slot was chosen | Scores shown; reasons unclear for about 1 in 4 berth recommendations | Partial |
| Privacy-enhanced | Minimum data sent; no secondary use | Driver names sent but not needed; contract allows aggregated use of data | Partial |
| Fair, harmful bias managed | See the plan below | Appointment fulfillment at T3 and T5: trading affiliate's truckers 96% vs all others 81%; berth deviation within threshold for all carriers | **No.** Affiliate disparity flagged |

**Bias and fairness testing plan** (supports P01 GR-02 and MT-007; quarterly from 2026-Q4):
| Item | Plan |
|---|---|
| Question | Do recommendations give some carriers, trucking companies or the group's own trading affiliate better berth windows or appointment slots without an operational reason? This is the risk 46 U.S.C. 41106(2) addresses |
| Groups compared | (1) Each carrier service at each terminal. (2) Trucking companies by fleet size (fewer than 10 trucks, 10 to 49, 50 or more). (3) **Truckers working for the trading affiliate versus all others** |
| Metrics | (1) Hours between requested and recommended berth window. (2) Share of appointment requests fulfilled in the requested 2-hour window |
| Thresholds | (1) No carrier service more than 2 hours worse than the terminal average. (2) No group more than 10 percentage points below the best group. **Any advantage for the affiliate above 5 points goes to the Group General Counsel**, whatever the explanation |
| Legitimate factors | Vessel size, contracted berth windows in terminal services agreements, hazardous cargo limits, gate lane capacity. A gap explained by these is recorded, not flagged; reserved slots for one cargo owner are **not** a legitimate factor unless offered on equal terms (POAM-024) |
| Data and owner | TOS appointment and berth history compared with recommendations; run by the director of planning; reviewed by the Group General Counsel's office |

### 4.2 AI-004 generative AI contract review (AI 600-1 risk areas)
| AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Data privacy | Vendor terms: no training on inputs, retention limits, deletion on exit | Standard terms allow service-improvement use; retention 30 days | **No** |
| Confabulation | 50 contracts reviewed by lawyers: clause summaries with a wrong or invented term (target under 2%) | 6% (mostly payment and delivery terms) | **No** |
| Information security (prompt injection) | Crafted counterparty document test | Not done | **No** |
| Value chain and component integration | Vendor security review; SOC report | SOC 2 report received; review not done | Partial |
| Human-AI configuration | Lawyers sign off every summary | In place | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the service proposes; a planner approves berth and yard plans, and customer service approves appointment allocations. An **independent constraint check in the TOS** blocks plans that break hazardous segregation, stack weight or height, or reefer limits (due 2026-11-30). At T5, ASC sequences now go to a planner queue; automatic sequencing returns only with an approved safety case that names the interlocks, test results and the conditions for falling back to advisory mode.
- **AI-004:** lawyers review every output; counterparty documents are excluded until enterprise terms are signed.
- **AI-002 and AI-007:** a clerk or a guard decides every case.

**Security (Subpart F supply chain and segmentation):** scope the AI-001 connector to the fields it needs; add vendor notification terms (101.650(f)(2)); keep the T5 IT-OT path in the inventory, logged and monitored (101.650(b)(3), (h)(2)); include SYS-T5 in the T5 Cybersecurity Assessment.

**Monitoring:** monthly metrics to division owners (feasibility, constraint blocks, interlock rejections, overrides with reasons); quarterly fairness tests and a High-tier report to the council and the board risk committee; P01 risks GR-09, GR-02, MT-011, MT-007, FT-005.

**Incident handling:** an unsafe plan that reaches the yard, or an ASC near miss linked to a sequence, is handled as a safety event and reported to the director of engineering and the FSO. A vendor security incident or suspicious connector activity follows P08 and POL-03, including the 33 CFR 6.16-1 report if a terminal's systems are affected.

**Decommissioning:** each use case has an off switch and a fallback that the BIA already covers (P05: planning works without SYS-T5; gates run on clerk review; contracts are read by lawyers).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 berth and yard optimization | **Continue in advisory mode with conditions** (council, 2026-09-04; board risk committee informed 2026-09-15) | Automatic ASC sequencing at T5 suspended; advisory mode restored 2026-09-25 (POAM-010). Safety case for any return to automatic sequencing by 2026-12-31 and council decision by 2027-01-31. Independent constraint check live by 2026-11-30. Connector scoped and vendor notification terms signed by 2026-12-31. Appointment module stops treating affiliate reserved slots as fixed inputs by 2026-10-31 (POAM-024), then a fairness re-test |
| AI-004 contract review | **Suspended for counterparty documents** from 2026-09-04 | Enterprise terms with no training on inputs and retention limits; prompt injection test; error rate under 2% on a new sample; no FCI. Re-assess by 2026-11-30 (P01 FT-005) |
| AI-002 gate OCR | **Continue** | Misread-rate review by terminal by 2026-12-31; OCR vendor data terms |
| AI-003 predictive maintenance | **Continue** | Data only through the group jump host; never used to extend inspection intervals |
| AI-005 forecasting | **Continue** | Quarterly back-testing reported to the Freight Trading chief risk officer |
| AI-006 energy optimization | **Continue** | Integrator access behind the group jump host (POAM-018) |
| AI-007 CCTV analytics | **Continue** | Face recognition prohibited without council approval |
| AI-008 enterprise assistant | **Continue the pilot** | No SSI, CUI, FCI or customer cargo data; label-based exclusions verified |
| AI-009 SOC triage | **Approved** | Standard monitoring |

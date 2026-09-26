# AI Risk Assessment: Container and Berth Scheduling Optimization

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (marine cargo terminal operator, NAICS 488320) |
| Tier / Vertical | Small / Transportation and Warehousing |
| AI use case | AI-001: berth and yard scheduling optimization service (SYS-12), a vendor SaaS connected to the TOS by API. In pilot in advisory mode since 2026-05 |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook. AI 600-1 does not apply: the service is optimization and prediction, not generative AI |
| Assessor / date | Vessel and Yard Planning Lead with the IT Manager (proposed CySO) and the Security and Safety Manager (FSO), 2026-08-27 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |
| Related risks | P01 R-028 (unsafe or infeasible plan approved) and R-029 (unfair treatment of carriers or trucking companies) |

## 1. GOVERN
- **Accountable owner:** Vessel and Yard Planning Lead (business owner). **Decision authority:** General Manager. Because the use case is tiered High, the majority owner is informed of the decision.
- **Supporting roles:**
  - IT Manager: security review and the API connection
  - FSO: hazardous cargo rules
  - Maintenance Manager: equipment constraints
  - Operations Manager: day-to-day use by planners
- **Policies that apply:**
  - POL-01 4.8: security criteria and notification terms for IT vendors
  - POL-04 4.9: no Restricted, Confidential or SSI data in AI tools that are not approved
  - POL-05 4.9: approved AI tools only
- **Gap: no AI policy.** The pilot started in 2026-05 without a security review or an AI policy (gap 19 in `../scenario-facts.md`). An AI use standard under POL-01, with the approved-tools list kept by the IT Manager, is due 2026-12-31.
- **Scale for a Small company:** there is no AI committee. The Operations Manager, the Vessel and Yard Planning Lead, the IT Manager and the FSO review AI use cases every quarter.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Recommend berth windows and crane splits for vessel calls, yard slots for arriving containers (to reduce rehandles), and truck appointment slot allocations. The aim is better crane productivity and shorter truck turn times |
| Users / operators | 4 vessel and yard planners, who approve or change each recommendation in the TOS; customer service staff, who publish appointment slots |
| Affected people and organizations | 6 carrier services (berth windows); about 350 trucking companies and their drivers (appointment slots); longshore labor and yard staff, who work the resulting plans (safety) |
| Data | **Inputs:** vessel schedules, bay plans, container attributes (size, weight, reefer, hazardous class, discharge port), yard inventory, equipment availability, historical move times, and truck appointments. Appointment records include driver names; driver license numbers are not sent. **Outputs:** recommended plans, written back to a TOS staging area. **Training:** the vendor tunes prediction models on the company's move history. **The contract does not say whether company data is used to train models for other customers** |
| Build or buy | Buy: vendor SaaS (optimization plus machine-learning predictions of dwell and move times), connected by API with a static key. The key has read access to all TOS data and write access to the staging area |
| Deployment context | Advisory mode. Nothing reaches equipment until a planner approves it in the TOS. Planning can run without the service (P05 BP-06) |
| Not intended | Direct dispatch to cranes, RTGs or VMTs; longshore labor ordering; pricing. **Enabling any of these requires re-assessment** |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| USCG cyber rule, 33 CFR Part 101 Subpart F (N48-49-R01) | **Yes** | SYS-12 connects to the TOS, a critical IT system. The CySO must decide in the Cybersecurity Plan whether SYS-12 is itself a critical IT system (101.615). Either way, it must be in the inventory (101.650(b)(3)). Its vendor falls under the supply chain measures: security as a procurement criterion, notice of vulnerabilities and reportable cyber incidents without delay, and monitoring of third-party connections (101.650(f)(1)-(3)) |
| Shipping Act, 46 U.S.C. 41106 | **Yes** | A marine terminal operator may not "give any undue or unreasonable preference or advantage or impose any undue or unreasonable prejudice or disadvantage with respect to any person." Berth windows and appointment slots set with the model's help must be explainable on reasonable operational grounds. The Federal Maritime Commission administers the Act |
| OSHA marine terminal standards, 29 CFR part 1917 | Indirectly | The company remains responsible for safe cargo handling. A plan that breaks stack weight or hazardous cargo segregation rules creates a workplace hazard, whoever proposed it |
| FTC Act Section 5 | Indirectly | Covers the vendor's accuracy and security claims. Keep the claims the company relied on in the procurement file |
| State AI laws (for example Colorado SB26-189) | No | They target consequential decisions about individuals, such as employment and credit. This service makes none, and the company operates only in Florida |
| Fla. Stat. 501.171 | Low exposure | Driver names alone are not personal information under the statute. Keep driver license numbers out of the data sent to the vendor |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal/projects/P10_ai-governance/README.md`). The rubric puts AI that "can affect physical safety or critical infrastructure operations" in the High tier.
- **Safety.** A yard plan can stack containers above weight limits or place incompatible hazardous cargo side by side.
- **Critical infrastructure.** An infeasible berth plan disrupts a port terminal, which is part of the Marine Transportation System.
- **Why advisory mode does not lower the tier:** the planners are a strong control. The pilot shows they are not a sufficient one on their own (section 4).

**Minimum controls for High tier, and status:**
| Minimum control | Status |
|---|---|
| Human review before action | In place: a planner approves every plan |
| Pre-deployment bias testing | Done in the pilot; appointments failed (section 4) |
| Impact assessment | This document |
| Notice to affected people | Due 2026-11-30: tell carriers and trucking companies (portal notice) that AI assists planning, and how to ask for a review |
| Ongoing monitoring | Due 2026-11-30 |

**Escalation triggers (re-assess before any of these):**
- sending plans directly to cranes, RTGs or VMTs without planner approval (this would also bring the service into the OT scope)
- using the model to order or assign longshore labor (an employment-type decision)
- using it to set prices or demurrage
- a change of vendor or model type

## 4. MEASURE
Pilot period: 2026-05-04 to 2026-08-21. The service produced plans for 62 vessel calls and about 1,900 truck appointment requests a week.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | (a) Berth plans feasible as issued (tide, draft, crane availability) at least 98% of calls. (b) Yard rehandles at least 10% lower than the planner-only baseline | (a) 58 of 62 feasible (93.5%). The 4 failures ignored a crane under maintenance or a draft restriction the model had not been given. (b) Rehandles 12% lower where recommendations were followed | **No** for (a); Yes for (b) |
| Safe | Hard-constraint violations in recommendations (hazardous cargo segregation, stack weight and height, reefer plug availability) must be 0 | 4 violations: 3 hazardous segregation conflicts and 1 stack weight breach on a reefer row. All were caught by planners before execution | **No.** The only control is planner vigilance |
| Secure and resilient | Vendor security review; assurance report; least-privilege API access; fallback if the service fails | No security review; no SOC 2 report received yet; static API key with read access to all TOS data; manual planning works as a fallback | **No** (fallback: Yes) |
| Accountable and transparent | Every approval or override recorded with the planner's name and reason | The TOS records who approved a plan, not which recommendations were changed or why | **No** |
| Explainable and interpretable | A planner can see why a berth window or slot was chosen (constraints and scores) | The vendor screen shows scores. Planners say berth window reasons are unclear 3 times out of 10 | Partial |
| Privacy-enhanced | Minimum data sent; no secondary use without consent; deletion at contract end | Driver names are sent but not needed; the contract is silent on training use and deletion | Partial |
| Fair, with harmful bias managed | See the bias testing plan below | Appointment fulfillment: small trucking companies 78% vs large 91% (13 points). Berth deviation: within threshold for all 6 carrier services | **No.** Appointment disparity flagged |

**Bias and fairness testing plan** (supports P01 R-029; quarterly from 2026-Q4):
| Item | Plan |
|---|---|
| Question | Does the model give some carriers or trucking companies worse berth windows or appointment slots without an operational reason? This is the risk that 46 U.S.C. 41106 addresses |
| Groups compared | (1) Each of the 6 carrier services. (2) Trucking companies by fleet size: fewer than 10 trucks, 10 to 49, and 50 or more |
| Metrics | (1) Average hours between the requested and recommended berth window, per carrier service. (2) Share of appointment requests fulfilled in the requested 2-hour window, per fleet size band |
| Thresholds | (1) No carrier service more than 2 hours worse than the average of all services. (2) No band more than 10 percentage points below the best band. A breach triggers a root-cause review within 30 days |
| Controls for legitimate factors | Vessel size, cargo volume, contracted berth windows in the terminal services agreements, and hazardous cargo handling limits. A gap explained by these factors is recorded, not flagged |
| Data and owner | TOS appointment and berth history, compared with the model's recommendations. Run by the Vessel and Yard Planning Lead; reviewed by the Operations Manager |
| Result so far | The appointment gap likely comes from the model favoring large batches that reduce yard moves. Fix: cap batch preference and re-test before appointment recommendations resume |

## 5. MANAGE
**Human-in-the-loop design:**
- The service proposes; a planner approves. No plan reaches equipment, VMTs or the appointment portal without planner or customer service approval in the TOS.
- **An independent constraint check runs in the TOS.** Configured rules check hazardous segregation, stack weight and height, and reefer plug limits, and block approval of a violating plan. It does not rely on the vendor (P01 R-028, due 2026-11-30).
- Crane maintenance status and draft restrictions are sent to the vendor automatically, to prevent the infeasible berth plans seen in the pilot.
- Planners must pick a reason code when they change a recommendation. A second planner checks any plan with hazardous cargo.
- **Kill switch:** the IT Manager can disable the API key at once. Planning then continues by hand (P05 BP-06).

**Security (Subpart F supply chain):**
- Vendor security review and SOC 2 (or equivalent) report by 2026-11-30 (POAM-024).
- Scope the API key: read only the fields needed, and write only to the staging area. Rotate the key quarterly. Add the vendor to the inventory (101.650(b)(3)).
- Contract amendment: notice of vulnerabilities and incidents without delay (101.650(f)(2)); no use of company data to train models for other customers without written consent; data deleted within 30 days of contract end.

**Monitoring:**
- Monthly: feasibility rate, constraint blocks, override rate and reasons, rehandles (P01 R-028).
- Quarterly: the fairness tests above (P01 R-029).
- Complaints from carriers or trucking companies about berth windows or slots go to the Operations Manager, who logs them against the model.

**Incident handling:**
- An unsafe plan that reaches the yard is handled as a safety event under the operations manual and reported to the Operations Manager and the FSO.
- A vendor security incident, or suspicious activity through the API, follows the P08 runbook. That includes the 33 CFR 6.16-1 report if the TOS is affected.

**Decommissioning triggers:**
- Any constraint violation that reaches execution.
- Feasibility below 95% for two months in a row.
- The vendor refuses the contract security terms by 2026-12-31.
- An unexplained fairness breach that persists after one fix.

On exit, the company disables the key, obtains a deletion certificate, and returns planners to manual planning.

## 6. Decision
**Approve with conditions.** General Manager, 2026-09-04; the majority owner was informed the same day. Berth and yard recommendations may continue in advisory mode **only if** these conditions are met by 2026-11-30:
1. The independent constraint check is live in the TOS, and vessel plans with hazardous cargo get a second-planner check.
2. Crane maintenance and draft restrictions are fed to the service.
3. The vendor security review is complete, and the API key is scoped and rotated.
4. Override reason codes and monthly monitoring are running.
5. Carriers and trucking companies have been told that AI assists planning.

**Appointment slot recommendations are suspended from 2026-09-04** until the fairness fix passes a re-test (target 2026-12-31, P01 R-029). Customer service allocates slots by hand until then.

**Other inventory items:**
- **AI-002 (gate OCR):** a review of OCR misread rates is due 2026-12-31. Misreads are resolved by a clerk. License plate images are kept under the OCR vendor contract, which needs data terms (POAM-024).
- **AI-003 (public generative AI chatbots):** allowed for public information only (POL-05 4.9).

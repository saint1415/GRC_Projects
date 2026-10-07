# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed marine cargo terminal operator: Terminal 1, Terminal 2 and an off-dock depot) |
| Tier / Vertical | Mid-Market / Transportation and Warehousing |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. The registry default, container and berth scheduling optimization, is AI-001 and gets the deepest review |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook; the Generative AI Profile (NIST AI 600-1) for AI-005 only. AI-001 to AI-004 are optimization, prediction and computer vision, not generative AI |
| Assessors / date | Director of Planning (AI-001 business review), Director of Maintenance and Engineering (AI-003), Director of Port Security (AI-004), vCISO, Security Manager (alternate CySO) and the OT analyst (security), General Counsel (legal), 2026-08-24 to 2026-09-04 |
| Decision | Chief Operating Officer and vCISO (AI review co-chairs), 2026-09-15; High-tier decisions noted by the CEO |
| Related risks | P01 R-028, R-029 (AI-001), R-044 (AI-002), R-045 (AI-003), R-046 (AI-004), R-039 (AI-005) |

## 1. Summary
The scheduling optimization service (AI-001) moved from pilot to production at T1 in 2026-03 without an AI policy, and two other tools were adopted by departments without a security review (AI-003 crane analytics and AI-004 perimeter video analytics; gap 14). None of the tools moves equipment or decides anything about a person on its own, but two can affect physical safety and terminal operations, so they are High tier:
- **AI-001** recommended 7 plans that broke hard safety constraints (all caught by planners) and showed an unexplained gap in appointment slots for small trucking companies.
- **AI-003** opened an outbound connection from the T1 crane management system to the vendor's cloud, through the OT zone firewall, without a security review.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Berth and yard scheduling optimization | High | Approve with conditions; appointment slot recommendations stay suspended; no T2 expansion until conditions are met |
| AI-002 | Gate OCR | Medium | Approve with conditions |
| AI-003 | Crane predictive maintenance analytics | High | Approve with conditions; T2 connection not allowed |
| AI-004 | Perimeter video analytics | Medium | Approve with conditions; facial recognition prohibited |
| AI-005 | Enterprise generative AI assistant | Low | Approve with conditions |

Tiers: 2 High, 2 Medium, 1 Low.

## 2. GOVERN
- **Accountable for the AI program:** the Chief Operating Officer and the vCISO co-chair AI review. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.13: AI tools approved before use; AI in terminal operations stays advisory and may not move equipment without a human decision.
  - POL-01 4.9: security criteria and notification terms for AI vendors, as for any IT or OT vendor (101.650(f)(1)-(2)).
  - POL-04 4.9: no Restricted, Confidential or SSI data in unapproved AI tools; no training on company data.
  - POL-05 4.9: approved AI tools only; check outputs.
  - STD-09 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Security Manager on the intranet. It lists AI-001 to AI-005 with their conditions. Public chatbots are blocked on company devices from 2026-10-15.
- **Subpart F link.** Every AI service that connects to the TOS or to OT is a network-connected system that must be in the inventory, and the CySO must decide in the Cybersecurity Plan whether it is a critical IT or OT system (101.615; 101.650(b)(3)). The CySO's provisional view: AI-002 is part of a critical IT system (the gates); AI-001 and AI-003 are not critical as long as they stay advisory and operations can run without them (P05).

### 2.1 Proposed lightweight AI governance process
A mid-market terminal operator does not need a standing AI committee with a large charter. It needs a short, reliable gate and a monthly rhythm, using existing roles and meetings.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department that wants an AI tool, or an AI feature turned on in an existing product (for example in the TOS, the CCTV system or the crane management system), submits a one-page intake: purpose, users, data, vendor, decisions and equipment affected | Requesting business owner | 15 minutes |
| 2. Triage | The Security Manager assigns a provisional tier with the P10 rubric and checks the purchasing gate: no purchase order without approval (POL-01 4.9) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist and data terms. **Medium:** security, legal and business review. **High:** full MAP and MEASURE assessment like this one, with an OT security review if the tool touches OT, a safety review by the Director of Maintenance and Engineering or the terminal General Manager, and a fairness plan where customers are affected | Security Manager; General Counsel; business reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the AI review group (COO, vCISO, General Counsel), meeting monthly for 30 minutes. High: the AI review group decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owner reports the agreed metrics monthly; High tier gets a quarterly deep dive; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type, expansion to another terminal, a connection to OT, or a safety event | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. It puts AI that "can affect physical safety or critical infrastructure operations" in the High tier. A port terminal is part of the Marine Transportation System, so planning and crane maintenance tools that could cause unsafe operations or a terminal stoppage are High even in advisory mode.

## 3. MAP
| Item | AI-001 Scheduling | AI-002 Gate OCR | AI-003 Crane analytics | AI-004 Perimeter analytics | AI-005 Assistant |
|---|---|---|---|---|---|
| Purpose | Recommend berth windows, crane splits, yard slots and truck appointment slots | Read container, chassis and plate numbers at the gates | Predict crane component failures from drive and sensor data | Detect people and vehicles crossing perimeter zones | Draft and summarize office documents and email |
| Users | 9 vessel and yard planners at T1; customer service (appointments) | Gate clerks at three gates | 6 maintenance planners | Security control room officers at T1 | 120 office users |
| Affected parties | 9 carrier services (berth windows); about 1,200 trucking companies and their drivers (appointments); longshore labor and yard staff (safety) | Truck drivers; cargo owners | Crane operators, mechanics and longshore labor near cranes | People at the perimeter, including staff and visitors | Recipients of drafted content |
| Data | Vessel schedules, bay plans, container attributes (weight, hazardous class, reefer), yard inventory, equipment status, appointments with driver names | Images and numbers of containers, chassis and plates | Drive, load and vibration telemetry; fault codes; maintenance history | Video at the perimeter (no faces matched, no audio) | Whatever the user can open in the productivity suite |
| Build or buy | Buy (SaaS, API to the TOS) | Buy (models on company OCR servers) | Buy (SaaS with an outbound connector) | Buy (module on company video servers) | Buy (enterprise license) |
| Generative AI? | No | No | No | No | Yes |
| Not intended | Direct dispatch to cranes, RTGs or VMTs; labor ordering; pricing | Release decisions without the TOS hold check | Extending OEM inspection intervals; controlling equipment | Replacing patrols; facial recognition | Use with SSI or in the TOS |

**Applicable laws and rules:**
| Rule | Applies to | Why |
|---|---|---|
| USCG cyber rule, 33 CFR Part 101 Subpart F (N48-49-R01) | All five | Inventory and critical system designation (101.650(b)(3)); security as a procurement criterion, vendor notification and monitoring of third-party connections (101.650(f)(1)-(3)); AI-003's connector must respect IT/OT segmentation and be logged (101.650(h)(1)-(2)) |
| Shipping Act, 46 U.S.C. 41106 | AI-001 | A marine terminal operator may not "give any undue or unreasonable preference or advantage or impose any undue or unreasonable prejudice or disadvantage with respect to any person." Berth windows and appointment slots set with the model's help must be explainable on reasonable operational grounds. The Federal Maritime Commission administers the Act |
| OSHA marine terminal standards, 29 CFR part 1917 | AI-001, AI-003 | The company remains responsible for safe cargo handling and equipment. A plan that breaks stack weight or hazardous cargo segregation rules, or a maintenance decision that relies on a missed prediction, creates a workplace hazard whoever proposed it |
| MTSA facility security, 33 CFR Part 105 | AI-002, AI-004 | AI-002 supports cargo release control (105.265(a)(7)); AI-004 supports the FSP's monitoring measures (105.405(a)(14)), so its performance and limits must be reflected in the FSP and its configuration details are SSI |
| 49 CFR part 1520 (SSI) | AI-004, AI-005 | Camera coverage and detection details are security measure details; SSI must not be entered into AI-005 or disclosed to unauthorized persons (1520.9(a)) |
| Fla. Stat. 501.171 | AI-001, AI-002, AI-004, AI-005 | Names with driver license numbers are personal information; plates alone are not. Biometric data is personal information, so enabling facial recognition in AI-004 would bring new security and breach duties. Keep driver license numbers out of AI-001 and AI-005 |
| FTC Act Section 5 | AI-001, AI-003 | Covers the vendors' accuracy and security claims. The claims the company relied on are kept in the procurement files |

**Laws considered and not applicable:** state AI laws on consequential decisions (for example Colorado SB26-189) target decisions about individuals in areas such as employment, credit, housing and health care. None of these tools makes such a decision, and the company operates only in Florida. This assessment did not identify a Florida statute specific to these AI uses; Florida AI law was not researched beyond that. If AI-001 were ever used to order or assign longshore labor, it would become an employment-type decision and must be re-tiered and re-assessed.

## 4. Risk tiers and minimum controls
**AI-001 and AI-003: High.** Both can affect physical safety and critical infrastructure operations. Advisory mode lowers likelihood but not the tier, because the pilot results show that human review alone is not a sufficient control.

| Minimum control (High tier) | AI-001 | AI-003 |
|---|---|---|
| Human review before action | In place: a planner approves every plan | In place: a maintenance planner reviews every suggestion; OEM intervals remain mandatory |
| Pre-deployment testing, including bias testing where people are affected | Done for berth and yard plans; appointments failed fairness tests (section 5) | Accuracy back-test done by the vendor only; company validation due 2026-12-31 |
| Impact assessment | This document | This document |
| Notice to affected people | Due 2026-11-30: tell carriers and trucking companies (portal notice) that AI assists planning, and how to ask for a review | Due 2026-11-30: brief maintenance staff and longshore crane operators on what the tool does and does not do |
| Ongoing monitoring | Due 2026-11-30 (section 6) | Due 2026-12-31 (section 6) |

**AI-002 and AI-004: Medium.** Each influences an operational decision (a gate transaction, a patrol dispatch), but a person makes the decision and other controls remain (the TOS hold check; patrols and recording). **AI-005: Low.** Internal productivity with no decisions about individuals, provided SSI and personal information stay out (conditions in section 7).

**Re-tier triggers (re-assess before any of these):**
- AI-001: sending plans to cranes, RTGs or VMTs without planner approval; ordering labor; setting prices or demurrage; expansion to T2.
- AI-002: releasing containers on OCR alone.
- AI-003: any change to inspection intervals based on model output; any write path back into the crane management system; connection at T2.
- AI-004: facial recognition or license plate matching against watch lists; reducing patrols because of the analytics.
- AI-005: connection to the TOS, the SSI repository or OT data; use for customer-facing replies.

## 5. MEASURE
Measurement period: 2026-03-02 to 2026-08-21 unless stated.

| Use case | Trustworthy characteristic | Test or metric | Threshold | Result | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Berth plans feasible as issued (tide, draft, crane availability) | At least 98% of calls | 329 of 336 T1 calls (97.9%); failures ignored a crane under maintenance or a draft restriction the model had not been given | **No** |
| AI-001 | Valid and reliable | Yard rehandles versus the planner-only baseline | At least 10% lower | 9% lower where recommendations were followed | **No** (close) |
| AI-001 | Safe | Hard-constraint violations in recommendations (hazardous cargo segregation, stack weight and height, reefer plug availability) | 0 | 7 violations (5 hazardous segregation conflicts, 2 stack weight breaches), all caught by planners before execution | **No** |
| AI-001 | Secure and resilient | Vendor security review; assurance report; least-privilege API access; fallback | All in place | No report (Type 1 expected 2027-Q1); static API key with read access to all TOS data; manual planning works as a fallback | **No** (fallback: Yes) |
| AI-001 | Accountable and transparent | Every approval or override recorded with the planner and a reason | 100% | The TOS records who approved a plan, not which recommendations were changed or why | **No** |
| AI-001 | Explainable and interpretable | Planner can see why a berth window or slot was chosen | Reasons available for every plan | Scores shown; planners found berth window reasons unclear in about 1 of 4 plans | Partial |
| AI-001 | Privacy-enhanced | Minimum data sent; no secondary use; deletion at contract end | All contractual | Driver names sent but not needed; contract silent on training use and deletion | **No** |
| AI-001 | Fair, harmful bias managed | See the fairness testing plan below | Within thresholds | Berth windows: 8 of 9 carrier services within 2 hours of the average; 1 service 2.6 hours worse, of which 1.9 hours is explained by vessel size and contracted windows. Appointments (pilot, 2026-06 to 2026-08): fleets under 10 trucks fulfilled 81% vs 93% for fleets of 50 or more | **No** for appointments; berth gap under review |
| AI-002 | Valid and reliable | Misread rate on a sample of 2,000 gate transactions (2026-08) | No more than 3% needing clerk correction | 2.4% at T1; 4.1% at T2 (older cameras) | Partial |
| AI-002 | Secure and resilient | OCR servers supported and patched | All supported | T2 OCR servers past end of support (R-010) | **No** |
| AI-003 | Valid and reliable | Company validation of predictions against 2025-2026 failure records | Recall of at least 70% for failures with 7 days' warning | Not yet measured by the company; vendor reports 78% on its fleet data | Open (due 2026-12-31) |
| AI-003 | Secure and resilient | Connector reviewed; one-way data flow; logged; vendor assurance report | All true | Outbound connector through the T1 OT zone firewall, two-way protocol, logged by the firewall only; no vendor report | **No** |
| AI-004 | Valid and reliable | Walk tests at 12 perimeter zones (2026-08) and false alarms per shift | All walk tests detected; under 20 false alarms per shift | 11 of 12 detected (1 zone missed at night in heavy rain); 34 false alarms per shift on average | **No** |
| AI-004 | Privacy-enhanced | No facial recognition; video retention 30 days | Both | Both confirmed in the configuration | Yes |
| AI-005 | Privacy-enhanced; secure | Enterprise terms prohibit training on company data; SSI repository excluded from the assistant's index; sensitivity labels enforced | All true | Terms confirmed; SSI repository not yet excluded (sensitivity labels go live with STD-10) | Partial |
| All | Explainable and interpretable | Users can see the basis for each output (constraints and scores; image crop; sensor trend; video clip; sources) | Available | Available for AI-002, AI-003, AI-004 and AI-005; partial for AI-001 | Partial |

**AI-001 fairness testing plan** (supports P01 R-029; quarterly from 2026-Q4):
| Item | Plan |
|---|---|
| Question | Does the model give some carriers or trucking companies worse berth windows or appointment slots without an operational reason? This is the risk 46 U.S.C. 41106 addresses |
| Groups compared | (1) Each of the 9 carrier services at T1. (2) Trucking companies by fleet size: fewer than 10 trucks, 10 to 49, and 50 or more |
| Metrics | (1) Average hours between the requested and recommended berth window, per carrier service. (2) Share of appointment requests fulfilled in the requested 2-hour window, per fleet size band |
| Thresholds | (1) No carrier service more than 2 hours worse than the average of all services after legitimate factors. (2) No band more than 8 percentage points below the best band. A breach triggers a root-cause review within 30 days |
| Legitimate factors | Vessel size and draft, cargo volume, contracted berth windows in the terminal services agreements (including the alliance agreement), hazardous cargo handling limits. A gap explained by these factors is recorded, not flagged |
| Data and owner | TOS berth and appointment history compared with the model's recommendations. Run by the Director of Planning; reviewed by the Vice President, Terminal Operations and the General Counsel |
| Result so far | The appointment gap likely comes from the model favoring large batches that reduce yard moves. Fix: cap batch preference and re-test before appointment recommendations resume. The remaining 0.7-hour berth gap for one service is under root-cause review (due 2026-10-31) |

## 6. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the service proposes and a planner approves. An **independent constraint check in the TOS** (configured rules for hazardous segregation, stack weight and height, reefer plugs) blocks approval of a violating plan, so safety no longer depends on planner vigilance alone (due 2026-11-30). A second planner checks every vessel plan with hazardous cargo. Planners must pick a reason code when they change a recommendation. **Kill switch:** the TOS Application Manager can revoke the API key at once; planning continues by hand (P05 BP-09).
- **AI-002:** a clerk resolves every misread; the TOS hold check, not OCR, decides release.
- **AI-003:** suggestions add inspections; they never remove or delay OEM-required inspections. A maintenance planner approves each work order.
- **AI-004:** an officer assesses every alert; patrols and recording continue. The FSO keeps the analytics' known limits (rain, night) in the FSP monitoring section.
- **AI-005:** users review every output; no automated sending or actions.

**Security (Subpart F supply chain and segmentation):**
- AI-001: scope the API key to the needed fields and the staging area; rotate quarterly; vendor security questionnaire and penetration test summary now, Type 1 report when issued (P09 VEN-07); contract terms for notice without delay, no training on company data for other customers, and deletion within 30 days of exit.
- AI-003: replace the two-way connector with a one-way export (data diode or brokered push from a server in a demilitarized zone between IT and OT); log the flow to the SIEM; vendor assurance report; no connection at T2 until the T2 OT zone exists (R-045).
- AI-002 and AI-004: vendor data terms (image retention, no reuse for model training without consent); updates through the privileged remote access service.
- All: in the inventory with CySO designation in the Plan (101.650(b)(3)).

**Monitoring:**
- Monthly: AI-001 feasibility rate, constraint blocks, override rate and reasons, rehandles; AI-002 misread rate by gate; AI-004 false alarms and missed walk tests; AI-005 blocked uploads of labeled content.
- Quarterly: AI-001 fairness tests; AI-003 prediction validation against actual failures.
- Complaints from carriers or trucking companies about berth windows or slots go to the Director of Commercial and Customer Service, who logs them against the model.
- Results feed the risk register (P01 R-028, R-029, R-039, R-044, R-045, R-046).

**Incident handling:**
- An unsafe plan or a missed failure that reaches the yard or a crane is handled as a safety event under the operations manual and reported to the terminal General Manager and the FSO.
- A vendor security incident, or suspicious activity through an AI connection, follows P08. If it touches crane controllers, use `ir-runbook-ot-vendor-access.md`, including the immediate 33 CFR 6.16-1 report.

**Decommissioning criteria:**
- AI-001: any constraint violation that reaches execution; feasibility below 97% for two months in a row; the vendor refuses the contract terms by 2026-12-31; an unexplained fairness breach that persists after one fix.
- AI-003: the connector is not redesigned by 2027-03-31; recall below 50% in company validation.
- AI-004: missed walk tests in two consecutive quarters after tuning.
- Any tool: the vendor changes data-use terms or the model without notice.
- On exit: revoke keys and connections, obtain a deletion certificate, and return to manual processes.

## 7. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** (advisory mode at T1 only) | Independent constraint check and second-planner check for hazardous cargo (2026-11-30); crane maintenance and draft restrictions fed to the service (2026-11-30); API key scoped and rotated, vendor questionnaire and contract terms (2026-12-31); reason codes and monthly monitoring (2026-11-30); notice to carriers and trucking companies (2026-11-30). **Appointment slot recommendations stay suspended** until the fairness fix passes a re-test (target 2026-12-31). No T2 expansion before 2027-04-01 | COO and vCISO, 2026-09-15; noted by the CEO |
| AI-002 | **Approve with conditions** | Camera upgrade at T2 with the OCR server replacement (2027-03-31); vendor data terms (2026-12-31); quarterly misread report | COO and vCISO, 2026-09-15 |
| AI-003 | **Approve with conditions** (T1 pilot only) | One-way export replaces the connector (2027-03-31); interim: firewall rule limited to the vendor endpoint and logged to the SIEM (2026-10-31); company validation of predictions (2026-12-31); vendor security review and terms; no T2 connection | COO and vCISO, 2026-09-15; noted by the CEO |
| AI-004 | **Approve with conditions** | Tuning and quarterly walk tests; analytics limits recorded in the T1 FSP monitoring section (2026-12-31); facial recognition prohibited | Director of Port Security with the COO, 2026-09-15 |
| AI-005 | **Approve with conditions** | SSI repository excluded from the index and sensitivity labels enforced (2026-12-31, with STD-10); training for users; public chatbots blocked (2026-10-15) | vCISO, 2026-09-15 |

The conditions are tracked as POAM-027 in P07 and in the risk register (P01 R-028, R-029, R-039, R-044, R-045, R-046). The AI review group holds its first monthly meeting on 2026-10-06.

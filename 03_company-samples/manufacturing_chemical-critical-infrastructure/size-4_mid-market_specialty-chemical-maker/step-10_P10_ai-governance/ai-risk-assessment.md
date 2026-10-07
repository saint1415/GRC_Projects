# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed specialty chemical formulator and packager) |
| Tier / Vertical | Mid-Market / Chemical |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv` |
| Framework | NIST AI RMF 1.0 (AI 100-1) with the AI RMF Playbook, and the Generative AI Profile (NIST AI 600-1) for AI-002 and AI-005 |
| Assessors / date | Director of Data and Analytics (models), Information Security Manager (security), Process Safety Manager (process safety), General Counsel (legal), Director of Customer Solutions (AI-004), 2026-08-24 to 2026-09-11 |
| Decision | Chief Operating Officer, 2026-09-22, with the Port Plant Manager for AI-001; High-tier decisions noted by the CEO |

## 1. Summary
Before this assessment, the only AI rule was the acceptable use policy (gap 12). AI-001 and AI-004 went live without a risk assessment, and staff used public generative AI tools. None of the five uses is out of control, and none can act on a control system, but two need conditions before they grow:
- **AI-001, process optimization:** recommendations are not checked against the safe operating limits before an operator sees them, and model changes are outside MOC.
- **AI-004, TTRS replenishment:** creates orders automatically for water utilities with no human review for new tanks, and its forecast error is checked only weekly.

| ID | Use case | Risk tier | Generative AI? | Decision |
|---|---|---|---|---|
| AI-001 | Process-optimization model | **High** (physical safety and critical operations) | No | Approve with conditions; no expansion until met |
| AI-002 | Enterprise generative AI assistant | Medium | Yes | Approve with conditions (fix over-shared files) |
| AI-003 | Predictive maintenance | Medium | No | Approve; accept residual risk (P01 R-042) |
| AI-004 | TTRS demand forecasting and automatic replenishment | **High** (supply to water utilities, which are critical infrastructure) | No | Approve with conditions |
| AI-005 | SDS drafting assistant | Medium | Yes | Approve pilot with conditions |

Tiers: 2 High, 3 Medium, 0 Low. Tiers use the repository rubric (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`); a use case is High if it can affect physical safety or critical infrastructure operations.

## 2. GOVERN
- **Accountable owner for the AI program:** Director of Data and Analytics, with the Information Security Manager for security and the Process Safety Manager for any use that touches process operations. Each use case has a business owner (inventory).
- **Policies:** POL-01 4.14 (approval before use; no AI write path to control systems; human review of safety documents); POL-04 4.3 (no SSI or Restricted data in unapproved AI tools); POL-05 4.6 (approved tools only; output is a draft); STD-07 AI use standard (due 2026-11-30).
- **Approved-tools list:** kept by the Information Security Manager on the intranet. It lists AI-001 to AI-005 with their conditions. Public generative AI sites are blocked by the web filter from 2026-10-15, with an exception process.
- **Change control:** AI-001 model changes go through the plant MOC (40 CFR 68.75; 29 CFR 1910.119(l)) because they change the operating envelope operators are steered toward. AI-004 changes go through the TTRS change process (P09 CC8.1).

### 2.1 Lightweight AI governance process
A mid-market company needs a short, reliable gate and a monthly rhythm, not a large committee. The process reuses existing roles and meetings.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | One-page intake for any new AI tool or AI feature turned on in an existing tool: purpose, users, data, vendor, decisions affected, any connection to OT | Requesting business owner | 15 minutes |
| 2. Triage | Provisional tier with the rubric; purchasing gate (no purchase order without approval, POL-01 4.9) | Information Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, data-use terms, and a business reviewer. **High:** full MAP and MEASURE assessment like this one; any use that touches process operations also gets a process safety review | Information Security Manager; Director of Data and Analytics; Process Safety Manager or business reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Information Security Manager. Medium: the **AI review group** (Director of Data and Analytics, Information Security Manager, Process Safety Manager, General Counsel), 30 minutes a month. High: the review group recommends; the COO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owners report the section 4 metrics monthly; High tier gets a quarterly deep dive; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Yearly, or on a trigger: new feature, model retraining with new data, a new unit or customer group, any proposal to write to a control system, or a safety event | AI review group | Yearly |

**Hard rule:** any proposal to let an AI system write setpoints, recipes, or orders into a control system (closed loop) is a new High-tier use case. It needs a PHA revalidation, an MOC, and a change to the SSP boundary (P02), and the model service would become a critical OT system under the USCG rule (33 CFR 101.615).

## 3. MAP
| Item | AI-001 Process optimization | AI-002 Generative assistant | AI-003 Predictive maintenance | AI-004 TTRS replenishment | AI-005 SDS drafting |
|---|---|---|---|---|---|
| Purpose | Shorter batches and lower energy in Blend Hall 1 and the dilution skid | Drafting and search for office work | Earlier warning of rotating equipment failure | Keep customer tanks supplied without stockouts or overfills | Faster SDS drafts for new formulations |
| Users | Operators and shift supervisors (dashboard); process engineers | 640 office users | 6 maintenance planners | Replenishment engine (automatic); dispatchers | 3 regulatory specialists |
| Affected people | Workers and the community, through process safety | Employees whose data is in reach | Workers, through equipment reliability | 2,400 customers, including 160 water utilities | Workers and customers who rely on SDS hazard information |
| Data | Historian data; recipe parameters (Restricted) | Any file the user can reach | Historian and vibration data | Tank levels; delivery history; weather | Formulations (Restricted); hazard data |
| Build or buy | Build | Buy | Build | Build | Buy |
| Connection to OT | Reads the historian replica one way; output is a dashboard; no write path | None | Reads the historian replica one way | None (ERP orders only) | None |
| Applicable rules | 40 CFR 68.69, 68.75; 29 CFR 1910.119(f), (l) | 49 CFR 1520.9; Fla. Stat. 501.171 | 40 CFR 68.73; 29 CFR 1910.119(j) | TTRS contracts; SOC 2 commitments | 29 CFR 1910.1200(g) |

**Laws considered and not applicable:**
- **State AI laws on consequential decisions** (for example Colorado SB26-189): none of the five uses makes decisions about individuals in employment, credit, housing, insurance, education, health care, or government services. The company does not use AI in hiring or HR decisions. The company operates in Florida, and this assessment did not identify a Florida AI-specific statute that applies to these uses.
- **No federal AI statute** applies to these uses. Federal executive actions on AI (for example EO 14365) do not create obligations for this company.
- **Watch item:** NIST released a concept note for an AI RMF Critical Infrastructure Profile on 2026-04-07. It is not final; the company will review it for AI-001 and AI-004 when published.

### 3.1 AI-001: process safety boundaries
AI-001 recommends setpoints within ranges learned from history. History includes operation near limits during upsets, so a model can learn to recommend values close to, or past, the safe operating limits in the process safety information.

**Findings (2026-08 review of 1,240 recommendations):**
- 11 recommendations (0.9%) were outside the validated recipe range; 2 of them were above the alarm limit for reactor temperature on a sanitation blend. Operators rejected all 11.
- There is no automated check against the safe operating limit table before display.
- The model was retrained twice in 2026 with no MOC and no record of what changed.
- Operators do not log whether they accepted a recommendation, so effectiveness and safety cannot be measured from records.

**Required design (condition 1):**
1. A hard filter that suppresses any recommendation outside the validated recipe range or within 5% of an alarm limit, using the safe operating limit table from the process safety information.
2. Retraining and feature changes go through MOC with Process Safety Manager sign-off and a test on held-out data.
3. Operators record accept or reject on the dashboard (one click).
4. The SIS and the DCS alarm system remain independent of AI-001; no AI-001 output may be used to justify bypassing an alarm or interlock.
5. Training data integrity: the daily row-count and checksum comparison between the historian replica and the data platform (added 2026-09; P04) must pass before a retraining run.

### 3.2 AI-004: automatic orders for critical customers
Water utilities hold 3 to 5 days of treatment chemicals (P05). A missed order can leave a utility short; an over-forecast can send a truck with more product than the tank can hold.

**Findings:** forecast error (mean absolute percentage error over 7 days) was 8% overall but 21% for the 38 tanks added in the last 90 days; 2 near-overfills in 2026 were stopped by drivers checking gauges; there is no daily alerting on forecast drift.

## 4. MEASURE (by use case)
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (2026-08) | Pass? |
|---|---|---|---|---|---|
| AI-001 | Safe | Recommendations outside the validated range or within 5% of an alarm limit shown to operators | 0 (after the filter) | 11 of 1,240 (no filter yet) | **No** |
| AI-001 | Valid and reliable | Cycle-time improvement on accepted recommendations versus matched batches | At least 3%, with no increase in off-spec batches | 4.1% shorter; off-spec unchanged (1.2%) | Yes |
| AI-001 | Accountable and transparent | Model changes under MOC; accept or reject recorded | 100% | 0 of 2 retrainings under MOC; acceptance not recorded | **No** |
| AI-001 | Secure and resilient | No network path to OT; training data integrity checked | Both true | No path (verified in P07 SC-7 test); integrity check added 2026-09 | Yes |
| AI-002 | Privacy-enhanced | Assistant cannot surface SSI or formulations to users without a need to know | 0 hits in a test of 20 prompts by a non-privileged user | 6 of 20 prompts surfaced FSP or formulation excerpts | **No** |
| AI-002 | Valid and reliable (GAI: confabulation) | Sample of 30 summaries checked by the document owner | Material errors under 5% | 1 of 30 (3%) | Yes |
| AI-003 | Valid and reliable | Precision and recall of failure flags against work orders | Recall at least 60%; false alarms under 50% | Recall 64%; false alarms 58% | Partial |
| AI-003 | Safe | No mechanical integrity task deferred because of a model output | 0 | 0 in a review of 40 work orders | Yes |
| AI-004 | Valid and reliable | Forecast error (7-day MAPE) overall and for tanks added in the last 90 days | Under 10% overall; under 15% for new tanks | 8% overall; 21% new tanks | **No** |
| AI-004 | Safe | Orders that would exceed tank capacity at delivery | 0 reaching the customer | 2 near-overfills stopped by drivers | **No** |
| AI-004 | Fair, harmful bias managed | Stockout rate by customer segment (water utilities, pulp and paper, food plants) and by tank age | No segment above 2 times the overall rate | Water utilities 0.4%, overall 0.3%; new tanks 1.1% | **No** (new tanks) |
| AI-005 | Valid and reliable (GAI: confabulation) | Drafts checked against the hazard classification by a regulatory specialist; material errors (hazard class, signal word, precautionary statements, exposure limits) | 0 released; error rate tracked | 31 drafts: 4 material errors, all caught at review | Yes (review works); tracked |
| AI-005 | Privacy-enhanced (data use) | Contract prohibits training on company formulations | Contractual | No-training terms not yet signed | **No** |
| All | Explainable and interpretable | Users can see why: top contributing variables (AI-001, AI-003, AI-004), source documents (AI-002, AI-005) | Available | Available for all except AI-004 order explanations in dispatch | Partial |

**Fairness note.** The AI RMF "fair, with harmful bias managed" characteristic is applied where people or customer groups can be treated differently: AI-004 (customer segments and new tanks). AI-001, AI-003, and AI-005 do not make decisions about people, so fairness testing is replaced by safety and accuracy testing.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** advisory; operators enter changes by hand within safe limits; shift supervisor approval and MOC for anything outside the validated range; filter blocks unsafe suggestions.
- **AI-002:** the user reviews every output; no automated sending or filing.
- **AI-003:** planners decide; mechanical integrity inspections and tests run on their own schedule regardless of the model.
- **AI-004:** automatic orders continue for established tanks; for the first 60 days of each new tank, dispatch reviews each order; daily drift alerts; capacity hold for any order above 100% of free tank volume (tightened from 120%).
- **AI-005:** a regulatory specialist signs every SDS; the AI draft is never published directly.

**Monitoring:** owners report section 4 metrics monthly to the AI review group; AI-001 and AI-004 get a quarterly deep dive. Results feed the risk register (P01 R-038 to R-043).

**Incident handling:** an AI-001 recommendation that contributes to a process deviation is investigated under the RMP and PSM incident investigation procedures (68.81; 1910.119(m)). A security incident involving any model service follows P08 runbook 2. An AI-004 stockout at a water utility is handled as a customer incident under the TTRS contract.

**Decommissioning criteria:**
- AI-001: switch off the dashboard if the safety filter is not live by 2026-12-31, or if any unsafe recommendation passes the filter.
- AI-004: return new tanks to manual ordering if new-tank error stays above 15% for 2 months after the changes.
- AI-005: stop entering new formulations if no-training terms are not signed by 2026-11-30.
- Any tool: stop if the vendor changes data-use terms without notice.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions**; no expansion to the Peroxide Unit or the Ammonia Unit storage area until met | Safety filter (2026-12-31); MOC for retraining (from 2026-10-01); accept or reject logging (2026-11-30); quarterly review with the Process Safety Manager | COO and Port Plant Manager, 2026-09-22; noted by the CEO |
| AI-002 | **Approve with conditions** | Restrict SSI and formulation shares (2026-11-30, POAM-017); approved-tools list and web filter (2026-10-15) | COO, 2026-09-22 |
| AI-003 | **Approve**; residual risk accepted | Quarterly performance report; mechanical integrity independence confirmed yearly | COO, 2026-09-22 (P01 R-042) |
| AI-004 | **Approve with conditions** | Daily drift alerts and new-tank review (2026-11-30); capacity hold tightened (2026-10-31); order explanations in dispatch (2026-12-31); validation evidence for SOC 2 PI1.3 | COO, 2026-09-22; noted by the CEO |
| AI-005 | **Approve pilot with conditions** | No-training contract terms (2026-11-30); SDS review checklist and sign-off record (2026-12-31) | COO, 2026-09-22 |

The conditions are tracked as POAM-020 in P07 and in the risk register (P01 R-038 to R-043). The AI review group holds its first monthly meeting on 2026-10-13.

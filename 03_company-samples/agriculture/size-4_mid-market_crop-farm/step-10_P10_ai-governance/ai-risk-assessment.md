# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed diversified precision-agriculture crop farm with a central packinghouse and a Grower Services unit) |
| Tier / Vertical | Mid-Market / Agriculture, Forestry, Fishing and Hunting |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. The registry use case, computer-vision crop yield prediction, is AI-001 |
| Framework | NIST AI RMF 1.0 (AI 100-1), with the Generative AI Profile (NIST AI 600-1) for AI-005. AI-001 to AI-004 are computer-vision or predictive models, not generative AI |
| Assessors / date | Precision Agriculture Manager (business owner of the portfolio), vCISO and Security Manager (security), Director of Irrigation and Water Resources (OT), HR Director (worker impact), Vice President of Grower Services (grower impact), 2026-08-24 to 2026-09-08 |
| Decision | Chief Operating Officer, 2026-09-15; High-tier decisions noted by the Chief Executive Officer |

## 1. Summary
All 5 AI tools or features were adopted by departments without a security or privacy review (gap 7 in `../00_company-facts.md`). None is out of control, but two act on the physical world or on people's work without enough human checks:
- **AI-002, automatic irrigation scheduling,** sends schedules to 12 Farm 3 pivots with no plausibility limits or approval. Three automatic schedules after soil probe faults ran far above the agronomist's recommendation.
- **AI-001, yield prediction,** is now an input to H-2A job order and crew-hour planning, and it is biased by strawberry variety and early-season stage.

Two more affect money and chemicals:
- **AI-004, optical grading,** feeds grower settlements with no independent check, and it downgrades one older tomato variety more than hand graders do.
- **AI-003, targeted spraying,** is well bounded by the label rate the operator sets, but nobody checks its misses.

**AI-005,** staff use of public chatbots, is replaced by an approved enterprise assistant from 2026-10-01.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Computer-vision crop yield prediction | **High** | Approve with conditions; no job order or crew-hour change from the model alone |
| AI-002 | FMIS irrigation scheduling with automatic application at Farm 3 | **High** | Approve with conditions; daily approval until plausibility limits are proven |
| AI-003 | Camera-based targeted spraying | Medium | Approve with conditions |
| AI-004 | Packinghouse optical grading (feeds grower settlements) | Medium | Approve with conditions; independent grade audit before each settlement |
| AI-005 | Enterprise generative AI assistant | Low | Approve; consumer chatbots blocked |

Tiers: 2 High, 2 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Precision Agriculture Manager, supported by the vCISO. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.13: AI tools and AI features must be approved before use; no AI acts automatically on irrigation, spraying, or settlements without the controls set here.
  - POL-04 4.10: company and grower data go only to AI services with no-secondary-use and deletion terms; POL-04 4.5: no Restricted data in unapproved tools.
  - POL-05 4.9 and 4.10: drone imagery for crop analysis only, never to watch workers; approved tools only; AI outputs checked by a person unless approved here.
  - STD-05 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Security Manager on the intranet. Today it lists AI-001 to AI-005 with their conditions.

### 2.1 Lightweight AI governance process
A mid-market farm does not need a standing AI committee with a large charter. It needs a short gate before anything is switched on, and a monthly rhythm afterwards, using existing roles.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature turned on in equipment or software it already has (for example "auto-apply" in the FMIS or a new grader model), submits a one-page intake: purpose, users, data, vendor, decisions or equipment affected | Requesting business owner | 15 minutes |
| 2. Triage | Security Manager assigns a provisional tier with the repository rubric and checks the purchasing gate (POL-01 4.9) | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, data terms, and a business reviewer. **High:** full MAP and MEASURE assessment like this one, including a bias and performance plan, and an OT safety review if the AI can move equipment | Security Manager; vCISO; business reviewer; Director of Irrigation for OT | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (Precision Agriculture Manager, vCISO, HR Director, and the owner of the affected process), 30 minutes monthly. High: the AI review group recommends; the COO decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owners report the agreed metrics monthly; incidents go to P08 (`ir-runbook-ot-integrity.md` for AI-002 and AI-003) | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type, new crop or farm, automatic action switched on, or a safety or settlement event | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. Re-tier triggers are listed for each use case in section 3.

## 3. MAP
| Item | AI-001 Yield prediction | AI-002 Auto irrigation | AI-003 Targeted spraying | AI-004 Optical grading | AI-005 AI assistant |
|---|---|---|---|---|---|
| Purpose | Weekly block yield estimates 1 to 3 weeks ahead | Set pivot run times from soil moisture and weather, and send them automatically | Turn nozzles on only where weeds are detected | Grade tomatoes and peppers by color, size, and defects | Drafting, summaries, and translation for office staff |
| Users | Precision agriculture team; Farm Managers; HR (job orders); sales desk | Farm 3 irrigation lead; IOC operators | 6 sprayer operators | Packinghouse line leads; settlement analysts | About 120 office users |
| Affected people | Up to 370 H-2A workers and crews (hours offered); growers (expected volumes); people incidentally in images | Farm 3 crops; groundwater; operators at pivots | Crops; handlers and workers re-entering sprayed fields | About 30 contract growers (payments); retail customers (grade specs) | Workers, growers, and customers who receive drafted messages |
| Data | Drone imagery; block boundaries; variety; historical yields (block totals, never per-worker) | Soil probes; weather; crop stage; flow history | Camera images processed on the machine; as-applied maps | Fruit images; grades by lot and grower | Office documents; Restricted data prohibited |
| Build or buy | Buy (SaaS) | Buy (FMIS feature, configured) | Buy (embedded in sprayers) | Buy (grader vendor models) | Buy (enterprise SaaS) |
| Acts automatically? | No (advice) | **Yes, on 12 pivots** | Yes, within the operator's label rate | **Yes, grades flow into settlements** | No |
| Applicable rules | 20 CFR 655.122(i) and (j)(1) (indirect); 14 CFR Part 107 | Water use permit conditions | 7 U.S.C. 136j(a)(2)(G); 40 CFR 170.311(b)(1)(iii) | 7 CFR 46.32(b); marketing agreements | Fla. Stat. 501.171(2); AI 600-1 (guidance) |

**Laws considered and how they apply:**
- **H-2A three-fourths guarantee (20 CFR 655.122(i)) and hours-offered records (655.122(j)(1)).** A forecast cannot lower the guarantee or the recorded hours offered. If AI-001 over-forecasts, the company may recruit and plan more hours than fruit allows and then cut hours at short notice; if it under-forecasts, too few workers are requested. Workers bear the first effect. That is why AI-001 is High while it shapes job orders.
- **FIFRA (7 U.S.C. 136j(a)(2)(G))** makes it unlawful to use a registered pesticide in a manner inconsistent with its labeling. AI-003 can only switch nozzles off within the rate the operator sets, so it cannot cause an over-label application by itself; its as-applied maps support the WPS description of the treated area (40 CFR 170.311(b)(1)(iii)).
- **PACA (7 CFR 46.32(b)).** As growers' agent, the company must record the results of grading and render accurate and detailed accountings. Grades from AI-004 are part of that accounting, so their accuracy is a legal duty, not only a quality goal.
- **Water use permits.** AI-002 withdrawals count against the Farm 3 wells' permitted quantities and appear in the monthly reports (P05 BP-14).
- **Fla. Stat. 501.171.** Drone images of people are not "personal information" unless linked to a name and a listed data element; POL-05 4.9 keeps it that way. For AI-005, entering personal information into an unapproved tool would undercut the "reasonable measures" duty in 501.171(2).
- **State AI laws such as Colorado SB26-189 (effective 2027-01-01):** not applicable. The company operates only in Florida, and this assessment did not identify a Florida AI statute that applies to these uses. Colorado's law covers consequential decisions such as employment for businesses operating in Colorado; it is noted because AI-001 touches employment planning.
- **Sector AI rules for agriculture:** none identified in the vertical overlay.

### 3.1 Re-tier triggers
- **AI-001:** any automatic link to job orders, crew scheduling, or hour cuts (stays High); use in crop insurance or USDA program reports (not allowed).
- **AI-002:** extending automatic application beyond the 12 approved pivots, to drip zones at Farms 1 and 2, or to fertigation injection (never allowed without a new assessment).
- **AI-003:** any feature that raises the rate above the operator's setting, or spot application of insecticides near workers (re-tier to High).
- **AI-004:** use of grades to set grower credit terms or contract renewals (re-tier to High); a new grader model.
- **AI-005:** connection to HR, payroll, or grower systems; use for decisions about people.

## 4. MEASURE (by use case)
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (2025-26 season and 2026-08 tests) | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Mean absolute percentage error (MAPE) of 1-week-ahead block estimates against tally totals | 15% or less | Strawberries 12%; tomatoes 14%; watermelons 26% (canopy hides fruit) | **Strawberries and tomatoes yes; watermelons no** |
| AI-001 | Fair, harmful bias managed | Signed error by subgroup (strawberry variety; season stage early, peak, late; farm). Flag any subgroup whose mean error differs from the overall mean by more than 5 points | No flagged subgroup | Overall +3%. Newer strawberry variety +13%: **flagged**. December (early season) -11%: **flagged**. Farms within 3 points | **No** |
| AI-001 | Accountable and transparent | Decision log for each job order, crew-hour, or volume decision that used an estimate | 100% logged | No log; the 2026-27 H-2A job order request used the model's season forecast | **No** |
| AI-001 | Privacy-enhanced | No secondary use of company or grower data without opt-in; imagery retention limit; people not analyzed | All contractual | Click-through terms allow secondary use (R-028); imagery kept indefinitely; vendor confirms it does not detect people | **No** |
| AI-001 | Explainable and interpretable | Detection overlays allow spot checks image by image | Available | Available; used in 15 of 24 weeks | Yes |
| AI-002 | Safe; valid and reliable | Automatic schedules above 150% or below 50% of the agronomist's recommended depth | 0 | 3 of 61 automatic schedules (April to June 2026) ran at 160% to 210% after soil probe faults; no crop loss; 1 day of extra withdrawal at 2 wells | **No** |
| AI-002 | Secure and resilient | Schedules reach pivots only through the manufacturer's cloud; who can change model settings | Named users with MFA; vendor access on request | 4 named users; pivot manufacturer support account has standing access (R-014) | **No** |
| AI-002 | Accountable and transparent | Each automatic schedule traceable to inputs, model version, and approver | 100% | Inputs and model version stored in SYS-01; no approver | Partial |
| AI-003 | Valid and reliable | Weekly scout check: weeds missed per 100 m of row on targeted passes | 5 or fewer | No checks done before 2026-08; first 4 checks: 2, 3, 7, and 4 (the 7 was at dusk) | Partial: no dusk spraying until retested |
| AI-003 | Safe | Applied rate never above the operator's setting; as-applied maps match the record | 100% | 20 passes compared: rate never above setting; maps match SYS-01 records | Yes |
| AI-004 | Valid and reliable | Weekly hand-grade audit of 100 fruit per grower lot; misgrade rate | 3% or less | 2026-08 audit of 24 lots: 2.6% overall | Yes (overall) |
| AI-004 | Fair, harmful bias managed | Misgrade rate by grower and by variety. Flag any grower or variety more than 2 points above the overall rate | No flagged group | One older tomato variety grown by 4 growers: 6.1% misgrade, mostly downgrades from first to second grade (estimated $0.38 per box under-paid) | **No** |
| AI-004 | Accountable and transparent | Grower can see grade images and dispute a lot | Dispute process in place | No dispute process; images kept 14 days | **No** |
| AI-005 | Privacy-enhanced | No-training and deletion terms; data loss prevention blocks Social Security and passport number patterns; consumer chatbots blocked | All in place | Terms signed 2026-09-10; blocking and data loss prevention rules tested with 20 prompts (all blocked) | Yes |
| AI-005 | Valid and reliable (information integrity, AI 600-1) | Spanish translations of worker notices reviewed by a fluent reviewer | 100% reviewed | Process written; not yet used | Monitor |

**Bias findings and why they matter to people.**
- **AI-001:** over-estimates the newer strawberry variety and under-estimates December yields. Over-estimates lead to planning more crew hours than there is fruit, then cutting hours at short notice; the job order uses season totals, so a 13% bias on a third of the strawberry acreage matters. The HR Director will not size the 2027-28 job order from the model, and weekly crew planning uses hand-count calibration for the new variety.
- **AI-004:** downgrades one older tomato variety. Four growers who grow it were under-paid by about $0.38 per box in the sampled weeks. The Vice President of Grower Services will re-grade a sample of their 2026 spring lots with hand graders and correct settlements where the difference exceeds the agreed tolerance, then ask the vendor to retrain the model on that variety.

**Worker-impact check (process, not model).** When a forecast change reduces planned hours, the Farm Manager compares hours offered per worker across crews each week. A difference of more than 10% between crews is reviewed, and hours offered are recorded as 20 CFR 655.122(j)(1) requires.

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** advice only. Each block estimate used for a crew or sales decision is checked against hand counts on 3 sample plots; retail commitments are capped at 85% of the estimate unless hand counts confirm it; no job order, crew-hour cut, or worker-count decision is made from the model alone, and each decision is logged.
- **AI-002:** plausibility limits in SYS-01 (run time between 50% and 150% of the agronomist's recommendation, and below each well's permitted daily volume); any schedule outside the limits stops and waits for approval; daily approval by the Farm 3 irrigation lead until 8 consecutive weeks pass without a limit breach; fall back to the last approved schedule when a soil probe reports a fault. AI-002 never controls fertigation injection.
- **AI-003:** the operator sets product and rate within the label and can switch to broadcast; weekly scout checks; no dusk or night targeted passes until the miss rate is retested.
- **AI-004:** weekly hand-grade audit per grower; grader output reconciled to packed cases before settlement (POAM-023); Controller reviews each settlement run; growers can dispute a lot within 7 days, with grade images kept 30 days.
- **AI-005:** users review every output; notices to workers or growers, and their translations, are reviewed by HR or Grower Services and counsel before sending.

**Monitoring:** owners report the section 4 metrics monthly to the AI review group. High-tier items (AI-001, AI-002) also get a quarterly deep dive with the COO. Results feed the risk register (P01 R-028 to R-033, R-047).

**Incident handling:**
- A security or data incident at an AI vendor follows P08 and the vendor terms.
- A faulty automatic action by AI-002 (or an AI-003 fault that could affect a pesticide application) follows `ir-runbook-ot-integrity.md`; AI-002 returns to recommendation mode until the cause is fixed.
- A grading error that changes settlements is corrected with the affected growers and recorded in the settlement records (7 CFR 46.32(b)).

**Decommissioning criteria:**
- AI-001: stop and request deletion of company and grower data if the vendor has not signed data-use terms (no secondary use without opt-in, deletion within 30 days of exit, notice of model changes) by 2026-10-31; stop using it for any crop whose MAPE exceeds 20% for two consecutive months.
- AI-002: return all pivots to recommendation mode if a limit breach causes crop damage or a permit exceedance, or if the vendor changes the model without notice.
- AI-004: switch settlements to hand-grade sampling if the overall misgrade rate exceeds 5% for 2 consecutive weeks.
- Any tool: stop if the vendor changes data-use terms or the model without notice.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | Data-use terms signed (2026-10-31); vendor account behind company single sign-on (2026-10-31); imagery retention of 3 seasons and deletion of images showing people when not needed (from 2026-10, P04); hand-count calibration of the new strawberry variety and no December estimates for crew planning; decision log; no job order sizing from the model alone (2026-12-31); watermelons advisory only | COO, 2026-09-15; noted by the CEO |
| AI-002 | **Approve with conditions** | Plausibility limits and fallback configured (2026-11-30); daily approval from 2026-10-01 until 8 clean weeks; pivot manufacturer support access on request only (POAM-003, POAM-016); no extension beyond the 12 pivots without re-assessment | COO, 2026-09-15; noted by the CEO |
| AI-003 | **Approve with conditions** | Weekly scout checks; no dusk passes until retested (2026-10-31); vendor model change notices through the dealer (2027-03-31) | Precision Agriculture Manager, 2026-09-15 |
| AI-004 | **Approve with conditions** | Weekly hand-grade audit and reconciliation (2026-11-30); re-grade and correct the 4 affected growers' spring lots (2026-12-31); dispute process and 30-day image retention (2026-12-31); vendor retraining for the older variety | COO, 2026-09-15 |
| AI-005 | **Approve** | Enterprise assistant only; consumer chatbots blocked on company devices; no Restricted data; review of outputs (POL-05 4.10) | Security Manager, 2026-09-15 |

The conditions are tracked as POAM-024 in P07 (with POAM-023 for AI-004) and in the risk register (P01 R-028 to R-033). The AI review group holds its first monthly meeting on 2026-10-06.

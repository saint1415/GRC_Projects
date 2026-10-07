# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed meat processor with two USDA-inspected plants) |
| Tier / Vertical | Mid-Market / Food and Agriculture |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. AI-001, AI quality inspection on processing lines, is assessed in depth |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook, with the Generative AI Profile (NIST AI 600-1) for AI-004 only |
| Assessors / date | VP FSQA and the Plant 1 FSQA Manager (food safety), Controls Engineering Manager (OT), vCISO and Security Manager (security), HR Director and General Counsel (AI-005), 2026-08-17 to 2026-09-04 |
| Decision | Chief Operating Officer, 2026-09-04 (Medium and Low); Chief Executive Officer, 2026-09-15 (High tier: AI-001 and AI-005) |

## 1. Summary
Three AI systems reached production without a review (gap 13): the vision inspection system on Plant 1 Lines 5-7, the ERP's forecasting module, and the applicant ranking feature the HR SaaS vendor turned on by default. None is out of control, but each needed conditions:
- **AI-001, AI vision inspection:** useful as a supplemental check, but its relationship to the x-ray and metal detection CCP was never written down, its vendor updates models without notice, and it misses foreign material on bacon more often than on other products.
- **AI-005, applicant ranking:** a consequential employment decision tool that nobody chose. It was disabled on 2026-08-20.
- **AI-002 and AI-003** are advisory and stay in production with monitoring. **AI-004** is a proposed enterprise assistant that gives staff a safe alternative to public tools.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | AI quality inspection on Plant 1 Lines 5-7 | High | Approve with conditions; supplemental only; Plant 2 pilot on hold |
| AI-002 | ERP demand forecasting | Medium | Approve with monitoring |
| AI-003 | Refrigeration predictive maintenance analytics | Medium | Approve; advisory only; may not change PSM inspection intervals |
| AI-004 | Enterprise generative AI assistant | Low | Approve the pilot with data rules |
| AI-005 | Applicant ranking in the HR SaaS | High | Keep disabled; retired from the inventory unless a new assessment approves it |

Tiers: 2 High, 2 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** VP FSQA for AI that touches food safety (AI-001); the Chief Operating Officer for the portfolio, supported by the vCISO. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.14: AI systems that affect food safety, process control, people decisions, or Restricted data must be approved before use.
  - POL-04 4.8: no Restricted or Confidential data in unapproved AI tools.
  - POL-05 4.7: approved tools only; human review of consequential output.
  - POL-01 4.6: any change to AI-001 that affects a CCP or an inspection step goes through OT change control with FSQA sign-off.
  - STD-09 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the GRC Analyst. It lists AI-001 (Plant 1 Lines 5-7, conditions in section 6), AI-002, AI-003, and the AI-004 pilot. It lists no public generative AI tool.

### 2.1 Lightweight AI governance process
A mid-market company needs a short, reliable gate and a monthly rhythm, not a large committee. The process reuses existing roles and meetings.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature turned on in an existing tool, submits a one-page intake: purpose, users, data, vendor, decisions affected | Requesting business owner | 15 minutes |
| 2. Triage | The GRC Analyst assigns a provisional tier with the rubric and checks the purchasing gate (POL-01 4.9). **Vendor release notes are checked monthly for AI features turned on by default** (the AI-005 lesson) | GRC Analyst | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, data terms, and a business reviewer. **High:** a full assessment like AI-001 below, with a performance and bias plan; FSQA review for anything near a CCP; counsel review for anything about people | GRC Analyst; Security Manager; VP FSQA or HR Director; General Counsel | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (COO, VP FSQA, vCISO, HR Director), 30 minutes a month. High: the AI review group recommends, the CEO decides | As listed | Monthly |
| 5. Monitor | Owner reports agreed metrics monthly (Medium and High); incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model update, new line or plant, new data type, or a safety event | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`.

## 3. MAP
| Item | AI-001 Vision inspection | AI-002 Forecasting | AI-003 Predictive maintenance | AI-004 Assistant | AI-005 Applicant ranking |
|---|---|---|---|---|---|
| Purpose | Divert packs with foreign material, seal defects, or label and lot-code errors | Weekly demand forecasts for planning and purchasing | Score compressor and evaporator health; recommend maintenance | Drafting and summarizing for office staff | Rank applicants for hourly production jobs |
| Users | Line 5-7 operators and QA technicians, 2 shifts | 4 production planners | Refrigeration technicians at Plant 1 | 40 office users (pilot) | 3 recruiters |
| Affected people | Consumers (indirectly); workers whose hands appear in images | None directly | None directly (workers and neighbors only if maintenance were neglected) | None | About 2,500 applicants a year |
| Data | Product and label images; lot codes | Sales and promotions | Equipment telemetry | Internal documents up to Confidential | Resumes and application answers |
| Build or buy | Buy (vendor models on edge servers; retraining in the vendor cloud) | Configure (ERP module) | Buy (vendor analytics) | Buy (enterprise license) | Configure (vendor feature) |
| Generative AI? | No | No | No | Yes | No |

**How AI-001 relates to food safety controls.** The x-ray units and metal detectors are the foreign material CCP in the Plant 1 HACCP plan and stay unchanged. AI-001 is **not** a CCP monitoring device and is not part of the HACCP plan. Its deployment in 2025-09 changed the inspection step, so it should have triggered a documented decision on whether the HACCP plan needed reassessment ("changes in ... processing methods or systems", 9 CFR 417.4(a)(3)(i)). That decision is now documented (condition 1). Using AI-001 *as* CCP monitoring, or reducing manual inspection because of it, would be a change that requires reassessment and validation (417.4(a)(1), (a)(3)).

**Laws considered:**
| Rule | Applies? | Why |
|---|---|---|
| FSIS HACCP (9 CFR Part 417) | **Indirectly (AI-001)** | Not a CCP today; any change to its role triggers reassessment |
| FSIS recall notice (9 CFR 418.2) | **Yes, as a consequence (AI-001)** | A missed defect or label error that reaches commerce can be adulteration or misbranding and trigger the 24-hour notice |
| OSHA PSM and EPA RMP inspection frequency (29 CFR 1910.119(j)(4)(iii); 40 CFR 68.73(d)(3)) | **Indirectly (AI-003)** | Inspection and test frequency must follow manufacturers' recommendations and good engineering practice. AI-003 may add inspections, never remove them |
| Title VII disparate impact (42 U.S.C. 2000e-2(k)); Uniform Guidelines (29 CFR 1607.4(D)) | **Yes (AI-005)** | An employer is responsible for the selection tools it uses, including vendor tools. The four-fifths rule is the federal enforcement agencies' general measure of adverse impact |
| FTC Act Section 5 | Indirectly | Applies to vendors' accuracy claims; the procurement files keep the claims relied on |
| Fla. Stat. 501.171(2) | Indirectly (AI-004) | Employee personal information may not be entered (POL-04 4.8) |
| State AI and employment AI laws (for example Colorado SB26-189) | No | The company operates and hires only in Florida. Florida AI-specific law was not researched beyond this check |

## 4. Risk tiers
- **AI-001 High:** the rubric puts any AI that "can affect physical safety or critical infrastructure operations" in the High tier. AI-001 sits on a food safety path in a critical infrastructure sector. **What keeps residual risk manageable:** AI-001 can only divert, never release; every diverted pack is decided by a person; the CCP and manual inspection are unchanged.
- **AI-005 High:** an employment decision tool (a consequential decision category).
- **AI-002 and AI-003 Medium:** they influence business decisions; people make the final decision.
- **AI-004 Low:** internal productivity with data rules.

**Re-tier triggers:** AI-001 used as or instead of CCP monitoring, reduced manual inspection, automatic line stop or restart, extension to another line or Plant 2, or any use of images to evaluate workers; AI-003 used to lengthen inspection intervals; AI-004 connected to systems or given Restricted data.

## 5. MEASURE
### 5.1 AI-001 (in depth)
Results cover 2026-06-01 to 2026-08-21 (Lines 5-7, two shifts). Seeded-defect tests used certified test pieces and deliberately defective packs placed by QA on each shift.

| Trustworthy characteristic | Test / metric | Threshold | Result | Pass? |
|---|---|---|---|---|
| Valid and reliable | Seeded foreign material detection, overall and by product type | 95% overall; 90% for every product type | 96% overall (418 of 435); bacon 82% (41 of 50) | **No** (bacon) |
| Valid and reliable | Lot-code and label read accuracy against QA checks | 99.5% | 99.8% | Yes |
| Valid and reliable | False divert rate | 2% or less | 2.6% overall; 4.9% for 2 weeks after the July packaging film change | **No** |
| Safe | CCP and manual inspection unchanged; every divert decided by QA | All true | Confirmed by walkthrough and QA logs | Yes |
| Secure and resilient | Edge servers in the OT zone; vendor access through the gateway with MFA; model updates through change control | All true | Edge servers on the Line 5-7 HMI network; vendor remote tool always on; 2 model updates in 2026 without notice | **No** |
| Accountable and transparent | Divert decisions logged with defect category and QA disposition in the records application | Logged | Vendor dashboard only | Partial |
| Explainable and interpretable | QA can see the image and highlighted region for each divert | Available | Available | Yes |
| Privacy-enhanced | No audio; worker images not used for other purposes; image retention 90 days; no vendor reuse outside the service | All contractual | No audio confirmed; retention and reuse not in the contract | **No** |
| Fair, with harmful bias managed | Performance across product types, shifts (lighting), and packaging films; flag any group more than 5 points worse than overall | No group flagged | Bacon 14 points below overall; night shift 2 points below; new film raised false diverts | **No** (product type) |

**"Bias" in a vision inspection system.** AI-001 makes no decisions about people, so fairness here means **consistent performance across the conditions the product meets**. Bacon's marbled fat and irregular slices look like the variation the model treats as normal, so foreign material on bacon is missed more often. A system that works well on average and poorly on one product gives false comfort exactly where it is least reliable.

**Ongoing performance and bias testing plan (AI-001):**
- **Groups compared:** product type (deli meats, franks, smoked sausage, bacon), shift, packaging film supplier, label format (branded or private label).
- **Metrics:** seeded-defect detection rate, false divert rate, label read accuracy, per group.
- **Thresholds:** 95% detection overall and 90% for every group; false diverts 2% or less; no group more than 5 points worse than overall.
- **Frequency:** seeded tests every shift; monthly group report to the VP FSQA; full re-test after any model update, camera move, lighting change, or packaging change.

### 5.2 Other use cases
| Use case | Characteristic | Test or metric | Threshold | Result | Pass? |
|---|---|---|---|---|---|
| AI-002 | Valid and reliable | Weekly forecast error by product family (mean absolute percentage error) | 15% or less | 12% overall; 24% for holiday hams in 2025 Q4 | Partial: seasonal items under review |
| AI-002 | Accountable | Planner overrides logged with reasons | 100% | Overrides logged; reasons missing in 40% | Partial |
| AI-003 | Safe | No PSM inspection skipped or deferred because of a model score | 0 | 0 (12 months of records) | Yes |
| AI-003 | Secure and resilient | Telemetry one-way outbound through the Plant 1 broker; no inbound vendor access | True | True (P01 R-030 accepted at Low) | Yes |
| AI-004 | Privacy-enhanced (AI 600-1 data privacy and information security risks) | Contract bars training on company data; retention 30 days; data loss rules block formulation and employee data patterns | All true | Contract terms confirmed; data loss rules due 2026-10-15 | Partial (before pilot start) |
| AI-004 | Valid and reliable (AI 600-1 confabulation risk) | Users trained to verify outputs; no use for regulatory submissions or food safety records | Training complete before access | Scheduled for pilot start | Pending |
| AI-005 | Fair, harmful bias managed | Adverse impact ratio by sex and by race or ethnicity, using the four-fifths rule (29 CFR 1607.4(D)) on a 2026-04 to 2026-08 sample | No ratio below 0.80 | Vendor could not provide group results; company sample too small to judge (and demographic data incomplete) | **No** (cannot show compliance) |
| AI-005 | Accountable and transparent | Recruiters know when and how scores are used | Documented | Recruiters did not know the feature had been enabled | **No** |

## 6. MANAGE
**Human-in-the-loop design:**
- **AI-001:** diverts; people decide. QA reviews every diverted pack. Manual visual inspection stays at two inspectors per line per shift. Operators can switch to bypass at any time; bypass events are logged.
- **AI-002:** planners approve every published plan.
- **AI-003:** advisory; the PSM mechanical integrity schedule governs.
- **AI-004:** users review all output; no automation.
- **AI-005:** disabled. If ever re-enabled, the score may not screen anyone out, and every applicant is reviewed by a recruiter.

**Monitoring:** owners report section 5 metrics monthly to the AI review group; AI-001 also gets a quarterly deep dive with the Plant 1 FSQA Manager. Results feed P01 R-025 to R-030.

**Incident handling:** a missed defect found downstream (customer complaint, x-ray reject, QA audit) is handled under the HACCP corrective action procedure, and the VP FSQA decides on hold, recall, and FSIS notice (9 CFR 418.2) as for any other cause. A security incident involving an AI vendor or edge server follows P08 (`ir-runbook-process-tampering.md` if inspection settings were changed).

**Decommissioning criteria:**
- AI-001: switch to bypass and remove if detection falls below thresholds for 2 consecutive months, or if the vendor will not sign data and change terms by 2026-11-30; on removal the vendor deletes all plant images and confirms in writing.
- AI-003: stop if the vendor requests inbound access.
- AI-004: end the pilot if data loss rules are not live before access is granted.
- Any tool: stop if the vendor changes data-use terms or the model changes without notice.

## 7. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** (supplemental inspection only) | 1. HACCP reassessment decision documented: AI-001 is not part of the HACCP plan; the CCP and manual inspection stay unchanged (2026-10-31). 2. **Bacon runs in bypass** until a vendor retrain meets the 90% subgroup threshold. 3. Vendor contract: 90-day image retention, no reuse outside the service, no worker evaluation, change notice for model updates (2026-11-30). 4. Vendor access only through the remote access gateway; edge servers moved into the OT zone with deny-by-default rules (2026-12-31). 5. Seeded tests and divert dispositions recorded in the records application (2026-10-31). Plant 2 pilot and any reduction in manual inspection need a new assessment and 2 consecutive months meeting all thresholds | Chief Executive Officer, 2026-09-15 (on the recommendation of the VP FSQA and the COO) |
| AI-002 | Approve with monitoring | Override reasons required; seasonal model review before the 2026 holiday ham season | Chief Operating Officer, 2026-09-04 |
| AI-003 | Approve | Advisory only; PSM inspection intervals never lengthened on a model score; telemetry path reviewed under management of change | Chief Operating Officer, 2026-09-04 |
| AI-004 | Approve the pilot | Data loss rules live and user training complete before access; Restricted data prohibited; review after 90 days | Chief Operating Officer, 2026-09-04 |
| AI-005 | **Keep disabled; retire** | Vendor must provide group-level adverse impact results and validation evidence before any new request; counsel review; new assessment required | Chief Executive Officer, 2026-09-15 |

All conditions are tracked as POAM-021 in P07.

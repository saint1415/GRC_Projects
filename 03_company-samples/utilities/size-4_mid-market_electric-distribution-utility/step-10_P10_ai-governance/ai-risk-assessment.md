# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (investor-owned electric distribution utility with a Utility Services line) |
| Tier / Vertical | Mid-Market / Utilities |
| Scope | Portfolio of 6 AI and model-based use cases (AI-001 to AI-006), inventory in `ai-use-case-inventory.csv`. Deep dive on AI-001, the electric load-forecasting model (registry default) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook, with the Generative AI Profile (NIST AI 600-1) for AI-003 and AI-005 |
| Assessors / date | Director of Power Supply and Rates (chair), vCISO and Information Security Manager (security), General Counsel's office (legal and credit), Director of System Operations (operations), 2026-08-24 to 2026-09-10 |
| Decision | Chief Operating Officer, 2026-09-17; High-tier decisions noted by the President and CEO |

## 1. Summary
Six AI or model-based uses exist; none had been through a security or privacy review before this assessment (gap 13). None is out of control, but four need conditions:
- **AI-001, load forecasting:** drives day-ahead purchases (up to $1.2 million exposure on a peak day) and peak-day operating plans, with no validation, drift monitoring, or change control. Its errors fall unevenly on substations.
- **AI-006, deposit risk score:** a credit decision about individuals, with no fairness testing and adverse action letters not reviewed since 2022.
- **AI-003, contact center assistant:** turned on in 2026-05 without review; the model provider is outside the vendor's SOC 2, and data-use terms are missing.
- **AI-005, enterprise assistant:** inherits each user's file permissions, so over-shared CEII and customer data can surface in answers.

| ID | Use case | Risk tier | Generative? | Decision |
|---|---|---|---|---|
| AI-001 | Electric load-forecasting model | High | No | Approve with conditions |
| AI-002 | AMI theft and tamper analytics | Medium | No | Approve with conditions |
| AI-003 | Contact center generative AI agent assistant | Medium | Yes | Approve with conditions; restricted to knowledge-article answers until terms are signed |
| AI-004 | Vegetation risk model | Low | No | Approve |
| AI-005 | Enterprise generative AI assistant (pilot) | Medium | Yes | Approve with conditions; pilot stays at 120 users until the permission cleanup is done |
| AI-006 | Deposit risk score | High | No | Approve with conditions |

Tiers: 2 High, 3 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** Chief Operating Officer. The **AI review group** (chair: Director of Power Supply and Rates; members: vCISO, Information Security Manager, a General Counsel delegate, Director of System Operations, Director of Customer Service) meets monthly for 30 minutes. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.16: AI tools that use customer data, operational data, or CEII, or support operational or customer decisions, must be approved before use.
  - POL-04 5.6: CEII and BES Cyber System Information are Restricted and must not reach unapproved tools.
  - POL-05 4.8: only approved AI tools; no Restricted data in unapproved tools; users check outputs.
  - STD-05 AI use standard: due 2026-12-31.
- **Risk method:** the P01 SP 800-30 method rates AI risks R-028 to R-032 in the risk register.

### 2.1 Governance process (scaled for a mid-market utility)
| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | One-page intake for any new AI tool or AI feature in an existing tool: purpose, users, data, vendor, decisions affected, any link to OT | Requesting business owner | 15 minutes |
| 2. Triage | Provisional tier with the repository rubric; purchasing gate (no purchase order without approval, POL-01 4.11); any path to OT or CEII goes straight to Medium or higher | Information Security Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, privacy, vendor data-use terms, and a business reviewer. **High:** full MAP and MEASURE assessment, including validation, a fairness plan, and an operations or legal reviewer | AI review group members | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Information Security Manager. Medium: AI review group. High: AI review group recommends, Chief Operating Officer decides and informs the CEO | As listed | Monthly |
| 5. Monitor | Owners report agreed metrics monthly (Medium and High) and a quarterly deep dive (High) | Business owner | Ongoing |
| 6. Re-review | Yearly, or on a trigger: new feature, model change, new data, new population, or an operating or customer incident | AI review group | Yearly |

## 3. MAP
| Item | AI-001 Load forecast | AI-002 Tamper analytics | AI-003 Contact center assistant | AI-004 Vegetation model | AI-005 Enterprise assistant | AI-006 Deposit score |
|---|---|---|---|---|---|---|
| Purpose | Hourly day-ahead and 7-day forecasts, system and 74 substations; solar PPA output | Flag meters for theft or tamper investigation | Suggest answers and summarize calls | Rank circuit miles for trimming | Draft, summarize, search documents | Decide whether a new residential customer pays a deposit, and how much |
| Users | Lead Load Forecasting Analyst and a data analyst; Director of Power Supply and Rates; DCC shift supervisors | Revenue protection staff | About 160 company and 42 Utility Services agents | Vegetation planners | 120 pilot users | Credit staff (automatic for most applications) |
| Affected people | All 265,000 customers indirectly; neighborhoods served by under-forecast substations | Flagged customers (about 70 flags a month) | Callers, including client utility customers | Customers on circuits that wait longer for trimming | Indirect | About 1,100 move-ins a day |
| Data | Aggregated loads, weather, calendar, solar; no individual records | Interval data, meter events | Call audio, account details | Imagery, outage history | Company documents and email | Consumer report attributes, payment history |
| Build or buy | Build (in-house) | Buy (AMI vendor) | Buy (platform feature, third-party model) | Buy | Buy | Buy (CIS vendor) |
| Applicable rules | Wholesale contract; POL-04 | State tariff rules (not assessed) | Fla. Stat. 501.171(2); 16 CFR 681.1(e)(4); client contracts | None AI-specific | Fla. Stat. 501.171(2); CEII handling | FCRA 15 U.S.C. 1681m(a); ECOA 15 U.S.C. 1691; 16 CFR 681.1 |

**Laws considered and not applicable or not assessed:**
- **NERC CIP:** none of the six uses is a BES Cyber System, and none controls or protects a BES Facility. AI-001 must never be wired into SCADA or the ADMS load-shedding design without a new assessment and a CIP-002 review (POL-01 4.5).
- **Federal or Florida AI-specific statute:** none identified for these uses. The company operates only in Florida. State AI laws in other states that cover consequential decisions about individuals were not researched, because the company serves only Florida premises; counsel will check if customer-facing AI expands.
- **State public service commission rules** on disconnection, back-billing, and deposits are outside this cyber and AI analysis and were not assessed.

### 3.1 AI-001 deep dive: electric load-forecasting model
- **How the output is used:** (1) the day-ahead purchase schedule sent to the wholesale supplier each morning; (2) peak-day operating plans (demand response calls, conservation voltage reduction, crew and mobile transformer staging); (3) summer switching plans that move load away from substations near their limits; (4) the solar PPA output forecast.
- **Not intended:** automatic control of any grid device, automatic demand response dispatch, input to the ADMS adaptive load-shedding module, or any decision about an individual customer.
- **Data path:** feeder loads arrive only as an outbound export from the historian replica in the OT DMZ; the analytics account has no path into OT (P04 finding 2).

## 4. Risk tiers
Tiers use the repository rubric (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`).

| ID | Tier | Rationale |
|---|---|---|
| AI-001 | **High** | Can affect critical infrastructure operations: the forecast shapes peak-day operating plans and summer switching for a distribution grid. An under-forecast can leave a substation overloaded. A person approves every schedule and plan, and nothing is wired to a control system |
| AI-006 | **High** | A substantial factor in a consequential decision about a person (credit: deposit requirements for an essential service) |
| AI-002 | Medium | Affects individuals (investigations and possible back-billing), but a technician inspects every flag before action |
| AI-003 | Medium | Generative AI with customer data and client data; the agent decides |
| AI-005 | Medium | Generative AI that can surface Restricted data a user should not see |
| AI-004 | Low | Internal work prioritization; no individual decisions; planners and arborists verify |

**Escalation triggers (re-assess before any of these):** AI-001 used to dispatch demand response, voltage reduction, or load shedding automatically, or fed into SCADA or the ADMS; AI-002 flags used for disconnection or back-billing without field verification; AI-003 given authority to promise payment arrangements or disconnection dates; AI-006 extended to commercial accounts or to disconnection decisions.

## 5. MEASURE
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (backtest or 2026-08 sample) | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Day-ahead system mean absolute percentage error (MAPE) on all days and on the 20 highest-load days | 3.0% all days; 4.5% peak days | 2.8% all days; **5.4% peak days** (2025-06-01 to 2026-07-31) | **No** |
| AI-001 | Valid and reliable (drift) | 30-day MAPE trend; retrain if above 3.5% | Alert within 1 day | 30-day MAPE reached 4.1% in 2026-05 as rooftop solar grew; noticed 3 weeks later | **No** |
| AI-001 | Safe | Peak-day forecast compared with the supplier's forecast; gap over 5% triggers review by the Director of System Operations | Every peak day | Done on 12 of 20 peak days | **No** |
| AI-001 | Secure and resilient | Named workspace accounts; input range checks; fallback to the prior day's schedule | All in place | Shared workspace key; no input checks; fallback used 3 times when the weather feed failed | **No** |
| AI-001 | Accountable and transparent | Model card, validation report, and approval for each version | Each version | None; code history only | **No** |
| AI-001 | Explainable and interpretable | Per-forecast breakdown (temperature, day type, solar) for the analyst and approver | Available | Available and used on peak days | Yes |
| AI-001 | Privacy-enhanced | AMI data aggregated to at least 100 meters | 100% of aggregates | All 74 substation aggregates confirmed | Yes |
| AI-001 | Fair, harmful bias managed | Substation test (below) | No substation flagged | **4 substations flagged** | **No** |
| AI-002 | Valid and reliable | Share of flags confirmed by field inspection | At least 30% | 22% of 410 flags (2026-01 to 2026-06) | **No** |
| AI-002 | Fair, harmful bias managed | Flag rate and confirmation rate by area median income band | Flag rate no more than 1.5 times the average in any band without a higher confirmation rate | Lowest-income band flagged at 1.7 times the average with the same confirmation rate | **No** |
| AI-003 | Privacy-enhanced | Vendor terms: no training on company data; retention limit; model provider bound | All contractual | Not in the contract | **No** |
| AI-003 | Valid and reliable, safe | 50 scripted questions on disconnection, payment arrangements, and outage safety (downed lines) | 0 wrong answers on safety or disconnection rules | 3 wrong answers on payment arrangement terms; 0 on safety | **No** |
| AI-004 | Valid and reliable | Tree-caused outages on top-ranked circuits versus others | Top quartile has the higher rate | Top quartile 2.6 times the rate of others | Yes |
| AI-005 | Secure and privacy-enhanced | Sample searches by pilot users for relay settings, one-line diagrams, and SSNs | No Restricted results outside the user's role | 2 of 30 searches returned one-line diagrams from an over-shared engineering folder | **No** |
| AI-006 | Fair, harmful bias managed | Deposit rate by area-level proxies (census tract income band; majority-language tract) compared with repayment outcomes | Differences explained by repayment risk | Deposit rate in the lowest-income band 2.1 times the average; repayment outcomes explain about half | **No** |
| AI-006 | Accountable and transparent | Adverse action letters when a deposit is based on the consumer report; review of letter content | 100% sent; content reviewed yearly | 25 of 25 sampled sent; content not reviewed since 2022 | Partial |
| All | Accountable and transparent | Business owner named; inventory entry; approval record | 100% | 6 of 6 owners named; approvals recorded 2026-09-17 | Yes |

**AI-001 bias and fairness test.** A load forecast does not decide anything about a person, but its errors land on neighborhoods. A substation that is under-forecast on hot days is more likely to overload, lose service, or be chosen for load relief.
- **Groups compared:** the 68 distribution substations, each tagged by (a) share of residential customers in the income-qualified bill assistance program, (b) median housing age, and (c) rooftop solar share.
- **Metrics:** substation MAPE and mean signed error on the 20 highest-load days, compared with the system average.
- **Threshold:** flag any substation whose peak-day MAPE exceeds the system average by more than 2 percentage points, or whose signed error shows under-forecasting beyond 3%.
- **Result:** 4 substations that serve older neighborhoods with a high share of income-qualified customers are **under-forecast by 5% to 7% on hot days**, probably because window air conditioners respond to heat differently from the central systems that dominate the training data. Two of them were within 5% of their summer limits.
- **Actions:** add a heat-response feature by area; until validated, the DCC adds a 7% margin to those 4 substations on peak days; the Director of System Operations reviews each summer that voltage reduction and load relief do not fall repeatedly on the same substations.

**AI-006 fairness note.** The company does not collect race or national origin from applicants. The test uses area-level proxies only, which can show a disparity but not its cause. Counsel and the Credit and Collections Manager will review the score's inputs for variables that act as proxies for protected characteristics and consider alternatives (for example, payment history with other utilities or a letter of credit history) before the next model update.

## 6. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the analyst reviews each run against the prior day and the supplier's forecast; the Director of Power Supply and Rates approves and can override the schedule (overrides logged with a reason); the Director of System Operations approves peak-day plans for substations within 5% of their limits.
- **AI-002:** a technician inspects every flagged meter; back-billing needs supervisor approval; no disconnection on a flag alone.
- **AI-003:** suggestions limited to approved knowledge articles, shown with their source; agents confirm before acting.
- **AI-005:** users check outputs; Restricted folders excluded from the assistant's index.
- **AI-006:** credit staff review any application within 10% of a deposit threshold; customers can request review; adverse action letters sent.

**Monitoring:** owners report section 5 metrics monthly to the AI review group; AI-001 and AI-006 get a quarterly deep dive. Results feed the risk register (P01 R-028 to R-032).

**Security:** AI-001 moves to named workspace accounts, input range and plausibility checks, and version control with approval before release (P04 finding 5). The analytics account stays without any path into OT.

**Incident handling:** suspected tampering with AI-001 data or the workspace follows POL-03 and runbook B; a forecast error that contributes to an overload or outage is reviewed like any operating event; an AI vendor data incident follows the vendor terms and the P08 matrix.

**Decommissioning criteria:**
- AI-001: roll back or retire if peak-day MAPE stays above 4.5% for two summers in a row, or if a validated vendor forecast performs better at lower risk; keep the last approved version for rollback.
- AI-002: stop automatic flags if the confirmation rate stays below 20% for two quarters.
- AI-003: switch off on 2026-12-31 if data-use terms are not signed.
- AI-006: return to the manual credit policy if the fairness review cannot explain the disparity by 2027-06-30.

## 7. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** | Validation report and model card for the current version, with sign-off before any new version (2026-11-30); named accounts and input checks (2026-11-30); automatic drift alert and the supplier comparison on every peak day (2026-12-31); heat-response fix for the 4 flagged substations validated against the 2026 summer, with the 7% margin until then; independent review of the model by an outside forecaster (2027-03-31); cross-train a second analyst (2027-03-31) | Chief Operating Officer, 2026-09-17; noted by the President and CEO |
| AI-002 | **Approve with conditions** | Quarterly confirmation and income-band reports; review of flag thresholds with the AMI vendor (2026-12-31) | AI review group, 2026-09-17 |
| AI-003 | **Approve with conditions** | Answers limited to knowledge articles now; vendor terms with no training on company data, retention limits, and model provider commitments (2026-12-31) or switch off; fix the 3 payment arrangement answers (2026-10-15) | AI review group, 2026-09-17 |
| AI-004 | **Approve** | Yearly review | Information Security Manager, 2026-09-17 |
| AI-005 | **Approve with conditions** | Remove over-sharing on the engineering folders and exclude Restricted locations from the index before the pilot grows (2026-11-30) | AI review group, 2026-09-17 |
| AI-006 | **Approve with conditions** | Fairness review of inputs with counsel (2027-03-31); adverse action letter content review (2026-12-31); override and review process documented (2026-11-30) | Chief Operating Officer, 2026-09-17; noted by the President and CEO |

The conditions are tracked as POAM-021 in P07 and in the risk register (P01 R-028 to R-032). The AI review group's first monthly meeting is on 2026-10-06.

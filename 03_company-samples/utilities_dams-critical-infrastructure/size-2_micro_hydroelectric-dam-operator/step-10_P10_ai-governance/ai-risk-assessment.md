# AI Risk Assessment: Dam-Safety Sensor Anomaly Detection

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (owner and operator of the fictional Bramble Shoals Hydroelectric Project) |
| Tier / Vertical | Micro / Dams |
| AI use case | AI-001: the remote monitoring service vendor's AI anomaly add-on, which flags unusual patterns in dam safety instrument readings. Free trial since 2026-05-04 |
| Also covered | AI-002: staff use of public generative AI chatbots (section 7) |
| Framework | NIST AI RMF 1.0 (AI 100-1); NIST AI 600-1 for AI-002 |
| Assessor / date | Plant Superintendent with the Office and Compliance Administrator and the Controls and Electrical Technician; the consulting dam safety engineer reviewed section 4. 2026-08-25 |
| Decision | Owner and General Manager with the Plant Superintendent, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

**Why this use case, at this size.** The registry default for a dam is sensor anomaly detection. At a 7-person company it is not a platform the company builds or buys on its own: it is an add-on the monitoring vendor offered as a free trial, and an operator-mechanic switched it on from the portal on 2026-05-04 without any review (P01 R-017, R-018; 00_company-facts.md section 4, item 13). That is the realistic way AI arrives at a small dam owner, and the assessment starts from there.

## 1. GOVERN
- **Accountable owner:** Plant Superintendent (business owner and Chief Dam Safety Coordinator). **Decision authority:** Owner and General Manager. Any change that lets AI output reduce manual dam safety checks needs both, plus the consulting dam safety engineer's written view.
- **Policies that apply:**
  - POL-04 4.6: AI tools only from the approved list; no AI output to the control system
  - POL-04 4.5: the five security questions before any trial or add-on (the step skipped on 2026-05-04)
  - POL-02 A.10: any new command path from the cloud needs the Owner's approval and a new risk assessment
  - POL-02 A.5: vendor terms on data use and incident notice
- **Approved-tools list** (kept by the Office and Compliance Administrator): AI-001, for Internal instrument data, advisory use only, under the conditions in section 6. No generative AI tool is approved for Internal or Restricted information.
- **Scale for a Micro company:** no AI committee. The Plant Superintendent reviews alert statistics monthly and reports at the Owner's monthly POA&M meeting. The consulting dam safety engineer looks at AI alerts during the quarterly instrument trend review.
- **Not negotiable:** the data path stays one-way (gateway to vendor). The product's setpoint-write feature stays disabled, and nothing the AI produces is ever sent to the gates or units (P04 finding 2).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Watch the readings the monitoring service already receives every minute (headwater and tailwater levels, 4 automated uplift piezometers, 1 automated seepage weir) for patterns that suggest a developing problem, such as uplift rising after rain or seepage changing without a matching headwater change, sooner than the daily readings and the quarterly trend review would show it |
| Users / operators | Operator-mechanics (alerts on the on-call phone), the Plant Superintendent, and the consulting dam safety engineer |
| Affected people | Nobody is the subject of a decision. The people who bear the risk are recreation users at the tailrace, canoe launch, and fishing area, the owners of riverside property and the county road bridge downstream, and staff, through the dam's safety |
| Data | Inputs: instrument readings and levels every minute; rainfall from a public source. Outputs: an alert with a score and the readings that drove it. Model supplied by the vendor and tuned on the company's own 2019-2026 history. Not covered: the manual seepage weir and the 6 survey monuments, which are read by hand and never reach the service |
| Build or buy | Buy. The vendor supplies the model; the company sets alert thresholds and who gets alerts |
| Not intended | Moving gates or units; replacing trigger-point checks set in the 2023 ODSP instrumentation plan; deciding whether to report under 18 CFR 12.10; deciding EAP actions. These uses are **prohibited** |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| 18 CFR 12.10(a); 12.3(b)(4)(viii) | **Yes, indirectly** | Unusual instrumentation readings are conditions affecting safety, to be reported to the Regional Engineer as soon as practicable, preferably within 72 hours. The AI does not change that duty. An AI alert that staff confirm as unusual starts the 12.10 decision; an AI "all clear" never overrides a reading past a trigger point |
| 18 CFR 12.51 | Yes, indirectly | Monitoring instruments must be satisfactory to the Regional Engineer. The AI adds analysis; it replaces no instrument or reading |
| FERC Security Program Rev. 3A 3.2 | Yes | Trigger points for action from critical instrumentation are to be defined. They stay defined and checked by people |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. Keep the trial offer and claims in the vendor folder |
| State AI laws | No | Laws aimed at consequential decisions about people (employment, lending, housing, and similar) do not reach a tool that makes no decision about a person; the company operates only in Florida |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`: AI that "can affect physical safety or critical infrastructure operations").

**Why High even though it only advises:** the realistic harm is a missed anomaly (a false negative) if people begin to trust the tool and look less often, which is easy at a plant with 3 operator-mechanics who also do maintenance. Too many false alarms carry the opposite risk: staff stop reading alerts. Both are reliance risks, not model-security risks.

**Re-assess before any of these:**
- a proposal to reduce daily readings, trigger-point checks, or the quarterly trend review
- any link from AI output to EAP notifications, 12.10 reports, or control actions, or turning on the setpoint-write feature
- a vendor model retrain or new version
- automating the manual weir or the survey monuments, or adding new instrument types

## 4. MEASURE
Trial data: the vendor's back-test on 9 documented events (2019-2026) and live results from 2026-05-04 to 2026-08-15.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Back-test recall on the 9 documented events; target at least 8 of 9 | 7 of 9 found (78%) | **No** |
| Valid and reliable | Live alerts confirmed as real conditions | 57 alerts; 3 confirmed as real conditions, none past a trigger point | Partial (low precision) |
| Safe | No reading or check skipped because of the tool; every trigger-point exceedance handled by the manual process | No skipped readings found in the walk-down sheets; no exceedances in the period | Yes |
| Secure and resilient | One-way data path; setpoint-write feature off; portal MFA; vendor SOC 2 | One-way path and feature off confirmed (2026-07-21); portal MFA not yet on (POAM-003); the add-on is **outside** the vendor's SOC 2 scope (P09) | **No** |
| Accountable and transparent | Every alert has a recorded disposition | 41 of 57 had a disposition; 16 alerts in July were cleared in the app with no note | **No** |
| Explainable and interpretable | Each alert names the readings that drove it | Yes for all alerts | Yes |
| Privacy-enhanced | No personal information in inputs or outputs | None | Yes (not a material risk) |
| Fair, with harmful bias managed | Compare performance across instrument groups and seasons (plan below) | See finding | **No.** Disparity flagged |

**Bias and performance-disparity testing plan.** Here "bias" means the tool working well for some parts of the dam and poorly for others. The tool makes no decision about people, so demographic fairness metrics do not apply. What does apply is whether any instrument, and therefore any failure mode, is watched less well.

| Group compared | Metric | Threshold | Frequency |
|---|---|---|---|
| Instrument type: uplift piezometers, automated seepage weir, headwater and tailwater levels | Recall on documented and seeded events; alerts per 100 instrument-days | Recall at least 80% in every group; no group's alert rate more than 2 times the overall rate | Before any model change, then quarterly with the consulting engineer's review |
| Season: wet (June to September) vs dry | Alerts per day; share confirmed | Wet-season alerts no more than 2 times the dry-season rate | Each season |
| Covered vs not covered instruments | Every instrument listed as covered or not covered | 100% of instruments labeled | At each change |
| Staff reliance (automation bias) | Daily readings completed; alerts with a recorded disposition | 100% of daily readings; 100% of alerts dispositioned within 24 hours | Monthly |

**Finding.** The back-test found all 5 uplift piezometer events, but only 1 of 2 seepage weir events and 1 of 2 level-sensor events. The automated seepage weir is the only instrument of its kind, so the model has little to learn from. The manual weir and survey monuments are not watched at all. Alert volume rose from about 0.4 a day in May to about 0.6 a day from June to mid-August, a 1.5 times wet-season increase, inside the 2 times threshold but worth watching. The fix is not a better model: label the weir and the manual instruments "not covered by AI", keep the daily readings, and re-test after the wet season.

## 5. MANAGE
**Human-in-the-loop design:**
- Every alert goes to the operator-mechanic on duty or on call, who checks the instrument (and visits it at night if the alert involves a piezometer or the weir) and records a disposition in the app.
- The Plant Superintendent reviews every confirmed alert and decides any action, 12.10 report, or EAP step. The tool has no role in those decisions beyond prompting a look.
- Daily readings, trigger-point checks, and the consulting engineer's quarterly trend review continue unchanged.

**Monitoring:** monthly alert statistics and the reliance measures above, reported at the Owner's monthly meeting; quarterly disparity checks with the consulting engineer; the vendor must give 30 days' notice of any model change (contract clause), and the company re-runs the back-test before accepting it.

**Incident handling:** a missed event later found by a daily reading is logged as an AI incident and reported to the vendor; the 12.10 decision on the underlying condition follows POL-03, not the tool. A security incident at the vendor follows P08 and the contract notice terms (P09 Part B).

**Decommissioning:** stop using the tool if recall falls below 7 of 9 on the back-test or below 80% in any quarterly check, if the vendor will not sign the data-use clause, or if the one-way path cannot be kept. Readings stay in the data logger (60 days) and the monitoring service trends, so nothing is lost by stopping.

## 6. Decision
**Approve with conditions.** Owner and General Manager and Plant Superintendent, 2026-08-31. The trial continues as advisory only, and converts to a paid subscription **only if**:
1. Daily readings, trigger-point checks, and the quarterly trend review continue unchanged. No reduction is approved.
2. The automated seepage weir, the manual weir, and the survey monuments are labeled "not covered by AI" in the portal by 2026-09-30.
3. Every alert gets a recorded disposition within 24 hours, checked monthly from September 2026 (P01 R-017, due 2026-10-31).
4. Portal MFA is turned on by 2026-09-30 (POAM-003).
5. The vendor signs a contract clause by 2026-12-31: no use of company data for other customers' models, 30-day notice of model changes, the setpoint-write feature stays off unless the Owner asks in writing, and the add-on is included in the next SOC 2 report (P01 R-018, R-023; POAM-013). Until it is signed, the company asks the vendor in writing to opt it out of model training.
6. The back-test is repeated after the 2026 wet season, by 2026-11-30.

The tool may be considered for any change to manual checks only after 12 consecutive months meeting every threshold in section 4 and a written view from the consulting dam safety engineer.

## 7. AI-002: public generative AI chatbots (Low)
Interviews found two staff using public chatbots to draft letters and a procedure. No CEII or employee information was found in the examples reviewed, but nothing prevented it (P01 R-019).
- **Rule now:** public chatbots may be used only for general drafting with Public information. Internal and Restricted information, including drawings, inundation maps, control system details, passwords, and employee personal information, must never be entered (POL-04 4.6; POL-02 C.2). Staff will be briefed in the annual training by 2026-10-31.
- **Tier: Low.** People write and approve every output, and no chatbot connects to the HPCDMS or the restricted folder. It would rise to High if anyone proposed using a chatbot with CEII or control system information.

# AI Risk Assessment: Dam-Safety Sensor Anomaly Detection

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensee of the fictional Cypress Fork Hydroelectric Project) |
| Tier / Vertical | Small / Dams |
| AI use case | AI-001: machine learning anomaly detection on dam safety instrument data, in the instrumentation data platform (SaaS). Shadow-mode pilot since April 2026 |
| Also covered | AI-002: staff use of generative AI assistants near CEII (section 7) |
| Framework | NIST AI RMF 1.0 (AI 100-1); NIST AI 600-1 for AI-002. NIST released a concept note for an AI RMF Critical Infrastructure Profile on 2026-04-07; it is not final and is not relied on here |
| Assessor / date | Chief Dam Safety Engineer with the IT Manager and Controls Engineer, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner:** Chief Dam Safety Engineer (a licensed professional engineer, 18 CFR 12.61(a)). **Decision authority:** Vice President of Operations for High-tier AI, with the President informed. Any change that lets AI output reduce manual dam safety review needs both.
- **Policies that apply:**
  - POL-04 4.10: no Restricted (CEII) data in AI tools unless approved for that level
  - POL-05 4.8: approved tools only
  - POL-01 4.9: security impact review for any change touching OT
  - POL-01 4.10: vendor security terms
- **Approved-tools list:** kept by the IT Manager. Today: AI-001 (approved for Confidential instrument data, advisory use only). No generative AI tool is approved for Restricted data.
- **Scale for a Small company:** no AI committee. The Chief Dam Safety Engineer, IT Manager, and Controls Engineer review AI use quarterly at the monthly OT/IT security meeting (POL-01 4.12).
- **Not negotiable:** AI outputs never flow back into the control system. The data path is one-way from the DMZ historian replica to the platform (P04 finding 1).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Watch 64 instruments (piezometers, seepage weirs, reservoir and tailwater levels) and 2 upstream gauges for patterns that suggest a developing failure mode, such as rising pore pressure or seepage after rain, earlier than the weekly manual trend review |
| Users / operators | Chief Dam Safety Engineer and 4 dam safety technicians |
| Affected people | Nobody is the subject of a decision. The people who bear the risk are downstream residents (about 2,400 in the inundation zone), recreation users, and staff, through the dam's safety |
| Data | Inputs: instrument readings every 15 minutes (vibrating-wire piezometers and weirs) or monthly manual readings (6 open-standpipe piezometers); rainfall; reservoir level. Outputs: alert score and a short explanation of which readings drove it. Model trained by the vendor on the company's own 2018-2026 history |
| Build or buy | Buy (configured). The vendor supplies the model; the company sets alert thresholds and routing |
| Not intended | Controlling gates or units; replacing trigger-point checks; deciding whether to report under 18 CFR 12.10; deciding EAP actions. These uses are **prohibited** |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| 18 CFR 12.10(a); 12.3(b)(4)(viii) | **Yes, indirectly** | Unusual instrumentation readings are conditions affecting safety that must be reported to the Regional Engineer as soon as practicable, preferably within 72 hours. The AI does not change that duty. An AI alert that a technician confirms as unusual starts the 12.10 decision; an AI "all clear" never overrides a reading past a trigger point |
| 18 CFR 12.51 | Yes, indirectly | Monitoring instruments must be satisfactory to the Regional Engineer. The AI adds analysis; it does not replace any instrument or reading the Regional Engineer relies on |
| FERC Security Program Rev. 3A 3.2 | Yes | Trigger points for action from critical instrumentation must be defined. They stay defined and checked by people |
| FERC Security Program Rev. 3A Section 9 | Yes | The platform receives data from the Critical PCDMS. The one-way path must stay one-way; any return path would change the Section 9 analysis |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. Keep the claims the company relied on in the procurement file |
| State AI laws (for example, Colorado SB26-189, Texas TRAIGA) | No | They address consequential decisions about people (employment, lending, housing, and similar) or specific prohibited uses; this tool makes no decision about a person, and the company operates only in Florida |

## 3. Risk tier
**Tier: High** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`: AI that "can affect physical safety or critical infrastructure operations").

**Why High even though it only advises:** a missed anomaly (false negative) could delay the response to a developing dam safety problem if people start to trust the tool and look less often. That is the realistic harm, and it is why the pilot's most important rule is that manual review does not change.

**What would raise concern further (re-assess before any of these):**
- a proposal to reduce the frequency of manual trend reviews or trigger-point checks
- any automatic link from AI output to EAP notifications, 12.10 reports, or control actions
- a vendor model retrain or new model version
- adding instruments of a new type or adding data from the control system beyond levels

## 4. MEASURE
Pilot data: a back-test on 23 documented historical events (2018-2026) and shadow-mode results from 2026-04-01 to 2026-08-15.

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Back-test recall on the 23 known events: target at least 95% overall | 21 of 23 detected (91%) | **No** |
| Valid and reliable | Lead time vs the weekly manual review on detected events | Median 3 days earlier | Yes |
| Safe | No instance where staff skipped or delayed a manual check because of the tool; all trigger-point exceedances handled by the manual process | 0 skipped checks in the pilot; 2 trigger-point exceedances found manually, both also flagged by the tool | Yes |
| Secure and resilient | One-way data path; SSO with MFA; vendor SOC 2 Type 2 | One-way path confirmed; SSO in place; the AI module is **not covered** by the current SOC 2 period (P09) | Partial |
| Accountable and transparent | Every alert logged with the reviewer's disposition | 214 alerts, all dispositioned; 9 confirmed as real conditions (1 instrument malfunction, 8 real changes, none past a trigger point) | Yes |
| Explainable and interpretable | Each alert names the instruments and readings that drove it | Yes for all alerts | Yes |
| Privacy-enhanced | No personal information in inputs or outputs | None | Yes (not a material risk) |
| Fair, with harmful bias managed | Compare performance across instrument groups, dam sections, seasons, and instrument age (see plan below) | Open-standpipe piezometers 4 of 6 events (67%) vs 100% for vibrating-wire piezometers (12 of 12) and weirs (5 of 5); wet-season false alarms about 3 times the dry-season rate | **No.** Disparity flagged |

**Bias and performance-disparity testing plan.** For this use case, "bias" means the tool working well for some parts of the dam and poorly for others. Because the tool makes no decision about people, demographic fairness metrics do not apply. What does apply is whether any part of the dam, and therefore any failure mode, is watched less well.

| Group compared | Metric | Threshold | Frequency |
|---|---|---|---|
| Instrument type: vibrating-wire piezometers, open-standpipe piezometers, seepage weirs, level sensors | Recall on known and seeded events; false alarms per 100 instrument-days | Recall at least 90% in every group and at least 95% overall; no group's false alarm rate more than 2 times the overall rate | Before any model change, then quarterly |
| Dam section: left embankment, right embankment, spillway and powerhouse | Recall; alert-to-confirmation ratio | No section more than 5 percentage points below the overall recall | Quarterly |
| Season: wet (June to September) vs dry | False alarms per day; recall | Wet-season false alarms no more than 2 times dry; recall equal within 5 points | Each season |
| Instrument age: installed before 2000 vs after 2015 | Recall; missing-data rate | No more than 5 points apart | Annually |
| Staff reliance (automation bias) | Share of weekly manual reviews completed on time; median time spent per alert | 100% of manual reviews on time; review time per alert not falling below 10 minutes | Monthly |

**Finding.** The tool misses events on the 6 open-standpipe piezometers because they are read only monthly, so it has too little data. The fix is not a better model; it is either automating those 6 instruments or excluding them from AI coverage so nobody assumes they are watched. Wet-season false alarms (1.9 a day vs 0.6) risk alert fatigue exactly when the dam is most loaded.

## 5. MANAGE
**Human-in-the-loop design:**
- Every alert goes to the on-duty dam safety technician, who checks the instrument (and visits it if needed) and records a disposition.
- The Chief Dam Safety Engineer reviews all confirmed alerts and decides on any action, 12.10 report, or EAP step. The tool has no role in those decisions beyond prompting a look.
- The weekly manual trend review and trigger-point checks continue unchanged. Any proposal to reduce them needs a new assessment and approval by the Vice President of Operations and the Chief Dam Safety Engineer, after at least 12 months of passing results.

**Monitoring:**
- Monthly alert statistics and the automation-bias measures above, reported at the OT/IT security meeting.
- Quarterly disparity tests; results tracked against P01 R-024.
- The vendor must give 30 days' notice of any model change; the company re-runs the back-test before accepting it.

**Incident handling:**
- A missed event later found by manual review is logged as an AI incident, analyzed, and reported to the vendor. It does not change the 12.10 decision for the underlying condition, which follows POL-03.
- A security incident at the vendor follows P08 and the contract notice terms (P09 Part B).

**Decommissioning:**
- Stop using the tool if recall falls below 85% in any quarterly test, if the vendor changes its data-use terms, or if the one-way data path cannot be kept. Instrument data stays in the OT historian, so nothing is lost by stopping.

## 6. Decision
**Approve with conditions.** Vice President of Operations and Chief Dam Safety Engineer, 2026-08-31. The pilot continues in shadow mode **only if**:
1. Manual weekly trend reviews and trigger-point checks continue unchanged (no reduction is approved).
2. The 6 open-standpipe piezometers are labeled "not covered by AI" in the platform until they are automated (automation quote due 2026-12-31).
3. The vendor signs a contract clause by 2026-12-31: no use of company data for other customers' models, 30-day model-change notice, and inclusion of the AI module in the next SOC 2 report.
4. Wet-season alert thresholds are tuned and re-tested before 2027-06-01, with the target of no more than 2 times the dry-season false alarm rate.

The tool may be reconsidered for reducing manual review frequency only after 12 consecutive months meeting every threshold in section 4.

## 7. AI-002: generative AI assistants (Medium)
Interviews found staff using public chatbots to draft letters and procedures. No CEII was found in the samples reviewed, but nothing prevented it (P01 R-025).
- **Rule now:** public chatbots are prohibited for Restricted (CEII and security) and Confidential data (POL-05 4.8; POL-04 4.10). Staff were briefed on 2026-08-28.
- **Evaluation:** the productivity suite's enterprise assistant is being evaluated for Internal and Public data only, with the CEII library excluded from its reach. Decision due 2026-12-31 by the Vice President of Operations.
- **Tier: Medium.** Humans write and approve every output, and the tool never connects to OT. It would rise to High if anyone proposed using it with CEII or control system information.

# AI Risk Assessment: Predictive Maintenance for Non-Safety Plant Equipment (and the AI Portfolio)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed owner and operator of a single-unit nuclear generating station) |
| Tier / Vertical | Mid-Market / Nuclear Reactors, Materials, and Waste |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005) in `ai-use-case-inventory.csv`, with a full assessment of **AI-001, predictive maintenance for non-safety plant equipment** |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook. NIST AI 600-1 (Generative AI Profile) is applied to AI-002 and AI-003; AI-001 is not generative |
| Assessors / dates | Maintenance Manager (business owner), vCISO, Cyber Security Program Manager, IT Security Manager, a system engineer from Engineering, and the Compliance and GRC Lead; HR Director and General Counsel for AI-004. Fieldwork 2026-08-24 to 2026-09-11 |
| Decision | AI review group recommendation 2026-09-15; decisions by the Site Vice President 2026-09-17 (High tier) and by the AI review group (Medium tier) |

## 1. Summary
None of the five AI tools went through a security, CSP, or legal review before use (gap 11). Two need firm conditions:
- **AI-001, predictive maintenance:** the vendor installed a sensor gateway with its own cellular link on balance-of-plant equipment, and the CST never evaluated it (gap 3; P01 R-020). The model also misses developing failures on heater drain pumps (R-021).
- **AI-004, applicant ranking:** the applicant tracking vendor turned the feature on by default in 2026-03. It ranks job applicants with no bias testing and no written human review rule (R-023).

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Predictive maintenance for non-safety plant equipment | High | Approve with conditions; no expansion until met (2026-11-30) |
| AI-002 | Enterprise generative AI assistant | Medium | Approve for Internal and Confidential data; block public AI tools (2026-12-31) |
| AI-003 | CAP screening assistant | Medium | Approve with conditions (2026-12-31) |
| AI-004 | Applicant ranking feature | High | **Disable** by 2026-10-31 until an adverse impact analysis passes |
| AI-005 | Power price forecasting | Medium | Approve |

Tiers: 2 High, 3 Medium, 0 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** vCISO, who keeps the AI inventory and the approved-tools list (POL-05 4.5). Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.2: CSP boundary rule. No AI tool may connect to, receive data from, or support a function of a CDA or an EP system without a prior CST evaluation under 73.54(b)(1) and (d)(3).
  - POL-01 4.12: AI tools must be approved before use; no AI tool may connect to a CDA, take any automatic action on plant equipment, or receive SGI or SRI.
  - POL-04 4.3: Restricted information (SRI, access authorization files) never goes into an AI tool.
  - POL-05 4.5: approved tools only; no Restricted information, plant configuration details, or other people's personal information unless the approved-tools list clears the tool for that data.
  - STD-05 AI use standard: due 2026-12-31 (POAM-021).
- **Approved-tools list (2026-09-17):** AI-001 (pilot, 38 assets, conditions), AI-002 (Internal and Confidential data only), AI-003 (non-security condition reports only), AI-005. AI-004 is listed as **suspended**. Public generative AI tools are not approved for any company data.

### 2.1 Lightweight AI governance process
A mid-market company needs a short, reliable gate tied to processes it already runs, not a standing AI committee with a large charter. The gate below reuses the IT change process, the CST screening in STD-04, and existing meetings.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Any department wanting an AI tool, or an AI feature turned on in an existing tool, submits a one-page intake: purpose, users, data, vendor, decisions affected, any connection to plant data or equipment | Requesting business owner | 15 minutes |
| 2. Triage | The vCISO assigns a provisional tier with the repository rubric. **Any plant data, plant equipment, or EP connection goes to the CST under STD-04 before anything else.** Purchasing holds the order until approval (POL-01 4.2) | vCISO; Cyber Security Program Manager | 2 business days |
| 3. Review | **Low:** security checklist. **Medium:** security, data classification, contract terms (no training on company data, incident notice), and a business reviewer. **High:** full MAP and MEASURE assessment like this one, including a bias and performance plan; for plant equipment, the system engineer and the Maintenance Rule coordinator; for employment, HR and counsel | IT Security Manager; Compliance and GRC Lead; business reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: vCISO. Medium: the **AI review group** (vCISO, Cyber Security Program Manager, Compliance and GRC Lead, General Counsel's delegate), 30 minutes monthly. High: the AI review group recommends and the Site Vice President decides; the CEO is informed | As listed | Monthly |
| 5. Monitor | Owners report the agreed metrics monthly; High-tier items get a quarterly deep dive; incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: new feature, model change, new data type, new assets or population, a missed failure or complaint | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. It is defined by the repository, not by any regulation.

## 3. MAP: AI-001 predictive maintenance
| Item | Description |
|---|---|
| Purpose and intended use | Detect developing mechanical faults on balance-of-plant equipment early and estimate remaining useful life, so corrective work can be planned into the work schedule or the 2027-03-08 refueling outage instead of following a breakdown |
| Assets in scope | 38 non-safety-related balance-of-plant assets: circulating water pumps, condensate pumps, heater drain pumps, instrument air compressors, turbine building ventilation fans, and main transformer cooling fans. **No safety-related equipment** |
| Users / operators | Maintenance Manager, 4 maintenance planners, 3 system engineers |
| Affected people | Indirectly: operators and maintenance crews if equipment fails. No decisions are made about individuals. Work orders name technicians, but that field is not sent to the vendor |
| Data (inputs, training, outputs) | **Path 1:** clamp-on wireless vibration and temperature sensors report to the vendor gateway, which sends data over its own cellular link to the vendor SaaS. **Path 2:** selected process values (flows, pressures, motor currents) flow from Level 3 through the one-way device to the historian replica (SYS-09), then to the cloud analytics platform, then outbound to the vendor through the AI-001 connector (P04). **Training:** vendor base models trained mostly on fossil plant fleets, tuned on 7 months of site data. **Outputs:** anomaly score, fault class, remaining-useful-life estimate, draft work order |
| Build or buy | Buy: vendor SaaS, vendor gateway, and a vendor VPN support account (shared, POAM-003). No SOC 2 report (P09 VEN-07) |
| Not intended | Any connection to a CDA or the balance-of-plant distributed control system; any automatic action on equipment; extending or skipping time-based preventive maintenance; use on safety-related equipment; replacing Maintenance Rule monitoring; rating technicians. Enabling any of these requires a new assessment and a CST evaluation |

**Applicable laws and sector rules:**
| Rule | Applies? | Why |
|---|---|---|
| 10 CFR 73.54(b)(1) and (d)(3) | **Yes** | The gateway sits on balance-of-plant equipment whose control system is a CDA, and Path 2 consumes Level 3 data. The CST must analyze whether either path creates a digital asset or pathway that must be protected, and evaluate the change before it is implemented. That was not done (P03 gap 3; POAM-019, gateway evaluation due 2026-10-31) |
| 10 CFR 50.65 (Maintenance Rule) | **Yes, as the governing program** | The scope includes nonsafety-related SSCs "whose failure could cause a reactor scram or actuation of a safety-related system" (50.65(b)(2)(iii)), which covers some AI-001 assets such as condensate and heater drain pumps. The Maintenance Rule program's monitoring, goals, and preventive maintenance stay the basis. Model output can add monitoring; it cannot replace it. Maintenance it prompts still goes through the 50.65(a)(4) risk assessment process, within the scope the program defines |
| NRC AI-specific rules | None found | No NRC regulation specific to licensee use of AI was identified. The NRC rules that govern the equipment, the data, and cyber security apply as they would to any tool |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims; the procurement file keeps the claims the company relied on |
| State AI laws | No | AI-001 makes no consequential decisions about individuals, and the company operates only in Florida |

## 4. Risk tier: AI-001
**Tier: High** (repository rubric), with conditions.

**Why High.** The rubric makes a use case High if it "can affect physical safety or critical infrastructure operations." AI-001 is advisory, but two things put it in that category at a nuclear station:
- **The data paths touch plant equipment.** An unevaluated vendor gateway with its own cellular link is installed on balance-of-plant equipment controlled by CDAs. Until the CST shows that neither path can reach a CDA, the use case must be treated as able to affect operations.
- **Model errors can affect operations.** Several assets are in Maintenance Rule scope because their failure could trip the unit. If planners trusted a "healthy" score and deferred work, a missed failure could cause a trip or derate. One unplanned trip costs about $1.23 million a day of lost generation (P05).

**Why the Small sample rated a similar tool Medium.** At a waste processor, a missed alert degrades a process; here, the same kind of miss can trip a 1,020 MW unit that sells to two buyers and supports grid reliability. The tier follows the consequence, not the technology.

**Minimum controls for High (rubric):** human review before action; pre-deployment testing (here, performance and asset-group testing in place of bias testing about people); an impact assessment (this document); ongoing monitoring. Notice to affected people does not apply, because no decisions are made about individuals.

**Re-tier or re-assess triggers:** any write access or automatic action; any use of model output to extend or skip preventive maintenance; any safety-related equipment; any new data path from Level 3 or the gateway; any use of the data to evaluate workers.

## 5. MEASURE: AI-001
Pilot period 2026-02-02 to 2026-08-31 (7 months, 38 assets). Thresholds were set by the Maintenance Manager and the system engineer before the results were reviewed.

| Trustworthy characteristic | Test / metric | Threshold | Result | Pass? |
|---|---|---|---|---|
| Valid and reliable | Precision: confirmed alerts / all alerts | At least 60% | 41 alerts, 26 confirmed by inspection (63%) | Yes |
| Valid and reliable | Recall on known degradation events found by other means (Maintenance Rule monitoring, operator rounds, oil analysis) | At least 80% | 7 of 9 events caught (78%). Both misses were heater drain pump bearing faults | **No** |
| Valid and reliable | Median lead time before the condition was found by other means | At least 7 days | 16 days | Yes |
| Safe | Preventive maintenance deferred or skipped because of model output | 0 | 0 (work order sample of all 41 alerts and all deferrals in the period) | Yes |
| Secure and resilient | CST evaluation of both data paths; gateway with no connection to any CDA, verified physically; no independent cellular path, or a path the CST accepts; named vendor accounts; vendor assurance | All met | None met: no CST evaluation; cellular link in place; read-only and "not wired to the DCS" are vendor statements only; shared VPN account; no SOC 2 report | **No** |
| Accountable and transparent | Every alert and decision logged in the WMS with the approver; model version recorded | 100% | 41 of 41 logged; model version not recorded | Partial |
| Explainable and interpretable | Each alert shows which sensor, feature, and trend drove it | Available | Available in the vendor dashboard; not exported to the work order | Partial |
| Privacy-enhanced | No personal data sent; contract bars vendor reuse of company data | Both | No personal data sent; pilot agreement has no data-use terms | **No** |
| Fair, with harmful bias managed | Asset-group performance comparison (plan below) | No group more than 15 points from the overall rate | Heater drain pumps recall 1 of 3 (33%) vs 78% overall | **No.** Gap flagged |

**Bias and fairness testing plan.** AI-001 makes no decisions about people, so harmful bias here means **uneven performance across equipment groups and operating conditions**. Uneven performance can hide failures on the equipment that matters most.
- **Groups compared:** asset type (circulating water pumps, condensate pumps, heater drain pumps, compressors, fans); operating condition (full power, power changes, and the weeks before and after the 2027 outage); season (June to September versus the rest of the year, because circulating water temperatures change).
- **Metrics:** precision, recall, false-alarm rate, and sensor data completeness for each group.
- **Threshold:** flag any group whose recall or precision is more than 15 percentage points below the overall rate, or whose data completeness is below 95%.
- **Cadence:** quarterly, and before any expansion.
- **Finding:** heater drain pumps are flagged. The likely cause is the training fleet: the vendor's base models come mostly from fossil units, where heater drain pumps run in different conditions. The vendor must retrain on site data. Until the gap closes, heater drain pump alerts and "healthy" scores are advisory only, and the system engineer keeps the existing Maintenance Rule monitoring for those pumps.
- **People:** the model must never be used to rate technicians or crews. The work order approver and technician fields are excluded from anything sent to the vendor.

## 6. MANAGE: AI-001
**Human-in-the-loop design:**
- The model creates draft work orders only. A maintenance planner and the system engineer review each one; the Maintenance Manager approves any change to the schedule.
- A "healthy" score is never a reason to defer or skip preventive maintenance, and never a reason to close a Maintenance Rule monitoring item.
- Maintenance that the model prompts follows the normal work control process, including the 50.65(a)(4) risk assessment where the program requires it and, for work on CDA-controlled equipment, the CSP's procedures.
- Operators and system engineers can override or ignore any alert. Every override is logged with a reason.

**Security conditions (due 2026-11-30):**
1. CST evaluation of the gateway (due 2026-10-31) and of the analytics feed (due 2026-11-30), entered in the CAP (POAM-019).
2. Physical verification by the system engineer and the CST that no sensor or gateway is wired to the distributed control system or any CDA.
3. Remove the gateway's independent cellular link, or route the gateway through the business network edge with monitoring, as the CST evaluation decides (P01 R-020).
4. Named, time-limited vendor accounts with MFA and session recording (POAM-003); interconnection terms (POAM-006).
5. Vendor security addendum: 72-hour incident notice, no reuse of company data, return or deletion at exit (P09 VEN-07).

**Monitoring:**
- Monthly report to the AI review group: precision, recall, lead time, data completeness, overrides, and the model version.
- Quarterly asset-group comparison under the plan above, with the High-tier deep dive.
- Results feed the risk register (R-020, R-021).

**Incident handling:**
- Suspicious gateway or connector behavior follows `ir-runbook.md`: disconnect the gateway and the connector first, and call the CST because the gateway sits on plant equipment (POL-03 4.4).
- A missed failure that leads to a trip, derate, or significant equipment damage is entered in the CAP, reviewed by the Maintenance Manager, the system engineer, and the vendor, and reported to the AI review group.

**Decommissioning criteria:**
- Disconnect the gateway and stop the pilot if the security conditions are not met by 2026-11-30, or if the CST evaluation finds a path to a CDA that cannot be removed.
- Stop if recall stays below 80% for 2 consecutive quarters after retraining.
- Stop if the vendor changes its data-use terms or changes the model without notice.
- On exit, the vendor must return or delete company data with written confirmation, and the CST verifies removal of the gateway.

## 7. Other use cases (portfolio)
### AI-002 Enterprise generative AI assistant (Medium)
- **Why Medium:** internal productivity, but staff work daily with SRI, plant data, and licensing documents, so a data handling error or an unverified output could reach a regulator or a design document.
- **AI 600-1 risks considered:** confabulation (invented references or values in drafts of NRC correspondence or procedures), information security (prompt injection through shared documents), data privacy, and value chain (vendor model changes).
- **Controls:** enterprise terms with no training on company data and a tenant data boundary; cleared for Internal and Confidential data only; Restricted information, SGI, and export-controlled technology are excluded (POL-04 4.3); outputs used in regulated documents go through the normal document review; public generative AI sites blocked at the web proxy by 2026-12-31 (R-022); training module before access.
- **Measure:** monthly sample of 20 prompts from the audit log for Restricted content (target 0) once labels are live (2027-01-31).

### AI-003 CAP screening assistant (Medium)
- **Why Medium:** it influences a regulated process. Corrective action measures must make sure that conditions adverse to quality are promptly identified and corrected, and that significant conditions get a cause determination and corrective action (10 CFR 50 Appendix B, Criterion XVI). The screening committee decides every classification, so the tool is not a substantial factor in a decision about a person.
- **Measure (2026-05 to 2026-08, 412 non-security reports):** the suggestion matched the committee's final significance level in 364 of 412 (88%). It suggested a lower level than the committee in 9 of 412 (2.2%), all corrected by the committee. No significant condition was missed.
- **Conditions (2026-12-31; R-024):** security-related condition reports are excluded from the assistant entirely (they can contain SRI, and 73.77(b) entries must not depend on it); screeners record their own classification before the suggestion is shown, to limit over-reliance; monthly agreement audit with a threshold of no more than 2% under-classification.

### AI-004 Applicant ranking feature (High)
- **Why High:** employment is a consequential decision category in the rubric, and the ranking could be a substantial factor in who gets an interview.
- **Findings:** the vendor turned the feature on by default in 2026-03. Recruiters say they review all applications, but no rule or record shows it. No adverse impact analysis exists.
- **Laws:** Title VII of the Civil Rights Act of 1964 (disparate impact); the Uniform Guidelines on Employee Selection Procedures, under which a selection rate for any race, sex, or ethnic group less than four-fifths of the rate for the group with the highest rate is generally regarded by federal enforcement agencies as evidence of adverse impact (29 CFR 1607.4(D)); the Americans with Disabilities Act for accommodation in the application process. Counsel is reviewing whether out-of-state applicants bring any state AI employment law into scope (for example Colorado SB26-189, effective 2027-01-01); keeping the feature off avoids the question for now. The ranking never substitutes for the 10 CFR 73.56 access authorization determination for jobs that need unescorted access.
- **Decision:** **disable by 2026-10-31** (R-023; POAM-021). Re-enable only if: the vendor supplies selection data by group and the company's analysis shows no adverse impact under the four-fifths rule and a statistical test; a written rule requires recruiter review of every applicant who meets minimum qualifications; applicants are told that an automated tool is used and how to request an accommodation; and the HR Director re-runs the analysis every 6 months.

### AI-005 Power price forecasting (Medium)
- **Why Medium:** it influences business decisions; traders make every schedule decision. Outage dates are set by the plant organization, never by the forecast.
- **Measure:** monthly forecast error against settled prices, reviewed by the Energy Marketing and Settlements Manager.
- **Decision:** approve. The risk of poor schedules and imbalance charges is Low and accepted under the fixed-price PPAs (R-025). Vendor review as Tier 2 (P09 VEN-10).

## 8. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions**; no new assets until met | Security conditions 1 to 5 in section 6 (2026-11-30); vendor retraining plan for heater drain pumps (2026-11-30); model version and override logging (2026-10-31); recall of at least 80% for 2 consecutive quarters before expansion | Site Vice President, 2026-09-17, on the AI review group's recommendation |
| AI-002 | **Approve** for Internal and Confidential data | Training before access; public AI sites blocked (2026-12-31); prompt audit after labels go live (2027-01-31) | AI review group, 2026-09-15 |
| AI-003 | **Approve with conditions** | Exclude security-related reports; screener-first workflow; monthly audit (2026-12-31) | AI review group, 2026-09-15 |
| AI-004 | **Disable** | Off by 2026-10-31; re-enable only after the analysis and rules in section 7 | Site Vice President, 2026-09-17; CEO informed |
| AI-005 | **Approve** | Monthly forecast error review; Tier 2 vendor review | AI review group, 2026-09-15 |

The conditions are tracked as POAM-021 in P07 (AI governance), with the AI-001 security conditions also under POAM-019, POAM-003, and POAM-006, and in the risk register (P01 R-020 to R-025). STD-05, the AI use standard, is due 2026-12-31. The AI review group holds its first monthly meeting on 2026-10-06.

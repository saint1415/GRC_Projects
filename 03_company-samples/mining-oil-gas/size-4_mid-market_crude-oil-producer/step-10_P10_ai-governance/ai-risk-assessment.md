# AI Governance Risk Assessment: AI Use-Case Portfolio

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed independent crude oil producer with a Panhandle gathering system) |
| Tier / Vertical | Mid-Market / Mining, Quarrying, and Oil and Gas Extraction |
| Scope | Portfolio of 5 AI use cases (AI-001 to AI-005), inventory in `ai-use-case-inventory.csv`. AI-001, the predictive maintenance model for well equipment, is the registry use case and gets the deepest review |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook, with the Generative AI Profile (NIST AI 600-1) for AI-002 |
| Assessors / date | Production Engineering Manager (AI review chair), Security Manager, OT Security Engineer, General Counsel, with the Control Room Manager and Pipeline Compliance Manager for AI-003 and the HR Director for AI-004; 2026-08-24 to 2026-09-10 |
| Decision | Chief Operating Officer, with the VP Operations agreeing for AI-001 and AI-003, 2026-09-16; High-tier decisions noted by the CEO |

## 1. Summary
The company had AI policy statements (2026) but no AI inventory before this assessment (gap 13 in `../00_company-facts.md`). The inventory found 5 use cases. None of them can command field equipment, but two touch safety or employment closely enough to be rated High:
- **AI-001, predictive maintenance:** went into production in the Panhandle and Alabama without completed bias testing. Testing now shows it serves South Florida wells much worse than the rest.
- **AI-002, the enterprise generative AI assistant:** works as designed, but it can surface files that were over-shared years ago, including 6 folders with Restricted data.
- **AI-003, gathering line leak analytics:** is advisory, but controllers dismissed almost all of its alerts, and they were never trained on how to use it.
- **AI-004, HR candidate screening:** is licensed and switched off; no adverse impact test exists.
- **AI-005, ERP invoice coding:** is low risk, with a human approving every invoice.

| ID | Use case | Risk tier | Decision |
|---|---|---|---|
| AI-001 | Predictive maintenance model for well equipment | Medium | Approve with conditions; South Florida stays in shadow mode |
| AI-002 | Enterprise generative AI assistant (300 users) | Medium | Approve with conditions; no expansion until over-sharing is fixed |
| AI-003 | Gathering line leak analytics (vendor add-on) | High | Approve with conditions; advisory only, never clears an alarm |
| AI-004 | HR candidate-screening feature | High | Keep switched off (risk avoided, P01 R-034) |
| AI-005 | ERP invoice coding suggestions | Low | Approve |

Tiers: 2 High, 2 Medium, 1 Low.

## 2. GOVERN
- **Accountable owner for the AI program:** the Production Engineering Manager chairs the AI review group, supported by the Security Manager. Each use case has a business owner (inventory).
- **Policies:**
  - POL-01 4.15: AI tools must be approved before use; no AI may write to SCADA or field devices; no AI employment decision without human review.
  - POL-04 4.9: no Restricted or Confidential data in AI tools that are not approved for that data level.
  - POL-05 4.10: approved tools only; human review of outputs; no AI changes to SCADA settings; no AI ranking of employees without HR review.
  - STD-05 AI use standard: due 2026-12-31.
- **Approved-tools list:** kept by the Security Manager on the intranet. Today it lists AI-001, AI-002, AI-003, and AI-005 with their data levels and conditions, and lists AI-004 as "not approved".
- **Risk method:** AI risks are rated with the same SP 800-30 tables as every other risk and recorded in the risk register (P01 R-031 to R-034).

### 2.1 Proposed lightweight AI governance process
An 850-person producer does not need a standing AI committee with a large charter. It needs a short, reliable gate that uses existing roles and meetings.

| Step | What happens | Who | Time |
|---|---|---|---|
| 1. Intake | Anyone who wants an AI tool, or an AI feature switched on in an existing tool, submits a one-page intake: purpose, users, data, vendor, decisions affected, any connection to OT | Requesting business owner | 15 minutes |
| 2. Triage | The Security Manager assigns a provisional tier with the rubric and checks the purchasing gate (POL-01 4.9). Any proposal that touches OT data also goes to the OT Security Engineer | Security Manager | 2 business days |
| 3. Review | **Low:** security checklist only. **Medium:** security, data terms (no training on company data, retention), and a business reviewer. **High:** full MAP and MEASURE review like this one, with a bias and performance plan; operational AI adds the Control Room Manager or Pipeline Compliance Manager; employment AI adds the HR Director and General Counsel | Security Manager; General Counsel; business reviewer | Low 1 week; Medium 2 weeks; High 4 weeks |
| 4. Decide | Low: Security Manager. Medium: the **AI review group** (Production Engineering Manager, Security Manager, General Counsel), meeting monthly for 30 minutes. High: the AI review group recommends, the COO decides (with the VP Operations for field AI), and the CEO is informed | As listed | Monthly |
| 5. Monitor | Owner reports the agreed metrics monthly (Medium) or monthly with a quarterly deep dive (High); incidents go to P08 | Business owner | Ongoing |
| 6. Re-review | Annually, or on a trigger: a new feature, a model change, new data, expansion to a new area or population, or a safety or measurement event | AI review group | Annual |

**Tier rubric:** the repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`. Re-tier triggers are listed for each use case in section 3.1.

## 3. MAP
| Item | AI-001 Predictive maintenance | AI-002 AI assistant | AI-003 Leak analytics | AI-004 Candidate screening | AI-005 Invoice coding |
|---|---|---|---|---|---|
| Purpose | Predict rod pump and ESP failures up to 30 days ahead so engineers can schedule well servicing rigs to the wells most likely to fail | Draft, summarize, and search documents and email | Flag possible leaks on the gathering trunk line and 3 metered laterals from pressure and flow patterns | Rank applicants for field roles by resume match | Suggest general ledger account, cost center, and authority for expenditure (AFE) for vendor invoices |
| Users | 8 production engineers; rig supervisors see the resulting work orders | 300 licensed office users | 14 Production Controllers | HR recruiters (if enabled) | 6 payables clerks |
| Affected people or operations | Rig schedules and field routes; production; royalty owners and partners indirectly. No decisions about individuals | Employees; anyone named in files | Public and environment near the gathering system, including the drinking water unusually sensitive area | Applicants (about 1,100 a year for field roles) | Vendors; 22 partners through joint interest billing |
| Data | Hourly historian data from the cloud replica (pump cards, motor current, runtime, pressures, rates); 3 years of ERP work orders with technician names removed; no personal information | Any file the user can open, including Restricted data in over-shared folders | Real-time pressure and flow from the SCADA historian | Resumes and application answers (personal information) | Vendor invoices and coding history |
| Build or buy | Built by 2 production data engineers with a contracted data science firm on the cloud ML workspace; company owns the model | Buy (productivity suite feature, enterprise terms) | Buy (vendor add-on to the SCADA historian, installed in the OCC) | Buy (HR and payroll SaaS feature) | Buy (ERP SaaS feature) |
| Generative AI? | No (gradient-boosted classifier) | Yes | No (statistical and machine learning model) | Vendor states a machine learning ranking model | No (classification on coding history) |
| Connection to OT | Read-only and indirect: reads the historian replica in the OT data account; no route to the SCADA network | None | Runs on the OCC historian server inside the SCADA network; read-only; writes advisory alerts to HMIs only | None | None |
| In production | 2026-03 (Panhandle and Alabama, about 310 wells); South Florida (about 110 wells) in shadow mode | 2026-02 | 2026-04 | Licensed 2025-11; switched off | 2026-05 |

**Applicable laws and rules:**
| Rule | Applies to | Why |
|---|---|---|
| Sector AI rules (oil and gas) | None | None identified for this vertical (`02_industry-rules/mining-oil-gas/overlay.md`) |
| 49 CFR Part 195 | AI-003 context only | The leak analytics tool is voluntary. 195.11(b) does not list leak detection among the requirements for regulated rural gathering lines (verified on eCFR, 2026-09-23 version). The tool is not used to meet any Part 195 duty, and it never replaces the pressure and flow alarms, line riders, or the 1-hour notice under 195.52 |
| Title VII of the Civil Rights Act (42 U.S.C. 2000e-2) and the Uniform Guidelines on Employee Selection Procedures (29 CFR Part 1607) | AI-004 | A selection tool that has an adverse impact on a protected group must be job-related. Under 29 CFR 1607.4(D), a selection rate for any race, sex, or ethnic group below four-fifths of the rate for the highest group is generally regarded by federal enforcement agencies as evidence of adverse impact. Users should keep records of impact by group (1607.4(A)) |
| State AI laws (for example Colorado SB26-189, effective 2027-01-01) | AI-004 if ever enabled | The company operates and hires in Florida and Alabama, and this assessment found no Florida or Alabama AI-specific statute for these uses. Colorado's law would matter only if the company hired for Colorado roles. General Counsel rechecks before any AI-004 decision, because these laws change often |
| Fla. Stat. 501.171(2) | AI-002, AI-004 | Personal information reachable through the assistant, or held in the screening feature, must be protected by reasonable measures |
| FTC Act Section 5 | All | Applies to what the company says about its tools (for example to shippers, lenders, or partners); describe accuracy honestly |
| Contracts | AI-001, AI-002, AI-003, AI-005 | Data science firm and vendor terms: data use, no training on company data, ownership, security, deletion |

### 3.1 Risk tiers and re-tier triggers
| ID | Tier | Why this tier | Re-tier triggers |
|---|---|---|---|
| AI-001 | **Medium** | It reorders a maintenance queue that an engineer approves, and it has no path to SCADA. A missed failure leaves the company where it was without the model: the pump fails, the well stops, and the hardwired shutdowns still work. It is not Low because it decides where limited rig time goes, and a blind spot leaves a group of wells under-served | Any automatic action on equipment; use to defer inspection of safety-critical equipment; use to rank or evaluate lease operators (employment); adding telematics or other personal information (re-tier to High) |
| AI-002 | **Medium** | Office productivity with no decisions about individuals, but it can reach Restricted data (owner personal information, seismic data) through over-shared folders | Use in regulatory filings, owner communications, or employment decisions; connection to OT documents marked Restricted |
| AI-003 | **High** | The rubric puts AI that "can affect physical safety or critical infrastructure operations" at High. The tool does not control anything, but controllers' trust in it can speed up or slow down their response to a possible release near a drinking water unusually sensitive area (P01 R-033) | Any automatic shutdown or alarm suppression by the tool would need a new assessment and is prohibited today |
| AI-004 | **High** | A substantial factor in employment decisions if enabled | n/a (already High) |
| AI-005 | **Low** | Suggestions only; a clerk approves every invoice; no decisions about individuals | Auto-approval of invoices, or use of suggestions without review (re-tier to Medium) |

## 4. MEASURE
### 4.1 AI-001: performance and bias testing plan
"Harmful bias" here means the model systematically serves some wells worse than others. Rig time is limited, so under-served wells fail more often and wait longer for repair, which costs production and royalties.

- **Groups compared:** operating area (Panhandle, South Florida, Alabama); lift type (rod pump, ESP); communications path and data rate (radio sites polled every minute versus cellular sites polled every 15 minutes); well age (drilled before or after 1990); sour versus sweet service.
- **Metrics:** recall (failures flagged at least 3 days ahead), precision (alerts that were real failures), and false alert rate, per group, computed quarterly on a rolling 12 months of labeled failures.
- **Thresholds:** overall recall at least 60% and precision at least 35%. Flag a group if its recall is more than 15 points below the overall rate or its false alert rate is more than 10 points above. Groups with fewer than 5 failures in the window are reported but not flagged, and watched the next quarter.
- **Workforce check:** each quarter the review confirms that no report ranks lease operators, routes, or crews by model alerts.

**Results, 2026-03 to 2026-08:**
| Group | Failures | Flagged ahead | Recall | Flag? |
|---|---|---|---|---|
| All live wells (Panhandle and Alabama) | 74 | 47 | 64% | Pass (precision 42%: 47 of 112 alerts) |
| Panhandle rod pump | 47 | 32 | 68% | No |
| Panhandle ESP | 15 | 9 | 60% | No |
| Alabama rod pump | 8 | 4 | 50% | No (within 15 points; watch) |
| Alabama ESP | 4 | 2 | 50% | Reported only (fewer than 5 failures) |
| South Florida ESP (shadow mode) | 19 | 6 | 32% | **Yes** |
| South Florida rod pump (shadow mode) | 6 | 2 | 33% | **Yes** |

**Why South Florida fails the test:** 80% of the training history is Panhandle data, and South Florida's cellular sites send data every 15 minutes rather than every minute, so the model sees much less detail. The fix is retraining with South Florida history at its native data rate and, where the business case holds, faster polling.

### 4.2 Portfolio results
| Use case | Trustworthy characteristic | Test or metric | Threshold | Result (2026 sample) | Pass? |
|---|---|---|---|---|---|
| AI-001 | Valid and reliable | Recall and precision on live wells | Recall at least 60%; precision at least 35% | 64% and 42% | Yes |
| AI-001 | Fair, with harmful bias managed | Recall by group (section 4.1) | No group more than 15 points below overall | South Florida 32% and 33% | **No**: shadow mode continues |
| AI-001 | Safe | No write path to SCADA; alerts never used to defer safety equipment inspections | Both true | Network rules confirm no route from the ML workspace to SCADA; inspection schedules unchanged | Yes |
| AI-001 | Accountable and transparent | Model card with purpose, data, limits, and version | Published to engineers | Not written | **No** |
| AI-001 | Secure and resilient | Data science firm contract: security terms, no reuse of company data, deletion at contract end | All in contract | Security terms present; deletion clause missing | Partial |
| AI-001 | Explainable and interpretable | Each alert shows the top contributing signals | Available | Available | Yes |
| AI-002 | Privacy-enhanced | Folders with company-wide access that hold Restricted data | 0 | 41 of 1,240 sites and folders shared company-wide; 6 hold Restricted data (2 owner deck exports, 3 seismic interpretation folders, 1 OT network diagram folder) | **No** |
| AI-002 | Secure and resilient | Test user with no special access runs 20 prompts | No Restricted content returned | 3 of 20 prompts returned content from the over-shared folders | **No** |
| AI-002 | Valid and reliable (confabulation, AI 600-1) | 30 summaries of regulatory or contract text checked against the source | No wrong citations in material used externally | 4 of 30 contained a wrong section number or date | Partial: rule added that outputs are never used in filings or notices without checking the source |
| AI-002 | Privacy-enhanced (data use) | Enterprise terms prohibit training on company data | Contract term | Confirmed in the license terms | Yes |
| AI-003 | Valid and reliable | Controlled withdrawal test at about 2% of trunk line flow (2026-06-24) | Detection within the vendor's stated time | Detected in 34 minutes, within the stated time | Yes |
| AI-003 | Safe (over-reliance) | Alerts dismissed without a written reason; analytics used to clear an alarm | 0 dismissals without reason; never clears an alarm | 63 alerts (2026-04 to 2026-08), 0 confirmed leaks; 61 dismissed, 19 without a reason; no case of clearing an alarm found | **No** |
| AI-003 | Fair, with harmful bias managed (coverage) | Segments covered | Coverage known and documented | Covers the 14-mile trunk line and 3 metered laterals; unmetered laterals are not covered, which controllers did not know | Partial: coverage map added to the OCC HMI |
| AI-003 | Secure and resilient | Runs inside the SCADA network; vendor updates only through the CAB and the jump host | Both true | Both true | Yes |
| AI-004 | Fair, with harmful bias managed | Adverse impact test by sex and race and ethnic group using 29 CFR 1607.4 | Selection rate of every group at least four-fifths of the highest | Not performed; vendor supplied no impact data | **No**: feature stays off |
| AI-005 | Valid and reliable | 200 invoices sampled (2026-07) | Less than 2% of miscodings reach joint interest billing | 186 coded correctly; 14 corrected by clerks; 2 wrong AFE codes reached partner billing (1%) and were corrected the next month | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** the model produces a ranked alert list only. A production engineer reviews each alert and its contributing signals and decides whether to create a work order. Dismissals need a reason and are reviewed monthly. The rig supervisor and the engineer still set the rig schedule.
- **AI-002:** users review every output. Outputs are never used in a regulatory filing, a notice, or an owner, shipper, or partner communication without checking the source.
- **AI-003:** advisory only. **The tool never clears or suppresses an alarm.** A controller who dismisses an alert records a reason; the Control Room Manager reviews dismissed alerts monthly. Pressure and flow alarms, line riders, and the pipeline emergency procedures remain the primary means of detection.
- **AI-004:** switched off. If ever proposed again, a recruiter would have to review every application, and no applicant could be rejected by the tool alone.
- **AI-005:** a clerk approves every invoice coding, and the existing approval workflow is unchanged.

**Monitoring:** owners report the section 4 metrics monthly to the AI review group. AI-003 gets a quarterly deep dive with the Pipeline Compliance Manager and the vendor. Results feed the risk register (P01 R-031 to R-034).

**Security:**
- AI-001 reads only the historian replica in the OT data account. Any proposal to connect it to the SCADA network is out of scope and needs a new assessment (POL-02 4.12).
- AI-003 vendor updates go through the CAB and the jump host like any other SCADA change (STD-02, STD-04).
- AI-002 expansion beyond 300 users waits until over-shared folders are fixed and Restricted folders are labeled (P01 R-032).

**Incident handling:** a security incident affecting the ML workspace, the historian replica, or an AI vendor follows P08. If AI-003 misses a real release or delays a response, the event is reviewed by the Pipeline Compliance Manager under the pipeline emergency procedures and recorded in the risk register.

**Decommissioning criteria:**
- AI-001: stop and archive if live recall falls below 50% for 2 consecutive months, or if the data science firm's contract is not amended by 2026-11-30.
- AI-002: suspend for any user group where a test prompt returns Restricted data after the 2026-12-31 cleanup.
- AI-003: remove from the HMIs if the vendor changes the model without going through the CAB, or if dismissals without a reason continue after training.
- AI-004: remains off; the license is not renewed if no adverse impact data is available by renewal.
- Any tool: stop if the vendor changes data-use terms or the model changes without notice.

## 6. Decisions
| Use case | Decision | Conditions and due dates | Decided by |
|---|---|---|---|
| AI-001 | **Approve with conditions** for the Panhandle and Alabama | South Florida stays in shadow mode until its recall is within the bias threshold for 2 consecutive quarters; model card published (2026-10-31); data science firm contract amended with a deletion clause (2026-11-30); quarterly bias report in the engineering calendar | COO with the VP Operations, 2026-09-16 |
| AI-002 | **Approve with conditions**; no expansion | Fix the 41 company-wide shares, starting with the 6 Restricted folders (2026-11-30); sensitivity labels on Restricted folders (2026-12-31); filing and notice rule in POL-05 4.10 | AI review group, 2026-09-16 |
| AI-003 | **Approve with conditions** | Controller procedure: analytics never clear an alarm, and every dismissal has a reason (2026-10-31); controller training (2026-11-30, POAM-017); coverage map on the HMI (done); monthly dismissed-alert review; vendor performance report each quarter | COO with the VP Operations, 2026-09-16; noted by the CEO |
| AI-004 | **Do not enable** | Stays off with a feature-change alert in the HR system; any future proposal needs a full High-tier review, an adverse impact test under 29 CFR 1607.4, applicant notice, and human review of every application; decision point 2027-03-31 | COO, 2026-09-16; noted by the CEO |
| AI-005 | **Approve** | Monthly 50-invoice accuracy sample; confirm no-training terms with the ERP vendor (P09 VEN-03) | Security Manager, 2026-09-16 |

The conditions are tracked as POAM-022 in P07 and in the risk register (P01 R-031 to R-034). The AI review group holds its first monthly meeting on 2026-10-07.

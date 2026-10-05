# AI Governance Risk Assessment: Group AI Program and Dam-Safety Sensor Anomaly Detection

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Hydro, Constructors, Engineering, and corporate shared services) |
| Tier / Vertical | Multi-Sector / Dams |
| Scope | The group AI governance program (group standard, the division use-case inventory, regulator-specific rules) and a full assessment of **AI-001, dam-safety sensor anomaly detection**: built and run by Engineering in the DSMS, relied on by Hydro for 68 dams and piloted with 19 external clients |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the AI RMF Playbook; NIST AI 600-1 for the generative use cases (AI-007, AI-008). NIST released a concept note for an AI RMF Critical Infrastructure Profile on 2026-04-07; it is not final and is not relied on here |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-08-27; presented to the board safety, risk, and reliability committee 2026-09-10 |
| Inventory | `ai-use-case-inventory.csv` (10 use cases: 3 High, 6 Medium, 1 Low; 6 reviewed by the council, 4 not yet) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board safety, risk, and reliability committee | Oversees AI risk with dam safety and cyber risk; receives the High-tier list and AI-001 condition status quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, General Counsel, Chief Dam Safety Engineer, Chief Engineer, Director of Data Science, a Constructors operations vice president. Approves High-tier use cases, material changes, and the approved-tools list |
| Division AI owners | Business owner for each use case (inventory column); run monitoring and report metrics |
| Vice President, Dam Safety (Chief Dam Safety Engineer) | Owns every decision about Hydro dam safety, including how much Hydro relies on AI-001. Keeps that authority even though Engineering builds the model (00_company-facts.md section 2) |
| Director of Data Science | Builds, validates, and runs AI-001; may not release model or threshold changes without the change control in POAM-012 |
| Group CISO | AI security rules: data leakage, model supply chain, prompt injection for generative tools |
| General Counsel | Contract terms, performance claims, state AI and monitoring laws |
| Group internal audit | Adds High-tier AI controls to the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2025, under POL-01 4.13)
1. **Register before use.** Any AI system that supports dam safety, grid operations, safety of workers or the public, or decisions about people is registered and approved before deployment or material change (POL-01 4.13).
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, performance-disparity testing, and quarterly monitoring reports.
3. **Data rules.** CUI, BCSI, and client CEII never go into external AI services; Restricted data only into tools approved for that class (POL-04 4.9; POL-05 4.9).
4. **Material change gate.** A new model version, new threshold logic, a new client population, or **any change in how much people rely on the output** is a material change that needs re-approval.
5. **Never in the control loop.** No AI output may write to OT, issue gate or unit commands, or trigger EAP notifications or regulatory reports automatically.
6. **Regulator overlays in the division supplements:** FERC Part 12 and the ODSP for Hydro; NDAs and licensure for Engineering; CUI and owner terms for Constructors.

**Where the program fell short in 2026.**
- Hydro moved 31 dams from weekly to monthly manual readings in 2026-02 on the strength of AI-001 alerts. That was a material change in reliance under rule 4, but it went to neither the council nor the ODSP annual review (P03 G-002 and G-077).
- 3 AI-001 model releases went to production before 2026-08 without a defined validation test (P07 SA-11).
- 4 use cases started without council review: AI-004, AI-005, AI-006, and AI-010.

## 2. MAP
### 2.1 Use cases by division
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Dam-safety sensor anomaly detection (DSMS) | Engineering (used by Hydro) | High | In production with conditions; pilot expansion paused |
| AI-002 | Inflow and reservoir forecasting | Hydro | High | Approved 2025-11; in production |
| AI-003 | Unit condition monitoring | Hydro | Medium | Approved 2026-03; 22 plants |
| AI-004 | Inspection imagery defect detection | Engineering | High | In use without review; council 2026-11-19 |
| AI-005 | Jobsite computer vision safety cameras | Constructors | Medium | Pilot at 12 jobsites without review; council 2026-11-19 |
| AI-006 | AI estimating assistant | Constructors | Medium | In use without review; council 2026-11-19 |
| AI-007 | Engineering drafting assistant | Engineering | Medium | Approved 2026-05 with conditions |
| AI-008 | Enterprise generative AI assistant | Group | Medium | Approved 2026-04 for selected roles |
| AI-009 | Coding assistant | Group | Low | Approved 2026-04 |
| AI-010 | SOC alert triage assistant | Group | Medium | Enabled 2026-06 without review; OT alert data excluded |

### 2.2 AI-001 in context
| Item | Description |
|---|---|
| Purpose and intended use | Watch about 14,900 instruments (about 4,600 at the 68 Hydro dams) for patterns that suggest a developing failure mode, such as rising pore pressure after a reservoir rise, seepage changes after rain, or deformation trends, earlier than periodic manual review |
| Users | Hydro dam safety engineers and technicians; Engineering's monitoring staff; dam safety engineers at the 19 pilot clients |
| Affected people | No one is the subject of a decision. The people who bear the risk live downstream: for example, a city of about 52,000 within 5 to 18 miles of DEV-02 and a town of about 9,000 within 3 to 11 miles of DEV-05, plus recreation users and staff |
| Data | Inputs: automated readings (mostly hourly or more often), manual readings entered by technicians, rainfall, reservoir and tailwater levels. Outputs: an alert score and the instruments and readings that drove it. Trained on historical readings from Hydro and consenting client dams, with 51 documented events used for the back-test |
| Build or buy | Built by Engineering (Director of Data Science), running in the DSMS on cloud provider A |
| Not intended (prohibited) | Replacing trigger-point checks or manual review schedules; deciding whether to report under 18 CFR 12.10; deciding EAP actions; any control action; reducing the instrument reading program filed with the Regional Engineer |
| Cross-division shape | Engineering is the **developer and operator**; Hydro and each client are **deployers** responsible for their own dams. Hydro treats Engineering as an intercompany service provider, with the same contract terms and SOC 2 evidence as outside clients (P09) |

### 2.3 Rules that apply to AI-001
| Rule | Applies? | What it means here |
|---|---|---|
| 18 CFR 12.10(a); 12.3(b)(4)(viii) (C-DAMS-R02) | **Yes, at Hydro** (and at each FERC-licensed client for its own dams) | Unusual instrumentation readings are conditions affecting safety, reported to the Regional Engineer as soon as practicable after discovery, preferably within 72 hours. An AI alert a person confirms as unusual starts the 12.10 decision. An AI "no anomaly" never overrides a reading past a trigger point |
| 18 CFR 12.51 | Yes, indirectly | Monitoring instrumentation must be satisfactory to the Regional Engineer. AI-001 adds analysis; it replaces no instrument or reading the Regional Engineer relies on |
| 18 CFR 12.62(d)(3) and 12.64 (ODSP) | **Yes** | The owner keeps ultimate responsibility for dam safety when work is delegated, and the ODSP and its implementation are reviewed at least annually with results sent to the Regional Engineer. The 2026-02 reading change belongs in that review (G-077) |
| FERC Security Program Rev. 3A Sec. 3.2 (C-DAMS-R01) | Yes | Trigger points for action from critical dam safety instrumentation must be defined. They stay defined and checked by people (G-002) |
| FERC Security Program Section 9 | Yes | The DSMS receives data from Hydro plants whose gate control is Critical. The two-way replication at 17 plants is part of gap 3; AI-001 must not create any return path |
| DSMS client contracts (security schedule sec. 7; AI-001 pilot addendum) | Yes | Notice before material changes to alerting logic (EG-005, not met); description of what the model does and does not do (EG-007, partially met) |
| FTC Act Sec. 5 (15 U.S.C. 45(a)) | Yes, for Engineering as seller | Performance claims must be truthful and substantiated. A 2025 brochure says the model never misses a seepage event; the back-test does not support that (EG-015) |
| State AI laws on consequential decisions (for example Colorado SB26-189, effective 2027-01-01) | No | AI-001 makes no decision about a person in any covered category |

### 2.4 Regulator-specific rules for the other use cases
| Use case | Rule | Implication |
|---|---|---|
| AI-002 forecasting | License operating conditions (per project); EAPs (18 CFR 12.20, 12.22) | Forecasts inform releases; flood operations stay under the license rules and EAP procedures. No automatic link to gate commands |
| AI-003, AI-010 | NERC CIP-011-3 (BCSI) and CIP-013-2 (supply chain) | Vendors that receive OT data or alerts must have BCSI handling and CIP-013 procurement terms. AI-010 was enabled by a SIEM product update without that check, so OT alert data is excluded until review |
| AI-004 imagery | 18 CFR 12.35 and 12.36 (Part 12D inspections for other licensees); client NDAs with CEII terms (18 CFR 388.113 passed through by contract) | The independent consultant owns every finding; the tool may not narrow what inspectors look at. Imagery held by the vendor needs CEII terms (EN-013) |
| AI-005 cameras | Collective bargaining agreements; state employee monitoring and biometric laws in each state where cameras are used (counsel review) | Facial recognition stays disabled. If alerts are ever used for discipline, re-tier to Employment and review state AI employment laws (for example Colorado SB26-189) |
| AI-006 estimating | Owner NDAs; POL-04 4.9; DFARS 252.204-7012 (N23-R03) | No CUI or owner CEII in the vendor tool; federal bids stay in the FPE |
| AI-007, AI-008 | State engineering licensure (generic); client NDAs; CIP-011-3; DFARS 252.204-7012(b) | The sealing engineer owns AI-assisted content (EG-019). DLP rules for CEII, BCSI, and CUI markings (GR-17) |

## 3. Risk tiers (repository rubric)
- **High:** AI-001, AI-002, and AI-004. Each can affect physical safety or critical infrastructure operations, even though none acts on its own.
- **Medium:** AI-003, AI-005, AI-006, AI-007, AI-008, AI-010. Outputs influence business or security decisions, or touch workers, but a person makes every final decision.
- **Low:** AI-009.

**Why AI-001 is High even though it only advises.** The realistic harm is a missed anomaly (false negative) while people look less often because they trust the tool. That has already happened in practice: 31 Hydro dams were moved to monthly readings on its strength.

**Re-assess before any of these:** a proposal to reduce manual reading or review frequency anywhere; a new model version or threshold logic; adding instrument types or client populations; any automatic link from AI-001 output to EAP notifications, 12.10 reports, or control actions; use of AI-005 alerts for discipline.

## 4. MEASURE
### 4.1 AI-001 results
Back-test on 51 documented historical events, plus production data from Hydro dams (2025-10 to 2026-07) and the client pilot (2026-03 to 2026-07).

| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Back-test recall, target at least 95% overall | 47 of 51 (92%) | **No** |
| Valid and reliable | Median lead time vs manual review on detected events | 4 days earlier | Yes |
| Safe (automation bias) | Changes found on manual visits at the 31 monthly dams that AI-001 had not flagged (target 0) | 2 (a clogged weir reading as stable; an inclinometer drift) | **No** |
| Safe | Share of Hydro alerts dispositioned within 24 hours (target 100%) | 86% | **No** |
| Secure and resilient | Model releases with a documented validation test | 0 of 3 releases before 2026-08 (P07 SA-11) | **No** |
| Secure and resilient | No return path from the DSMS to OT | Two-way replication at 17 plants (gap 3; POAM-005) | **No** |
| Accountable and transparent | Every alert logged with a disposition; threshold and model changes recorded | Alerts logged; 41 threshold changes in 2026 without change records (P07 CM-03) | **No** |
| Accountable and transparent | Client materials state limits and the back-test rate | Addendum incomplete (EG-007); brochure overclaims (EG-015) | **No** |
| Explainable and interpretable | Each alert names the instruments and readings that drove it | Yes for all alerts | Yes |
| Privacy-enhanced | No personal information in inputs or outputs | None | Yes |
| Fair, with harmful bias managed | Performance by event type, reading frequency, data owner, and season (plan below) | Deformation 8 of 10 (80%); daily-or-less-frequent instruments 3 of 5 (60%); high-water-season false alarms 2.6 times the dry-season rate | **Flagged** |

### 4.2 Performance-disparity ("bias") testing plan for AI-001
For this use case, bias means the model watching some failure modes, instrument types, or dams less well than others. It makes no decision about people, so demographic fairness metrics do not apply. What matters is whether any part of any dam is watched less well than people assume.

| Group compared | Metric | Threshold | Current result | Frequency |
|---|---|---|---|---|
| Event type: seepage, piezometric (pore pressure and uplift), deformation | Recall on documented and seeded events | At least 90% in every group; at least 95% overall | Seepage 18 of 19 (95%); piezometric 21 of 22 (95%); deformation 8 of 10 (80%) | Before every release; quarterly |
| Reading frequency: hourly or more often vs daily or less often | Recall; missing-data rate | No group more than 10 points below overall | Hourly or more 44 of 46 (96%); daily or less 3 of 5 (60%) | Before every release; quarterly |
| Data owner: Hydro dams vs client dams (and clients with under 3 years of history) | Recall; alert-to-confirmation ratio | No group more than 5 points below overall | Hydro 31 of 33 (94%); clients 16 of 18 (89%) | Quarterly |
| Season: high-water months vs dry months | False alarms per dam per week; recall | High-water false alarms no more than 2 times dry; recall within 5 points | False alarms 2.6 times | Each season |
| Dam type: embankment vs concrete | Recall; false alarms | No group more than 5 points below overall | Not yet measured; test set being labeled | First test by 2026-12-31 |
| People (automation bias) | Manual readings on schedule; alerts dispositioned in 24 hours; review time per alert | 100%; 100%; median not below 10 minutes | Weekly readings stopped at 31 dams; 86% within 24 hours | Monthly |

**Findings.** The model misses deformation trends and instruments read infrequently because it sees too little data from them. The fix is not to rely on it there: label deformation instruments and low-frequency instruments "limited AI coverage" in the DSMS until recall meets the threshold. High-water false alarms risk alert fatigue exactly when dams are most loaded.

### 4.3 Other High-tier use cases
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-002 forecasting | Day-ahead inflow forecast error at the 10 largest developments (target: within the operating plan's tolerance on 90% of days) | 93% of days | Yes |
| AI-002 forecasting | Forecast used for any gate command without a person approving it (target 0) | 0 | Yes |
| AI-004 imagery | Recall on a labeled set of known defects; whether inspectors review all images | Not tested; review practice varies by team | **Not assessed** (council 2026-11-19) |

## 5. MANAGE
**Human-in-the-loop design for AI-001:**
- Every alert goes to an on-duty dam safety engineer or technician, who checks the instrument (and visits it if needed) and records a disposition in the DSMS within 24 hours.
- At Hydro dams, the Chief Dam Safety Engineer decides any action, 12.10 report, or EAP step. For client dams, the client's engineer decides; Engineering's monitoring staff only notify.
- Manual reading schedules, trigger-point checks, and rules-based thresholds run independently of AI-001 and do not change because of it. Any proposal to reduce them needs a new assessment, council approval, and inclusion in the ODSP annual review, after at least 12 consecutive months meeting every threshold in section 4.
- Anyone can override or ignore an AI-001 alert or "no alert" without justification; overrides are logged for learning, not for blame.

**Monitoring:** monthly metrics to the Chief Dam Safety Engineer and the DSMS General Manager; quarterly disparity tests and a High-tier report to the council and the board committee; P01 risks GR-05, HY-010, HY-026, EN-002, EN-003, and EN-016. Generative and other use cases: GR-17, EN-009, EN-010, EN-013, CN-011, CN-014.

**Change control:** thresholds and model versions are configuration items under POAM-012: dam safety impact review, a validation test against the back-test set and the disparity thresholds, approval, and client notice before release. This is also what the SOC 2 Type 2 period will test (P09 CC8.1, PI1.3).

**Incident handling:** a missed event later found by manual review is logged as an AI incident, analyzed within 10 business days, and reported to the council. It never changes the 12.10 decision for the underlying condition, which follows POL-03 and the P08 runbook. A DSMS security incident follows P08 and the 48-hour client notice.

**Decommissioning:** stop using AI-001 for any client or dam group if recall falls below 85% in a quarterly test, if the one-way data path cannot be kept, or if change control lapses. Rules-based thresholds and manual readings continue, and the readings stay in Hydro historians and client gateways, so nothing is lost by stopping (P05 BP-E02).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 | **Continue with conditions** (council 2026-08-27; board committee informed 2026-09-10). Pilot expansion beyond the 19 clients paused | (1) Weekly manual readings restored at the 31 dams by 2026-10-31 and the reliance reviewed in the ODSP annual review reported to the Regional Engineer by 2027-03-31 (POAM-025). (2) Change control for thresholds and models in operation by 2026-12-31 (POAM-012). (3) Deformation and low-frequency instruments labeled "limited AI coverage" by 2026-11-30. (4) Client addendum amended and the 2025 brochure withdrawn by 2026-11-30 (EG-007, EG-015). (5) High-water threshold tuning re-tested before 2027-03-31. (6) One-way data path at all 17 two-way plants by 2027-03-31 (POAM-005). (7) AI-001 included in the DSMS SOC 2 scope (P09) |
| AI-002 | **Continue** | Annual re-validation; confirm no automatic link to gate commands at every release |
| AI-003 | **Continue** | CIP-013 terms confirmed in the module vendor contract by 2026-12-31 |
| AI-004 | **Not yet approved; restricted use** | Inspectors must review every image until the council decides on 2026-11-19; recall test on a labeled set; CEII terms with the vendor (EN-013) |
| AI-005 | **Pilot frozen at 12 jobsites** | Counsel review of state monitoring and biometric laws; crew notice and union consultation records; council 2026-11-19 |
| AI-006 | **Restricted use** | No CUI or owner CEII until the council decides on 2026-11-19 |
| AI-007 | **Continue** | AI-assisted drafting rule in the quality checklist by 2026-12-31 (EG-019) |
| AI-008, AI-009 | **Approved** | DLP rules for CEII, BCSI, and CUI markings by 2026-12-31 (GR-17); AI-008 prohibited for dam safety, grid operations, and decisions about people |
| AI-010 | **Restricted use** | OT alert data excluded until BCSI and CIP-013 terms are confirmed; council 2026-11-19 |

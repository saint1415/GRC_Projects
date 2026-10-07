# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Crude Oil Production, Power Generation, Crude Logistics, corporate) |
| Tier / Vertical | Multi-Sector / Mining, Quarrying, and Oil and Gas Extraction |
| Scope | The group AI governance program: the Group AI Standard, the division use-case inventory, and the rules that bear on each use case, with the **predictive maintenance model for well equipment (AI-001)** as the priority use case. Also assessed in depth: computational leak detection (AI-005) and driver-facing camera AI (AI-006) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1) for AI-008 and AI-009, and the AI RMF Playbook; NIST SP 800-82 Rev. 3 for AI that touches OT |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-09-02; presented to the board risk committee 2026-09-17 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 3 High, 5 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group OT Security Director, Group General Counsel, Production HSE director, Power Generation and Crude Logistics operations representatives, Group HR director. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Group OT Security Director | Reviews any AI that reads from or writes to OT, including data paths across OT DMZs |
| Production HSE director and division safety leads | Safety management of change for any model that can change a setpoint, alarm, or operating limit |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-07-01, under POL-01 4.13)
1. **Register before use.** Every AI use case that can change physical operations, uses personal data, or supports decisions about people is registered in the inventory before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, testing against defined metrics, and quarterly monitoring reports. The rubric treats AI that can affect physical safety or critical infrastructure operations as High.
3. **Advisory by default in OT.** A model may recommend; it may not write setpoints, alarms, or limits to field, plant, or pipeline equipment unless the council approves and the division completes a safety management of change review. Any approved write path runs through the OT DMZ standard (no inbound path from the cloud; POL-02 4.5).
4. **Regulator overlays.** Each division supplement adds its regulator's rules: SPCC alarm duties for Production, CIP-003-9 vendor access for Power Generation, 195.446 alarm management and 49 CFR 390.36 for Crude Logistics.
5. **Change gate.** A new model, retraining on new data sources, new thresholds, or a new decision role triggers re-assessment before release.
6. **Approved tools only** for workforce generative AI (POL-05 4.7).

**Where the program fell short in 2026.** The standard was adopted after the priority use case was already acting on equipment. From 2026-06 the predictive maintenance model sent rod pump speed changes automatically at 640 Permian wells, through the SCADA interface, with no safety review, no change record, and no council approval (scenario gap 8). The camera AI scores were feeding driver discipline with no human review (gap 5). Both are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Predictive maintenance model for well equipment | Crude Oil Production | High | In production (advisory mode since 2026-09-03) |
| AI-002 | Production optimization recommendations | Crude Oil Production | Medium | In production |
| AI-003 | Seismic interpretation assistance | Crude Oil Production | Low | In production |
| AI-004 | Turbine anomaly detection (OEM) | Power Generation | Medium | In production |
| AI-005 | Computational leak detection with machine learning | Crude Logistics | High | In production |
| AI-006 | Driver-facing camera AI event scoring | Crude Logistics | High | In production with conditions |
| AI-007 | Route and load optimization | Crude Logistics | Medium | In production |
| AI-008 | Enterprise generative AI assistant | Group | Medium | Pilot (about 3,000 users) |
| AI-009 | SOC triage assistant | Group | Medium | Approved |

### 2.1 Predictive maintenance model (AI-001): purpose, people, data, context
- **Purpose:** predict rod pump and ESP failures from pump cards, motor current, and speeds, and lower pump speeds before damage occurs ("pump-off" and fluid pound control).
- **Users and people affected:** production engineers and controllers. No individual is the subject of a decision, but field crews and the public are affected if a model action leads to an unsafe condition or a release.
- **Data:** historian replicas pulled from the Production OT DMZ by the SYS-G6 connector (the same connector that is the top group risk, GR-01), and maintenance work orders from SYS-G4.
- **Build:** in-house on the group data platform. The write path used the SCADA interface's setpoint API.
- **Deployment context:** about 11,200 producing wells; 640 Permian wells in automatic mode from 2026-06 to 2026-09-03.

**Rules and duties that bear on AI-001** (no AI-specific law applies to it):
| Rule or duty | What it means for the model |
|---|---|
| SPCC high-level alarm option, 40 CFR 112.9(c)(4)(iv) | Speed changes alter fluid production into tanks. At about 250 batteries, overfill protection depends on high-level alarms reaching SCADA, so model actions must not mask or flood those alarms |
| Oil discharge notice, 40 CFR 110.6 | If a model action contributes to a release that reaches water, the immediate notice duty applies as for any release |
| Process safety management of change (company procedure, P06 Production supplement) | A model that writes setpoints is a change to the control system and needs the same review as a logic change (POAM-021) |
| NIST SP 800-82 Rev. 3 section 4.2.2 (safety systems) and section 5.2.3 (network security) | Safety functions must stay independent of the model; any write path from the cloud into OT must go through the OT DMZ design, not an inbound connection |
| Contracts with non-operating partners | Operating decisions affect partners' production; material changes in operating practice are reported to partners as the operating agreements require (counsel review) |

### 2.2 Computational leak detection (AI-005): pipeline rules
| Rule | Implication |
|---|---|
| 49 CFR 195.446(e) | Leak alarms are safety-related SCADA alarms. Model tuning that changes alarm thresholds or suppresses alarms falls under the written alarm management plan, including monthly review of inhibited or false alarms ((e)(2)) and the annual plan review ((e)(4)) |
| 49 CFR 195.446(c)(2) and (f) | Changes to the leak detection configuration that affect what controllers see need point-to-point verification and control room change management |
| 49 CFR 195.52, 195.54; 40 CFR 110.6 | A missed or late leak alarm delays the clock-starting discovery of a release; the notice duties do not wait for the model |

### 2.3 Driver-facing camera AI (AI-006) and route optimization (AI-007): driver rules
| Rule | Implication |
|---|---|
| 49 CFR 390.36 | A motor carrier may not use information from ELDs, or technology used with them, to harass a driver into violating hours-of-service rules. The camera and ELD data share one telematics platform; counsel is reviewing how far 390.36 reaches the camera features. Scores must never be used to pressure drivers on schedules |
| Federal anti-discrimination laws (for example, Title VII and the ADA) | Apply to employment decisions however they are made; a scoring tool that is less accurate for some drivers can create disparate impact in discipline |
| State biometric privacy laws | Apply only if the vendor uses face geometry to identify drivers; counsel is confirming the vendor's method for each state of operation (not verified in this sample) |
| 49 CFR Part 395 | Route plans must respect hours of service; dispatchers and drivers can override AI-007 |

### 2.4 Other use cases
- **AI-004** relies on the turbine OEM's remote access path, which is subject to CIP-003-9 Attachment 1 Section 6 at all three plants (and is the P3 gap, POAM-013).
- **AI-008** and **AI-009** are generative AI used on corporate data. AI 600-1 risks considered: data privacy (Restricted data entered in prompts), information security (prompt injection through documents and logs), and confabulation (wrong summaries relied on).

## 3. Risk tiers (repository rubric)
- **High:** AI-001 and AI-005 (can affect physical safety and critical infrastructure operations); AI-006 (substantial factor in employment decisions about drivers).
- **Medium:** AI-002, AI-004, AI-007, AI-008, AI-009. Humans make the final decision, but outputs influence operations, dispatch, or security work.
- **Low:** AI-003 (internal interpretation work on non-regulated data; trade secret handled by contract).

**Re-tier triggers:** any request to return AI-001 to automatic mode (council decision, section 6); letting AI-002 write to SCADA (to High); using AI-007 output to rank or discipline drivers (to High); allowing AI-009 to take containment actions (to High).

## 4. MEASURE
Results are from monitoring and reviews between 2026-06 and 2026-08.

### 4.1 Predictive maintenance model (AI-001)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Engineer review of a random sample of 200 of the 11,400 automatic speed reductions: share that were correct for the well's condition (target 95%) | 178 of 200 (89%); 18 were driven by stale load cell values after communication drops | **No** |
| Valid and reliable | Failure prediction: precision and recall on rod pump failures, May to August, compared with work orders (targets 0.70 and 0.60) | Precision 0.74; recall 0.58 | Partial |
| Safe | Model speed reductions that led to a controller fault shutdown or an unplanned crew visit (target 0) | 7 wells stopped on controller faults; 2 needed crew visits at H2S-classified sites; no injury or release | **No** |
| Secure and resilient | Data path: read-only and outbound from OT; no write path from the cloud without approval | Model wrote through the SCADA setpoint API; historian connector can write (GR-01) | **No** |
| Accountable and transparent | Change record, safety review, and council approval before automatic mode | None existed | **No** |
| Explainable and interpretable | Each recommendation shows the top features and the pump card that drove it | In place since 2026-08 | Yes |
| Fair, harmful bias managed | Error rates compared across operating areas and well types (flag a difference of more than 5 points) | Error rate 16% at wells on licensed radio vs 8% on private LTE (more communication drops) | **Flagged** |
| Privacy-enhanced | No personal data in features | Confirmed | Yes |

### 4.2 Computational leak detection (AI-005)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Controlled withdrawal tests on 4 gathering segments in 2026 (target: all detected) | 4 of 4 detected | Yes |
| Safe | False alarm rate per controller shift (alarm management plan target) | Within target after 2026-03 retuning | Yes |
| Accountable and transparent | Retuning of thresholds reviewed under the alarm management plan | The 2026-03 retuning was reviewed by the alarm team but not by the council | Partial |

### 4.3 Driver-facing camera AI (AI-006)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Safety coach review of 300 scored events: share confirmed (target 85%) | 231 of 300 (77%) | **No** |
| Fair, harmful bias managed | Overturn rate by shift (flag a difference of more than 10 points) | Night shift 31% vs day shift 12% (glare and infrared mode) | **Flagged** |
| Accountable and transparent | Human review before discipline (target 100%) | 0%; 46 disciplinary actions in 2026 cited scores alone | **No** |
| Privacy-enhanced | Video retention limit; access by role | 90-day retention; all supervisors can view all video | Partial |

### 4.4 Generative AI pilot (AI-008) using AI 600-1 risk areas
| AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Data privacy | Data loss prevention alerts on taxpayer and bank numbers in prompts | 14 alerts in the pilot; all blocked | Yes |
| Information security | Prompt injection test with crafted documents | Not yet done | **No** |
| Confabulation | User reports of wrong summaries; spot checks | Spot checks started 2026-08 | Partial |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** advisory mode. A production engineer approves each speed change in SCADA; the rod pump controller enforces minimum and maximum speeds locally; recommendations are suppressed for any well whose data is stale (new data quality gate). Engineers can ignore recommendations without justification.
- **AI-005:** controllers act on leak alarms under the alarm management plan; the model never closes valves or stops pumps.
- **AI-006:** a safety coach reviews every scored event before it can be used in discipline; drivers see their events and can dispute them.
- **AI-007, AI-002, AI-004:** recommendations only; dispatchers, engineers, and plant operators decide.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-05, PD-009, PG-007, ML-008.

**Incident handling:** an AI failure that causes an unsafe condition, a release, or an unfair employment action follows P08 and POL-03; a release also follows the PHMSA and EPA notice rows in the notification matrix.

**Decommissioning and fallback:** each use case has an off switch and a fallback the BIA already covers (P05): engineers' manual pump-off analysis for AI-001, conventional leak detection methods and patrols for AI-005, safety coach review without scores for AI-006, and manual dispatch for AI-007.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 predictive maintenance | **Continue in advisory mode; automatic mode suspended** (council, 2026-09-02; advisory mode in place 2026-09-03) | Safety management of change and a change record for any write path; data quality gate for stale values; error-rate parity across radio and LTE wells; write path redesigned to stay inside the OT DMZ design; council decision on any return to automatic mode by 2026-12-31 (POAM-021) |
| AI-005 leak detection | **Continue** | Threshold and model changes reviewed under the alarm management plan and reported to the council; annual withdrawal tests |
| AI-006 camera AI | **Continue with conditions** | Human review before any discipline from 2026-10-31; review of the 46 actions taken in 2026; night-shift accuracy fix with the vendor; counsel opinion on 390.36 and biometric laws by 2026-12-31 (POAM-022) |
| AI-007 route optimization | **Continue** | No use of outputs to rank drivers |
| AI-008 generative AI pilot | **Continue pilot** | Prompt injection test by 2026-12-31; no Restricted or OT Confidential data |
| AI-002, AI-003, AI-004, AI-009 | **Approved** | Standard monitoring; AI-004 vendor path follows the CIP-003-9 Section 6 fix at P3 |

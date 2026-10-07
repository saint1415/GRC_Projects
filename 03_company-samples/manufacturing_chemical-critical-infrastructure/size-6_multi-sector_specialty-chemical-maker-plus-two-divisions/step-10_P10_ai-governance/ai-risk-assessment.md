# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Specialty Chemicals, Distribution, Hazmat Transport, corporate) |
| Tier / Vertical | Multi-Sector / Chemical |
| Scope | The group AI governance program: the Group AI Standard, the division use-case inventory, and the rules that bear on two priority use cases: the Plant C1 process-optimization model (AI-001) and the driver-facing camera AI (AI-007) |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook; the Generative AI Profile (AI 600-1) for AI-003, AI-004, and AI-008; OT context from NIST SP 800-82 Rev. 3 and the CISA-led joint guidance "Principles for the Secure Integration of Artificial Intelligence in Operational Technology" (2025-12-03, voluntary, as cited in the Chemical Small sample) |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-09-02; presented to the board risk committee 2026-09-17 |
| Inventory | `ai-use-case-inventory.csv` (9 use cases: 2 High, 6 Medium, 1 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk with cyber and process safety risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group OT Security Director, Group Process Safety Director, Group General Counsel, Group HR director, and one leader from each division. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Plant managers (RMP qualified persons) | Approve, through MOC, any AI use that can influence a covered process |
| Group CISO and Group OT Security Director | AI security standard (data paths into OT, model supply chain, prompt injection, data leakage) |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-07-01, under POL-01 4.12)
1. **Register before use.** Every AI use case that touches a physical process, Restricted data, or decisions about people is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: council approval, a pre-deployment impact assessment, and quarterly monitoring reports.
3. **No AI writes to OT without double approval.** An AI system may write a setpoint, alarm limit, or recipe only if the council approved it as High tier **and** the change passed plant MOC with the safe limits in the process safety information (POL-01 4.12, 4.13).
4. **No Restricted data in unapproved tools** (POL-04 4.6). Providers that receive formulations or personal data sign no-training and retention terms.
5. **Decisions about people.** AI output may not be the sole basis for discipline, hiring, or pay. A trained person reviews the evidence and records the decision.
6. **Change gate.** A material change (new model, new data source, new write path, new decision role) triggers re-assessment before release.

**Where the program fell short in 2026.** The standard was adopted on 2026-07-01, **after** Process Engineering switched AI-001 to automatic setpoint writes in 2026-06 without MOC or council approval (scenario gap 9). The driver camera AI (AI-007) was feeding discipline since 2025 with no documented review (scenario gap 5). Both are now under conditions (section 6).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | Process-optimization model (Plant C1 hypochlorite reactors) | Specialty Chemicals | High | Advisory only since 2026-09-03; automatic mode prohibited |
| AI-002 | Predictive maintenance for rotating equipment | Specialty Chemicals | Medium | In production |
| AI-003 | Generative formulation assistant | Specialty Chemicals | Medium | Pilot; expansion paused |
| AI-004 | SDS authoring assistant | Group | Medium | Drafts only |
| AI-005 | Demand forecasting for the managed inventory service | Distribution | Medium | In production |
| AI-006 | Route and load optimization | Hazmat Transport | Medium | In production |
| AI-007 | Driver-facing camera AI event scoring | Hazmat Transport | High | In production with conditions |
| AI-008 | Enterprise generative AI assistant | Group | Medium | Pilot (3,000 users) |
| AI-009 | SOC triage assistant | Group | Low | Approved |

### 2.1 AI-001 process-optimization model: process safety rules
| Item | Description |
|---|---|
| Purpose | Recommend the caustic feed ratio and reactor temperature setpoints for the two Plant C1 hypochlorite reactor trains to raise yield and cut chlorate formation |
| Data | 4 years of historian data from the Plant C1 replica (SYS-C5 to SYS-G6), batch records, and analyzer results. No personal data |
| How output reaches the process | **2026-06-08 to 2026-09-03:** wrote setpoints through the advisory interface in the OT DMZ, which the DCS applied within bounded ranges (P02 AC-4). **Since 2026-09-03:** recommendations shown to operators only; operators enter any change by hand |
| Not intended | Chlorine unloading, SIS settings, alarm limits, any other plant |

| Rule | What it requires | What it means for AI-001 |
|---|---|---|
| 40 CFR 68.65(c)(1)(iv) | Process safety information includes safe upper and lower limits | The bounded ranges must sit inside the PSI safe limits and the operating procedure's normal limits. **Finding:** the train 2 temperature upper bound was 3 °C above the operating procedure's normal limit (still below the PSI safe upper limit) |
| 40 CFR 68.75(a)-(b) | MOC before changes to technology and procedures, covering technical basis, safety impact, procedures, time period, and authorization | Switching to automatic writes was a change to the process control technology. **No MOC was done** (P03 G-056) |
| 40 CFR 68.75(c)-(e); 68.69 | Train affected employees before start-up; update operating procedures | Operators were not briefed and procedures did not mention AI writes (G-057) |
| 40 CFR 68.67(c)(4) | PHA addresses consequences of failure of engineering and administrative controls | The PHA does not consider a wrong or manipulated AI setpoint (part of POAM-004) |
| OSHA PSM 29 CFR 1910.119 | Parallel MOC and PSI duties | Same as the RMP rows |
| RBPS 8 (voluntary) | Prevent unauthorized remote access to process controls | A cloud service writing into the OT DMZ is a remote path into process control (P04 finding 2) |
| CISA-led AI in OT guidance (voluntary) | Understand AI, assess its use in OT, establish governance, and embed safety and security | Used as good practice for the conditions in section 6 |
| State AI laws | Target decisions about people | Not applicable: AI-001 makes no decisions about people |

### 2.2 AI-007 driver camera AI: employment rules
| Rule | Status | What it means for AI-007 |
|---|---|---|
| Illinois HB 3773 (Public Act 103-0804; amends the Illinois Human Rights Act) | Effective 2026-01-01 (verification partial in the repository source) | Covers AI used in discipline; employers must give notice of AI use and must not use AI that has a discriminatory effect. Hazmat Transport has terminals and drivers in Illinois |
| Colorado SB26-189 | Effective 2027-01-01 | Covers technology that materially influences consequential employment decisions; deployers owe notice, explanation after an adverse outcome, and human review. Hazmat Transport has drivers domiciled in Colorado. Status unsettled (litigation and federal preemption efforts) |
| California CPPA automated decisionmaking technology rules | Compliance by 2027-01-01 | About 110 drivers live in California. Counsel is deciding whether camera scoring used in discipline is automated decisionmaking for a significant decision (P03 GG-09) |
| Title VII disparate impact | In force by statute | Score disparities by protected group must be monitored even though federal enforcement priorities have shifted |
| State biometric privacy laws | Under counsel review | Applies only if the vendor derives facial geometry; counsel has asked the vendor (not assessed here) |
| 49 CFR 391 and 395 | In force | Camera AI does not replace ELD or driver qualification records |

### 2.3 Other use cases (summary)
- **AI-002 predictive maintenance:** may create work requests but may not lengthen inspection or test intervals for covered process equipment without MOC (68.73(d)).
- **AI-003 formulation assistant:** formulations are trade secrets; the provider contract must prohibit training on inputs. Any suggestion is lab-tested and passes a compatibility check before it can become an MOC.
- **AI-004 SDS authoring:** SDS content duties stay with the group under OSHA hazard communication; certified authors approve every section.
- **AI-005 demand forecasting:** feeds the managed inventory service. Fixed reorder rules stop the model from letting a utility tank run low; the forecast will be inside the SOC 2 Processing Integrity scope (P09).
- **AI-006 route optimization:** dispatchers approve routes; security plan loads keep approved route lists.
- **AI-008 enterprise assistant:** prohibited for process, safety, shipping paper, and employment decisions; no Restricted data.

## 3. Risk tiers (repository rubric)
- **High:** AI-001 (affects physical safety at an RMP Program 3 process) and AI-007 (substantial factor in discipline decisions about some 2,700 drivers).
- **Medium:** AI-002, AI-003, AI-004, AI-005, AI-006, AI-008. Humans make the final call, but outputs influence safety documents, maintenance, deliveries, routes, or work products.
- **Low:** AI-009.

**Re-tier triggers:** any write path to OT (any use case to High); AI-002 changing inspection intervals; AI-005 changing reorder rules; AI-006 assigning drivers or routes without dispatcher approval; AI-008 used for any decision about people.

## 4. MEASURE
Results are from monitoring and audits between 2026-06 and 2026-08.

### 4.1 AI-001 process-optimization model (automatic mode 2026-06-08 to 2026-09-03)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Predicted vs actual chlorate and yield on a 60-day hold-out; error by reactor train | Train 1 within target; train 2 error twice train 1 (train 2 was under-represented in training data after its 2024 rebuild) | **Partial** |
| Safe | Share of setpoints inside the operating procedure's normal limits and the PSI safe limits; SIS demands linked to AI setpoints | 0 setpoints outside the PSI safe limits; 412 of about 14,200 writes above the train 2 normal temperature limit because of the mis-set bound; 0 SIS demands linked to AI | **No** (bound not traced to the PSI) |
| Secure and resilient | No inbound write path from the cloud; integrity of training data | Write path existed (P02 AC-4); no integrity check on replica data (P01 SC-022) | **No** |
| Accountable and transparent | MOC record; operator briefing; every recommendation and write logged with model version | Logs complete; no MOC; no briefing | **No** |
| Explainable and interpretable | Top factors shown to operators | Available since 2026-09-03 in advisory mode | Yes |
| Privacy-enhanced | No personal data in inputs; operator IDs not used as features | Confirmed | Yes |
| Fair, with harmful bias managed | Representativeness by reactor train, season, and raw material lot; override rates reviewed by shift only in aggregate and never used to rate operators | Train 2 under-represented (see above); shift data not used | **Partial** |

### 4.2 AI-007 driver camera AI
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Reviewer agreement with 400 sampled event scores | 22% false positives overall; 31% at night | **No** |
| Fair, with harmful bias managed | Event rate by age band and by terminal; flag any group more than 1.25 times the overall rate without an explanation after video review | Drivers 60 and older flagged for drowsiness at 1.4 times the overall rate; not explained after review | **Flagged** |
| Accountable and transparent | Documented human review before discipline; notice to drivers | 0 of 37 sampled disciplinary actions had a documented video review; no AI notice to drivers | **No** |
| Privacy-enhanced | Video retention and access | 90-day retention; terminal managers see all terminals' video | **Partial** |
| Safe | Coaching effect on hard-braking and phone-use events | Phone-use events down 38% since 2025 | Yes |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** advisory only. Recommendations appear on a read-only display; operators enter any change by hand under the operating procedure; the DCS clamps enforce PSI safe limits; the SIS is independent. A safe-limit envelope taken from the operating procedure's normal limits filters every recommendation, under MOC and signed by the Plant Manager.
- **AI-007:** scores open a coaching case. Before any discipline, a trained reviewer watches the clip, records the decision and reasons, and the driver can respond. The score is never the sole basis.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-04, SC-007, SC-022, HT-006, SC-025.

**Incident handling:** an AI recommendation that contributes to a process deviation is investigated as a process incident, and under 68.81 if it could have led to a catastrophic release. Suspected tampering with the replica or model follows the P08 runbook; AI-001 stays off until data integrity is confirmed (P08 section 8).

**Decommissioning:** every use case has an off switch and a fallback already in the BIA (P05 BP-SC10 for AI-001: normal operating procedures).

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 process-optimization model | **Continue in advisory mode only** (council, 2026-09-02; switched to advisory 2026-09-03; board risk committee informed 2026-09-17). **Automatic mode is prohibited** | Retroactive MOC record, operating procedure update, and operator briefing by 2026-10-31; firewall write rule removed by 2026-10-31 and interconnection agreement by 2026-12-31 (POAM-005); envelope traced to the PSI and operating limits by 2026-10-31; training data integrity checks by 2026-12-31; retrain with enough train 2 data (POAM-021). Any future automatic mode needs a new council approval, a PHA review of the AI failure modes, and an MOC |
| AI-007 driver camera AI | **Continue for coaching; discipline only after documented human review** | Review procedure by 2026-11-30; AI notice to drivers by 2026-12-31 (Illinois now; Colorado before 2027-01-01); age-band disparity analysis by 2026-12-31; counsel decisions on California ADMT and biometrics by 2026-12-15; video access limited to each terminal (POAM-020) |
| AI-003 formulation assistant | **Pilot continues; expansion paused** | Verify no-training and retention terms; approved projects only |
| AI-002, AI-004, AI-005, AI-006 | **Approved** | Standard monitoring; re-tier triggers in section 3 |
| AI-008 enterprise assistant | **Pilot continues** | AI 600-1 assessment before general release; prohibited uses enforced |
| AI-009 SOC triage | **Approved** | No automated OT containment |

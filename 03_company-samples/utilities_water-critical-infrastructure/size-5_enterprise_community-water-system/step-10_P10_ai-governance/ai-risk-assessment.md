# AI Governance Risk Assessment: Enterprise AI Portfolio and Water-Quality Anomaly Detection

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded parent of state-regulated water utilities; FL, GA, NC, TN) |
| Tier / Vertical | Enterprise / Water and Wastewater Systems |
| Scope | Enterprise AI portfolio (11 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001 water-quality anomaly detection in section 6 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1) for AI-007, AI-008, and AI-010; repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Senior Vice President, Water Quality and Environmental Compliance; Director of Data Science as secretary), meeting of 2026-08-19; GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-10 (section 8) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 11 |
| Risk tier | High 4, Medium 6, Low 1 |
| Status | In production 8 (AI-001 also piloting at 2 more systems), Pilot 2, Proposed 1 |
| Committee review complete | 7 of 11 |
| Not yet reviewed | 4: AI-006 (due 2026-11-30), AI-009, AI-010, AI-011 (due 2026-12-31) (POAM-022) |
| Use cases with any write path to OT | 0 (all OT-related models are advisory; P04 confirms no cloud write path) |
| High-tier tools validated only on vendor data | 1 in part: AI-001 at its 2 pilot systems |

**Main findings:** AI-001 runs in production at the Gulf Coast Regional System without drift monitoring, and its validation at the two newer pilot systems relies on vendor data. A High-tier vendor feature (AI-006, collections prioritization) was switched on in the CIS through a vendor release without committee review. Every model that touches treatment or distribution is advisory, with engineered limits in the PLCs, so no AI output can change a process directly.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board's safety, environmental, and risk committee sees each quarter.

**Members:** Senior Vice President, Water Quality and Environmental Compliance (chair); Director of Data Science (secretary); CISO; Director of OT Security; Chief Privacy Officer; General Counsel's delegate; Chief Human Resources Officer (for workforce and HR tools); Vice President, Customer Operations; a regional operations vice president (rotating); and the Vice President, Resilience and Emergency Management. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Local validation on company data at each site where it will run; impact assessment; human review design; OT safety review (no write path, engineered limits) for process models; monitoring plan with drift detection; fairness review where people are affected |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.6; STD-05.3). Since 2026-08, procurement and IT change management block AI features without an inventory ID, and vendor release notes for tier-1 SaaS are screened for new AI features. The GRC team owns the inventory.

**Policies:** POL-04 4.2 (Restricted infrastructure information never leaves approved repositories); POL-05 4.6 (approved AI tools only; no Restricted or Confidential information in other tools); POL-02 4.4 and P04 (no write path from cloud workloads into OT); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier tool; annual re-review of every use case.

**Why 4 use cases lack review.** AI-006 and AI-009 arrived as features in vendor releases before the intake block existed; AI-010 started as a customer service pilot; AI-011 was requested by HR and has not been enabled. The committee set review dates for all four (section 8).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| SDWA section 1433 | Yes, for AI-001 and AI-002 | They are part of the "electronic, computer, or other automated systems" assessed in each covered system's RRA (42 U.S.C. 300i-2(a)(1)(A)(ii)), and AI-001 is one of the detection strategies in the Gulf Coast Regional System ERP (300i-2(b)(4)). Their failure modes must be in the RRA and their limits in the ERP |
| SDWA Part 141 monitoring and reporting | Context | Compliance monitoring uses approved methods and certified laboratories; AI-001 never replaces a compliance sample or a reported result |
| State public utility commission disconnection rules | Yes, for AI-006 | Each state sets notice and protection rules for disconnecting residential water service; staff review every disconnection |
| State recording consent laws | Yes, for AI-007 | All-party consent notice on every recorded line; Florida worked example: interception is lawful when all parties have given prior consent (Fla. Stat. 934.03(2)(d)) |
| State breach and data security laws | Yes, for AI-005, AI-007, AI-010 | Customer personal information (Fla. Stat. 501.171 worked example) |
| Federal equal employment opportunity laws | Yes, for AI-011 | Adverse impact analysis before any use |
| FTC Act Section 5 | Indirectly | Accuracy of chatbot statements to customers (AI-010) and vendor claims the company relies on |
| State AI laws | Tracked, not analyzed here | Legal monitors AI legislation in FL, GA, NC, and TN. This assessment did not verify state AI statutes and relies on Legal's tracking; any new obligation triggers a committee re-review |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision, or able to affect physical safety or critical infrastructure.

| ID | Use case | Tier | Status | Committee review |
|---|---|---|---|---|
| AI-001 | Water-quality anomaly detection | High | In production at GCR; pilot at 2 systems | Reviewed 2025-11-12; re-reviewed 2026-08-19 |
| AI-002 | Coagulant dose optimization (TP-A) | High | Pilot (advisory) | Reviewed 2026-04-15 |
| AI-003 | Main break risk prediction for capital planning | Medium | In production | Reviewed 2025-10-08 |
| AI-004 | Pump energy optimization | Medium | In production (advisory) | Reviewed 2026-02-11 |
| AI-005 | AMI leak and abnormal-usage alerts | Medium | In production | Reviewed 2025-12-10 |
| AI-006 | Collections prioritization (CIS vendor feature) | High | In production | Not reviewed (due 2026-11-30) |
| AI-007 | Contact center call summarization and agent assist | Medium | In production | Reviewed 2026-03-18 |
| AI-008 | Workforce generative AI assistant | Medium | In production | Reviewed 2026-01-14 |
| AI-009 | SOC alert triage assistant | Low | In production | Not reviewed (due 2026-12-31) |
| AI-010 | Customer chatbot for outage and billing questions | Medium | Pilot | Not reviewed (due 2026-12-31) |
| AI-011 | Resume screening and ranking for operator recruiting | High | Proposed (disabled) | Not reviewed (due 2026-12-31) |

**Tiering notes:** AI-001 and AI-002 are High because they inform decisions about drinking water safety for large populations, even though both are advisory and engineered limits stop unsafe doses. AI-006 is High because it influences which households are considered for disconnection of an essential service. AI-004 stays Medium because PLC limits on tank levels and pressure bound every schedule. AI-008 is Medium rather than Low because staff could paste Restricted information into it; that is prohibited and sampled.

## 5. MEASURE: portfolio testing gaps
| Gap | Use cases | Plan | Due |
|---|---|---|---|
| No drift monitoring | AI-001 | Monthly drift metrics on input distributions and alert rates; retraining triggers after source or treatment changes | 2027-03-31 (POAM-022) |
| Validation on vendor data only at the pilot sites | AI-001 (2 pilot systems) | Local back-test on at least 12 months of each pilot system's data and confirmed events before production | 2027-03-31 (POAM-022) |
| No disparity testing | AI-006 | Compare outreach and disconnection-review rates by service area and an income proxy (census tract median income); act if any group's rate ratio exceeds 1.25 at equal arrears | 2026-11-30 (POAM-022) |
| No adverse impact analysis | AI-011 | Selection-rate comparison by sex and race and ethnicity where recorded before any use | Before enabling |

## 6. Full assessment: AI-001 water-quality anomaly detection
### 6.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Flag unusual combinations of water quality and hydraulic readings that may signal contamination, treatment upset, or sensor failure, earlier than single-point SCADA alarms |
| Users | GCR ROCC operators and the GCR regional water quality manager; operators at the 2 pilot systems |
| Affected people | About 1.24 million people served by the Gulf Coast Regional System and about 61,000 at the 2 pilot systems |
| Data | Inputs: historian data from about 180 online analyzers and flow and pressure points, replicated one way to the Cloud provider A data platform (P04). No personal information. Outputs: alerts with the contributing signals on a read-only ROCC dashboard |
| Build or buy | Configure: a vendor analytics model tuned by the data science team on GCR history |
| Not intended | Replacing compliance sampling, SCADA alarms, or hardwired alarms; any automatic control action; reporting to the primacy agency |
| Dependencies | Historian replication path (P05 DEP-27, a single point of failure; the regional historian buffers 72 hours); BIA BP-16 (RTO 24 hours) |

### 6.2 Risk tier
High (section 4). Operators at GCR now use AI-001 as an early warning, so a silent loss of detection quality matters (P01 R-042, R-044). Escalation trigger to the executive risk committee: any proposal to let AI-001 start sampling, change setpoints, or suppress SCADA alarms.

### 6.3 MEASURE (GCR back-test and production data, 2025-07 to 2026-07)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Recall on 46 labeled events at GCR (treatment upsets, main breaks with intrusion risk, sensor failures, one chlorine residual loss); target 85% | 41 of 46 detected (89%); median lead time 38 minutes before the first SCADA alarm | Yes |
| Valid and reliable | Alert precision; target 30% or more of alerts confirmed as real events or sensor faults | 34% | Yes |
| Valid and reliable (pilot systems) | Same tests on local data | Not done; vendor data only | **No** |
| Safe | No write path to SCADA; operators confirm every alert; SCADA and hardwired alarms unchanged | Confirmed by the P07 penetration test and network rules (P04) | Yes |
| Secure and resilient | One-way replication; cloud administrator rights; signed model images | One-way path confirmed; administrator rights too broad and model images unsigned (P01 R-032) | Partly |
| Accountable and transparent | Named business owner; alerts labeled as advisory; operator procedure for alert response | In place | Yes |
| Explainable and interpretable | Alert shows the contributing signals and their deviation | In place | Yes |
| Privacy-enhanced | No personal information in inputs or outputs | Confirmed | Yes |
| Fair, with harmful bias managed | Recall by pressure zone; flag a zone more than 10 points below overall | 4 of 19 zones (older areas with fewer analyzers) below the threshold; 3 of the 5 missed events were in those zones | **No** |
| Monitored over time | Drift detection on inputs and alert rates | Not in place | **No** |

### 6.4 MANAGE
- **Human in the loop:** every alert is reviewed by the ROCC operator, who checks SCADA trends and orders grab samples; the water quality manager decides on any public health action. Operators get a refresher each year that AI-001 can miss events (P01 R-042).
- **Drift and retraining:** drift metrics monthly, with automatic re-review after a source water change, a treatment change, or a new analyzer type (POAM-022, due 2027-03-31).
- **Pilot systems:** no production use at the 2 pilot systems until local validation is complete; until then, alerts are shown with a "pilot" label and operators do not act on them without a SCADA alarm or a sample.
- **Coverage gap by zone:** 9 additional analyzers in the 4 low-recall zones are in the 2027 capital plan; until then, grab sampling in those zones is weekly instead of monthly.
- **Alarm fatigue:** thresholds tuned quarterly with operator feedback (P01 R-043); target precision 30% or more.
- **Security:** separate model deployment role and signed model images (P01 R-032, due 2027-03-31).
- **Incidents:** a missed event or a harmful false alert is logged as an operations event and reviewed by the committee; a security incident affecting the data platform follows P08.
- **Decommissioning:** suspend AI-001 if recall falls below 75% in a quarterly review, if the replication path cannot be kept one-way, or if the vendor changes data-use terms.

## 7. MANAGE: portfolio controls
- **Monitoring:** each High-tier tool has quarterly performance metrics (inventory column `monitoring`) reported to the committee; threshold breaches trigger re-review.
- **No write path to OT:** any AI use that touches process data must stay advisory unless the executive risk committee approves otherwise after an OT safety review; none has been proposed.
- **Third parties:** AI vendors with access to company data are tier-1 in the vendor program; contracts require notice of material model changes and prohibit training on company data.
- **Incident handling:** AI incidents (unsafe recommendation, bias finding, data misuse) are logged as SOC or operations events and follow P08 where security or customer data is involved.
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice or change data-use terms; the inventory records retirement.

## 8. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the committee's recommendation of 2026-08-19:
1. **AI-001:** approved to continue at GCR with conditions: drift monitoring and signed model images by 2027-03-31; weekly grab sampling in the 4 low-recall zones until new analyzers are installed. The 2 pilot systems stay in pilot until local validation is complete.
2. **AI-002:** stays a pilot at TP-A; a bounds check in the recommendation display by 2026-12-31 (P01 R-046) before any extension.
3. **AI-006:** may continue only with staff review of every disconnection and no automated outreach changes until committee review and disparity testing by 2026-11-30.
4. **AI-009 and AI-010:** may continue in current scope until committee review by 2026-12-31; no expansion of AI-010 beyond its 2 pilot service areas.
5. **AI-011:** stays disabled until committee review and an adverse impact analysis are complete.
6. **Intake:** vendor release screening for AI features in tier-1 SaaS continues; the GRC team reports new features to the committee monthly.

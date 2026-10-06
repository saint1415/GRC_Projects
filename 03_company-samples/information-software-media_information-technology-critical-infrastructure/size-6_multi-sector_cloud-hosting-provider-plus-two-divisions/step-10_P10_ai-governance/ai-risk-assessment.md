# AI Governance Risk Assessment: Group AI Program | Cris Santos Company Holdings

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (Cloud Hosting, Managed IT and Consulting, Payment Processing, corporate) |
| Tier / Vertical | Multi-Sector / Information Technology |
| Scope | The group AI governance program: group standards, the division use-case inventory, and the regulator-specific rules for four priority use cases: the SOC's AI-driven alert triage and automated response (AI-001, the registry default), Managed IT's AI runbook automation agent (AI-005), and Payment Processing's fraud and merchant underwriting models (AI-007, AI-008) |
| Framework | NIST AI RMF 1.0 (AI 100-1), the Generative AI Profile (AI 600-1), and the AI RMF Playbook |
| Assessors / date | Group AI council (chaired by the Group Chief Risk Officer), 2026-09-04; presented to the board risk committee 2026-09-17 |
| Inventory | `ai-use-case-inventory.csv` (10 use cases: 4 High, 3 Medium, 3 Low) |

## 1. GOVERN (group program)
### 1.1 Structure
| Body or role | Responsibility |
|---|---|
| Board risk committee | Oversees AI risk as part of cyber and enterprise risk; receives the High-tier list quarterly |
| Group AI council | Group Chief Risk Officer (chair), Group CISO, Group Chief Privacy Officer, Group General Counsel, the three division security leads, the Payment Processing chief risk officer. Approves High-tier use cases and the approved-tools list |
| Division AI owners | Named business owner for each use case (inventory column); run monitoring |
| Owners of regulated environments | Approve, in writing, any AI action in G1, the CDE, or the CUI enclave (POL-01 4.13) |
| Group CISO | AI security standard (prompt injection, model supply chain, data leakage) |
| Group internal audit | Includes High-tier AI controls in the annual assessment from 2027 |

### 1.2 Group AI Standard (adopted 2026-04-20, under POL-01 4.13)
1. **Register before use.** Every AI use case that touches customer, client, agency, merchant, or consumer data, makes or supports decisions about them, or takes actions in their systems is registered before deployment or material change.
2. **Tier with the repository rubric** (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`). High tier: the council approves; a pre-deployment impact assessment, bias or accuracy testing, and quarterly monitoring are required.
3. **Actions need an owner's consent.** An AI system may act (isolate, disable, suspend, run a script) only on action classes the owner of the affected environment has approved in writing. G1, the CDE, and the CUI enclave need analyst approval for every action until their owners approve otherwise.
4. **Data stays in scope.** Prompts and context sent to a model must not carry G1 identifiers, CUI, or account data to a service outside the relevant documented scope (POL-04 4.4).
5. **Regulator overlays.** Each division supplement adds its own rules: FedRAMP and DFARS for Cloud Hosting, CMMC and client terms for Managed IT, card network and FTC rules for Payment Processing.
6. **Change gate.** A material change (new model, new provider, new action class, new data source) triggers re-assessment before release.

**Where the program fell short in 2026.** Three High-tier use cases were live before the standard was adopted: the SOC's AI triage (2025-11), the runbook automation agent (2026-03), and the fraud model (2024). None had been approved by the owners of the environments it acts in (scenario gap 4).

## 2. MAP (division use cases and applicable rules)
| ID | Use case | Division | Tier | Status |
|---|---|---|---|---|
| AI-001 | AI-driven security operations: alert triage and automated response | Group | High | In production with conditions |
| AI-002 | Customer support assistant | Cloud Hosting | Medium | In production |
| AI-003 | Fleet failure prediction | Cloud Hosting | Low | In production |
| AI-004 | Abuse and fraud detection with resource suspension | Cloud Hosting | Medium | In production with conditions |
| AI-005 | AI runbook automation agent (RMM) | Managed IT | High | In production with conditions; unattended mode suspended |
| AI-006 | Consulting delivery assistant | Managed IT | Low | Approved |
| AI-007 | Transaction fraud scoring | Payment Processing | High | In production |
| AI-008 | Merchant underwriting risk model | Payment Processing | High | In production with conditions |
| AI-009 | Engineer coding assistant | Group | Low | Approved |
| AI-010 | Enterprise generative AI assistant | Group | Medium | Approved (pilot, 3,000 users) |

### 2.1 SOC alert triage and automated response (AI-001)
The service sits in SYS-G2 and sees every division's logs. It ranks alerts, auto-closes those it judges benign (about 64%), and can run 7 SOAR actions without a human: isolate a host, disable a workforce account, revoke sessions, block an address, quarantine a file, suspend a cloud workload, and reset credentials.

| Rule or commitment | What it means for AI-001 |
|---|---|
| FedRAMP MAS-CSO-IIR, MAS-CSO-MDI, MAS-CSO-TPR (G1) | G1 logs and resource metadata flow into the service and on to a third-party model service. Both must be documented as information resources or third-party information resources of the G1 offering, with usage, justification, mitigations, and compensating controls. **Gap:** not documented (POAM-008) |
| FedRAMP IEC-CSO-EFR | An auto-closed alert can hide a FedRAMP Reportable Incident. The reportability evaluation must not depend on an unvalidated auto-close for G1 sources |
| 32 CFR 170.19(c)(2) (CMMC) | Enclave logs are Security Protection Data. A cloud service that processes Security Protection Data (without CUI) is in the enclave's assessment scope as a Security Protection Asset, so the SIEM, the triage service, and the model service will be assessed with the enclave |
| PCI DSS v4.0.1 Requirements 10 and 12.10 | Log review and incident response for the CDE must be reliable. An auto-closed CDE alert in the seeded test (section 4.1) is a monitoring failure, and unattended containment in the CDE can disrupt settlement |
| 16 CFR 314.4(c)(8) | Monitoring of authorized users' activity for Payment Processing customer information depends on this service |
| Customer agreements and SLAs | An unattended action that suspends a customer workload is a service event under the SLA |
| FTC Act Section 5; SEC Reg S-K Item 106 | Statements about "AI-powered security" in marketing, trust center pages, or the annual report's risk management description must be accurate. The 10-K description should not imply validated autonomous detection that has not been tested |

### 2.2 AI runbook automation agent (AI-005)
| Rule or commitment | What it means |
|---|---|
| Client agreements and BAAs | Clients approve changes to their systems. Unattended execution of runbooks was never in the agreements |
| NIST SP 800-171 Rev. 2, 3.1.15; 32 CFR 170.19(c)(2) | Privileged commands run remotely on DIB clients' systems must be authorized; the agent's actions are inside DIB clients' CMMC scope |
| 12 CFR 53.4 | A wrong action that disrupts a bank client's covered services for 4 hours or more triggers bank notices |
| POL-02 4.9 | Jobs that target more than one client or a regulated environment need two-person approval; the agent cannot be one of the two |

### 2.3 Payment Processing models (AI-007, AI-008)
| Rule or commitment | Use cases | Implication |
|---|---|---|
| Card network rules and sponsor bank standards (contractual) | AI-007, AI-008 | Fraud and underwriting decisions follow network and sponsor bank requirements; the models must not weaken them |
| FTC Act Section 5 | AI-007, AI-008 | Unfair outcomes or untrue claims about automated decisions are an enforcement risk |
| 16 CFR 314.4 | AI-007, AI-008 | Training and scoring data is customer information under the division's Safeguards program |
| Colorado SB26-189 (effective 2027-01-01) | AI-008 | Covers developers and deployers of automated decision-making technology that materially influences consequential decisions, including financial or lending services, with no small-business exemption in the signed text. Counsel is reviewing whether merchant underwriting of sole proprietors in Colorado is such a decision. The law's enforcement posture is unsettled (litigation and federal preemption efforts; see `00_universal-framework/cross-sector/us-cross-sector-obligations.md`) |

## 3. Risk tiers (repository rubric)
- **High:** AI-001 and AI-005 (can affect critical infrastructure operations: they act in cloud, payment, bank, and defense customers' environments); AI-008 (a substantial factor in a financial decision about merchants, including individuals operating as sole proprietors); AI-007 (makes real-time automated decisions on consumers' payments at very large scale, with no human deciding at the time; the council tiers it High by choice although payment authorization is not one of the rubric's listed categories).
- **Medium:** AI-002, AI-004, AI-010. AI-004 suspends free-tier and new accounts automatically, but suspensions are reversible, and enterprise accounts get human review first.
- **Low:** AI-003, AI-006, AI-009.

**Re-tier triggers:** letting AI-001 act on customer-owned resources (not only group systems); letting AI-005 run any runbook without technician approval again; using AI-008 to set pricing; AI-004 suspending paying accounts without human review.

## 4. MEASURE
Results are from monitoring and tests between 2026-05 and 2026-08.

### 4.1 SOC alert triage and automated response (AI-001)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Seeded test: 40 true-positive alerts planted across HCP, CDE, and Managed IT sources; target 0 auto-closed | 3 auto-closed (2 HCP, 1 CDE); 0 of 15 Managed IT | **No** |
| Valid and reliable, by division | Auto-close share of all alerts, by source division | Cloud Hosting 61%; Managed IT 70%; Payment Processing 58% | Monitor; validation per division due |
| Safe (unattended actions) | Unattended containment actions reversed as wrong; target under 1% | 1,240 actions; 31 reversed (2.5%), including 2 CDE connected-to hosts isolated during a settlement window (one file delayed 40 minutes) | **No** |
| Secure and resilient (prompt injection) | Red-team: 20 crafted log lines containing instructions to lower severity | Severity lowered in 1 of 20 | **No** |
| Privacy-enhanced and data minimization | Share of G1 alerts whose context sent to the model service includes G1 resource identifiers; target 0% | 100% | **No** (POL-04 4.4) |
| Accountable and transparent | Triage rationale stored with every decision | 100% stored; reviewed only after incidents | Partial |
| Fair, harmful bias managed | Unattended account disables by workforce group (country of residence, contractor or employee, division); flag if a group's rate exceeds the overall rate by 2 times | Contractors 2.4 times the employee rate (travel and new-device signals) | **Flagged.** Review rules that weigh new devices |

### 4.2 AI runbook automation agent (AI-005), using AI 600-1 risk areas
| AI 600-1 risk | Test / metric | Result | Pass? |
|---|---|---|---|
| Confabulation | Executions on the wrong host (2026-03 to 2026-08) | 9 of about 4,800 (0.19%), from ambiguous host names in tickets | **No** (target 0 for privileged actions) |
| Information security (prompt injection) | Red-team: 10 tickets with embedded instructions to change the target host | Target changed in 2 of 10 | **No** |
| Human-AI configuration | Technician approval before execution | Not required until 2026-10-01; required since | Yes (since 2026-10-01) |
| Value chain and component integration | Vendor model change notice in the RMM contract | None | **No** |

### 4.3 Payment Processing models (AI-007, AI-008)
| Use case | Metric | Result | Pass? |
|---|---|---|---|
| AI-007 fraud scoring | Fraud caught (share of confirmed fraud declined) | 87% | Yes (target 80%) |
| AI-007 fraud scoring | False decline rate by ZIP-code median income band (proxy); flag a band more than 1.5 times the overall rate | Overall 1.9%; lowest-income band 3.4% (1.8 times) | **Flagged.** Feature review due 2026-12-31 |
| AI-008 underwriting | Decline rate, sole proprietors compared with all applicants | 22% compared with 9% | **Flagged.** Causal review: thin processing history explains part, not all |
| AI-008 underwriting | Share of declines with documented principal reasons given to the applicant | 60% | **No** (target 100%) |
| AI-008 underwriting | Model approvals later closed for fraud within 90 days | 0.4% | Yes (target under 1%) |

## 5. MANAGE
**Human-in-the-loop design:**
- **AI-001:** from 2026-10-15, an analyst approves every containment action in G1 and the CDE. Each division approves which of the 7 action classes may run unattended in its environment. Auto-close is disabled for High-severity alerts until each division's quarterly seeded test passes. G1 identifiers are redacted from model context (or G1 alerts are triaged by a model inside the G1 scope).
- **AI-005:** a technician approves every execution, sees the target host before approving, and cannot approve a multi-client job alone (POL-02 4.9).
- **AI-007:** merchants set thresholds; cardholders can resolve false declines through the issuer; analysts review false-decline complaints weekly.
- **AI-008:** underwriters decide every decline and reserve and give principal reasons to every declined applicant.

**Monitoring:** monthly metrics to division owners; quarterly High-tier report to the council and the board risk committee; P01 risks GR-04, GR-15, GR-19, CH-020, CH-021, CH-023, MS-013, PY-009, PY-010.

**Incident handling:** an AI failure that hides an incident, disrupts a customer, or acts on the wrong system follows P08 and POL-03. The P08 scenario includes the alert AI-001 auto-closed at 01:20; re-testing it is a lessons-learned action.

**Decommissioning:** each use case has an off switch and a fallback the BIA already covers (P05): manual triage, manual runbooks, rules-based fraud screening, and manual underwriting.

## 6. Decisions
| Use case | Decision | Conditions and dates |
|---|---|---|
| AI-001 SOC triage and response | **Continue with conditions** (council, 2026-09-04; board risk committee informed 2026-09-17) | Analyst approval for containment in G1 and the CDE from 2026-10-15; division approvals of unattended action classes by 2026-11-30; auto-close off for High-severity alerts until tests pass; G1 redaction by 2026-12-15; quarterly seeded tests per division from 2026-12; prompt-injection filtering; document the model service in the G1 FedRAMP scope by 2027-01-31 (POAM-003, POAM-008) |
| AI-005 runbook automation | **Continue with technician approval only** | Unattended mode stays off until wrong-host and injection tests pass twice in a row; vendor model change notice at contract renewal; reassess by 2026-12-31 |
| AI-007 fraud scoring | **Continue** | Feature review of the income-band disparity by 2026-12-31; quarterly subgroup testing |
| AI-008 underwriting | **Continue with conditions** | Principal reasons for 100% of declines by 2026-11-30; disparity review by 2026-12-31; counsel's Colorado SB26-189 opinion before 2027-01-01 |
| AI-004 abuse detection | **Continue with conditions** | Human review before suspending any paying account by 2026-12-31 |
| AI-002, AI-003, AI-006, AI-009, AI-010 | **Approved** | Standard monitoring; AI-010 prohibited for decisions about customers, merchants, or consumers; AI-009 not permitted in the CUI enclave or the CDE build pipeline |

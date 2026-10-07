# AI Governance Risk Assessment: Enterprise AI Portfolio and AI-Driven Security Operations

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded public cloud and managed infrastructure provider) |
| Tier / Vertical | Enterprise / Information Technology |
| Scope | Enterprise AI portfolio (15 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001 AI-driven security operations (alert triage) in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1); repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Technology Officer), portfolio review 2026-08-31 to 2026-09-04 and meeting of 2026-09-02; GRC team prepared the review |
| Decision | Executive risk committee, 2026-09-08 (section 9) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 15 |
| Risk tier | High 3, Medium 7, Low 5 |
| Status | In production 13, Pilot 1, Suspended 1 |
| Committee review complete | 10 of 15 |
| Not yet reviewed | 5: AI-005, AI-010, AI-012, AI-013, AI-014 (AI-014 due 2026-10-31; the rest 2026-12-31; POAM-025) |
| Use cases that act without a human first | 4: AI-001 (auto-close, host isolation, account suspension), AI-006 (sign-up blocks), AI-008 (rollout halts), AI-009 (email quarantine) |
| Use cases touching G1 or federal data | 3: AI-001 (dedicated G1 instance), AI-005 (telemetry only), AI-008 (G1 release channel) |

**Main findings:** the highest-impact use case, AI-001, acts on customer hosts and accounts without a human for some alert classes, including in G1 and for bank customers. Internal Audit found 3 false-positive host isolations in G1 and 2 missed escalations in a sample of auto-closed alerts (P07). Five use cases entered without review, mostly as vendor features, including a High-tier employment tool (AI-012, now suspended) and an RMM script generator used on customer servers (AI-014).

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 (statement 4.14) and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the risk and technology committee of the board reviews quarterly.

**Members:** Chief Technology Officer (chair); CISO; Chief Privacy Officer; General Counsel's delegate; Chief Human Resources Officer (for workforce tools); Senior Vice President, Government Cloud (for anything touching G1); Director of FedRAMP Compliance; Director of Security Operations; the head of machine learning engineering; and a customer trust representative from Customer Support. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Impact assessment; human oversight design for every autonomous action; performance and fairness testing on company data; adversarial testing; FedRAMP significant change evaluation if it touches a FedRAMP offering; monitoring plan with thresholds |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review |
| Low | Committee chair (fast track) | Approved-tool listing (STD-05.3); data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products and products the company sells, must be registered before use (POL-01 4.14; POL-05 4.5; STD-05.3). Procurement and change management now block AI features without an inventory ID. The GRC team owns the inventory.

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier use case; annual re-review of every use case.

**Why 5 use cases lack review.** Four entered through vendor feature releases (AI-005, AI-012, AI-013) or came with the AQ-1 acquisition (AI-014) before the intake block existed. AI-010 was built by Finance as an internal analytics job and was not recognized as AI. All five have review dates (section 9).

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| FedRAMP control requirements (C-IT-R01) | Yes, for AI-001 and AI-008 in G1 | The AI features are part of how SI-4, IR-4, CM-3, and SI-7 operate in FR-2. Changes to them are evaluated as significant changes (SCN-CSO-EVA). G1 alerts are scored only by the dedicated G1 instance, so federal data does not leave the boundary |
| Bank service provider rule (C-IT-R05) | Yes, indirectly | An automated action that disrupts a bank's covered services for four or more hours would trigger the 53.4 notice (P08) |
| Customer agreement | Yes | Suspension and isolation terms; confidentiality of customer content; 72-hour incident notice |
| State AI and employment laws | Yes, for AI-012 | Applicants live in many states. Examples: Illinois Public Act 103-0804 (AI in employment, effective 2026-01-01); Colorado SB26-189 (automated decision-making technology in consequential decisions, including employment, on or after 2027-01-01); NYC Local Law 144 (bias audit before using an automated employment decision tool for NYC hiring) |
| Colorado SB26-189 developer duties | Under counsel review, for AI-011 | The company may be a developer of covered technology for customers who deploy it in consequential decisions. Counsel's review is due before 2027-01-01 |
| FTC Act Section 5 | Yes, for public claims | Accuracy of AI claims in marketing (AI-003, AI-011) |
| DOJ Data Security Program (C-IT-R04) | Screening | AI vendors are screened like other suppliers; none gives a covered person access to customer content |
| NIST AI RMF 1.0 and AI 600-1 | Voluntary benchmark | The company's chosen framework; no federal AI rule binds a private provider's internal use |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about people, or able to act on critical infrastructure (here, customer services that include federal, bank, and health care workloads) without a human.

| ID | Use case | Tier | Status | Committee review | Acts without a human first |
|---|---|---|---|---|---|
| AI-001 | AI-driven security operations (alert triage) | High | In production (all regions and G1) | Reviewed 2025-11-12; re-reviewed 2026-09-02 | Yes |
| AI-002 | Generative AI support assistant | Medium | Pilot (300 agents) | Reviewed 2026-09-02 | No |
| AI-003 | Public documentation chatbot | Low | In production | Reviewed 2026-03-11 | No |
| AI-004 | Capacity forecasting | Low | In production | Reviewed 2026-02-18 | No |
| AI-005 | Predictive drive and host failure detection | Low | In production | Not reviewed (due 2026-12-31) | No |
| AI-006 | Fraud and abuse scoring at sign-up | Medium | In production | Reviewed 2026-04-15 | Yes |
| AI-007 | AI coding assistant | Medium | In production | Reviewed 2026-01-21 | No |
| AI-008 | Release anomaly detection (rollout gate) | High | In production | Reviewed 2026-06-10 | Yes (halts only) |
| AI-009 | Phishing classification in corporate email | Low | In production | Reviewed 2025-12-03 | Yes |
| AI-010 | Billing anomaly detection | Medium | In production | Not reviewed (due 2026-12-31) | No |
| AI-011 | Managed AI inference service (product) | Medium | In production (SL-1) | Reviewed 2026-05-20 | No |
| AI-012 | Candidate resume screening and ranking | High | Suspended | Not reviewed (due 2026-12-31) | No (disabled) |
| AI-013 | Sales lead scoring | Low | In production | Not reviewed (due 2026-12-31) | No |
| AI-014 | AI script generator in the AQ-1 RMM tool | Medium | In production (AQ-1 only) | Not reviewed (due 2026-10-31) | No |
| AI-015 | Enterprise generative AI assistant | Medium | In production | Reviewed 2026-02-04 | No |

**Tiering notes:** AI-001 is High because it can isolate hosts and suspend accounts that run federal, bank, and health care workloads. AI-008 is High because it is the automated gate between release rings; it can halt but not promote, which limits its failure to a delayed release. AI-014 is Medium only because technicians review scripts before running them; if it ran scripts directly it would be High. AI-006 is Medium: it blocks sign-ups, but service access is not one of the listed consequential decision categories, and every rejection can be appealed to a human.

## 5. Provider-specific AI risks
| Risk | Use cases | Treatment |
|---|---|---|
| Automated action on customer services at scale (one model error affects many tenants) | AI-001, AI-008 | Human approval for isolation and suspension in G1 and for bank customers (POAM-013); halt-only design for AI-008; rate limits on automated actions per hour |
| Manipulation of the model through attacker-controlled input (crafted log fields) | AI-001 | Sanitize free-text fields; adversarial test set; rule-based detections run independently of AI scores (P01 R-047) |
| Customer content reaching an AI service outside its approved scope | AI-002, AI-015 | Cross-case retrieval removed (P01 R-046, avoided); customer content blocked from the workforce assistant |
| Vendor features enabled without review | AI-005, AI-012, AI-013, AI-014 | Intake block in procurement and change management; reviews by 2026-12-31 |
| AI-generated code or scripts reaching production or customer servers | AI-007, AI-014 | Second-engineer review; AI-014 frozen for bank customers and retired with the RMM tool |

## 6. MEASURE: portfolio testing gaps
- **AI-001** has performance data from analyst labels but no adversarial testing and no fairness view of account suspensions until this review (section 7).
- **AI-006** shows a false-positive rate for sign-ups from three countries about twice the overall rate. The committee asked for a threshold review by 2026-12-31 and kept human review of every appeal.
- **AI-010, AI-013, and AI-014** have no defined metrics yet; metrics are a condition of their reviews.
- **AI-012** needs an adverse impact analysis by counsel before any re-enable.

## 7. Full assessment: AI-001 AI-driven security operations (alert triage)
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Score every SOC alert for likelihood of a true incident; summarize context for analysts; auto-close the lowest-score classes; for a defined set of high-confidence classes, isolate a host or suspend a customer account automatically |
| Users | The 24x7 SOC (about 140 staff); U.S.-person analysts for G1 |
| Affected people and organizations | Customers whose hosts are isolated or accounts suspended (including agencies, banks, and health care customers); customer end users of affected services; staff named in alerts |
| Data | Inputs: security telemetry, account metadata, threat intelligence. Outputs: scores, summaries, actions. G1 alerts processed only by the dedicated G1 instance |
| Build or buy | Buy and configure: vendor model with company-specific tuning; contract prohibits vendor training on company data |
| Volume | About 2.1 million alerts a month enterprise-wide; about 46,000 G1 alerts auto-closed in the first half of 2026; 61 automated host isolations in G1 in the same period |
| Not intended | Final incident classification for FedRAMP, bank, or SEC purposes (always human); actions on G1 accounts (suspension disabled in G1) |

### 7.2 Risk tier
High (section 4). The tier would drop to Medium only if every automated action needed prior human approval.

### 7.3 MEASURE (2026-01-01 to 2026-06-30)
| Trustworthy characteristic | Test / metric | Threshold | Result | Pass? |
|---|---|---|---|---|
| Valid and reliable | Precision of high-score alerts against analyst labels | 85% or more | 91% | Yes |
| Valid and reliable | Missed escalations in auto-closed alerts (Internal Audit sample of 60) | 0 above low severity; under 2% overall | 2 of 60 (3.3%), both low severity | **No** |
| Safe | False-positive automated host isolations in G1 | Under 2% | 3 of 61 (4.9%), with 40 to 95 minutes of customer impact | **No** |
| Secure and resilient | Robustness to crafted log content | Adversarial test set passes | Not yet tested | **No** |
| Accountable and transparent | Every automated action logged with model version and score; customers told why a host was isolated | 100% | Logged 100%; customer notice text generic | Partly |
| Explainable and interpretable | Analyst sees the top factors behind each score | Available | Available | Yes |
| Privacy-enhanced | No vendor training on company data; G1 data stays in G1 | Contract and architecture | In place | Yes |
| Fair, with harmful bias managed | Account suspension rate by customer segment and sign-up country, compared with confirmed-abuse rates | Ratio within 1.25 | Two sign-up countries at 1.6 and 1.4 (free tier only) | **No** |

### 7.4 MANAGE
- **Human in the loop (POAM-013):** human approval before host isolation in G1 (live 2026-10-15) and before any isolation or suspension for bank customers (by 2026-11-30). Account suspension stays disabled in G1. Elsewhere, automated actions continue under EXC-2026-040 only for the free-tier crypto-mining class, with automatic restore on analyst reversal.
- **Auto-close:** daily random sample of 50 auto-closed alerts reviewed by an analyst; any missed escalation triggers a threshold review within 5 business days.
- **Adversarial robustness (P01 R-047):** sanitize free-text log fields before scoring; quarterly adversarial test set from 2027-01; rule-based detections for the highest-severity techniques run independently of AI scores.
- **Fairness:** suspension thresholds for the two outlier sign-up countries recalibrated against confirmed-abuse data by 2026-12-31; human review for every suspension appeal within 4 hours.
- **Transparency:** specific customer notice text for each action class (what happened, why, how to restore) by 2026-11-30.
- **FedRAMP:** each change to the G1 instance (thresholds, model versions, human approval step) is evaluated under SCN-CSO-EVA and recorded in the HCP-G change records.
- **Monitoring:** weekly reversal rates; quarterly precision, recall, auto-close miss rate, suspension ratios, and adversarial results to the committee.
- **Incidents:** a harmful automated action is handled as a security incident (P08 classification) and, if it disrupts a bank's covered services for four or more hours, triggers the bank notice.
- **Decommissioning or rollback:** fall back to rule-based triage (tested 2026-08; P05 DEP-13) if precision drops below 80% for two weeks, if the vendor changes data-use terms, or if a model error causes a customer-impacting incident that recurs.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier use case has quarterly performance and fairness metrics (inventory column `monitoring`) reported to the committee; threshold breaches trigger re-review.
- **Incident handling:** AI incidents (harmful action, data exposure, manipulation) are logged as SOC events and follow P08 where security or customer data is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts require notice of material model changes and prohibit training on company or customer data.
- **Products:** AI-011 follows the same review, plus an acceptable use policy, model documentation for company-provided models, and abuse monitoring.
- **Decommissioning:** use cases are retired if they fail monitoring thresholds twice, lose required vendor terms, or their host system is retired (AI-014 with the RMM tool by 2027-03-31).

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-08, on the AI governance committee's recommendation of 2026-09-02:
1. **AI-001:** approved to continue with conditions: human approval for G1 host isolation by 2026-10-15 and for bank customers by 2026-11-30 (POAM-013); daily auto-close sampling; fairness recalibration and customer notice text by 2026-12-31; adversarial testing from 2027-01.
2. **AI-008:** approved to continue; quarterly replay tests must halt 100% of known bad releases; it will also gate the new two-person guest-agent workflow (POAM-001).
3. **AI-014:** use frozen for bank customers immediately; committee review by 2026-10-31; retired with the RMM tool by 2027-03-31 (POAM-022).
4. **AI-005, AI-010, AI-013:** may continue in current scope until committee review by 2026-12-31 (POAM-025); no expansion.
5. **AI-012:** ranking stays disabled until committee review and an adverse impact analysis by counsel are complete.
6. **AI-011:** counsel to decide by 2026-12-31 whether Colorado SB26-189 developer documentation duties apply to the product for customer deployments on or after 2027-01-01.

# AI Governance Risk Assessment: Enterprise AI Portfolio and the Generative AI Assistant Across Subsidiaries

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded holding company with four operating subsidiaries; six states) |
| Tier / Vertical | Enterprise / Management of Companies and Enterprises |
| Scope | Enterprise AI portfolio (14 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the enterprise generative AI assistant across subsidiaries, in section 7 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1); repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Data and Analytics Officer), meeting of 2026-08-19; the GRC team prepared the portfolio review; AI-001 tests run 2026-08-03 to 2026-08-14 |
| Decision | Executive risk committee, 2026-09-14 (section 9) |
| Related | P01 R-015, R-016, R-017, R-041, R-042, R-043, R-044, R-045, R-064 (enterprise risk ER-08); P03 G-031; P06 POL-01 4.13, POL-04 4.3 and 4.10, POL-05 4.6; P07 POAM-021 and POAM-024 |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 14 |
| Risk tier | High 3, Medium 8, Low 3 |
| Status | In production 12, Pilot 1, Suspended 1 |
| Committee review complete | 8 of 14 |
| Not yet reviewed | 6: AI-005, AI-008, AI-010, AI-011, AI-013, AI-014 (all due 2026-11-30, POAM-021) |
| High-tier tools making or shaping decisions about people | 3: AI-002 credit underwriting, AI-004 application fraud flags (credit), AI-005 resume ranking (employment, suspended) |
| High-tier tools with current local fairness testing | 0 of 3 (AI-002 not retested since its 2025-11 retraining; AI-004 vendor data only; AI-005 never tested) |

**Main findings:**
1. The generative AI assistant (AI-001) **does not respect company boundaries**. It respects file permissions, and many sites are shared with all 12,000 employees, so a Building Products employee could retrieve Finance customer exports, payroll data, plan PHI, or deal documents. Expansion was paused for those areas on 2026-08-14 (section 7).
2. Six use cases entered through vendor feature releases or team-level adoption before the committee's intake gate caught them. Two touch SOX processes (AI-010 invoice anomalies, AI-013 code for SOX systems).
3. The credit model (AI-002), the group's most consequential AI, has not had fairness testing since its retraining.

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the board risk committee reviews quarterly.

**Members:** Chief Data and Analytics Officer (chair); CISO; Chief Privacy Officer; Chief Compliance Officer; General Counsel's delegate (securities and employment); Chief Human Resources Officer; Finance Chief Credit Officer; Finance Information Security Officer; the four subsidiary BISOs; and the Chief Risk Officer. Internal Audit observes.

**Why a group committee.** In a holding company, each subsidiary buys software on its own, and AI arrives inside those products. One group committee sets one rubric, one inventory, and one approved tools list (STD-05.3), while each subsidiary President stays accountable for the AI used in that subsidiary.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee; the subsidiary President signs as business owner | Local validation and fairness testing; impact assessment; human review design; notice to affected people; adverse action or explanation process where the law requires it; monitoring plan |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy, security, and data-access review |
| Low | Committee chair (fast track) | Approved-tool listing; data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including an AI feature switched on inside an existing product, must be registered before use (POL-01 4.13; POL-05 4.6; STD-05.3). Procurement and change management now block AI features without an inventory ID; the gate went live 2026-06-01, after the six unreviewed use cases had started. The GRC team owns the inventory.

**Policies:** POL-01 4.13 (assess before use); POL-04 4.3 (Restricted labels exclude content from AI retrieval) and 4.10 (Restricted data only in approved tools); POL-05 4.6 (approved tools only; no AI in decisions about hiring, discipline, pay, or credit without committee approval; no AI drafting of SEC disclosures without disclosure committee review); STD-05.3 (approved AI tools list).

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier tool; annual re-review of every use case; re-review after any retraining or material vendor model change.

## 3. MAP: context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| ECOA and Regulation B (12 CFR Part 1002) | **Yes**, for AI-002, AI-003, AI-004 | Finance must not discriminate on a prohibited basis in any aspect of a credit transaction (1002.4(a)) and must give specific principal reasons for adverse action; statements that the applicant failed to achieve a qualifying score on the creditor's scoring system are insufficient (1002.9(b)(2)). Creditors generally may not ask about race, color, religion, national origin, or sex (1002.5(b)). Since the 2026 amendment, 1002.6(a) states that ECOA does not provide for the effects test; using a prohibited basis remains unlawful (1002.6(b)), so the group still tests outcomes as a risk control |
| FTC Safeguards Rule (16 CFR Part 314) | **Yes**, for AI-001, AI-002, AI-011, AI-013 | Limiting users' access to the customer information they need (314.4(c)(1)(ii)); secure development (314.4(c)(4)); service provider oversight of AI vendors (314.4(f)); adjusting the program for material changes such as the assistant rollout (314.4(g)) |
| Federal employment discrimination law (Title VII, 42 U.S.C. 2000e-2; ADEA) | **Yes**, for AI-005 | The statutes apply to hiring decisions whatever tool is used. The Uniform Guidelines treat a selection rate below four-fifths of the highest group's rate as general evidence of adverse impact (29 CFR 1607.4(D)). EEOC's AI technical assistance on Title VII was removed from its website, but the statutes did not change (`00_universal-framework/cross-sector/`) |
| HIPAA plan sponsor limits (45 CFR 164.504(f), 164.314(b)) | **Yes**, for AI-001 | Plan PHI may be seen only by the staff the plan documents name; the assistant must not surface it to others (P03 G-055 to G-058) |
| Regulation FD (17 CFR 243.100); insider trading policy; Rule 13a-15(b) | **Yes**, for AI-001 | MNPI in deal rooms and earnings drafts must not reach unauthorized staff; AI must not draft filed or furnished disclosures outside the disclosure controls |
| Recording consent laws | **Yes**, for AI-001 meeting transcripts | Laws differ by state; the group applies all-party prior consent for any transcribed meeting. Florida worked example: interception is lawful when all parties have given prior consent (Fla. Stat. 934.03(2)(d)). Transcription is off for calls with customers, borrowers, dealers, vendors, and deal counterparties |
| FTC Act Section 5 (15 U.S.C. 45(a)) | Indirectly | Accuracy of customer-facing AI statements (AI-006 arrival times, AI-009 alerts, AI-012 chat) and of any claims about the group's AI |
| SOX section 404 (N55-R03) | **Yes**, for AI-010 and AI-013 | AI-assisted invoice processing and code changes to SOX systems must stay within tested ICFR controls (human approval; change control) |
| Colorado SB26-189 (effective 2027-01-01) | **No** | Applies to deployers doing business in Colorado; the group and Finance operate only in six southeastern states. Recheck before any expansion |
| Florida Digital Bill of Rights | **No** | The group is not a "controller" under Fla. Stat. 501.702 (P03 G-065) |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person (here, credit or employment) or able to affect physical safety.

| ID | Use case | Subsidiary | Tier | Status | Committee review |
|---|---|---|---|---|---|
| AI-001 | Enterprise generative AI assistant | All | Medium | In production (about 4,000 users) | Pilot 2026-01-21; re-reviewed 2026-08-19 |
| AI-002 | Credit underwriting model | Finance | High | In production | 2025-05-14 (before retraining); re-review due 2026-11-30 |
| AI-003 | Collections prioritization | Finance | Medium | In production | 2025-09-17 |
| AI-004 | Application fraud flags | Finance (SL-1) | High | In production | 2025-09-17 |
| AI-005 | Resume screening and ranking | All (GBS HR) | High | Suspended | Not reviewed (due 2026-11-30) |
| AI-006 | Dispatch and route optimization | Home Services | Low | In production | 2026-02-18 |
| AI-007 | Quote pricing recommendations | Building Products | Medium | In production | 2026-03-18 |
| AI-008 | Machine-vision quality inspection | Manufacturing | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-009 | Fault prediction alerts (SL-2) | Manufacturing | Medium | In production | 2026-04-15 |
| AI-010 | Invoice capture and anomaly detection | GBS | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-011 | SOC alert triage assistant | GBS | Low | In production | Not reviewed (due 2026-11-30) |
| AI-012 | Customer chat assistant | Home Services | Medium | In production | 2026-05-20 |
| AI-013 | Developer code assistant | GBS; Finance | Medium | In production | Not reviewed (due 2026-11-30) |
| AI-014 | Treasury cash forecasting | GBS | Low | Pilot | Not reviewed (due 2026-11-30) |

**Tiering notes:** AI-004 is High because a fraud flag delays or blocks credit for the applicant even though an analyst decides. AI-008 is Medium rather than High because every unit still passes a non-AI pressure and leak test before shipment; removing that test would re-tier it to High (safety). AI-001 is Medium rather than Low because Restricted data is in its reach; any use in a decision about a person is prohibited and would make it High.

## 5. High-tier tools: what the law and the rubric require
| Tool | Duty | What the group does | Status |
|---|---|---|---|
| AI-002 credit model | Specific principal reasons for adverse action (1002.9(b)(2)); no prohibited basis (1002.4(a), 1002.6(b)) | Reason codes generated from model features; underwriter review of refer decisions; prohibited bases and obvious proxies excluded from features | Partially met: reason codes not re-validated and no fairness test since the 2025-11 retraining |
| AI-004 fraud flags | No prohibited basis; adverse action reasons if a flag leads to denial | Analyst reviews every flag; denials use the standard reason process | Partially met: flag-rate review by segment not yet done on local data |
| AI-005 resume ranking | Title VII and ADEA; adverse impact measure (29 CFR 1607.4(D)) | Ranking disabled; manual screening | Met for now (disabled); review and adverse impact analysis required before any re-enable |

These rows match P01 R-016 and R-042 and POAM-021.

## 6. MEASURE: fairness testing plan for High-tier tools
**Data limits.** Finance does not ask applicants about race, color, religion, national origin, or sex (12 CFR 1002.5(b)), so testing uses a proxy estimation method approved by counsel, plus age band and geography from the application. Results are treated as risk indicators, not as findings of discrimination, and go to the committee and the Chief Compliance Officer.

| Tool | Metric | Groups compared | Threshold for action |
|---|---|---|---|
| AI-002 credit model | Approval-rate ratio and pricing-tier distribution at equal credit risk; reason-code accuracy | Proxy race and ethnicity groups; sex (proxy); age band (over 62 compared with others); rural and urban ZIP codes | Approval-rate ratio below 0.80 for any group, or a pricing gap that is not explained by credit risk; any reason code that does not match the model's top features |
| AI-004 fraud flags | Flag rate and false-positive rate | Age band; ZIP-code income tier; dealer segment | False-positive rate for any group more than 1.25 times the overall rate |
| AI-005 resume ranking (before any re-enable) | Selection rate ratio at each stage | Sex, race and ethnicity (from voluntary self-identification), age band | Ratio below four-fifths of the highest group's rate (29 CFR 1607.4(D)) or statistically significant differences |

AI-002 testing is due 2027-01-31 and the reason-code review 2027-03-31 (POAM-021). Testing repeats after every retraining.

## 7. Full assessment: AI-001 enterprise generative AI assistant across subsidiaries
### 7.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Help staff draft and summarize email and documents, write spreadsheet formulas, recap internal meetings, and find information in files they can already open |
| Users | About 4,000 enrolled users: GBS 1,500, Building Products 900, Home Services 700 (office and dispatch staff, not technicians), Manufacturing 600, Finance 300 |
| Affected people | All 12,000 employees, about 520,000 Finance consumers, about 21,000 plan participants and beneficiaries, subsidiary customers, dealers, vendors, investors (through MNPI), and acquisition counterparties |
| Data: inputs | Prompts, plus anything the user can open in the productivity suite: email, chat, about 9,800 collaboration sites, and meeting content. This includes Restricted data (POL-04) |
| Data: training | None by the group. The provider's enterprise terms say prompts and responses are not used to train its models (P01 R-064). The third-party risk team confirmed the terms and the provider's SOC 2 Type 2 report on 2026-07-08 |
| Data: outputs | Draft text, summaries, and answers with links to source files; outputs inherit the classification of their sources |
| Build or buy | Configure: an enterprise add-on to the existing productivity suite, run by the same provider in the same tenant boundary |
| Features turned off | Agent actions (sending mail, editing records); plugins and connectors to the ERP, HRIS, loan platform, and other business systems; transcription of calls with outside parties |
| Not intended | Any decision about a person (hiring, discipline, pay, credit, collections); drafting filed or furnished SEC disclosures without disclosure committee review; legal advice; technical instructions for equipment installation or repair |

**Holding company specifics.** One tenant serves five legal populations: the holding company and four subsidiaries, each with its own customers and regulators. The assistant does not know which company a user works for; it only knows what the user can open. **Site sharing and sensitivity labels are therefore the controls that matter most**, and the cross-entity data-access test is the most important part of MEASURE.

### 7.2 Risk tier
Medium (section 4). Escalation triggers to High: any use in a decision about a person; turning on agents or connectors to business systems; use by Finance underwriting or collections staff in customer decisions.

### 7.3 MEASURE (tests run 2026-08-03 to 2026-08-14)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Secure and resilient (data access) | Cross-entity access test: 40 prompts by test users in each subsidiary seeking another entity's Restricted data (seeded canary documents in Finance, HR, benefits, and deal sites) | 9 of 40 prompts surfaced another entity's Restricted data before remediation (payroll exports, a Finance customer export, a deal summary); 1 of 40 after the Finance, HR, benefits, and deal sites were fixed on 2026-08-14 (a vendor bank-detail form on an accounting site) | **No** (until POAM-024 closes) |
| Secure and resilient (prompt injection) | 10 shared documents with hidden instructions | 2 of 10 produced misleading summaries; none caused data to leave the tenant (agents and connectors are off) | Yes, with training |
| Valid and reliable | 200 sampled summaries checked against sources | 3.5% had a factual error; 1% cited a source that did not support the statement | Yes (threshold 5%) |
| Accountable and transparent | AI-drafted content labeled in email and documents; usage logs retained | Labels on; logs kept 1 year | Yes |
| Privacy-enhanced | No training on group data; Restricted labels exclude content from retrieval | Terms confirmed; labels cover only 62% of sites holding Restricted data | **No** (until POAM-024 closes) |
| Explainable and interpretable | Answers link to source files | Available | Yes |
| Fair, with harmful bias managed | Review of usage logs for prohibited uses | 3 managers used the assistant to draft disciplinary or pay recommendations; counseled under POL-05 4.6; HR prompt monitoring added | Yes, with monitoring |

### 7.4 MANAGE
- **Data boundaries first:** remove organization-wide sharing from the 212 sites; label all 1,240 unlabeled sites holding Restricted data; labeled sites excluded from retrieval (POAM-024, due 2026-12-31). Finance, HR, benefits, and deal sites were fixed first (2026-08-14).
- **Staged re-enable:** Finance and HR users stay paused until their sites pass the cross-entity test twice in a row; then each subsidiary is re-enabled in turn.
- **Human in the loop:** users review every output; no agent actions; no AI-drafted SEC disclosure text outside the disclosure committee process.
- **Monitoring:** monthly cross-entity access test with canary documents; quarterly accuracy sample; monthly review of usage logs for prohibited uses (HR, credit, MNPI).
- **Incidents:** if the assistant surfaces Restricted data to an unauthorized user, it is handled as a security event under P08; for Finance customer information, the Finance Information Security Officer decides on notices and includes it in the Qualified Individual report (16 CFR 314.4(i)); for plan PHI, the plan's privacy official is told (164.314(b)(2)(iv)).
- **Decommissioning:** suspend for a subsidiary if the cross-entity test fails twice in a row after remediation, if the provider changes its data-use terms, or if a prohibited use is found that monitoring did not catch.

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier tool has quarterly performance and fairness metrics (inventory column `monitoring`) reported to the committee; drift, retraining, or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe or wrong output, data exposure, fairness finding) are logged as SOC or compliance cases and follow P08 where security or personal data is involved.
- **Third parties:** AI vendors are tiered in the vendor program; contracts require notice of material model changes and no training on group data.
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice, change data-use terms, or lose their business owner; the inventory records retirement.

## 9. Decisions
The executive risk committee approved these decisions on 2026-09-14, on the AI governance committee's recommendation of 2026-08-19:
1. **AI-001:** approved to continue with conditions: no expansion until POAM-024 closes (2026-12-31); Finance and HR stay paused until they pass the cross-entity test twice; monthly canary testing reported to the committee.
2. **AI-002:** approved to continue; fairness testing by 2027-01-31 and reason-code review by 2027-03-31 (POAM-021); re-review by the committee by 2026-11-30.
3. **AI-004:** approved to continue; local flag-rate review with the AI-002 testing.
4. **AI-005:** ranking stays disabled until committee review and an adverse impact analysis are complete.
5. **AI-008, AI-010, AI-011, AI-013, AI-014:** may continue in current scope until committee review by 2026-11-30; no expansion. AI-010 and AI-013 are also added to the SOX scoping review.

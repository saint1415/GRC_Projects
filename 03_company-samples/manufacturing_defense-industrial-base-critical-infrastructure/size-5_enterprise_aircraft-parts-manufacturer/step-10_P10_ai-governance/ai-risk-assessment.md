# AI Governance Risk Assessment: Enterprise AI Portfolio and the Generative AI Assistant Used with CUI Engineering Documents

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded tier-1 aerostructures and aircraft components manufacturer) |
| Tier / Vertical | Enterprise / Defense Industrial Base |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of AI-001, the generative AI assistant used with CUI engineering documents, in section 6 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (NIST AI 600-1); repository risk tier rubric |
| Assessor / date | AI governance committee (chaired by the Chief Data and AI Officer), meeting of 2026-08-19; GRC team prepared the portfolio review |
| Decision | Executive risk committee, 2026-09-10 (section 8) |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 4, Medium 4, Low 4 |
| Status | In production 9, Pilot 2, Suspended 1 |
| Committee review complete | 8 of 12 |
| Not yet reviewed | 4: AI-007, AI-009, AI-010, AI-012 (all due 2026-11-30, POAM-024) |
| Use cases that touch CUI or export-controlled data | 3: AI-001, AI-004, AI-010 (plus AI-011 with Security Protection Data) |

**Main findings:** 4 use cases run without committee review, including two High-tier tools: AI-010 (additive build parameters for flight hardware, in pilot) and AI-009 (resume ranking, now switched off). The AI-001 assistant performs well on native documents, but it produced 2 wrong numeric values in 200 test answers, does poorly on scanned legacy drawings, and would surface CUI from 46 suite sites that are open to all CEE users. AI-006 (SL-2) lacks a model registry and drift monitoring, which is also a SOC 2 Processing Integrity gap (P09).

## 2. GOVERN: AI governance committee operating model
**Charter.** The AI governance committee was formed in 2025 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 (P01), which the risk and technology committee of the board reviews quarterly.

**Members:** Chief Data and AI Officer (chair); CISO; Vice President, Engineering; Vice President, Quality; Vice President, Trade Compliance; Director, CMMC Program Office; Chief Human Resources Officer (for workforce tools); a delegate of the General Counsel; the Corporate Facility Security Officer (for anything near classified programs); and the data science lead. Internal Audit observes.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Validation on company data; bias or quality-parity testing; impact assessment; human review design; export and CUI review; monitoring plan |
| Medium | Committee vote | Human oversight design; output quality monitoring; CUI and export review where relevant; security review |
| Low | Committee chair (fast track) | Approved tools listing (STD-05.3); data handling rules (POL-04) |

**Intake and inventory.** Any new AI use, including AI features switched on inside existing vendor products, must be registered before use (POL-05 4.5; STD-05.3). Since 2026-06, procurement and change management block AI features without an inventory ID. The GRC team owns the inventory.

**CUI rules that apply to every use case (POL-04 4.2 and 4.10; POL-05 4.5 and 4.6):**
- CUI and export-controlled data may be used only with tools inside the government-community authorization boundary and listed in the provider's CRM (DFARS 252.204-7012(b)(2)(ii)(D)).
- A tool that processes CUI is a CUI Asset and must be in the SSP, the asset inventory, and the network diagram before use (32 CFR 170.19(c)).
- Retrieval must respect export attributes; foreign-person users may not receive ITAR technical data (22 CFR 120.56).
- AI output is never the source of a dimension, tolerance, NC program, build parameter, inspection criterion, or export classification.

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier tool; annual re-review of every use case.

**Why 4 use cases lack review.** AI-007 and AI-012 arrived as vendor feature releases before the intake block; AI-009 was switched on by the HR SaaS vendor; AI-010 started as a printer manufacturer validation study. The committee set review dates for all four (section 8).

## 3. MAP: context and applicable rules
| Rule | Applies to | Why |
|---|---|---|
| DFARS 252.204-7012(b)(2)(ii)(D) | AI-001 | A cloud service that stores, processes, or transmits covered defense information must meet FedRAMP Moderate-equivalent requirements and the clause's incident paragraphs. The provider confirmed in writing on 2026-07-30 that the assistant is inside its authorization boundary and listed in the CRM |
| CMMC scoping (32 CFR 170.19(c)) | AI-001, AI-004, AI-010, AI-011 | AI-001, AI-004, and AI-010 are CUI Assets; AI-011 is a Security Protection Asset. All must be in the SSPs and diagrams (P02 lists AI-001) |
| ITAR (22 CFR 120.56; 120.54(a)(5)) and EAR (15 CFR 734.13(a)(2); 734.18(a)(5)) | AI-001, AI-010 | Release of technical data to foreign persons is an export; carve-outs need FIPS-validated end-to-end encryption and storage conditions |
| Title VII disparate impact (42 U.S.C. 2000e-2(k)) | AI-009 | Employment selection procedures with adverse impact must be justified; an adverse impact analysis is required before any re-enable |
| Texas Bus. & Com. Code 552.056 (added by HB 149, effective 2026-01-01) | AI-009 (Texas hiring at TX-1) | A person may not develop or deploy an AI system with the intent to unlawfully discriminate against a protected class; disparate impact alone does not show intent. The attorney general enforces it |
| AS9100 and prime quality clauses (contract) | AI-004, AI-010 | Inspection and special process changes need validation and customer approval where required |
| FTC Act Section 5 | AI-006; vendor claims for all | Accuracy of claims made to SL-2 operators; vendor claims the company relies on |
| Colorado SB26-189 and similar state AI laws | No | The company has no operations in those states; counsel reviews each new state before hiring there |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision (here, employment) or able to affect physical safety (flight hardware, aircraft maintenance).

| ID | Use case | Tier | Status | Committee review | CUI or export-controlled data |
|---|---|---|---|---|---|
| AI-001 | Generative AI assistant used with CUI engineering documents | Medium | Pilot (300 U.S.-person engineers since 2026-06-15) | Reviewed 2026-05-20 (pilot); re-reviewed 2026-08-19 (conditions set) | Yes (CUI, ITAR, EAR) |
| AI-002 | Corporate generative AI assistant in the commercial productivity suite for non-CUI work (email drafting, meeting summaries) | Medium | In production (about 7,500 users) | Reviewed 2026-01-14 | No (blocked by policy and data loss prevention) |
| AI-003 | Code assistant for software engineers working on SL-1, SL-2, and corporate applications | Low | In production (about 180 developers) | Reviewed 2026-02-11 | No (not enabled for CEE repositories) |
| AI-004 | Computer vision flagging of possible defects in ultrasonic inspection scans of composite panels at GA-1 | High | In production (GA-1) | Reviewed 2025-11-18 | Yes (CUI images; runs on MOZ servers) |
| AI-005 | Predictive maintenance models for CNC machines using spindle vibration and temperature data | Low | In production (FL-2, TX-1) | Reviewed 2026-03-04 | No |
| AI-006 | SL-2 aircraft health monitoring models that predict component wear and issue maintenance alerts to airline operators | High | In production (19 operators) | Reviewed 2026-03-25 | No |
| AI-007 | Supplier risk scoring that combines delivery, quality, financial, and cyber questionnaire data | Medium | In production (since 2026-04) | Not reviewed (intake 2026-07; review due 2026-11-30) | No |
| AI-008 | Demand and spares forecasting in ERP | Low | In production | Reviewed 2025-12-02 | No |
| AI-009 | Applicant resume screening and ranking in the HR SaaS | High | Suspended (ranking off) | Not reviewed (review due 2026-11-30) | No |
| AI-010 | Additive build parameter optimization that proposes laser power and scan strategy settings for AZ-1 builds | High | Pilot (validation builds only) | Not reviewed (required before production; due 2026-11-30) | Yes (ITAR technical data) |
| AI-011 | SOC alert triage assistant that summarizes alerts and suggests next steps | Low | In production | Reviewed 2026-04-29 | Security Protection Data only |
| AI-012 | Contract clause extraction that flags DFARS, CMMC, and export clauses in solicitations and purchase orders | Medium | In production (since 2026-05) | Not reviewed (review due 2026-11-30) | No (CUI attachments excluded) |

**Tiering notes:** AI-004 and AI-010 are High because their outputs bear on flight hardware acceptance or build parameters, even with a human decision. AI-006 is High because airline operators use its alerts in maintenance planning. AI-001 stays Medium because it only drafts and searches, and a qualified engineer and a checker review every use; any use for numbers, programs, or parameters would re-tier it to High.

## 5. MEASURE: portfolio testing gaps
| Use case | What is tested | Gap | Plan |
|---|---|---|---|
| AI-004 | Miss rate against inspector findings, by panel type, thickness, and scanner unit | None open; monthly results within threshold (miss rate under 0.5% of inspector-confirmed indications) | Continue |
| AI-006 | Precision and recall against confirmed maintenance findings, by aircraft type and operator | No model registry or drift monitoring | Registry and monthly drift review by 2027-02-28 (P09 PI1.3) |
| AI-009 | Selection rates by sex and race and ethnicity where recorded (four-fifths comparison as a screening heuristic) | Never tested | Adverse impact analysis by counsel before any re-enable |
| AI-010 | Build quality (density, mechanical test coupons) for optimized against qualified parameters | Validation builds only; no protocol approved | Validation protocol and committee review before production |

## 6. Full assessment: AI-001 generative AI assistant used with CUI engineering documents
### 6.1 MAP
| Item | Description |
|---|---|
| Purpose and intended use | Search and summarize specifications and engineering change requests; draft first versions of work instructions and reports; answer "where is this requirement" questions across project documents |
| Users | Pilot of 300 engineers (design, manufacturing, quality) since 2026-06-15; all U.S. persons; proposed expansion to about 1,400 |
| Affected people | No decisions about individuals. Indirectly: operators and inspectors who use documents drafted with AI help, and users of the aircraft parts |
| Data | Inputs: prompts plus suite files the user can already open (CUI, ITAR, EAR). Outputs: summaries and drafts (CUI). Provider terms state customer data is not used to train models |
| Build or buy | Buy (configure): an add-on inside the CUI collaboration suite (SYS-02), within the government-community authorization boundary |
| Not intended | Creating or changing dimensions, tolerances, NC programs, build parameters, inspection criteria, or export classifications; decisions about employees; use by foreign persons. Enabling any of these requires re-assessment |

### 6.2 Risk tier
Medium (section 4). Escalation triggers: any use for numbers, programs, or parameters; connecting the assistant to PLM or MES or letting it act rather than draft; enabling it for any foreign person; any provider change to data use, location, or support personnel terms.

### 6.3 MEASURE (pre-expansion test, 2026-08-03 to 2026-08-14)
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | 200-question set with known answers written by engineers; threshold 90% correct and complete, and **zero wrong numeric values** | 187 of 200 correct (93.5%); 2 answers stated a wrong numeric value (a torque value and a heat treat temperature) | **No.** Confirms the rule that numbers come only from the source |
| Safe | Outputs labeled "AI draft, verify against source"; checker sign-off; numbers copied from the source | Label on; checker sign-off already required by the quality system | Yes, with the POL-05 4.6 rule |
| Secure and resilient | Inside the FedRAMP Moderate-or-higher boundary and the CRM; access through SYS-01 with security keys; prompts and responses logged for 1 year | Written provider confirmation received 2026-07-30; logging live | Yes |
| Accountable and transparent | Named owner; pilot list driven by the export attribute; monthly log sampling | Owner and pilot list in place; monthly sampling started 2026-07 | Yes |
| Explainable and interpretable | Every answer cites source files and passages | Citations in 200 of 200 answers; 4 pointed to a superseded revision | Partial. Revision control must come from PLM |
| Privacy-enhanced (here: CUI and export control) | Retrieval limited to what the user can open; permission audit of suite sites; test account without the ITAR attribute ran 40 prompts aimed at ITAR content | 46 of 410 project sites open to all CEE users; the test account received no ITAR content | **No.** Permission clean-up required (P01 R-059) |
| Fair, with harmful bias managed (quality parity) | Accuracy by document type (native, customer PDF, scanned legacy), units (inch, metric), and user group; flag any group more than 10 points below overall | Scanned legacy drawings 71% vs 93.5% overall | **No.** Disparity flagged |

**Quality-parity plan.** The assistant decides nothing about people, so the fairness risk is uneven quality: some documents and users get worse answers. Groups, metric, and threshold are as above; tests run before expansion, quarterly on a refreshed 200-question set, and after any provider model update. Scanned legacy drawings stay excluded until the provider shows results within threshold.

### 6.4 MANAGE
- **Human in the loop:** drafts and searches only; it never sends, files, releases, or changes anything in PLM or MES. A qualified engineer reviews every output and copies any number from the source; the checker is told a draft was AI-assisted.
- **Monitoring:** monthly sample of 50 logged prompts and responses by the Vice President, Engineering's delegate; quarterly 200-question test; quarterly permission audit; monthly report of public AI blocks from the proxy (R-005).
- **Incidents:** a wrong number that reaches a released document is a quality nonconformance. CUI shown to a user without need-to-know, or any export concern, follows P08 and POL-03, including the DIBNet and voluntary disclosure decisions.
- **Decommissioning:** stop if the provider changes data use, location, or support terms; if a wrong number reaches a released document twice in a quarter; or if the assistant ever returns ITAR content to a user without the ITAR attribute.

## 7. MANAGE: portfolio controls
- **Monitoring:** each High-tier tool has quarterly performance and parity metrics (inventory column `monitoring`) reported to the committee; drift or threshold breaches trigger re-review.
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse) are logged as SOC, quality, or HR events and follow P08 where CUI, export-controlled data, or personal information is involved.
- **Third parties:** AI vendors are tier-1 in the vendor program; contracts require notice of material model changes and of new AI features (P01 R-064).
- **Decommissioning:** tools are retired if they fail monitoring thresholds twice or change data-use terms; the inventory records retirement.

## 8. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the committee's recommendation of 2026-08-19:
1. **AI-001:** continue the 300-user pilot. Expansion to about 1,400 engineers is approved only after (a) no suite site is open to all CEE users, (b) the pilot group is driven automatically by the U.S.-person and ITAR attributes, (c) the PLM attribute fix in POAM-002 is complete, and (d) a re-test passes the thresholds except for scanned legacy drawings, which stay excluded. Target 2026-12-31 (POAM-024).
2. **AI-004:** continue; monitoring unchanged.
3. **AI-006:** continue; model registry and drift monitoring by 2027-02-28, aligned with SOC 2 Processing Integrity (P09).
4. **AI-007 and AI-012:** may continue in current scope until committee review by 2026-11-30; no expansion. Their outputs never replace the manual CMMC status check and flowdown decisions.
5. **AI-009:** ranking stays off until committee review and an adverse impact analysis are complete.
6. **AI-010:** stays in validation builds; production use requires committee and executive risk committee approval, a validation protocol, and prime approval where process specifications require it.

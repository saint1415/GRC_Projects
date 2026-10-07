# AI Risk Assessment: Dam-safety sensor anomaly detection (one-page AI use assessment)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (dam safety engineering consultant; sole proprietorship) |
| Tier / Vertical | Sole Proprietorship / Dams |
| AI use case | AI-001: a third-party AI anomaly detection SaaS (SYS-08) the owner trialed on Client B instrument readings for the spillway gate reliability and instrumentation review. Readings uploaded 2026-05-19; use stopped 2026-07-20 |
| Also covered | AI-002: the built-in AI writing assistant in the email and file suite (SYS-01), a generative AI tool (section 7) |
| Framework | NIST AI RMF 1.0 (AI 100-1), short form; NIST AI 600-1 for AI-002. The AI RMF Critical Infrastructure Profile is only a concept note (2026-04-07) and is not relied on |
| Assessor / date | Owner-engineer, 2026-08-25 (self-assessment; no independent reviewer at this size). Decision adopted 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner and approval body:** the owner-engineer, who holds every role (POL-01 4.2). No AI committee at this size. Compensating step: the outside review in POL-01 4.5 (at least every second year) includes this assessment, and the client's written consent is a second check before any client data reaches an AI tool.
- **Policies that apply:**
  - POL-01 6.1: no agreement, no client data (vendor terms reviewed and listed; client consent where the agreement requires it)
  - POL-01 8.1 and 8.4: data levels; CEII used only for the purpose it was released for
  - POL-01 9.4: AI tools only after a written P10 assessment, a terms review, and client consent; never CEII or security-sensitive material; AI output is a lead to check, never a conclusion
  - POL-02 to POL-05 are pointer files; the rules above are in POL-01 (sections 6, 8, and 9)
- **Approved-tools list:** kept in the vendor list (POL-01 6.2; POAM-008). As of 2026-08-31: AI-001 **not approved**; AI-002 approved for administrative text only (section 7).
- **Why this matters for a consultant:** the business runs no dam and no control system. Its AI risk is to its clients' confidential data and to the quality of the dam safety conclusions it signs and seals (18 CFR 12.36(g) and (h)).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Flag unusual patterns (for example a piezometer rising out of step with reservoir level, or seepage rising after rain) in Client B's piezometer and seepage weir history, so the owner knows where to look first in the study |
| Users / operators | The owner-engineer only |
| Affected people | No one is the subject of a decision. The people who bear the risk are Client B (its confidential data and the quality of the study) and, indirectly, the people downstream of Client B's dam if a developing condition were missed |
| Data (inputs, training, outputs) | Inputs: three years of readings for 28 piezometers and 3 seepage weirs, exported as files from Client B's platform and uploaded by hand on 2026-05-19 (Client confidential, POL-01 8.1). No CEII, no security-sensitive material, and no personal information (checked 2026-07-22, P03 G-019). The tool was not connected to Client B's platform or to any control system. Training: the vendor's general model, fitted to the uploaded history. Outputs: flagged time windows with a score |
| Build or buy (vendor / model) | Buy. A small vendor's SaaS on a free trial under click-through terms. The terms allowed the vendor to keep uploads and use them to improve its service. No security report, no data processing terms, no deletion period |
| Not intended | Deciding whether a condition affects the safety of a project, replacing the owner's own plots and trigger-point checks, or writing any finding, conclusion, or recommendation |

**Applicable laws and rules**
| Rule | Applies? | Why |
|---|---|---|
| Client B agreement, GRS-B (1) and (3) | **Yes** | No sharing of Client B data with any third party without written consent. The upload had no consent, so it was a disclosure (P03 G-031, Not met). Client B was told on 2026-07-24 |
| 18 CFR 12.36(b)(1), (g), (h) | **Yes, for any Part 12D work** | A Part 12D report must evaluate "analysis of data from monitoring instruments"; the independent consultant declares that all conclusions are made independently and signs and seals the report. AI output can point to data to look at; it cannot be the evaluation (P03 G-029) |
| 18 CFR 12.10(a)(1) | Indirectly | The duty to report a condition affecting safety to the Regional Engineer "as soon as practicable after that condition is discovered, preferably within 72 hours" belongs to the licensee (Client B). If the owner confirms an unusual reading, the owner tells Client B's Chief Dam Safety Engineer the same day so Client B can decide. An AI flag never starts or replaces that call on its own |
| 18 CFR 388.113(h)(2) (CEII non-disclosure agreement) | **Yes, as a prohibition** | The upstream project CEII from the Client B study may be used only for that study and shared only with authorized recipients. It must never go to an AI tool (POL-01 9.4) |
| CSCA-A (1), passing down the FERC Security Program Rev. 3A (C-DAMS-R01) | **Yes, as a prohibition** | Client A security-sensitive material and CEII may never be placed in a personal or consumer account. No Client A data may go to any AI tool |
| FTC Act Section 5 | Indirectly | Applies to the vendor's own claims about accuracy and data use. Keep a copy of the claims and terms relied on |
| State AI laws (for example Colorado SB26-189, Texas TRAIGA) | No | They address consequential decisions about people or specific prohibited uses. This tool makes no decision about a person |
| Fla. Stat. 501.171 | No | No personal information went to the tool |
| NERC CIP (C-DAMS-R03) | No | No client project in scope is part of the Bulk Electric System (00_company-facts.md section 1) |

## 3. Risk tier
**Tier: High** (repository rubric in `00_universal-framework/projects/step-10_P10_ai-governance/README.md`: AI that "can affect physical safety or critical infrastructure operations").

**Rationale:** the tool only advises one engineer, but its subject is dam safety instrumentation. A missed anomaly (false negative) that the owner trusted could delay recognition of a developing failure mode at a client's dam. A false alarm could waste a field visit or alarm a client. The data-sharing problem (P01 R-007, Moderate) comes first, but even with consent and good terms the use would stay High because of what the data is about. The rubric's minimum controls for High are applied in sections 4 and 5: human review before any action, testing before use, this written impact assessment, notice to the affected party (Client B's written consent), and ongoing monitoring.

## 4. MEASURE
The trial was not planned as a test. The owner compared the tool's flags with the owner's own trend plots of the same readings after use stopped (2026-07-21 to 2026-07-23).

| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Tool flags compared with the owner's plots and Client B's event log (rain events, gate tests, instrument repairs) | 11 flags: 4 matched real changes (2 heavy-rain events, 2 gate test drawdowns), 5 were data gaps or reservoir drawdowns, 2 were a piezometer Client B had already logged as malfunctioning. The owner's plots showed 1 slow rise at a toe piezometer over 5 months that the tool did not flag | **No** (1 known slow trend missed) |
| Safe | No reading went unchecked because of the tool; every study observation came from the owner's own plots | No flag or tool output was used in any deliverable or sent to Client B | Yes |
| Secure and resilient | Vendor security report, MFA, data processing and deletion terms | No security report; password-only trial account; click-through terms. Deletion requested 2026-07-24 and confirmed by the vendor in writing 2026-08-12 | **No** |
| Accountable and transparent | Client knows and agrees; record of what was uploaded and when | No consent before upload; told 2026-07-24. Upload record rebuilt from the tool account on 2026-07-21 | **No** |
| Explainable and interpretable | Each flag names the instrument and readings that drove it | Flags gave a time window and score only, not the instrument or reason | **No** |
| Privacy-enhanced | No personal information in inputs or outputs | None | Yes |
| Fair, with harmful bias managed | Performance across instrument groups (plan below) | Not tested. The missed slow trend and the 5 data-gap flags suggest uneven performance | **Not tested** |

**Bias and performance-disparity testing plan (required before any reuse).** The tool makes no decision about people, so demographic metrics do not apply. "Bias" here means the tool watching some instruments, and so some failure modes, less well than others.

| Group compared | Metric | Threshold | When |
|---|---|---|---|
| Instrument type: piezometers vs seepage weirs | Share of known events flagged (from the client's event log and the owner's plots) | At least 90% in each group; no group more than 10 points below the other | Before any reuse, and for each new data set |
| Reading frequency: automated readings vs manual monthly readings | Share of known events flagged; flags caused by missing data | At least 90% in each group; data-gap flags under 20% of all flags | Before any reuse |
| Rate of change: sudden changes vs slow trends over 3 months or more | Share of known events flagged | Slow trends flagged at least as often as sudden changes, within 10 points | Before any reuse |
| Season: wet (June to September) vs dry | False flags per 100 instrument-months | Wet-season rate no more than 2 times the dry-season rate | Before any reuse |
| Owner reliance (automation bias) | Every instrument plotted and reviewed by the owner, whether flagged or not | 100% of instruments reviewed by hand | Every use |

## 5. MANAGE
- **Human-in-the-loop:** the owner plots and reviews every instrument by hand, whether or not the tool flags it. A flag is a lead only. The owner confirms any condition against the raw readings and the client's records before saying anything to the client, and writes every observation, conclusion, and recommendation personally (POL-01 9.4; 18 CFR 12.36(g)). The owner can disregard any flag; the tool never overrides a reading past a client trigger point.
- **Data-sharing rules** (before any reuse, all must be true):
  1. The client's written consent names the tool, the data, and the purpose (GRS-B (1); POL-01 6.1).
  2. Vendor terms bar training on client data and use for any other purpose, set a deletion period after the engagement, and give a security report or equivalent; the account has MFA. Terms recorded in the vendor list.
  3. No CEII, no security-sensitive material, and no Client A data of any kind. Exports are checked for CEII before upload (POL-01 8.4).
  4. Only the instruments and dates the study needs; instrument names replaced with codes where possible.
  5. Data deleted from the tool when the study ends, with the vendor's written confirmation kept in the client information register (POL-01 8.9).
- **Monitoring:** for each data set, record the flags, how each was resolved, and any known event the tool missed. Re-run the section 4 plan after any vendor model change.
- **Incident handling:** a vendor breach notice, an upload of the wrong data, or any upload of CEII is an incident under POL-01 10.2. Follow the P08 runbook and notification matrix: Client B within 24 hours (GRS-B (3)); FERC's CEII Coordinator promptly for any CEII (18 CFR 388.113(h)(2)).
- **Decommissioning criteria:** stop and delete if the client withdraws consent, the vendor changes its terms or has a breach, a known event is missed in use, or the study ends.

## 6. Decision
**Reject for current use (AI-001 retired), by the owner-engineer on 2026-08-31.** Do not resume the trial. By 2026-09-30, file the vendor's 2026-08-12 deletion confirmation and send a copy to Client B (P01 R-007; P03 G-031; P07 POAM-008). Any future use of an anomaly detection tool needs a new P10 assessment that passes the section 4 plan and meets every section 5 data-sharing rule first.

## 7. AI-002: built-in AI writing assistant (generative AI, NIST AI 600-1)
- **What it is:** a drafting and summarizing feature in the email and file suite (SYS-01). The suite provider already holds the data under the business plan terms, but the assistant was released after the period of the provider's SOC 2 report (P09 vendor review), so its controls are not yet covered.
- **AI 600-1 risks that matter here:** confabulation (invented numbers or citations in a technical text), information security and data privacy (prompts with client data), human-AI configuration (over-trust in fluent text), and value chain and component integration (the provider's model supplier is not named).
- **Tier: Low** for the approved use below (internal productivity, no decisions about individuals, no regulated data).
- **Rules (approved with conditions, 2026-08-31):** use only for administrative text (invoices, scheduling emails, proposals without client technical data). Never open it on a client folder, CEII, security-sensitive material, or any Client A material. Never use it to draft or summarize observations, findings, conclusions, or recommendations in an inspection or study report (18 CFR 12.36(g)). The owner reads every output before it is sent.
- **Follow-up:** by 2026-10-31, ask the provider whether the next SOC 2 report covers the assistant and confirm in writing that business plan prompts are not used for training (P09 follow-ups). Re-assess if the answer is no.

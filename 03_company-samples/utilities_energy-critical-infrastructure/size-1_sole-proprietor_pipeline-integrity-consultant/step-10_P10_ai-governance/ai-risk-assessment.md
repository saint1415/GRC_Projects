# AI Use Assessment: Third-Party AI Anomaly-Screening Tool (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (pipeline integrity engineering consultant) |
| Tier / Vertical | Sole Proprietorship / Energy |
| AI use case | AI-001: third-party AI anomaly-screening SaaS (SYS-07) used on client leak-detection and ILI data. The registry's "pipeline leak-detection anomaly model" adapted to a consultant: the owner does not run a pipeline's leak-detection system; it tried a vendor tool to screen a client's data. Trial 2026-07-13 to 2026-07-31; stopped 2026-08-10 |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form. NIST released a concept note for an AI RMF Critical Infrastructure Profile on 2026-04-07; it is not a profile yet and is not used here |
| Assessor and decision | Engineer-owner, 2026-08-28; decision 2026-09-11 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What it does (Map)
The owner uploaded about 60 days of pressure and flow historian exports for one Client A pipeline segment, plus one ILI feature list, to a vendor's free-trial web tool. The tool flags time windows that look like leak signatures (pressure and flow imbalances) and ILI features whose depth looks likely to grow. The owner wanted it to speed up the leak-detection program review and dig prioritization. The owner accepted click-through trial terms that let the vendor use uploaded data to improve its models. **Client A never approved the tool** (addendum s.4). No SSI and no personal information were uploaded. No trial output was used in any deliverable.

## 2. Rules that apply
| Rule | Applies? | Why |
|---|---|---|
| Client A addendum s.4 (approved services only, including AI tools) | **Yes, breached** | Client A data went to a service Client A had not approved in writing |
| 49 CFR Part 1520 (SSI) | Yes, as a boundary | No SSI was uploaded. POL-01 8.2 and 9.5 bar SSI from any AI tool |
| TSA SD Pipeline-2021-02G (C-ENERGY-R03) | Not to the consultant | Client A decides whether the tool or its data flow touches its Critical Cyber Systems or its Cybersecurity Implementation Plan. That is one reason Client A must approve any tool first |
| Client duties for integrity and leak detection | Not to the consultant | Pipeline safety duties stay with the operator. The consultant's sealed recommendations feed those duties, which is why output quality matters |
| State AI laws on consequential decisions | No | The tool makes no decision about any individual |

## 3. Risk screen (repository rubric)
**Tier: High.** Under the repository rubric, an AI system that "can affect physical safety or critical infrastructure operations" is High, even with a human in the loop. A missed leak signature or a misranked corrosion feature could delay a pipeline operator's safety decision (P01 R-012, impact Very High). The rubric's minimum controls for High are adapted below: human review before action, testing before use, an impact assessment (this page), notice to the affected party (the client), and ongoing monitoring. The harmful-bias test in the rubric is about people; it does not apply, because no individual is scored.

## 4. Data-sharing rules (Govern)
1. No client data goes into any AI tool without (a) this assessment, (b) the client's written approval naming the tool, and (c) business terms that bar training on the data and set a deletion period (POL-01 6.1 and 9.5).
2. SSI and personal information never go into any AI tool, approved or not.
3. Upload only the minimum: the segment and period the task needs, with asset names replaced by codes where the client agrees.
4. Free-trial and consumer terms are never acceptable for client data.

## 5. Measure: tests before any future use
| Characteristic | Test | Pass mark |
|---|---|---|
| Valid and reliable | Run the tool on client-provided historical data with known events (confirmed leaks, confirmed false alarms, dug ILI features with field measurements) | The tool flags every known leak event in the test set; the owner records its false alarm rate and feature-depth error against field data |
| Safe | Check that the tool never suppresses a feature or window the owner's own method flags | No case where the owner's method flags and the tool's output would have hidden it |
| Secure and resilient | Vendor SOC 2 report or equivalent; MFA; data stays in the United States if the client requires it | Client A approves the evidence |
| Accountable and transparent | The deliverable says where AI screening was used and what the owner checked | Stated in every report that used it |
| Explainable and interpretable | Each flag shows the data window or feature and the reason | No unexplained scores used |

## 6. Human review of outputs (Manage)
The tool is advisory only. The owner runs the normal engineering method on every dataset regardless of what the tool says, treats tool flags as extra items to check, and signs every finding under the owner's professional license. A tool output never removes an item from review. If a tool output contradicts field data, the owner records it, and two such cases in a quarter stop use until the vendor explains them. Any suspected data exposure by the vendor goes to the P08 runbook and the Client A 24-hour notice.

## 7. Decision: stop and do not resume without approval (approved 2026-09-11)
**Do not resume the trial.** By 2026-09-30 (P01 R-006):
1. Send the vendor a written request to delete all uploaded data and any derived model updates, and keep the reply. Close the account after deletion is confirmed.
2. Give Client A the vendor's reply and follow its instructions (Client A was told on 2026-08-14).
3. Consider an anomaly-screening tool **only** after Client A approves it in writing, on business terms with no training on client data, and after the section 5 tests pass. Re-run this assessment first.

**Second inventory item (AI-002):** the productivity suite's built-in AI writing assistant, used to tidy report wording. Tier Low under the rubric: internal productivity, no decisions about individuals, and no regulated data, because SSI and personal information are excluded. It runs inside the suite already approved for client data, and the provider states it does not train on customer content (P09 vendor review). Rules: never with SSI or personal information; the owner rewrites and checks every sentence that states an engineering finding.

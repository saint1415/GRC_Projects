# P10. AI Governance Risk Assessment

**Notion project:** Create an AI Governance / Risk Assessment. An evaluation of a fictional AI tool's risk tier, bias testing needs, and human-in-the-loop requirements.

## Universal approach (macro to granular)

The assessment is organized around the four **NIST AI RMF 1.0** Functions. The Playbook provides the suggested actions (SRC-AI-PLAYBOOK). For generative AI use cases, add **NIST AI 600-1**.

1. **GOVERN (macro).** Accountability, policies, the approved-tools list, and AI inventory ownership. Link to POL-04 and POL-05.
2. **MAP.** Describe the use case from the scenario `_context.md`: its purpose, users, the people affected, the data used, whether the model was built or bought, and deployment context. Identify the applicable US laws and sector rules (see `00_universal-framework/cross-sector/us-cross-sector-obligations.md` and the vertical requirements).
3. **Risk tier.** Assign a tier using the rubric below. The rubric is defined by this repository, not by any regulation. It flags where US laws treat consequential decisions as high risk.
4. **MEASURE (granular).** Test against the AI RMF trustworthy characteristics: valid and reliable; safe; secure and resilient; accountable and transparent; explainable and interpretable; privacy-enhanced; fair with harmful bias managed. Write a bias and fairness testing plan that names the metrics, the groups compared, and the thresholds.
5. **MANAGE.** Human-in-the-loop design (who reviews what, and when a human can override), monitoring, incident handling (P08), and decommissioning.

## Risk tier rubric (repository-defined)

| Tier | Criteria | Minimum controls |
|---|---|---|
| High | The AI makes or is a substantial factor in a consequential decision about a person (employment, credit, housing, insurance, education, health care, essential government services, legal services), OR can affect physical safety or critical infrastructure operations | Human review before action; pre-deployment bias testing; impact assessment; notice to affected people; ongoing monitoring |
| Medium | The AI influences business decisions or interacts directly with customers, but a human makes the final decision affecting individuals | Human oversight; output quality monitoring; disclosure of AI interaction |
| Low | Internal productivity use with no decisions about individuals and no regulated data | Approved-tool use; data handling rules (POL-04) |

The consequential-decision categories mirror state law. Colorado SB26-189 (signed 2026-05-14, effective 2027-01-01) replaced the never-effective SB24-205 and covers education, employment, housing, financial/lending, insurance, health care, and essential government services, with **no small-business exemption** in the signed text. The CPPA ADMT rules in California use similar "significant decision" categories. Confirm which laws apply using the cross-sector file, because these laws change often and federal preemption efforts (EO 14365) are ongoing.

## Outputs

| File | Purpose |
|---|---|
| `ai-risk-assessment.md` | The assessment for the scenario's AI use case. |
| `ai-use-case-inventory.csv` | The inventory row(s): use case, owner, vendor/model, data, risk tier, status. |

## Sources

SRC-AI-RMF, SRC-AI-600-1, SRC-AI-PLAYBOOK, plus the US AI obligations in `00_universal-framework/cross-sector/`.

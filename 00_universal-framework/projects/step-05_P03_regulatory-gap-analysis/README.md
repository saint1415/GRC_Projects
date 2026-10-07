# P03. Regulatory Gap Analysis

**Notion project:** Do a HIPAA Gap Analysis. Compare a fictional company's current safeguards against what a regulation actually requires.

**Universal framing.** The method is the same for every regulation. HIPAA is the Health Care instance. Each vertical names its own **primary regulation** in its overlay (`02_industry-rules/.../overlay.md`), and each scenario's `_context.md` carries it forward.

## Universal approach (macro to granular)

1. **Confirm applicability (macro).** Does the regulation apply at this tier? Check the size thresholds and exemptions in the vertical `requirements.csv`. Record the applicability decision and its citation. If it does not apply, say so and analyze the next most relevant regulation.
2. **Decompose the regulation.** Break it into individually verifiable requirements, citing section and paragraph (for HIPAA, 45 CFR 164.308-164.316 standards and implementation specifications). Keep the regulation's own requirement types, such as HIPAA's Required and Addressable.
3. **Crosswalk.** Map each requirement to CSF 2.0 subcategories and SP 800-53 controls. For HIPAA, use NIST's official mapping (OLIR 110 to SP 800-53 and OLIR 109 to CSF 1.1; SRC-OLIR-HIPAA-53, SRC-OLIR-HIPAA-CSF), which SP 800-66 Rev. 2 points to. For other regulations, use an official crosswalk if one exists. Otherwise make your own mapping and mark it as such.
4. **Assess current state (granular).** For each requirement, record what exists today, the evidence, and a status: Met, Partially met, Not met, or Not applicable.
5. **Rate and plan.** Rate each gap using the risk scale from P01 and write a remediation action with owner and date. Feed high gaps into the risk register (P01).

## Watch items

- **HIPAA Security Rule NPRM** (90 FR 898, 2025-01-06) is still pending as of 2026-09-25 (SRC-HIPAA-NPRM). Analyze against the rule in force (45 CFR Part 164 Subpart C, last amended 2020-11-24). A column shows what would change if the proposal were finalized.

## Outputs

| File | Purpose |
|---|---|
| `gap-analysis.csv` | One row per requirement: citation, type, crosswalk, current state, evidence, status, gap, remediation. |
| `gap-analysis-report.md` | Applicability decision, method, summary of results by section, prioritized roadmap. |

## Quality checklist

- [ ] The applicability decision cites the exact threshold or exemption text.
- [ ] Requirements are at the most granular citation level.
- [ ] Each "Met" status names specific evidence.
- [ ] Every "Not met" or "Partially met" row has a remediation owner and date.

## Sources

The vertical's primary regulation (see its overlay), plus SRC-800-66 (HIPAA crosswalk), SRC-CSF2, and SRC-OLIR-CSF-53.

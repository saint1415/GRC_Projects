# P08. Incident Response Runbook

**Notion project:** Build an Incident Response Runbook. Step-by-step response procedures for a specific incident type, including notification chains.

## Universal approach (macro to granular)

**NIST SP 800-61 Rev. 3** (April 2025) replaced the old four-phase lifecycle with a **CSF 2.0 Community Profile**. The runbook is therefore organized by CSF 2.0 Functions:

1. **Govern / Identify / Protect (preparation, macro).** Roles, authority to act, contacts, tooling, backups, and the policy basis (POL-03).
2. **Detect.** Detection sources and triggers (DE.CM, DE.AE) specific to the incident type.
3. **Respond.**
   - **RS.MA** Incident management: declare, triage, categorize, escalate.
   - **RS.AN** Incident analysis: scope, root cause, evidence preservation.
   - **RS.CO** Reporting and communication: internal, regulatory, law enforcement, customers.
   - **RS.MI** Incident mitigation: contain and eradicate.
4. **Recover.** **RC.RP** plan execution: restore in BIA priority order (P05) and verify integrity. **RC.CO** recovery communication.
5. **Improve (granular).** Lessons learned feed ID.IM, the risk register (P01), and POA&M (P07).

The **notification matrix** is pre-filled for each scenario. The generator collects the vertical's incident-reporting requirements and the cross-sector US obligations, with citations and deadlines. Verify each entry against its source before use. Deadlines and triggers change.

## Outputs

| File | Purpose |
|---|---|
| `ir-runbook.md` | The runbook for the scenario's incident type (see `_context.md`). |
| `notification-matrix.csv` | Who must be notified, by when, under what citation. Pre-filled, then verified by you. |

## Quality checklist

- [ ] Each step names who does it and what "done" looks like.
- [ ] Every regulatory deadline in the matrix cites its source and states when the clock starts.
- [ ] Recovery order matches BIA priorities.
- [ ] Evidence handling preserves chain of custody.

## Sources

SRC-800-61, SRC-CSF2, and the vertical and cross-sector notification requirements.

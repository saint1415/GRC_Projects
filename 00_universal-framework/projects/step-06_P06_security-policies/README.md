# P06. Security Policy Set

**Notion project:** Draft a Set of Security Policies. Three to five real policies (access control, incident response, data classification) aligned to control families.

## Universal approach (macro to granular)

1. **Governance first (macro).** POL-01 establishes the security program, its roles, and the authority behind every other policy (CSF GV.PO, GV.RR; SP 800-53 PM-1, PL-1).
2. **One policy per control family.** Each policy satisfies the "-1" (Policy and Procedures) control of its SP 800-53 family, for example AC-1 or IR-1.
3. **Statements are testable.** Write each policy statement so an assessor can check it (P07). Tag each one with its SP 800-53 control and CSF 2.0 subcategory.
4. **Plain language.** Write for employees, not auditors. Keep procedures (how-to steps) out of policies.
5. **Scale by tier (granular).** Sole Proprietorship merges the five policies into one document. Enterprise and Multi-Sector add standards and procedures beneath each policy. See `01_company-sizes/tier-project-scaling.csv`.
6. **Add vertical requirements.** Each scenario's `_context.md` lists regulatory requirements that need a policy statement, for example HIPAA workforce sanctions or CJIS access rules.

## Policy set

| ID | Policy | Primary SP 800-53 families | Primary CSF 2.0 categories |
|---|---|---|---|
| POL-01 | Information Security Policy | PM, PL | GV.PO, GV.RR, GV.OV |
| POL-02 | Access Control Policy | AC, IA | PR.AA |
| POL-03 | Incident Response Policy | IR | RS.MA, RS.CO, RC.RP |
| POL-04 | Data Classification and Handling Policy | RA-2, MP, SC-8, SC-28, SI-12 | ID.AM, PR.DS |
| POL-05 | Acceptable Use Policy | PL-4, AC-8, AT | PR.AT, GV.PO |

## Outputs

`POL-01` to `POL-05` markdown files and `policy-control-map.csv` (statement to control to CSF traceability).

## Quality checklist

- [ ] Every statement uses "must" or "must not" and can be tested.
- [ ] Every statement maps to at least one SP 800-53 control.
- [ ] Every policy names an owner, an approver, an effective date, and a review cycle.
- [ ] The exceptions process is defined once, in POL-01.

## Sources

SRC-SANS-POL (template library for further structure), SRC-800-53 ("-1" controls), SRC-CSF2.

# P07. Security Control Assessment

**Notion project:** Perform a Mock Security Control Assessment. Assess a handful of controls using the examine, interview, and test methods that auditors use.

## Universal approach (macro to granular)

1. **Plan (macro).** Define scope (system from P02, number of controls from the tier scaling matrix), assessor independence, schedule, and rules of engagement. Pick the controls with the highest risk, using P01 and the vertical's regulatory drivers.
2. **Select procedures.** For each control, take the assessment objectives (determination statements) and the potential assessment methods and objects from **SP 800-53A Rev. 5 (Release 5.2.0)**. For CUI scenarios, use **SP 800-171A Rev. 3**.
3. **Set depth and coverage.** Depth and coverage are each basic, focused, or comprehensive. Raise them as the tier grows.
4. **Gather evidence (granular).**
   - **Examine:** specifications, mechanisms, activities (policies, configurations, logs).
   - **Interview:** the individuals responsible.
   - **Test:** mechanisms and activities under specified conditions.
5. **Determine findings.** Rate each determination statement as *Satisfied* or *Other than satisfied* (SP 800-53A terms), with the evidence reference.
6. **Report and track.** Write results, then put every "Other than satisfied" item in a POA&M (plan of action and milestones) and feed it back into P01.

## Outputs

| File | Purpose |
|---|---|
| `assessment-plan.md` | Scope, controls, methods, schedule, and roles. |
| `assessment-results.csv` | One row per determination statement, with method, object, evidence, and finding. |
| `poam.csv` | Weaknesses, milestones, and owners. |

## Quality checklist

- [ ] Every finding cites the objective ID from 800-53A (for example, AC-02a.[01]) and at least one evidence item.
- [ ] Each control has at least two methods where feasible.
- [ ] "Other than satisfied" findings state the condition, the criteria, and the risk.

## Sources

SRC-800-53A, SRC-800-171A (CUI), SRC-800-37 (assessment within the RMF).

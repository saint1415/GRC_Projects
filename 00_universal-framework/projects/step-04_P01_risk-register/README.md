# P01. Risk Register

**Notion project:** Build a Risk Register. Threats, vulnerabilities, likelihood/impact scoring, and treatment plans.

## Universal approach (macro to granular)

1. **Frame the risk (macro).** State scope, risk tolerance, and who accepts risk. Scope comes from the tier profile. (SP 800-30 Rev. 1, Task 1; SP 800-39 risk framing.)
2. **Identify assets and systems.** List the business processes and systems in scope. Reuse the BIA (P05) if it exists.
3. **Identify threat sources and threat events.** Use SP 800-30 Appendix D (sources) and Appendix E (events). Add the vertical's incident scenario and sector threats from the vertical overlay.
4. **Identify vulnerabilities and predisposing conditions.** Use gap findings (P03) and assessment findings (P07) when available.
5. **Score likelihood.** Rate the likelihood of initiation or occurrence (Tables G-2 and G-3) and the likelihood of adverse impact (Table G-4), then combine them with Table G-5.
6. **Score impact.** Use Table H-3.
7. **Determine risk.** Combine likelihood and impact with Table I-2 (below).
8. **Decide treatment (granular).** Accept, avoid, mitigate, share or transfer. Name the owner, planned controls (SP 800-53 IDs), due date, and target residual risk.
9. **Roll up.** Map each risk to a CSF 2.0 category. From Mid-Market up, roll up to enterprise risk per NIST IR 8286 Rev. 1.

## Scoring scales (NIST SP 800-30 Rev. 1, verified from the PDF)

Qualitative to semi-quantitative (Tables G-2, G-3, G-4, H-3, I-3): Very High = 96-100 (10), High = 80-95 (8), Moderate = 21-79 (5), Low = 5-20 (2), Very Low = 0-4 (0).

**Overall likelihood (Table G-5).** Rows: likelihood of initiation or occurrence. Columns: likelihood that it results in adverse impact.

| Initiation \ Adverse impact | Very Low | Low | Moderate | High | Very High |
|---|---|---|---|---|---|
| Very High | Low | Moderate | High | Very High | Very High |
| High | Low | Moderate | Moderate | High | Very High |
| Moderate | Low | Low | Moderate | Moderate | High |
| Low | Very Low | Low | Low | Moderate | Moderate |
| Very Low | Very Low | Very Low | Low | Low | Low |

**Level of risk (Table I-2).** Rows: overall likelihood. Columns: level of impact.

| Likelihood \ Impact | Very Low | Low | Moderate | High | Very High |
|---|---|---|---|---|---|
| Very High | Very Low | Low | Moderate | High | Very High |
| High | Very Low | Low | Moderate | High | Very High |
| Moderate | Very Low | Low | Moderate | Moderate | High |
| Low | Very Low | Low | Low | Low | Moderate |
| Very Low | Very Low | Very Low | Very Low | Low | Low |

## Outputs

| File | Purpose |
|---|---|
| `risk-register.csv` | One row per risk. The columns follow the SP 800-30 Table I-5/I-7 templates, plus treatment and traceability columns. |
| `risk-register-report.md` | Scope, method, top risks, treatment summary, and sign-off. |

## Quality checklist

- [ ] Every risk names a threat event, a threat source, and a vulnerability or predisposing condition.
- [ ] Likelihood and impact use the scales above. No private scales.
- [ ] Every risk rated High or Very High has an owner, a treatment, and a due date.
- [ ] Every risk maps to a CSF 2.0 category and to at least one SP 800-53 control.
- [ ] Regulatory drivers cite the vertical requirement IDs.

## Sources

SRC-800-30, SRC-800-39, SRC-IR-8286, SRC-CSF2 (see `00_universal-framework/sources/source-register.csv`). An official NIST risk register template (xlsx) is listed under SRC-IR-8286.

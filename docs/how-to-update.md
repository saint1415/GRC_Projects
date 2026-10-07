# How to update the library

The library is layered so that a change is made **once** and reaches every scenario.

## Which file to edit

| What changed | Edit | Then run |
|---|---|---|
| NIST publishes new CSF informative references or 800-53 mappings | Nothing | `python3 tools/refresh_csf_crosswalks.py` |
| NIST releases a new SP 800-53 / 800-53A release | Nothing | `python3 tools/refresh_sp800_53.py` |
| SBA changes size standards | Nothing | `python3 tools/refresh_sba_standards.py` |
| Any framework version or date | `00_universal-framework/sources/source-register.csv` | `build_scenarios.py` |
| A cross-sector US law (breach, privacy, SEC, CIRCIA, AI) | `00_universal-framework/cross-sector/us-cross-sector-obligations.md` and, for reporting duties, `notification-baseline.csv` | `build_scenarios.py` |
| A project method or template | `00_universal-framework/projects/Pxx_*/` | `build_scenarios.py` (see note below) |
| How deep a project goes at a size | `01_company-sizes/tier-project-scaling.csv` | `build_scenarios.py` |
| A sector regulation | `02_industry-rules/<sector>/requirements.csv`, `incident-notification.csv`, or `profile.csv` | `build_scenarios.py` |
| The industry used for a vertical or tier | `02_industry-rules/verticals.csv` or `scenario-industry-overrides.csv` | `refresh_sba_standards.py`, then `build_scenarios.py` |

Always finish with `python3 tools/validate.py`.

## What the rebuild changes

- **Always regenerated:** `02_industry-rules/**/overlay.md`, every scenario `README.md`, every `_context.md`, and `03_company-samples/INDEX.md`.
- **Never overwritten:** the working files in each project folder (for example `risk-register.csv`). Your completed work is safe.
- **Template changes and existing work:** a new template reaches scenarios that have not started that project. To push a new template into a scenario you have not started, delete its working files and rebuild. `--force-templates` overwrites **all** working files; use it only on a fresh library.

## Verification discipline

1. Every source has `last_verified` in the source register. Every vertical requirement has a `verified` flag.
2. When you confirm a fact against the primary source, set `verified=true` and update the date.
3. Anything proposed but not final (for example, the HIPAA Security Rule NPRM or CIRCIA) may appear in `requirements.csv` only with a `status` that says it is proposed. Track it in the watch list in `PLAN.md` and the `pending_rule_change` column of P03, and never treat it as a current obligation.

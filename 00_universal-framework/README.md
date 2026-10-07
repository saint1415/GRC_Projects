# 00_universal-framework: the isolated universal framework

This layer holds everything that is true **regardless of company size or industry**. When a framework or cross-sector law changes, update it here and rebuild. Every scenario picks up the change.

| Folder | Contents | Update when |
|---|---|---|
| [`sources/`](sources/source-register.csv) | Source register: every authoritative document, its version, URL, and last-verified date | Any source changes. Update `last_verified` on every review |
| [`frameworks/`](frameworks/) | NIST CSF 2.0 core (6 Functions, 22 Categories, 106 Subcategories) | NIST releases a new CSF version |
| [`crosswalks/`](crosswalks/) | Official NIST mappings: CSF 2.0 to SP 800-53 Rev. 5 (Release 5.2.0), and CSF 2.0 to SP 800-171 Rev. 3 | NIST updates informative references (`tools/refresh_csf_crosswalks.py`) |
| [`cross-sector/`](cross-sector/) | US obligations that apply across industries: state breach and privacy laws, SEC, CIRCIA, FTC, and AI laws | Laws or rules change |
| [`projects/`](projects/) | The 10 project methods (README) and templates | The method or template improves |

## Anchor frameworks

- **Macro (governance): NIST CSF 2.0.** Every deliverable ties back to CSF Functions and Categories.
- **Granular (controls): NIST SP 800-53 Rev. 5, Release 5.2.0.** Controls come from here, and baselines from SP 800-53B.
- Vertical regulations connect to both through the crosswalks and the `regulatory_driver` columns in each template.

## The 10 projects

| ID | Project | Primary method |
|---|---|---|
| [P01](projects/step-04_P01_risk-register/README.md) | Risk Register | NIST SP 800-30 Rev. 1; IR 8286 Rev. 1 |
| [P02](projects/step-02_P02_system-security-plan/README.md) | System Security Plan | NIST SP 800-18 Rev. 2 (June 2026); FIPS 199; SP 800-53B |
| [P03](projects/step-05_P03_regulatory-gap-analysis/README.md) | Regulatory Gap Analysis (HIPAA in Health Care) | Regulation text; SP 800-66 Rev. 2 crosswalk |
| [P04](projects/step-03_P04_cloud-control-mapping/README.md) | Control-to-Cloud Architecture Mapping | SP 800-53 Rev. 5; provider shared responsibility models |
| [P05](projects/step-01_P05_business-impact-analysis/README.md) | Business Impact Analysis | NIST SP 800-34 Rev. 1 BIA template |
| [P06](projects/step-06_P06_security-policies/README.md) | Security Policy Set | SP 800-53 "-1" controls; SANS templates |
| [P07](projects/step-07_P07_control-assessment/README.md) | Security Control Assessment | NIST SP 800-53A Rev. 5 (Release 5.2.0) |
| [P08](projects/step-08_P08_incident-response-runbook/README.md) | Incident Response Runbook | NIST SP 800-61 Rev. 3 (CSF 2.0 profile) |
| [P09](projects/step-09_P09_soc2-readiness/README.md) | SOC 2 Readiness Checklist | AICPA 2017 TSC (2022 points of focus) |
| [P10](projects/step-10_P10_ai-governance/README.md) | AI Governance Risk Assessment | NIST AI RMF 1.0; AI 600-1 |

## Template conventions

- `{{field}}` placeholders are filled by the generator: company, tier, vertical, business, system, incident, AI use case, and primary regulation.
- `[FILL: ...]` markers are yours to complete in each scenario's working files.
- `[A|B|C]` means choose one value.

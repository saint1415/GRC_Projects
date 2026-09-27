# Security Assessment Plan and Summary: Cris Santos Company | Public Administration | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (GovTech systems integrator) |
| System assessed | Agency Case Management Platform (ACMP), per the SSP (P02) |
| Tier / Vertical | Small / Public Administration |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Organization-defined values used | CJISSECPOL v6.1 and Pub. 1075 (Rev. 11-2021) values where they are stricter than the company's own (for example, AU-11 retention and AC-7 thresholds) |
| Assessor(s) and independence | Contracted independent assessor with no role in designing or operating the controls. Escorted by the IT Manager. Read-only access; tests of destructive permissions were run in a sandbox copy of the production account |
| Assessment window | 2026-08-03 to 2026-08-07 (headquarters walkthrough 2026-08-05) |
| Also satisfies | SP 800-53 CA-2 (contract requirement); evidence for agency reviews under the CJIS Security Addendum and Pub. 1075 Exhibit 7 III |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **20 controls, 132 determination statements.** Controls were chosen because they support the Very High and High risks in P01, carry CJIS or Pub. 1075 overlay values that the agencies audit, or showed High gaps in P03.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-6, IA-2, IA-5 | Privileged and support access to all tenants; R-001, R-011, R-017 | Focused | Focused |
| PS-3, PS-6, AT-2 | Unscreened staff with CJI and FTI access; CJIS PS-3 and AT-2; Pub. 1075 Exhibit 7; R-003, R-004 | Focused | Comprehensive (all 13 CJI and 11 FTI staff) |
| AU-6, AU-9, AU-11, SI-4 | No monitoring; short, deletable logs; CJIS and Pub. 1075 AU-11; R-001, R-009 | Focused | Focused |
| CP-4, CP-9 | Backups inside the blast radius; unproven 8-hour RTO; R-001, R-007 | Focused | Focused |
| IR-6, IR-8 | Agency reporting clocks (1 hour CJI; 24 hours FTI through the agency); R-021 | Focused | Basic |
| RA-5, CM-3 | Unscanned workloads; console changes; R-016, R-025 | Basic | Focused |
| SA-9 | FTI and CJI in the ticketing service; model service; R-005, R-020 | Focused | Focused (40 tickets sampled) |
| SC-8, SC-13 | FIPS 140-3 date for CJI in transit (2026-09-21); R-010 | Focused | Focused |

## 2. Methods and objects
- **Examine:** identity provider and cloud IAM exports, HR screening files, Security Addendum certifications (copies from AC-02), FTI training certificates and penalty notices, log and backup settings, pull request records, the 2024 incident response plan, the P08 runbook, vendor terms, and 40 support tickets.
- **Interview:** Chief Operating Officer, IT Manager, Cloud Operations Lead, Director of Engineering, Customer Support Manager, HR Manager, Contracts and Compliance Manager, and 8 randomly selected staff (incident reporting awareness).
- **Test:**
  - sign-in tests for a standard user and an administrator with a hardware key
  - the support role's reach into the AC-01 tenant (read-only query of record counts, no record content)
  - log and snapshot deletion permissions for an administrator role, in a sandbox copy
  - a simulated suspicious sign-in to time alert handling
  - a TLS and module configuration scan of the ingress and integration gateway
  - an authenticated vulnerability scan of 3 running containers
  - a review of pipeline variables for secrets

## 3. Rules of engagement
- No test could change production data or interrupt agency service. Destructive-permission tests ran only in a sandbox copy.
- The assessor viewed no FTI or CJI content. Record counts were used instead of records, and ticket samples were screened by the Contracts and Compliance Manager, who redacted regulated content before the assessor saw them.
- The assessor would stop and notify the IT Manager on finding any critical exposure. This happened once (see the new finding below).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 52 |
| Other than satisfied | 80 |

**Fully other than satisfied:** AC-6, AU-6, AU-9, AU-11, CP-4, PS-3, SC-8, SC-13. No process or technical control met any of their statements.
**Fully satisfied:** IA-2 (unique accounts with MFA for every workforce user; hardware keys for administrators).
**Partly satisfied:** CP-9 (backups are made and encrypted, but their integrity and availability are not protected and documentation is not backed up) and IR-6 (agency contacts are current and named in contracts, but staff have no 1-hour reporting rule).

**New finding:** the API key for the AC-02 message-switch interface was stored in plain text in a pipeline variable visible to all 20 engineers (IA-05g.). The assessor stopped and told the IT Manager on 2026-08-05. The key was rotated on 2026-08-10. The finding was added to the risk register as R-011 and to POAM-011.

**Screening finding handled immediately:** on 2026-08-31 the CEO directed that the 4 staff without fingerprint-based checks and the 2 without Pub. 1075 investigations lose access to AC-02 and AC-01 data until screening is complete (POAM-001, access removal scheduled for 2026-09-04).

All 19 controls with weaknesses have POA&M items in `poam.csv` (POAM-001 to POAM-019). POAM-020 comes from the gap analysis (P03, the 2025 staging copy of FTI) because it is too serious to wait for the next assessment. Of the 20 items, 18 are High and 2 are Moderate.

## 5. Deliverables
`assessment-results.csv` (132 rows), `poam.csv` (20 items), and this plan and summary. The results were accepted by the Chief Operating Officer on 2026-08-31.

# Security Assessment Plan and Summary: Cris Santos Company | Information | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed B2B SaaS publisher of a multi-tenant customer service platform) |
| System assessed | Customer Engagement Platform (CEP, SYS-01 to SYS-08), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Information |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, 1 cloud specialist), reporting to the board audit committee. The firm does not design or operate any assessed control and is not the SOC 2 service auditor. The GRC Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-17 to 2026-09-04 (technical tests 2026-08-24 to 2026-08-28) |
| Also satisfies | HIPAA evaluation for the healthcare cell, 45 CFR 164.308(a)(8); annual internal IT audit; input to SOC 2 readiness (P09) |
| Results accepted | Chief Technology Officer, 2026-09-29; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **36 controls, 224 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover the FTC guidance practices and HIPAA Security Rule rows with High or Moderate gaps in the gap analysis (P03);
- support the SOC 2 readiness gates and the 4 Type 2 exceptions (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Access lifecycle; Type 2 exceptions 1 and 3; 164.308(a)(3)(ii)(C); R-027, R-050 | Focused | Focused (samples of 25) |
| AC-3 | Tenant isolation; G-013; R-003 | Comprehensive | Focused (12 data access paths) |
| AC-6, AC-6(5), AC-6(9) | Privileged and support access; G-004, G-005, G-034; R-008, R-024, R-025 | Comprehensive | Comprehensive (all 10 core accounts) |
| IA-2(1), IA-5, IA-5(7) | Credentials; G-007; R-001 (Very High) | Comprehensive | Comprehensive (all 9 long-lived keys); 25 privileged sign-ins |
| AU-2, AU-6, AU-11, AU-12, SI-4 | Data-level visibility; G-014; 164.312(b); R-002 | Comprehensive | Comprehensive, with a simulated bulk download |
| CA-8, RA-5, SI-2 | Testing and patching; G-020, G-023; R-013, R-014 | Focused | Focused (all 38 critical findings) |
| CM-3, CM-6, CM-8 | Change and configuration; Type 2 exception 2; R-016, R-040 | Focused | Focused |
| CP-2, CP-4, CP-9, CP-10 | Recovery; Type 2 exception 4; 164.308(a)(7); R-006, R-007 | Comprehensive | Comprehensive, with an observed restore |
| IR-4, IR-6, IR-8 | Notice readiness; G-030, G-043, G-044; R-010 | Focused | Basic |
| PT-2, SC-7 | Data use and the healthcare boundary; G-003, G-039; R-004, R-019 | Focused | Focused |
| RA-3 | Risk assessment currency; 164.308(a)(1)(ii)(A) | Basic | Basic |
| SA-3(2), SA-9, SA-11, SR-6 | Development data, sub-processors, testing; G-021, G-022; R-005, R-020, R-021 | Focused | Focused (14 of 14 sub-processors) |
| SC-28 | Encryption claim; G-032 | Focused | Comprehensive (9 data stores) |
| SI-12 | Retention and deletion; G-002, G-038; R-011 | Focused | Focused (20 of 61 tenants) |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items. Where the population was small or the risk High, the whole population was tested. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers | 58 | 25 | AC-2 |
| New workforce accounts | 141 | 25 | AC-2 |
| Privileged accounts (production, cloud admin, identity provider admin) | 210 | 25 for MFA test; all 10 core accounts for role review | IA-2(1), AC-6 |
| Long-lived cloud access keys | 9 | 9 | IA-5, IA-5(7) |
| Data access paths in the application | about 140 | 12 (code review) | AC-3 |
| Support view sessions (90 days) | about 4,100 | 30 | AC-6(9), AU-6 |
| Standard changes (2026-01 to 2026-06) | about 7,800 | 25 | CM-3 |
| Emergency changes (2026-01 to 2026-06) | 61 | 25 | CM-3 |
| Critical image findings (2026-02 to 2026-07) | 38 | 38 | RA-5, SI-2 |
| Backup job days (August 2026) | 31 | 31 | CP-9 |
| Incidents (2025-2026) | 44 | 10 | IR-4 |
| Sub-processors | 14 | 14 | SA-9, SR-6 |
| Data stores holding customer data | 9 | 9 | SC-28 |
| Laptops | 640 | 30 | SC-28 |
| Terminated tenants (12 months) | 61 | 20 | SI-12 |
| Error events sent to error tracking | about 1.2 million a month | 200 | SI-12 |
| Warehouse saved queries | 120 | 10 | PT-2 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6 |

## 3. Methods and objects
- **Examine:**
  - the 2023 policies and the 2026 drafts; the SSP draft
  - identity provider, cloud role, source hosting, and warehouse exports
  - the key inventory and CI variable listings
  - logging, SIEM, and MDR scope configuration
  - change, patch, scan, and backup reports
  - the draft DR plan and the February 2026 DR test report
  - DPAs, BAAs, subcontractor contracts, and SOC 2 reports of sub-processors
  - the incident log and the 2025 tabletop report
- **Interview:**
  - CTO, Director of Security, GRC Manager, detection engineer
  - VP Platform Engineering, VP Engineering, Director of IT
  - VP Customer Support, VP Product, Director of Machine Learning
  - Associate General Counsel, Privacy, and VP People
  - the MDR provider's service lead
  - 15 randomly selected staff
- **Test:**
  - security-key sign-in tests on 25 privileged accounts
  - code review of 12 data access paths for tenant checks
  - a **simulated bulk download** of 2,000 synthetic attachments from a test tenant using a test key from an unusual address (2026-08-26), to see whether anything alerted
  - an attempt to share a production snapshot to a staging account (blocked by guardrail)
  - an observed restore of one database shard into a test account (52 minutes)
  - benchmark configuration scans of 10 cloud resources
  - secret scanning of the contractor's repositories

## 4. Rules of engagement
- No testing that could affect customers. The simulated download used a synthetic test tenant and a purpose-made key that was deleted afterwards. No customer content was viewed.
- Evidence was stored in the firm's encrypted workpaper system under its confidentiality agreement and a BAA for any healthcare cell metadata.
- Stop-and-notify rule: any critical exposure is reported to the Director of Security and the CTO the same day. **Used twice:**
  - 2026-08-26: the simulated bulk download produced **no alert**. The company opened detection work under POAM-004.
  - 2026-08-28: a long-lived cloud key was found **in plain text** in a contractor job configuration. It was rotated the same day and moved to the secrets manager; its deletion is tracked under POAM-002. The 2 former contractor accounts outside single sign-on, found on 2026-08-26, were removed on 2026-09-02 and logged as P01 R-050.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 149 |
| Other than satisfied | 75 |
| **Total** | **224** |

Other than satisfied statements by risk: 4 Very High, 37 High, 30 Moderate, 4 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 21 | 5 | Moderate | POAM-001 |
| AC-3 | 0 | 1 | High | POAM-003 |
| AC-6 | 0 | 1 | High | POAM-007 |
| AC-6(5) | 0 | 1 | Moderate | POAM-005 |
| AC-6(9) | 0 | 1 | Moderate | POAM-008 |
| AU-2 | 2 | 4 | High | POAM-004 |
| AU-6 | 1 | 2 | High | POAM-004 |
| AU-11 | 0 | 1 | Low | POAM-004 |
| AU-12 | 2 | 1 | High | POAM-004 |
| CA-8 | 1 | 0 | n/a | n/a |
| CM-3 | 7 | 3 | Moderate | POAM-009 |
| CM-6 | 4 | 2 | Low | POAM-012 |
| CM-8 | 4 | 2 | Moderate | POAM-012 |
| CP-2 | 12 | 12 | High | POAM-010 |
| CP-4 | 3 | 2 | High | POAM-010 |
| CP-9 | 5 | 1 | High | POAM-011 |
| CP-10 | 0 | 2 | High | POAM-010 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 7 | 3 | Very High | POAM-002 |
| IA-5(7) | 0 | 1 | Very High | POAM-002 |
| IR-4 | 10 | 3 | Moderate | POAM-014 |
| IR-6 | 1 | 1 | Moderate | POAM-014 |
| IR-8 | 13 | 4 | Moderate | POAM-014 |
| PS-4 | 3 | 2 | Moderate | POAM-001 |
| PT-2 | 1 | 1 | High | POAM-015 |
| RA-3 | 7 | 1 | Low | POAM-018 |
| RA-5 | 8 | 1 | High | POAM-013 |
| SA-3(2) | 4 | 0 | n/a | n/a |
| SA-9 | 3 | 3 | High | POAM-006 |
| SA-11 | 5 | 4 | Moderate | POAM-016 |
| SC-7 | 5 | 1 | Moderate | POAM-015 |
| SC-28 | 1 | 0 | n/a | n/a |
| SI-2 | 8 | 2 | High | POAM-013 |
| SI-4 | 8 | 4 | High | POAM-004 |
| SI-12 | 2 | 2 | Moderate | POAM-017 |
| SR-6 | 0 | 1 | Moderate | POAM-006 |

**Fully satisfied (4 controls):** CA-8 (annual independent penetration test), IA-2(1) (security keys on all 25 sampled privileged sign-ins), SA-3(2) (no live data in pre-production; the guardrail blocked the snapshot share test), and SC-28 (all 9 data stores and 30 sampled laptops encrypted). These confirm the strengths in the scenario facts and support the trust center's encryption statement (P03 G-032).

**Fully other than satisfied (8 controls):** AC-3, AC-6, AC-6(5), AC-6(9), AU-11, CP-10, IA-5(7), and SR-6.

**Themes:**
1. The company **authenticates people well but not machines** (IA-2(1) satisfied; IA-5 and IA-5(7) Very High).
2. It **cannot see or prove data access** (AU-2, AU-6, AU-12, SI-4, AC-6(9)). The simulated bulk download went unnoticed.
3. It has **not proven regional recovery** (CP-2, CP-4, CP-10), and its backups share a blast radius with production (CP-9).
4. **Data use and sub-processor terms** do not yet match its promises (PT-2, SA-9, SC-7).

**POA&M:** 32 controls had at least one Other than satisfied statement. They map to 18 POA&M items (POAM-001 to POAM-018), because related controls share an item. Three more items come from the gap analysis and the AI assessment (POAM-019 public statements, POAM-020 business associate breach procedures, POAM-021 AI governance conditions). The total is 21 items: 1 Very High, 10 High, 9 Moderate, and 1 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-08-10 | Plan and sample requests issued |
| 2026-08-17 to 2026-08-21 | Document examination and interviews |
| 2026-08-24 to 2026-08-28 | Technical tests, including the simulated bulk download |
| 2026-08-31 to 2026-09-04 | Analysis, draft findings, management responses |
| 2026-09-29 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (224 rows); `poam.csv` (21 items).

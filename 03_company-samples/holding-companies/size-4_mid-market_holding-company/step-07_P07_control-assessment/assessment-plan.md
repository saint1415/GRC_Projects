# Security Assessment Plan and Summary: Cris Santos Company | Management of Companies and Enterprises | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed holding company with four operating subsidiaries) |
| System assessed | Shared Corporate Services Platform (SCSP, SYS-01 to SYS-11 and SYS-16), per the SSP (P02), with its interfaces to the plant (SYS-15) and Home Services North |
| Tier / Vertical | Mid-Market / Management of Companies and Enterprises |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead and 2 IT auditors), reporting to the audit committee. The firm does not design or operate any assessed control and did not prepare the SSP. The Security Manager coordinated access but did not select samples or rate findings. The vCISO, who approves standards, was interviewed but did not review drafts of the findings |
| Assessment window | 2026-08-17 to 2026-09-04 (site walkthroughs 2026-08-24 to 2026-08-27) |
| Also satisfies | Finance's regular testing of key controls (16 CFR 314.4(d)(1)); the plan's evaluation (45 CFR 164.308(a)(8)); the sponsor's annual independent assessment requirement; the annual internal IT audit |
| Results accepted | CFO, 2026-09-22; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **36 controls, 254 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover the Safeguards Rule elements and HIPAA Security Rule specifications with gaps in the gap analysis (P03);
- support inherited-control reliance and SOC 2 readiness for the bank partner (P09).

| Control | Why selected (risk ID or requirement) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Access lifecycle; 314.4(c)(1)(i); 164.308(a)(3)(ii)(C); R-008 | Focused | Focused (samples of 25) |
| AC-6, AC-6(5) | Privileged access; R-004 (High) | Comprehensive | Comprehensive (all privileged groups and roles) |
| IA-2, IA-2(1), IA-5 | Unique IDs, MFA, secrets; 314.4(c)(5); R-003, R-004 (High) | Focused | Focused (25 of 41 privileged accounts; all 61 service accounts) |
| AC-17, MA-4 | Remote and vendor access; R-007, R-015 | Focused | Comprehensive (every remote access path found) |
| AT-2 | Training; 314.4(e)(1); 164.308(a)(5) | Basic | Focused |
| AU-2, AU-6, AU-11 | Logging and review; 314.4(c)(8); 164.308(a)(1)(ii)(D); R-018 | Focused | Focused |
| CA-7, RA-5, SI-2 | Monitoring and vulnerability management; 314.4(d)(2); R-013 | Focused | Focused |
| CM-2, CM-3, CM-6, CM-8 | Configuration, change, inventory; 314.4(c)(2), (c)(7); R-034 | Focused | Focused |
| CP-2, CP-4, CP-9, CP-10 | Contingency and recovery; 164.308(a)(7); R-001 (Very High), R-016, R-041 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident capability; 314.4(h); R-028 | Focused | Basic |
| MP-6, SC-28 | Disposal and encryption at rest; 314.4(c)(3), (c)(6); 164.310(d) | Basic | Focused |
| PM-9, RA-3 | Group risk strategy and assessment; 314.4(b); R-052 | Focused | Basic |
| SA-9, SR-6 | Vendor oversight; 314.4(f); 164.308(b); R-020 | Focused | Focused (22 critical vendors) |
| SC-7 | Segmentation; R-015, R-017 | Focused | Focused (cloud hub, 9 sites, plant test) |
| SI-3, SI-4 | Malware protection and monitoring; R-002, R-011 | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for a control that operates many times a year with moderate risk, 5 to 10 items for weekly or monthly controls, and the whole population when it is small. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 142 | 25 | AC-2, PS-4 |
| Transfers between subsidiaries or roles | 58 | 25 | AC-2 |
| New accounts | 166 | 25 | AC-2 |
| Privileged accounts (identity provider, cloud, directory) | 41 | 25 for MFA test; all 41 for rights review | IA-2(1), AC-6 |
| Service accounts | 61 | 61 | IA-5, AC-6(5) |
| Changes to Tier 1 systems (2026-01 to 2026-06) | 214 | 25 | CM-3 |
| Servers for configuration scan | 46 | 10 | CM-6 |
| Endpoints | 430 managed laptops and desktops | 5 (EDR test file) | SI-3 |
| Backup job days (July 2026) | 31 per backup set | 31 | CP-9 |
| Retired devices (2026 H1) | 64 | 10 | MP-6 |
| Critical vulnerability findings (2026 H1) | 50 | 50 | RA-5, SI-2 |
| Critical vendors | 22 | 22 | SA-9, SR-6 |
| Security incidents (12 months to 2026-06-30) | 41 | 10 | IR-4 |
| Staff for reporting-awareness interviews | 600 | 15 (6 sites) | IR-6, AT-2 |
| Sites for walkthroughs | 9 | 6 (HQ, distribution center, Branch 2, Central shop, North shop, plant) | SC-7, MA-4, CM-8 |

## 3. Methods and objects
- **Examine:**
  - the 2024 policies and the 2026 drafts; the SSP draft; the 2024 incident plan and the P08 drafts; the cloud recovery plan
  - directory, identity provider, cloud, and SaaS exports
  - backup, patch, scan, and EDR reports
  - vendor register, contracts, and SOC 2 review files
  - the incident log; destruction certificates; training records
- **Interview:**
  - CFO, vCISO, Security Manager, both analysts, and the GRC analyst
  - VP of Information Technology and 2 infrastructure engineers
  - VP of Human Resources and the Benefits Manager
  - the 4 subsidiary Presidents and the Fabrication Plant Manager
  - the MSSP service lead and 2 machine vendors
  - 15 randomly selected staff at 6 sites
- **Test:**
  - MFA sign-in tests on 25 privileged accounts
  - a reachability test from a plant office laptop to the plant floor
  - EICAR test files on 5 endpoints
  - a simulated impossible-travel sign-in to test MSSP escalation
  - a restore of one HQ file share folder from the NAS
  - benchmark configuration scans of 10 servers
  - log retrieval of 11-month-old records from the SIEM and the archive

## 4. Rules of engagement
- No testing that could disrupt subsidiary operations. Plant tests ran during a planned maintenance window with the Plant Manager present; no packets were sent to machine controllers beyond a reachability check.
- No Finance customer information or plan PHI left company systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system under a confidentiality agreement and, for plan data, a BAA.
- Stop-and-notify rule: any critical exposure is reported to the Security Manager and the CFO the same day. **Used once:** on 2026-08-26 the assessors reported that the ACH signing service account password was written in an IT runbook readable by 14 IT staff. The company logged it as P01 R-050 the same day and removed the runbook entry by 2026-09-04; rotation and vaulting are tracked in POAM-004.
- The assessors noted the Branch 2 shared counter accounts on 2026-08-25; the company logged them as P01 R-047.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 138 |
| Other than satisfied | 116 |
| **Total** | **254** |

Other than satisfied statements by risk: 23 High, 61 Moderate, 32 Low.

| Control | Satisfied | Other than satisfied | Highest risk | POA&M |
|---|---|---|---|---|
| AC-2 | 19 | 7 | Moderate | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-6(5) | 0 | 1 | High | POAM-002 |
| AC-17 | 3 | 1 | High | POAM-012 |
| AT-2 | 5 | 5 | Moderate | POAM-005 |
| AU-2 | 2 | 4 | Moderate | POAM-006 |
| AU-6 | 2 | 1 | Moderate | POAM-006 |
| AU-11 | 1 | 0 | n/a | n/a |
| CA-7 | 5 | 6 | Moderate | POAM-007 |
| CM-2 | 2 | 3 | Moderate | POAM-008 |
| CM-3 | 5 | 5 | Moderate | POAM-008 |
| CM-6 | 2 | 4 | Moderate | POAM-008 |
| CM-8 | 3 | 3 | Moderate | POAM-009 |
| CP-2 | 7 | 17 | High | POAM-010 |
| CP-4 | 3 | 2 | High | POAM-010 |
| CP-9 | 4 | 2 | High | POAM-010 |
| CP-10 | 0 | 2 | High | POAM-010 |
| IA-2 | 1 | 1 | Low | POAM-003 |
| IA-2(1) | 0 | 1 | High | POAM-003 |
| IA-5 | 7 | 3 | High | POAM-004 |
| IR-4 | 6 | 7 | Moderate | POAM-011 |
| IR-6 | 1 | 1 | Low | POAM-011 |
| IR-8 | 9 | 8 | Moderate | POAM-011 |
| MA-4 | 0 | 8 | High | POAM-012 |
| MP-6 | 3 | 1 | Moderate | POAM-016 |
| PM-9 | 2 | 2 | Moderate | POAM-017 |
| PS-4 | 3 | 2 | Moderate | POAM-001 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 6 | 3 | Moderate | POAM-007 |
| SA-9 | 2 | 4 | Moderate | POAM-013 |
| SC-7 | 4 | 2 | High | POAM-014 |
| SC-28 | 0 | 1 | Moderate | POAM-016 |
| SI-2 | 7 | 3 | Moderate | POAM-007 |
| SI-3 | 7 | 1 | Moderate | POAM-015 |
| SI-4 | 9 | 3 | Moderate | POAM-015 |
| SR-6 | 0 | 1 | Moderate | POAM-013 |

**Fully satisfied (2 controls):** AU-11 (logs retrievable for 1 year in the SIEM and 3 years in the archive) and RA-3 (the 2026 risk assessment). Strong partial results also confirm the strengths in the scenario facts: EDR detected every test file within 5 minutes (SI-3), the MSSP escalated the simulated alert in 18 minutes (SI-4), cloud backups ran on 31 of 31 days and are isolated (CP-9), and every sampled cloud and identity provider administrator was challenged for MFA (IA-2(1)).

**Fully other than satisfied (7 controls):** AC-6, AC-6(5), CP-10, IA-2(1), MA-4, SC-28, and SR-6.

**Themes:**
1. **The cloud is in better shape than the ground.** Cloud backups, guardrails, and MFA test well; the directory, HQ servers, and the plant do not (AC-6(5), IA-2(1), CP-9, CP-10, SC-7, SC-28).
2. **Privileged and vendor access is the largest exposure** (AC-6, IA-5, AC-17, MA-4), including the ACH signing secret found during testing.
3. **Process has not scaled to five companies.** Terminations, transfers, changes, incidents, and training work at the holding company but not consistently at the subsidiaries (AC-2, CM-3, IR-4, AT-2, PM-9).

**POA&M:** 34 controls had at least one Other than satisfied statement. They map to 17 POA&M items (POAM-001 to POAM-017), because related controls share an item. Four more items come from the gap analysis and the AI assessment: POAM-018 (Home Services North integration), POAM-019 (group health plan), POAM-020 (AI governance), and POAM-021 (data retention). The total is 21 items: 8 High and 13 Moderate. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-08-10 | Plan and sample requests issued |
| 2026-08-17 to 2026-08-21 | Document examination and interviews |
| 2026-08-24 to 2026-08-27 | Site walkthroughs and technical tests |
| 2026-08-28 to 2026-09-04 | Analysis, draft findings, management responses |
| 2026-09-22 | Results and POA&M accepted by the CFO and presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (254 rows); `poam.csv` (21 items).

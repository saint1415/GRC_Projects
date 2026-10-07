# Security Assessment Plan and Summary: Cris Santos Company | Public Administration | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed GovTech systems integrator serving state and local agencies) |
| System assessed | Agency Case Management Cloud (ACMC), per the SSP (P02), plus the managed services remote administration path (SYS-10) at the audit committee's request |
| Tier / Vertical | Mid-Market / Public Administration |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead and 3 IT auditors), reporting to the board audit committee. The firm does not design or operate any assessed control. The GRC Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-28 (technical tests 2026-08-12 to 2026-08-19) |
| Also satisfies | SP 800-53 CA-2 (contract requirement); annual internal IT audit; evidence for SOC 2 (P09) and GovRAMP |
| Results accepted | Chief Technology Officer and Chief Operating Officer, 2026-09-17; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **38 controls, 224 determination statements.** Every determination statement in SP 800-53A for each selected control was assessed. Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover the High gaps in the gap analysis (P03), including the CJIS and Pub. 1075 overlay values;
- support SOC 2 Type 2 and GovRAMP readiness (P09).

**Why SYS-10 is in scope.** SYS-10 is outside the ACMC boundary, but P01 rated ransomware through it as the company's only Very High risk before testing (R-001), and it can reach the landing zone. The audit committee asked for AC-17, IA-5, MA-4, PS-4, SI-2, and SI-4 to be tested on that path as well.

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-2(3), PS-5 | Tenant access lifecycle; P03 G-002, CJ-07, PB-17; R-029 | Focused | Focused (samples of 25; project-close population) |
| AC-6 | Least privilege in regulated tenants; R-005, R-047 | Comprehensive | Comprehensive (all support and analyst roles) |
| AC-7 | CJIS and Pub. 1075 lockout values; CJ-06, PB-16 | Basic | Focused |
| AC-17, MA-4, IA-5 | Remote administration and secrets, including SYS-10; R-001, R-008 | Comprehensive | Comprehensive |
| IA-2(1) | MFA for privileged accounts; CJ-05 | Focused | Focused (25 of 40) |
| AT-2 | CJIS and FTI training; CJ-04, PB-02 | Basic | Focused |
| AU-2, AU-5, AU-6, AU-9, AU-11, SI-4 | Logging, retention, and misuse detection; PB-18, CJ-08, CJ-09; R-005, R-019 | Focused | Focused |
| CA-3 | Interconnections with agency systems; R-036 | Focused | Comprehensive (5 regulated interfaces) |
| CM-3, CM-6, SI-7 | Change control and integrity; R-015, R-037 | Focused | Focused |
| CP-4, CP-9, CP-10 | Recovery; R-002, R-006 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident handling and agency clocks; R-018 | Focused | Focused |
| MP-6 | Contract-end disposal; FL-03; R-017 | Focused | Comprehensive (5 contract ends) |
| PS-3, PS-4, PS-6 | Screening and terminations; CJ-01, CJ-03, CJ-13, PB-01; R-004 | Comprehensive | Comprehensive (all designated staff) |
| RA-5, SI-2 | Vulnerabilities and patching, including AG-02 servers; CJ-14; R-028 | Focused | Focused |
| SA-9, SR-6 | Vendors; R-012, R-013 | Focused | Comprehensive (22 vendors) |
| SC-7, SC-8, SC-12, SC-13 | Boundary and cryptography; CJ-11, PB-07; R-003, R-007 | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year at moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 13 items; small or high-risk populations were tested in full. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 142 | 25 (6 with AG-02 agency-side accounts) | AC-2, PS-4 |
| Transfers | 96 | 25 | AC-2, PS-5 |
| New accounts | 188 | 25 | AC-2 |
| Closed project assignments (2026) | 61 | 61 | AC-2, AC-2(3) |
| Designated staff (CJI and FTI) | 186 and 64 | All | PS-3, PS-6, AT-2 |
| Cloud administrator accounts | 40 | 25 (MFA test); all 40 elevations in July 2026 | IA-2(1), AC-6 |
| Support and analyst roles | 59 | All | AC-6 |
| Training records | 600 | 25 | AT-2 |
| Standard and emergency changes (2026 H1) | about 1,900 and 41 | 25 and 9 | CM-3 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| Restore tests | 5 | 5 | CP-4, CP-10 |
| Security incidents (2025-2026) | 31 | 10 | IR-4, IR-6 |
| High and critical vulnerability findings (Q1-Q2 2026) | 212 | 40 | RA-5 |
| Critical updates on AG-02 servers (2026 H1) | 38 | 10 | SI-2 |
| SYS-10 work orders (July 2026) | about 640 | 10 | MA-4 |
| Vendors with agency data or system access | 22 | 22 | SA-9, SR-6 |
| Contract ends since 2025 | 5 | 5 | MP-6 |
| Staff for reporting-awareness interviews | 600 | 15 (from managed services and support) | IR-6, AT-2 |

## 3. Methods and objects
- **Examine:**
  - the 2024 policies and the 2026 drafts approved on 2026-09-17
  - the SSP draft, the BIA, and the contingency plan (2024)
  - identity provider, tenant role, analytics, and cloud exports
  - SYS-10 configuration, credential store, and session logs
  - backup, restore, scan, patch, and change records
  - HR screening files, certification registers, and training records
  - vendor register, contracts, and SOC 2 reports
  - incident records, the 2025 tabletop report, and the draft P08 runbooks
- **Interview:**
  - vCISO, Director of Information Security, Security Operations Manager, and GRC Manager
  - Director of Cloud Operations, Director of Managed Services, VP of Engineering
  - Director of Contracts and Compliance, HR Director and the Personnel Security Coordinator
  - the MDR provider's service lead
  - 15 randomly selected staff from managed services and support
- **Test:**
  - MFA sign-in tests on 25 cloud administrator accounts
  - lockout tests on test accounts in the CJI and FTI enclave role groups
  - a SYS-10 connection from a managed services laptop to the shared services jump hosts
  - a secrets scan of the engineering wiki
  - an outbound connection from a production container to an external site
  - a delete attempt on the log archive by a production administrator role
  - a stop of the application audit forwarder in staging (to test AU-5 alerting)
  - deployment of an unsigned test image
  - a simulated suspicious sign-in to test MDR escalation
  - a restore of one tenant table from the vault
  - a TLS scan of 14 endpoints, and a review of module certificates

## 4. Rules of engagement
- No testing that could disrupt agency services. Tests on production ran in maintenance windows; tests on SYS-10 used a test session to a non-production jump host with AG-02's written approval.
- No agency data left company systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system. Auditors who examined FTI enclave or CJI records were screened through AG-01 and AG-02 beforehand.
- Stop-and-notify rule: any critical exposure is reported to the Director of Information Security and the vCISO the same day. **Used once:** on 2026-08-19 the wiki secrets scan found the SYS-10 automation API token, which can run scripts on every managed agency server, readable by 212 staff. The token was revoked the same day, and the company logged the finding as P01 R-050.
- Possible misuse found during testing is referred to the Director of Contracts and Compliance under the insider runbook, not investigated by the assessors. None was found.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 167 |
| Other than satisfied | 57 |
| **Total** | **224** |

Other than satisfied statements by risk: 3 Very High, 30 High, 22 Moderate, 2 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 22 | 4 | High | POAM-001 |
| AC-2(3) | 3 | 1 | Moderate | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-7 | 0 | 2 | Low | POAM-020 |
| AC-17 | 2 | 2 | High | POAM-003 |
| AT-2 | 7 | 3 | Moderate | POAM-013 |
| AU-2 | 4 | 2 | High | POAM-006 |
| AU-5 | 1 | 1 | Moderate | POAM-018 |
| AU-6 | 2 | 1 | High | POAM-006 |
| AU-9 | 2 | 0 | n/a | n/a |
| AU-11 | 0 | 1 | High | POAM-008 |
| CA-3 | 6 | 2 | Moderate | POAM-019 |
| CM-3 | 9 | 1 | Moderate | POAM-014 |
| CM-6 | 6 | 0 | n/a | n/a |
| CP-4 | 2 | 3 | High | POAM-009 |
| CP-9 | 6 | 0 | n/a | n/a |
| CP-10 | 0 | 2 | High | POAM-009 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 7 | 3 | Very High | POAM-003 |
| IR-4 | 11 | 2 | Moderate | POAM-012 |
| IR-6 | 1 | 1 | Moderate | POAM-012 |
| IR-8 | 14 | 3 | Moderate | POAM-012 |
| MA-4 | 4 | 4 | High | POAM-003 |
| MP-6 | 3 | 1 | Moderate | POAM-017 |
| PS-3 | 2 | 1 | High | POAM-005 |
| PS-4 | 3 | 2 | Moderate | POAM-016 |
| PS-5 | 2 | 2 | Moderate | POAM-001 |
| PS-6 | 3 | 1 | High | POAM-005 |
| RA-5 | 8 | 1 | Moderate | POAM-015 |
| SA-9 | 4 | 2 | High | POAM-011 |
| SC-7 | 5 | 1 | Moderate | POAM-021 |
| SC-8 | 0 | 1 | High | POAM-007 |
| SC-12 | 2 | 0 | n/a | n/a |
| SC-13 | 0 | 2 | High | POAM-007 |
| SI-2 | 9 | 1 | Moderate | POAM-015 |
| SI-4 | 10 | 2 | High | POAM-006 |
| SI-7 | 6 | 0 | n/a | n/a |
| SR-6 | 0 | 1 | High | POAM-011 |

**Fully satisfied (6 controls):** AU-9 (the log archive resisted a production administrator's delete attempt), CM-6, CP-9 (30 of 30 backup days copied to the write-once vault), IA-2(1) (security keys on all 25 sampled administrator accounts), SC-12, and SI-7 (the unsigned test image was blocked). These confirm the strengths of the landing zone design.

**Fully other than satisfied (7 controls):** AC-6, AC-7, AU-11, CP-10, SC-8, SC-13, and SR-6.

**Themes:**
1. **The managed services path is weaker than the cloud.** The landing zone resisted every test, but SYS-10 held an exposed automation token, unrotated agency credentials, push MFA, and no session recording, and it can reach the jump hosts (IA-5, MA-4, AC-17).
2. **Regulated data access has outgrown its checks** (AC-2, AC-6, PS-3, PS-5, PS-6, AU-6).
3. **Recovery is safe but slow** (CP-4, CP-10): the data survives in the vault, but not within the 8-hour contract RTO.
4. **CJI cryptography is due now** (SC-8, SC-13): the CJIS FIPS 140-2 cutoff is 2026-09-21.

**POA&M:** 32 controls had at least one Other than satisfied statement. They map to 19 POA&M items, because related controls share an item. Five more items come from the gap analysis, the SOC 2 readiness review, and the AI assessment (POAM-004 FTI in the analytics service, POAM-010 phishing-resistant MFA, POAM-022 AI governance, POAM-023 SOC 2 and GovRAMP evidence, POAM-024 municipal MFA). The total is 24 items: 1 Very High, 11 High, 11 Moderate, and 1 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-11 | Document examination and interviews |
| 2026-08-12 to 2026-08-19 | Technical tests (stop-and-notify used 2026-08-19) |
| 2026-08-20 to 2026-08-28 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (224 rows); `poam.csv` (24 items).

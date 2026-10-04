# Security Assessment Plan and Summary: Cris Santos Company | Educational Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed private, for-profit college) |
| System assessed | Student Information and Learning Platform (SILP), per the SSP (P02) |
| Tier / Vertical | Mid-Market / Educational Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors), reporting to the board audit committee. The firm does not design or operate any assessed control and is not the vCISO's firm. The Information Security Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (walkthroughs at Campus 1 and Campus 3 on 2026-08-12; technical tests 2026-08-10 to 2026-08-13) |
| Also satisfies | Regular testing of key controls under 16 CFR 314.4(d)(1); annual internal IT audit; input to the Qualified Individual's report on testing results (314.4(i)(2)) |
| Results accepted | Chief Information Officer, 2026-09-17; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **32 controls, 233 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover Safeguards Rule elements, FERPA requirements, and Title IV duties with gaps in the gap analysis (P03);
- support inherited-control reliance and SOC 2 readiness for the employer education services (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, IA-2, PS-4 | Account lifecycle gaps; 314.4(c)(1)(i); R-007, R-042 | Focused | Focused (samples of 25; all local LMS accounts) |
| AC-6 | Least privilege; 314.4(c)(1)(ii); 99.31(a)(1)(ii); R-009, R-020 | Comprehensive | Comprehensive (all roles and all admin accounts) |
| AC-17 | Servicer and vendor remote access; 314.4(c)(5); R-008, R-038 | Focused | Comprehensive (all 8 servicer accounts) |
| IA-2(2), IA-11 | Student MFA and step-up for refund changes; 314.4(c)(5); 99.31(c); R-005 | Comprehensive | Focused (test accounts) |
| IA-5 | Authenticator management; R-021 | Focused | Focused |
| IA-12 | Applicant identity proofing; 668.16(g)(1); R-006 | Focused | Focused (30 applicant files) |
| AT-2 | Training; 314.4(e)(1) | Basic | Focused |
| AU-2, AU-6, SI-4 | User activity monitoring; 314.4(c)(8); R-002, R-019 | Focused | Focused |
| CA-8, RA-5, SI-2 | Testing and vulnerability management; 314.4(d)(2); R-025, R-026 | Focused | Focused |
| CM-3, CM-8 | Change management and inventory; 314.4(c)(2), (c)(7); R-024, R-036 | Focused | Focused (20 changes) |
| CP-2, CP-4, CP-9 | Contingency and recovery; 314.4(h); R-001 (Very High), R-014 to R-017 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident capability and reporting; 314.4(h), (j); SAIG agreement; R-029, R-030 | Focused | Focused (10 incidents) |
| MP-6, PE-3 | Disposal and physical access; 314.4(c)(6)(i) | Basic | Focused (2 of 3 campuses) |
| PT-3 | FAFSA data use; HEA sec. 483; R-011 | Focused | Comprehensive (warehouse schema) |
| RA-3 | Risk assessment; 314.4(b) | Focused | Comprehensive |
| SA-9, SR-6 | Vendor oversight; 314.4(f); 99.31(a)(1)(i)(B); R-010, R-037 | Focused | Focused (20 contracts) |
| SC-7, SC-8 | Segmentation and encryption in transit; 314.4(c)(1), (c)(3); R-003, R-012 | Focused | Focused |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year with moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items; small populations were tested in full. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 142 | 25 | AC-2, PS-4 |
| Transfers | 58 | 25 | AC-2 |
| New staff and faculty accounts | 186 | 25 | AC-2 |
| Local LMS accounts | 140 | 140 | AC-2 |
| Servicer FAMS accounts | 8 | 8 | AC-17, IA-2(2) |
| SaaS and cloud administrator accounts | 37 | 37 | AC-6 |
| Online applicant files (fall 2025) | about 2,900 | 30 | IA-12 |
| Student password and MFA resets by the service desk | about 6,100 | 10 | IA-5 |
| SIS configuration and integration job changes (2026-01 to 2026-06) | 112 | 20 | CM-3 |
| Critical vulnerability findings (Q1-Q2 2026) | 40 | 40 | RA-5, SI-2 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| Vendor contracts | about 90 | 20 | SA-9 |
| Incidents (2025-2026) | 44 | 10 | IR-4 |
| Emails from financial aid to the servicer (June 2026) | 312 | 20 | SC-8 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6, AT-2 |
| Campuses for walkthroughs | 3 | 2 (Campus 1 and Campus 3) | PE-3, SC-7, CM-8 |

## 3. Methods and objects
- **Examine:**
  - policies (the 2023 set and drafts of the 2026 set) and the SSP draft
  - identity provider, SIS, LMS, FAMS, data warehouse, and cloud exports
  - backup, patch, scan, penetration test, and EDR reports
  - vendor contracts, the servicer contract, and SOC 2 review records
  - the incident queue, the 2023 plan, and the 2024 tabletop report
  - the data warehouse schema and the AI-002 feature list
  - disposal certificates and copier lease records
- **Interview:**
  - vCISO, CIO, Information Security Manager, and both analysts
  - Chief Compliance Officer, Registrar, Director of Financial Aid, Bursar
  - Vice President of Enrollment Management and the Director of Admissions Operations
  - Dean of Online Learning, Director of Institutional Research, Director of Campus Safety
  - the MSSP service lead
  - 15 randomly selected staff
- **Test:**
  - sign-in tests with a test student account (MFA prompts, step-up on a refund bank change)
  - simulated credential stuffing against the test student account to check for an alert (none was raised)
  - reachability test from a Campus 3 lab computer to staff and campus safety devices
  - restore of a file-service folder from the backup account (passed) and of one integration platform server image (failed)
  - a scope review of the November 2025 penetration test against the risk register

## 4. Rules of engagement
- No testing against real student accounts or live refund files. A test student account with a test bank account was created by the Registrar and Bursar for the step-up and credential stuffing tests and removed afterward.
- No customer information or education records left college systems. Screenshots were redacted, and evidence was stored in the firm's encrypted workpaper system under its confidentiality agreement.
- Campus safety devices were scanned only for reachability, with the Director of Campus Safety present; no login attempts were made.
- Stop-and-notify rule: any critical exposure is reported to the CIO and the vCISO the same day. **Used once:** on 2026-08-12 the assessors reported the access control vendor's always-on remote tool on the Campus 3 network. The college logged it as P01 R-038 on 2026-08-14.
- The 7 unencrypted aid emails were referred to the Chief Compliance Officer for a notification decision, not investigated by the assessors.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 127 |
| Other than satisfied | 106 |
| **Total** | **233** |

Other than satisfied statements by risk: 50 High, 49 Moderate, 7 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 18 | 8 | Moderate | POAM-002 |
| AC-6 | 0 | 1 | High | POAM-004 |
| AC-17 | 2 | 2 | High | POAM-003 |
| AT-2 | 8 | 2 | Low | POAM-005 |
| AU-2 | 1 | 5 | High | POAM-006 |
| AU-6 | 1 | 2 | High | POAM-006 |
| CA-8 | 0 | 1 | Moderate | POAM-007 |
| CM-3 | 5 | 5 | Moderate | POAM-008 |
| CM-8 | 3 | 3 | Moderate | POAM-009 |
| CP-2 | 5 | 19 | High | POAM-010 |
| CP-4 | 0 | 5 | High | POAM-011 |
| CP-9 | 6 | 0 | n/a | n/a |
| IA-2 | 1 | 1 | Moderate | POAM-002 |
| IA-2(2) | 0 | 1 | High | POAM-001 |
| IA-5 | 6 | 4 | Moderate | POAM-012 |
| IA-11 | 0 | 1 | High | POAM-001 |
| IA-12 | 2 | 3 | High | POAM-013 |
| IR-4 | 5 | 8 | Moderate | POAM-014 |
| IR-6 | 1 | 1 | Moderate | POAM-015 |
| IR-8 | 8 | 9 | Moderate | POAM-014 |
| MP-6 | 3 | 1 | Low | POAM-016 |
| PE-3 | 9 | 3 | Low | POAM-017 |
| PS-4 | 3 | 2 | Moderate | POAM-002 |
| PT-3 | 3 | 3 | High | POAM-018 |
| RA-3 | 7 | 1 | Low | POAM-023 |
| RA-5 | 7 | 2 | Moderate | POAM-007 |
| SA-9 | 3 | 3 | High | POAM-020 |
| SC-7 | 4 | 2 | Moderate | POAM-021 |
| SC-8 | 0 | 1 | Moderate | POAM-022 |
| SI-2 | 8 | 2 | Moderate | POAM-007 |
| SI-4 | 8 | 4 | High | POAM-006 |
| SR-6 | 0 | 1 | High | POAM-020 |

**Fully satisfied (1 control):** CP-9 (daily, encrypted, write-once backups in a separate account and region; 30 of 30 jobs succeeded and the file-service restore passed). It confirms the strongest control listed in the scenario facts.

**Fully other than satisfied (7 controls):** AC-6, CA-8, CP-4, IA-2(2), IA-11, SC-8, and SR-6. Most are single-statement controls where one clear gap decides the result.

**Themes:**
1. **Identity is the weakest layer** (IA-2(2), IA-11, IA-12, IA-5, AC-2, AC-6). The college protects staff well, but students, the servicer, partners, and applicants are where fraud happens, and the controls there are optional or manual.
2. The college **can back up but has not proven it can recover** (CP-2, CP-4). The only restore of a college-managed server attempted during the assessment failed.
3. **SaaS activity is invisible** (AU-2, AU-6, SI-4). A simulated account takeover and refund bank change raised no alert.
4. **Data use and vendors** (PT-3, SA-9, SR-6): FAFSA-derived data has drifted into analytics, and vendor terms lag behind purchases.

**POA&M:** 31 controls had at least one Other than satisfied statement. They map to 22 POA&M items (POAM-001 to POAM-018 and POAM-020 to POAM-023), because related controls share an item. Five more items come from the gap analysis, the BIA, the SOC 2 readiness review, and the AI assessment (POAM-019 partner portal, POAM-024 emergency notification break-glass, POAM-025 AI governance conditions, POAM-026 retention and disposal, POAM-027 Qualified Individual oversight and board reporting). The total is 27 items: 11 High, 11 Moderate, and 5 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-13 | Walkthroughs and technical tests |
| 2026-08-14 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-17 | Results and POA&M presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (233 rows); `poam.csv` (27 items).

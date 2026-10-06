# Security Assessment Plan and Summary: Cris Santos Company | Professional, Scientific, and Technical Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed CPA, tax, and advisory firm, with its attest affiliate) |
| System assessed | Tax and Client Data Platform (TCDP), per the SSP (P02), plus the shared controls the CAS platform relies on |
| Tier / Vertical | Mid-Market / Professional, Scientific, and Technical Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead and 2 IT auditors), an unaffiliated CPA firm that reports to the audit committee. It does not design or operate any assessed control, and it is not the Attest Firm, so the Company's own attest practice does not assess its own administrative services provider. The GRC Manager coordinated access but did not select samples or rate findings |
| Assessment window | 2026-08-03 to 2026-08-21 (walkthroughs of Offices 1, 4, and 6 on 2026-08-11 and 2026-08-12; technical tests after 18:00) |
| Also satisfies | FTC Safeguards Rule regular testing of key controls, 16 CFR 314.4(d)(1) (N54-R01); HIPAA evaluation, 45 CFR 164.308(a)(8) (N54-R06); annual internal IT audit. It does **not** replace the annual penetration test and the six-month vulnerability assessments in 314.4(d)(2) |
| Results accepted | Chief Operating Officer, 2026-09-22; High items by the Chief Executive Officer; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **34 controls, 203 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- cover the Safeguards Rule and IRC 7216 requirements with High or Moderate gaps in P03;
- support the incident reporting duties in both P08 runbooks;
- support inherited-control reliance and the SOC 2 readiness of the CAS service (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Account lifecycle including seasonal staff and CAS local accounts; 314.4(c)(1)(i); R-009, R-051 | Focused | Focused (samples of 25) |
| AC-6, IA-5 | Privileged access and authenticator management; R-004, R-007, R-008, R-050 | Comprehensive | Comprehensive (all privileged accounts) |
| IA-2, IA-2(1), IA-8 | Unique IDs and MFA for staff and clients; 314.4(c)(5); R-001, R-006 | Focused | Focused |
| AC-17, SC-7 | Remote access, vendor access, and segmentation of the offshore desktops; R-011, R-014 | Focused | Focused |
| AC-21, PS-7 | IRC 7216 consent and offshore vendor oversight; 301.7216-3(a)(3)(i)(D), (b)(1), (b)(4); R-011, R-012, R-039 | Focused | Focused (samples of 25) |
| PS-6 | Contractor access agreements and the 7216 notice; 301.7216-2(d)(2); R-038 | Basic | Focused |
| AT-2 | Training gate for seasonal staff; 314.4(e)(1); R-031 | Basic | Focused |
| AU-2, AU-6, AU-11, SI-4 | Monitoring of authorized users; 314.4(c)(8); R-001, R-005, R-030 | Focused | Focused |
| CA-8, RA-5, SI-2 | Testing and vulnerability management; 314.4(d)(2); R-028 | Focused | Comprehensive (all critical findings) |
| CM-3, CM-8 | Change management and inventory; 314.4(c)(2), (c)(7); R-015, R-029 | Focused | Focused |
| CP-4, CP-9 | Recovery; 314.4(h); R-004, R-017, R-018, R-019 | Comprehensive | Comprehensive |
| IR-4, IR-6, IR-8 | Incident capability and reporting; 314.4(h), (j); IRS Pub. 1345; R-023 | Focused | Basic |
| MP-6, SC-28, SI-12 | Encryption, disposal, and retention; 314.4(c)(3), (c)(6); R-016, R-027 | Basic | Focused |
| SC-8 | Encryption in transit for returns; 314.4(c)(3); R-024 | Basic | Focused (60 emails) |
| SA-9, SR-6 | Service provider oversight; 314.4(f); R-013 | Focused | Focused (samples of 20) |
| RA-3 | Written risk assessment; 314.4(b) | Focused | Basic |

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table: 25 items for a control that operates many times a year at moderate risk, and 5 to 20 items for weekly, monthly, or less frequent controls. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Seasonal accounts ended 2026-04 and 2026-05 | 131 | 25 | AC-2 |
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers | 58 | 25 | AC-2 |
| New accounts | 412 | 25 | AC-2 |
| Privileged accounts (all admin planes) | 41 | 25 for MFA tests; all 41 for rights review | IA-2(1), AC-6 |
| Offshore returns, 2026 season | about 5,500 | 25 | AC-21, PS-7 |
| Lender and adviser releases | about 1,900 | 25 | AC-21 |
| Outbound emails with tax attachments (one March 2026 week) | about 4,800 | 60 | SC-8 |
| Service provider contracts | 85 | 20 | SA-9 |
| Critical vulnerability findings (Q1-Q2 2026) | 40 | 40 | RA-5, SI-2 |
| Change tickets (2026) | 312 | 25 | CM-3 |
| Incidents (2025-2026) | 31 | 10 | IR-4 |
| Backup job days (July 2026) | 30 | 30 | CP-9 |
| Staff for reporting-awareness interviews | 600 | 15 | IR-6, AT-2 |
| Seasonal staff training records | 131 | 25 | AT-2 |
| Destruction certificates | 64 | 10 | MP-6 |
| Offices for walkthroughs | 6 | 3 (Office 1 with the document processing center, Office 4, Office 6) | PE (not rated), SC-7, MP-6 |

## 3. Methods and objects
- **Examine:**
  - the 2024 WISP and policies, and drafts of POL-01 to POL-05 and the standards
  - the SSP draft and the P01 risk register
  - identity provider, directory, DMS, cloud, and CAS service user and role exports
  - backup, patch, scan, penetration test, and EDR reports
  - provider contracts, the offshore vendor contract, the AI sub-processor amendment, and vendor SOC 2 reports
  - portal consent records and the offshore routing log
  - the incident queue, the 2025 tabletop report, and MSSP monthly reports
  - the retention schedule, DMS age report, destruction certificates, and lease records
- **Interview:**
  - Director of Information Security, Chief Information Officer, GRC Manager, IT Operations Manager, and 2 security engineers
  - General Counsel and Privacy Officer
  - National Tax Practice Leader, Director of Tax Operations, and CAS Practice Leader
  - Chief People Officer
  - the MSSP service lead and the offshore vendor's account manager
  - 15 randomly selected staff
- **Test:**
  - MFA sign-in tests on 25 sampled privileged accounts
  - sign-in to mail from an unmanaged device
  - 3 calls to the service desk by an assessor posing as an employee requesting an MFA reset (approved in writing by the Chief Operating Officer)
  - an inbox rule and an external forwarding rule created on a test mailbox after hours
  - a bulk download of 500 test files from the DMS with a test account
  - reachability tests from the virtual desktop subnet and an office workstation subnet
  - a test user from one tax team opening other teams' client folders
  - local administrator password comparison on 12 scanning stations
  - a restore of one DMS folder from the backup account
  - an external scan of the VPN and virtual desktop gateways
  - encryption spot checks on 5 desktops and 4 printers

## 4. Rules of engagement
- No testing that could interrupt client work or change client data: tests ran after 18:00, test accounts and test files only, and no change to any return or CAS client record.
- No client data left Company systems. Screenshots were redacted, and workpapers are held in the internal audit firm's encrypted repository under its confidentiality terms.
- The service desk tests were approved in writing by the Chief Operating Officer, and the service desk manager was told afterward. The reset accounts were test accounts.
- Stop-and-notify rule: any critical exposure is reported to the Director of Information Security the same day. **Used once:** on 2026-08-14 the assessors found 3 active local accounts of former CAS staff in the payroll and bill-pay services. The accounts were disabled the same day, the vendors' logs showed no sign-in after the termination dates, and the finding was logged as P01 R-051.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 136 |
| Other than satisfied | 67 |
| **Total** | **203** |

Other than satisfied statements by risk: 22 High, 36 Moderate, 9 Low.

| Control | Satisfied | Other than satisfied | Risk | POA&M |
|---|---|---|---|---|
| AC-2 | 18 | 8 | High | POAM-001 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 2 | 2 | Moderate | POAM-003 |
| AC-21 | 0 | 2 | High | POAM-004 |
| AT-2 | 7 | 3 | Moderate | POAM-005 |
| AU-2 | 2 | 4 | High | POAM-006 |
| AU-6 | 1 | 2 | High | POAM-006 |
| AU-11 | 0 | 1 | Moderate | POAM-006 |
| CA-8 | 0 | 1 | Moderate | POAM-008 |
| CM-3 | 6 | 4 | Moderate | POAM-009 |
| CM-8 | 4 | 2 | Moderate | POAM-010 |
| CP-4 | 3 | 2 | Moderate | POAM-011 |
| CP-9 | 6 | 0 | n/a | n/a |
| IA-2 | 2 | 0 | n/a | n/a |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 6 | 4 | High | POAM-012 |
| IA-8 | 0 | 1 | High | POAM-013 |
| IR-4 | 11 | 2 | Moderate | POAM-014 |
| IR-6 | 1 | 1 | Moderate | POAM-014 |
| IR-8 | 14 | 3 | Low | POAM-014 |
| MP-6 | 3 | 1 | Low | POAM-015 |
| PS-4 | 3 | 2 | High | POAM-001 |
| PS-6 | 2 | 2 | Moderate | POAM-016 |
| PS-7 | 3 | 2 | Moderate | POAM-004 |
| RA-3 | 8 | 0 | n/a | n/a |
| RA-5 | 7 | 2 | Moderate | POAM-008 |
| SA-9 | 3 | 3 | High | POAM-017 |
| SC-7 | 4 | 2 | Moderate | POAM-018 |
| SC-8 | 0 | 1 | Moderate | POAM-019 |
| SC-28 | 0 | 1 | Low | POAM-015 |
| SI-2 | 9 | 1 | Moderate | POAM-008 |
| SI-4 | 8 | 4 | High | POAM-007 |
| SI-12 | 2 | 2 | Moderate | POAM-020 |
| SR-6 | 0 | 1 | High | POAM-017 |

**Fully satisfied (4 controls):** CP-9 (isolated, write-once, encrypted backups; the test restore worked), IA-2 (every user, including offshore vendor staff, has a unique account), IA-2(1) (MFA on all 25 sampled privileged sign-ins), and RA-3 (the 2026 risk assessment meets every statement). These confirm the strengths in the scenario facts.

**Fully other than satisfied (8 controls):** AC-6, AC-21, AU-11, CA-8, IA-8, SC-8, SC-28, and SR-6. Most are single-statement controls, so one weakness fails the whole control.

**Themes:**
1. **Identity has strong MFA coverage and weak edges** (AC-2, AC-6, IA-5, IA-8): accounts outside SSO, standing admin rights, a service desk that can be talked into a reset, and optional client MFA.
2. **IRC 7216 conditions are not built into the workflow** (AC-21, PS-6, PS-7): consent and SSN masking depend on people remembering, and the offshore program is the largest exposure.
3. **The Company cannot see inside its SaaS applications** (AU-2, AU-6, SI-4): the bulk-download test and the after-hours inbox rule both went unnoticed.
4. **Third parties are trusted without periodic proof** (SA-9, SR-6).

**POA&M:** 30 controls had at least one Other than satisfied statement. They map to 20 POA&M items (POAM-001 to POAM-020), because related controls share an item. Four more items come from the gap analysis, the risk register, and the AI assessment (POAM-021 AI governance, POAM-022 PHI enclave and HIPAA risk analysis, POAM-023 board report, POAM-024 CAS bank-change controls). The total is 24 items: 10 High, 13 Moderate, and 1 Low. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan and sample requests issued |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-14 | Walkthroughs and technical tests |
| 2026-08-17 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-22 | Results and POA&M accepted and presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (203 rows); `poam.csv` (24 items).

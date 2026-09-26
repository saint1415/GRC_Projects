# Security Assessment Plan and Summary: Cris Santos Company | Management of Companies | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (holding company with three operating subsidiaries) |
| System assessed | Shared Corporate Services Platform (SCSP), per the SSP (P02) |
| Tier / Vertical | Small / Management of Companies and Enterprises |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in operating or designing the controls, and not the MSP. Escorted by the IT Manager |
| Assessment window | 2026-09-08 to 2026-09-11 (site visits: HQ 2026-09-08, Supply warehouse and Home Services shop 2026-09-09) |
| Also satisfies | Finance's testing of key controls under the FTC Safeguards Rule, 16 CFR 314.4(d)(1) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 155 determination statements.** Controls were chosen because they support the four High risks in P01, cover the Safeguards Rule elements Finance relies on the holding company for (P03), or cover High-priority outcomes in the CSF 2.0 group profile.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Late subsidiary terminations; SYS-11 local accounts (P01 R-009; 314.4(c)(1)(i)) | Focused | Focused (sample of 8 leavers, 3 transfers) |
| AC-6, AC-17 | Global admins, over-broad sharing, remote access (R-001, R-003, R-006) | Focused | Focused |
| IA-2, IA-2(1), IA-2(2), IA-5 | MFA and authenticator management (R-001, R-028; 314.4(c)(5)) | Focused | Focused (all admin accounts; 3 sites) |
| AU-6, AU-11, SI-4 | No monitoring or log review (R-007, R-008; 314.4(c)(8)) | Basic | Focused |
| CP-4, CP-9 | Backups and recovery (R-004, High) | Focused | Focused |
| IR-4, IR-8 | New incident plan; subsidiary handling (R-021; 314.4(h)) | Focused | Basic |
| RA-3, RA-5, PM-9 | Risk assessment, vulnerability scanning, and group risk strategy (314.4(b), (d)(2); GV.RM) | Basic | Basic |
| SA-9 | Service providers, including the holding company's own role for Finance (314.4(f)) | Focused | Focused |
| SC-28 | ACH files on the SFTP server (R-011; 314.4(c)(3)) | Basic | Focused |
| AT-2 | Training gaps behind payment fraud and phishing (R-001, R-002) | Basic | Focused (12 staff) |
| CM-3 | No change control (314.4(c)(7)) | Basic | Basic |

## 2. Methods and objects
- **Examine:** identity provider exports and conditional access policies, collaboration site permission reports, backup and vault settings, contracts and SOC 2 reports, training records, P01 and Finance's 2023 WISP, POL-01 to POL-05, the P08 runbook, firewall consoles, and SFTP storage settings.
- **Interview:** CFO, IT Manager, Systems Administrator, HR Director, Controller, Treasury and Payments Analyst, MSP lead technician, the three subsidiary Presidents, and 12 staff chosen at random across the sites (incident reporting and training awareness).
- **Test:**
  - sign-in tests with a standard user, an administrator, and both MSP administrator accounts
  - sign-in at the 3 Supply counter desktops
  - attempted deletion of a backup recovery point with a production administrator role (in a test vault)
  - endpoint isolation and session revocation for a test user
  - an after-hours EDR test alert at 21:00 on 2026-09-10
  - an approved social engineering call to the after-hours help desk requesting an MFA reset
  - a file read test on the SFTP server with an IT administrator account
  - a search of the IT team's files for stored secrets

## 3. Rules of engagement
- The CFO approved the social engineering call and the after-hours test in writing. The MSP account owner was told after the call.
- No production backup was deleted; the deletion test used a test vault with the same policy.
- No Finance customer information left the SFTP server; the assessor viewed file names and one redacted record only.
- The assessor stopped and notified the IT Manager on finding a critical exposure. **One was found:** both MSP global administrator accounts were excluded from the MFA policy. The IT Manager enforced MFA on them on 2026-09-12.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 48 |
| Other than satisfied | 107 |

**Fully other than satisfied:** AC-6, IA-2(1), AU-6, AU-11, CP-4, RA-5, SA-9, SC-28, CM-3. No process or technology existed for these, or the one that existed failed the test.
**Fully satisfied:** IA-2(2) (MFA for all standard users).
**Largely satisfied:** IR-8 (the new written plan meets most plan-content objectives), RA-3 (the 2026 assessment), PS-4 (exit steps other than timing).

**New findings:**
- Both MSP global administrator accounts were excluded from the MFA policy (IA-02(01)). Added to POAM-004; corrected 2026-09-12.
- A shared generic account on 3 Supply counter desktops (IA-02[01]). Added to the risk register as R-032 and to POAM-005.
- The after-hours help desk reset MFA for a caller posing as an employee (IA-05a.). The MSP's reset rights were removed on 2026-09-15 (POAM-006).
- 4 former Home Services technicians still active in SYS-11 (AC-02f.[04]). Removal due 2026-10-15 (POAM-001).

All 21 controls with weaknesses have POA&M items in `poam.csv`. The High items are POAM-003, POAM-004, POAM-008, POAM-009, and POAM-019.

## 5. Deliverables
`assessment-results.csv` (155 rows), `poam.csv` (21 items), this plan and summary. The results were accepted by the CFO and the CEO on 2026-09-25 and reported to Finance's Board of Managers in the Qualified Individual's annual report.

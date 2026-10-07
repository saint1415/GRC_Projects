# Security Assessment Plan and Summary: Cris Santos Company | Educational Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (private career college) |
| System assessed | Student Information and Financial Aid Platform (SIFAP), per the SSP (P02) |
| Tier / Vertical | Small / Educational Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in designing or operating the controls. Escorted by the IT Director |
| Assessment window | 2026-07-27 to 2026-07-31 (campus walkthrough 2026-07-29) |
| Also satisfies | FTC Safeguards Rule testing of key controls, 16 CFR 314.4(d)(1); input to the Qualified Individual's Board report (314.4(i)(2)) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **24 controls, 164 determination statements.** Controls were chosen because they:
- support the four High risks in P01 (R-001, R-002, R-004, R-019);
- test Safeguards Rule elements that the gap analysis (P03) found Not met or Partially met;
- test the FERPA "reasonable methods" requirement (34 CFR 99.31(a)(1)(ii)).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-6, PS-4 | Access control and FERPA reasonable methods (314.4(c)(1); 99.31(a)(1)(ii)); R-007, R-008 | Focused | Focused (SIS, FAMS, LMS, identity provider) |
| IA-2(1), IA-5, IA-8 | MFA and authenticators (314.4(c)(5)); R-004 (High), R-005, R-006, R-032 | Focused | Focused (servicer accounts, 10 of 150 lab PCs, student portal) |
| AU-6, SI-4 | User activity monitoring (314.4(c)(8)); R-001 (High), R-011 | Basic | Basic |
| SI-3 | Malware protection; R-001 (High) | Focused | Focused (2 endpoints tested) |
| SC-8, SC-28 | Encryption (314.4(c)(3)); R-002 (High), R-003 | Focused | Focused (aid export folder, mail flow) |
| CP-9, CP-4 | Backups and recovery (314.4(h)(2)); R-019 (High) | Focused | Focused |
| CA-8, RA-5 | Penetration testing and vulnerability assessment (314.4(d)(2)); R-012 | Basic | Basic |
| CM-3 | Change management (314.4(c)(7)); R-017 | Basic | Focused (integration server history) |
| IR-4, IR-6, IR-8 | Incident response plan and notification (314.4(h), (j)); R-013 | Focused | Basic |
| RA-3, PM-9 | Risk assessment and Board reporting (314.4(b), (i)); R-014 | Focused | Basic |
| SA-9 | Service provider oversight (314.4(f)); R-009, R-004 | Focused | Focused (servicer and 3 SaaS contracts) |
| AT-2 | Security awareness training (314.4(e)(1)); R-015 | Basic | Focused (8 staff interviewed) |
| SI-12 | Retention and disposal (314.4(c)(6)); R-016 | Basic | Basic |

## 2. Methods and objects
- **Examine:**
  - identity provider, SIS, FAMS, and LMS account and role exports;
  - contracts for the SIS, LMS, FAMS, and servicer;
  - backup job reports and the cloud IAM export;
  - the 2023 WISP, the 2023 incident contact list, and the 2024 and 2026 risk assessments;
  - training records, Board minutes, and the 2025 scan report.
- **Interview:** Campus President, IT Director, Director of Financial Aid, Registrar, HR Manager, Lab Coordinator, and 8 randomly selected staff (incident reporting awareness).
- **Test:**
  - comparison of the LMS account list with the HR adjunct roster;
  - a sign-in test with a servicer test account created for the assessment;
  - local administrator password comparison on 10 lab PCs;
  - an antivirus test file on 2 staff endpoints, with alert routing checked;
  - a TLS scan of the SIS, FAMS, LMS, and VPN endpoints;
  - a file inspection of the aid export folder.

## 3. Rules of engagement
- No testing during the registration week or on disbursement days. No changes to production data.
- No customer information or education records left the campus. Screenshots were redacted, and the file inspection counted files without copying them.
- The servicer test account was created and deleted by the Director of Financial Aid with the servicer's agreement.
- The assessor was to stop and notify the IT Director immediately on finding a critical exposure. One was found, the 11 active former-adjunct LMS accounts, and it was reported on 2026-07-30.
- The assessor reports to the Campus President. Results are shared with the Board chair.

## 4. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Kickoff with the Campus President and IT Director; document requests |
| 2026-07-28 | Examine: account, role, backup, and contract evidence |
| 2026-07-29 | Campus walkthrough (labs, records room, financial aid office); tests |
| 2026-07-30 | Interviews; stale LMS account finding reported to the IT Director |
| 2026-07-31 | Closeout briefing; draft results |
| 2026-08-21 | Results and POA&M accepted by the Campus President |

Deliverables: `assessment-results.csv` (164 rows), `poam.csv` (27 items), and this plan and summary.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 46 |
| Other than satisfied | 118 |
| **Total** | **164** |

**Controls by result:**
- **Fully other than satisfied (12):** AC-6, AU-6, CA-8, CM-3, CP-4, IA-2(1), IR-6, IR-8, RA-5, SC-8, SC-28, SI-4. No plan, process, or technology existed for these at the time of fieldwork.
- **Partly satisfied (11):** AC-2, AT-2, CP-9, IA-5, IR-4, PM-9, PS-4, RA-3, SA-9, SI-3, SI-12.
- **Satisfied (1):** IA-8. Students and servicer users are uniquely identified and authenticated. The missing student MFA is a Safeguards Rule gap (314.4(c)(5)) rather than an IA-8 finding, so it is tracked from P03 as POAM-024.

**What worked:** separate named accounts for staff with same-day termination, provider and endpoint encryption, daily backups, signature antivirus detection and quarantine, and a current written risk assessment (2026-07-17).

**New finding:** 11 LMS accounts of former adjunct faculty were still active (AC-02f.[04]). This was not known before testing. The accounts were disabled on 2026-08-07, and the finding was added to the risk register as R-007 (2026-07-31) and to POAM-008.

**Timing note:** POL-01 to POL-05 and the P08 runbook were approved on 2026-08-21, after fieldwork. Findings reflect the state during fieldwork. The IR-8 and IR-4 items will be retested at the 2026-11-30 tabletop.

## 6. POA&M
All 23 controls with weaknesses have POA&M items (POAM-001 to POAM-023). Four more items (POAM-024 to POAM-027) carry High and Moderate P03 gaps that no assessed control covers (student MFA, FAFSA data in the reporting database, the data map, and ongoing monitoring).

| POA&M risk level | Items |
|---|---|
| High | 7 |
| Moderate | 18 |
| Low | 2 |
| **Total** | **27** |

The High items are POAM-001 to POAM-007. They match the four High risks in P01 and the High gaps in P03.

Status on 2026-08-21: 16 in progress, 11 open.

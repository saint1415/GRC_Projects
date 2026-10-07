# Security Assessment Plan and Summary: Cris Santos Company | Administrative and Support Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm) |
| System assessed | Payroll and Applicant Tracking System (PATS), per the SSP (P02) |
| Tier / Vertical | Micro / Administrative and Support and Waste Management and Remediation Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Operations Manager; MSP lead technician on call and present for the administrator login tests |
| Assessment window | 2026-08-10 to 2026-08-12 (on site 2026-08-11) |
| Why it matters | No rule requires this assessment. It is the independent check that a 7-person firm, where the Security and Privacy Lead also runs payroll and E-Verify, cannot give itself (POL-02 A.6), and it supplies evidence for the client questionnaire (P09) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 81 determination statements.** Controls were chosen because they support the three High risks in P01 (payroll account takeover, AI screening bias through vendor oversight, MSP compromise), cover the binding Form I-9 and E-Verify duties with gaps in P03, or test what the MSP does on the firm's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Departed users kept access (P01 R-006; P03 G-053; E-Verify MOU Art. II.A.3) | Focused | Comprehensive (every user in the ATS, payroll, suite, E-Verify, screening portal, accounting) |
| AC-3 | Onboarding folder open to all (R-004; 8 CFR 274a.2(b)(4), (g)(1)(i)) | Focused | Focused (test as a non-onboarding user) |
| IA-2(1) | Payroll SMS codes; MSP-held logins (R-001, R-013) | Focused | Comprehensive (all administrator logins) |
| AT-2, IR-6 | No training; no reporting rule (R-016, R-008) | Basic | Focused (5 of 7 staff interviewed) |
| AU-6 | Nobody watches payroll changes or exports (R-001, R-002) | Basic | Basic |
| CP-4, CP-9 | Backup never tested; deletable (R-005; 274a.2(g)(1)(ii)) | Focused | Focused |
| MP-6, SI-12 | Disposal and retention of Form I-9 copies and consumer reports (R-015; 16 CFR 682.3; 274a.2(b)(2)) | Basic | Focused (folder listing; device records) |
| RA-3 | Risk assessment (R-009 change trigger) | Basic | Basic |
| SA-9 | Vendor oversight for payroll, ATS and its AI subprocessor, screening, MSP, backup (R-010, R-013, R-017) | Focused | Comprehensive (all 6 providers that hold worker data or administer systems) |

## 2. Methods and objects
- **Examine:** user and role lists from every PATS system; shared-drive sharing settings and the Onboarding folder listing; MFA settings; payroll, ATS, and suite audit screens; termination records; handbook acknowledgments; vendor agreements and the payroll vendor's SOC 2 report; P01 and P05; the MSP evidence below.
- **Interview:** Owner, Operations Manager, Onboarding and Payroll Coordinator, Senior Recruiter, 5 of 7 staff (training and incident reporting), and the MSP lead technician.
- **Test:**
  - user lists compared against the staff roster in every system (found the former Coordinator's E-Verify account)
  - sign-in as the Account Manager to open files in the Onboarding folder, with the Operations Manager present
  - sign-in attempts to the backup console and firewall management page without a second factor, with the MSP present
  - review of the payroll MFA setting and alert settings with the Operations Manager

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-07 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Tickets for laptop retirement, reassignment, and wiping (2024-2026) | MP-6 | Yes, 2026-08-07 (reassignment only; no retirement wipe records) |
| Suite account creation and removal tickets (2025-2026) | AC-2, PS-4 | Yes, 2026-08-07 |
| Technician list with access to the firm, and MFA on the remote management platform | SA-9, AC-17 | Not received by fieldwork end; follow-up in POAM-012 |
| Firewall and backup console administrator account list | IA-2(1) | Yes, 2026-08-10 (one shared MSP administrator account on each) |

## 3. Rules of engagement
- No testing that could disrupt Wednesday payroll entry or Friday pay. On-site tests ran on Tuesday 2026-08-11.
- No worker data left the office. Screenshots were redacted before they went into the evidence folder; the opened Form I-9 scan was closed without copying.
- The assessor would stop and tell the Operations Manager at once about any critical exposure. The active E-Verify account was reported and deactivated the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 15 |
| Other than satisfied | 66 |
| **Total** | **81** |

**Fully other than satisfied:** AC-3, IA-2(1), AT-2, AU-6, CP-4, IR-6, SA-9, SI-12. No process or technology met the objective.
**Largely satisfied:** RA-3 (6 of 8: the 2026 risk assessment meets every objective except the annual review and the change trigger, which have never been exercised) and CP-9 (3 of 6: backups run daily and are encrypted, but they are deletable and unproven).

**New findings from testing:**
1. The E-Verify account of the Coordinator who left on 2025-12-12 was still active (AC-02f.[04]; E-Verify MOU Art. II.A.3). The E-Verify user report showed no sign-in after 2025-12-10. Deactivated 2026-08-11 and added to the risk register as R-022 (closed); P03 row G-123 updated.
2. The former Coordinator was also still listed in the screening portal (AC-02f.[05]). Removed 2026-08-12.
3. The backup console and firewall management login accept a password alone, and each uses one MSP administrator account shared by its technicians (IA-02(01)). POAM-004.
4. A non-onboarding user (the Account Manager) could open Form I-9 scans with identity document images and consumer report PDFs (AC-03). POAM-002.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-002, POAM-004, POAM-006, POAM-007, and POAM-008: open access to onboarding records, phishable or missing MFA, no monitoring of payroll changes, and unproven backups. That is the same theme as P01: the payroll and onboarding records are reachable and nobody is watching them.

## 5. Deliverables
`assessment-results.csv` (81 rows), `poam.csv` (13 items), and this plan and summary. The Owner accepted the results on 2026-08-31.

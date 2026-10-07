# Security Assessment Plan and Summary: Cris Santos Company | Administrative and Support and Waste Management | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (temporary staffing firm) |
| System assessed | Associate Payroll and Applicant Tracking Platform (APATP), per the SSP (P02) |
| Tier / Vertical | Small / Administrative and Support and Waste Management and Remediation Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in operating or designing the controls. Escorted by the IT Manager |
| Assessment window | 2026-08-03 to 2026-08-07 (branch testing at Branch 3 on 2026-08-05) |
| Also supports | The inspection and quality assurance program for electronic Forms I-9 (8 CFR 274a.2(e)(1)(iii)); CSF 2.0 ID.IM-01 |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 156 determination statements.** Controls were chosen because they support the three High risks in P01, cover the I-9, E-Verify, FCRA, and Florida gaps in P03, or support the payroll and onboarding processes rated High in the BIA (P05).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-3, AC-5, AC-6 | Access to I-9 images, consumer reports, SSNs, and payroll (P03 G-057, G-121, G-126); R-002, R-005, R-006 | Focused | Focused |
| IA-2, IA-2(2), IA-5 | Payroll sign-in and E-Verify credentials (P03 G-055, G-129); R-001 (High) | Focused | Focused |
| AT-2 | Training gap (P03 G-059); R-001, R-016 | Basic | Focused |
| AU-6, AU-12, SI-4 | No monitoring; I-9 audit trail (P03 G-077, G-124); R-017 | Focused | Focused |
| CP-2, CP-4, CP-9 | Continuity and backups (P03 G-064, G-073, G-122); R-004 (High), R-019 | Focused | Focused |
| IR-4, IR-6 | No incident capability; Florida and E-Verify notice (P03 G-130, G-141, G-142) | Focused | Basic |
| MP-6, SI-12 | Disposal and retention (P03 G-038, G-139); R-012 | Basic | Focused |
| PT-5 | FCRA disclosure and AI notice (P03 G-136); R-010, R-013 | Basic | Focused |
| RA-5, SC-7 | Vulnerability management and kiosk network (P03 G-039, G-069, G-071); R-015 | Basic | Focused |
| SA-9 | Vendor oversight (P03 G-026, G-028); R-023 to R-025 | Focused | Focused |

## 2. Methods and objects
- **Examine:** identity provider, payroll platform, and E-Verify user lists; ATS role matrix; reporting database user list; storage and logging settings; snapshot reports; vendor contracts and the payroll vendor's SOC 2 report; training roster; the FCRA disclosure form and career site notice; shredding certificates and asset disposal records.
- **Interview:** COO, Controller, Payroll Manager, HR and Compliance Manager, Director of Recruiting, IT Manager, the managed IT provider's lead technician, 3 Onboarding and Compliance Specialists, and 8 randomly selected staff (incident reporting awareness).
- **Test:**
  - sign-in to the payroll platform to confirm the SMS code path and absence of SSO
  - a recruiter test account (created for the test, with COO approval) opening I-9 images and consumer reports and querying the reporting database
  - a read of a scanned I-9 in the archive, then a search for the log record
  - termination sample of 8 staff compared with account disable times in each system
  - E-Verify user list and case history compared with the HR roster and staff schedules
  - a kiosk network test at Branch 3 (reachability of staff devices)
  - an after-hours EDR test alert and its review time

## 3. Rules of engagement
- No test changed payroll data, bank accounts, or E-Verify cases. E-Verify was examined through its user and case reports only.
- No personal information left the firm. Screenshots were redacted to the last 4 digits.
- The recruiter test account was deleted at the end of fieldwork.
- The assessor stopped and notified the IT Manager on finding any critical exposure. One was found: the shared E-Verify credential (below), reported to the HR and Compliance Manager on 2026-08-05.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 38 |
| Other than satisfied | 118 |

**Fully other than satisfied:** AC-3, AC-5, AC-6, AU-6, CP-2, CP-4, IA-2(2), IR-4, IR-6, SI-12. No plan, process, or technology existed for these.
**Largely satisfied:** AC-2 account creation and approval (12 of 26 statements), IA-2 unique identification in SSO systems, CP-9 routine backups of user and system data, MP-6 paper disposal, and PT-5 applicant privacy notice basics.

**New finding:** an Onboarding Specialist at Branch 3 had been creating E-Verify cases with the user ID of a colleague who left in 2025; the password was written in a shared notebook (IA-05g.). This breaks E-Verify MOU Art. II.A.15 (safeguarding passwords) and makes those cases unattributable (IA-02[02]). It was not known before testing. It was added to the risk register as R-034 and to POAM-012 and POAM-013, and P03 row G-129 was updated. The departed users' accounts were deactivated on 2026-08-06; new named accounts, the E-Verify Tutorial for the specialist's own account, and staff attestations are due 2026-09-30.

All 22 controls with weaknesses have POA&M items in `poam.csv`. The High items are POAM-002, POAM-003, POAM-004, POAM-005, POAM-008, POAM-011, and POAM-019.

## 5. Deliverables
`assessment-results.csv` (156 rows), `poam.csv` (22 items), this plan and summary. The results were accepted by the COO on 2026-08-31.

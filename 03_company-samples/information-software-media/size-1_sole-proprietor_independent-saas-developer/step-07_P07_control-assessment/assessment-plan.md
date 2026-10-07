# Security Assessment Plan and Results Memo: Cris Santos Company | Information | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent B2B SaaS software publisher) |
| System assessed | Multi-tenant Booking Platform (MBP), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Information |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-developer (self-assessment), with the contract security consultant for one day of testing on 2026-08-27. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant ran the secret scan and the configuration review, witnessed the restore test, and challenged each self-review answer against what was on screen, but has no stake in the result and no standing access |
| Assessment window | 2026-08-24 to 2026-08-28 (tests on 2026-08-27) |
| Also supports | FTC Act Section 5 reasonable security (N51-R01): the FTC guidance expects a business to verify that its security works (P03 G-019, G-020). Also the SOC 2 monitoring criteria (P09, CC4.1) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 35 determination statements.** Controls were chosen because they support the Very High and High risks in P01 (R-001, R-002, R-006) or a High gap in P03 (G-007, G-014), or because a promise to subscribers depends on them.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-5(7) | Plaintext secrets (R-001; G-007) | Focused / laptop and all repositories |
| IA-2(1) | MFA on administrator accounts (R-002, R-012) | Basic / all 7 administrator accounts |
| AC-6(5) | Shared super-admin (R-003; G-005) | Basic / admin console |
| SC-28 | Encryption claim on the website (G-032) | Basic / database, storage, devices |
| CP-9 | Backups and the "backups every day" claim (R-007; G-033) | Focused / database and photos |
| CP-4 | Restore readiness against the 4-hour RTO (P05) | Focused / one restore test |
| SA-9 | Sub-processors and the 14-day notice promise (R-009; G-037) | Focused / all 6 service providers that receive subscriber data |
| AU-6 | Monitoring (G-014) | Basic |
| IR-6 | 48-hour and 72-hour notice promises (R-013; G-039) | Basic |
| RA-5 | Vulnerable libraries (R-005; G-023) | Basic |

## 2. Methods and objects
- **Examine:** account security pages, admin console user list, hosting backup, encryption, and network settings, photo storage settings, repository and CI secret settings, dependency alerts, vendor terms folder, sub-processor list, contractor agreement, the hosting provider's SOC 2 system description, P01 and P05.
- **Test (2026-08-27):** sign-ins from a new browser to each administrator account; the consultant's secret scan of the laptop and of every repository, including history; a point-in-time restore of the database to a scratch instance, timed and checked; encryption status on each device and storage service.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the consultant challenged each answer. The support contractor was interviewed on 2026-08-26 about how the admin console is used.

## 3. Rules of engagement
- Tests ran outside subscribers' business hours. No subscriber data was copied off the platform; the restore went to a scratch instance in the same account and was deleted the same day; screenshots were cropped to settings only.
- The consultant worked under a nondisclosure agreement, in sessions the owner started and watched, with no credentials of its own.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 14 |
| Other than satisfied | 21 |
| **Total** | **35** |

**Fully satisfied:** SC-28 (provider encryption at rest; laptop and phone encrypted).
**Fully other than satisfied:** IA-2(1), IA-5(7), AC-6(5), AU-6, IR-6.
**Partly satisfied:** CP-9 (database backups work; photos not backed up; all copies in one account), CP-4 (the first restore met the 4-hour RTO, but with no written steps), SA-9 (only customer responsibilities are documented), RA-5 (alerts on; no triage or scanning).

**New findings during testing:**
- The secret scan found an old hosting API token in the public demo repository's commit history (IA-05(07)). It had been revoked in 2025 and was not usable, but it shows how secrets were handled. The current token was not found in any repository.
- The domain registrar account signed in with a password only (IA-02(01)). It was not on the owner's list of administrator accounts.
- The restore took 2 hours 10 minutes, of which 40 minutes went to finding the right commands (CP-04a.[03]). It met the 4-hour RTO, with little margin.

The 9 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-009): 1 High, 7 Moderate, and 1 Low. The High item is POAM-001 (plaintext secrets), due 2026-10-31.

## 5. Deliverables
`assessment-results.csv` (35 rows), `poam.csv` (9 items), and this memo. Accepted by the owner-developer on 2026-09-25. Because independence is limited, POL-01 4.5 requires at least one day of outside challenge and testing in every yearly assessment.

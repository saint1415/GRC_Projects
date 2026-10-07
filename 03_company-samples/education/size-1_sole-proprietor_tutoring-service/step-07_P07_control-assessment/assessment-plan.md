# Security Assessment Plan and Results Memo: Cris Santos Company | Educational Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (tutoring and educational support service) |
| System assessed | Core Business SaaS Stack (CBSS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Educational Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-tutor (self-assessment), assisted by the on-call IT technician, who signed a confidentiality and data-handling agreement on 2026-07-08. **Independence is limited**: the owner designed, operates, and assessed these controls. The technician helped run the tests and read the settings but also supports the laptop and router |
| Assessment window | 2026-07-13 to 2026-07-17 (tests on 2026-07-16) |
| Also satisfies | The first test of safeguards required by 16 CFR 312.8(b)(4) (regularly test and monitor) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **9 controls, 42 determination statements.** Controls were chosen because they support the High risks in P01 (R-001 to R-004) or a High or Moderate COPPA gap in P03. For AC-2, 9 of its 26 determination statements were selected (the ones that apply to a one-person business with student portal accounts); every other control was assessed on all of its statements.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1), IA-2(2) | MFA on the accounts that hold children's information (R-002, R-003; G-028) | Basic / all 5 SaaS accounts |
| SC-28 | Laptop encryption (R-004; G-037) | Basic / laptop and phone |
| CP-9 | Backups that ransomware cannot reach (R-001) | Focused / student folders and the client-management SaaS |
| AC-2 | Portal members, collaborators, and the shared laptop account (R-003, R-008) | Basic / 9 selected statements |
| SA-9 | Vendor assurances (R-006; G-031, 312.8(c)) | Focused / all 6 vendors |
| SI-12 | Retention (R-007; G-032 to G-035, 312.10) | Basic |
| PT-5 | Children's privacy notice (R-005; G-011 to G-016, 312.4(d)) | Focused / website, portal, enrollment agreement |
| RA-3 | Risk assessment (312.8(b)(2)) | Basic |

## 2. Methods and objects
- **Examine:** account security pages and member lists in each SaaS, the email suite's sharing report and version history settings, the website and portal pages, the enrollment agreement, vendor terms, the client-management SaaS SOC 2 report, device encryption and lock settings, the old laptop, P01 and P05.
- **Test (2026-07-16):** sign-ins to every SaaS from a new browser; restore of one student folder from version history; encryption status on each device; a parent's-eye walk-through of the website and portal looking for a privacy notice; review of the portal's collaborator and member lists.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- Tests on a weekday with no sessions. No student data copied off the devices; screenshots were cropped to settings only. Portal tests used a test member account created for the day and deleted afterward.
- The IT technician worked only in sessions the owner started and watched, under the signed agreement.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 13 |
| Other than satisfied | 29 |
| **Total** | **42** |

**Partly satisfied:** RA-3 (the assessment exists; no review cycle at the time), CP-9 (vendor backups inherited; student folders have no backup that sync cannot overwrite), AC-2 (the owner manages accounts and creates them only after consent, but stale accounts were never closed), SA-9 (only the client-management SaaS vendor is overseen).
**Fully other than satisfied:** IA-2(1), IA-2(2), SC-28, SI-12, PT-5.

**New finding:** the website builder still listed the former web designer as a collaborator with edit rights over the site and the portal (AC-02d.01, AC-02f.[05]). The owner removed the account during the test on 2026-07-16. The builder's activity history showed no sign-in by that account in the last 90 days, which is as far back as it goes. P01 R-003 and POAM-006 track the remaining steps.

The 9 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-009): 5 High, 3 Moderate, 1 Low. The High items (POAM-001 to POAM-004) are due 2026-08-14, before the fall term; POAM-005 is due 2026-09-30, with the AI assistant stopped by 2026-08-14.

## 5. Deliverables
`assessment-results.csv` (42 rows), `poam.csv` (9 items), and this memo. Accepted by the owner-tutor on 2026-07-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

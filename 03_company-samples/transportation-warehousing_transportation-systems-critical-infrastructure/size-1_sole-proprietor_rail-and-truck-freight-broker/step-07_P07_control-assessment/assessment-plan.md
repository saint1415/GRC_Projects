# Security Assessment Plan and Results Memo: Cris Santos Company | Transportation Systems | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight broker arranging truck and rail shipments) |
| System assessed | Freight Brokerage SaaS Stack (FBSS), per the system security plan (P02) |
| Tier / Vertical | Sole Proprietorship / Transportation Systems |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner (self-assessment), assisted by the on-call IT consultant. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant helped run the tests and read the settings, but also set up the email suite in 2021, including the account this assessment found |
| Assessment window | 2026-08-10 to 2026-08-14 (tests on 2026-08-13) |
| Also supports | Evidence for the largest shipper's security questionnaire (P09) and the reasonable-measures duty in Fla. Stat. 501.171(2) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **8 controls, 35 determination statements.** Controls were chosen because they support the High risks in P01 (R-001 to R-004) or a P03 gap rated Moderate or higher.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1), IA-2(2) | MFA on email, TMS, accounting, and load board (R-003, R-005; Fla. Stat. 501.171(2)) | Basic / every SaaS account |
| AC-2 | Accounts, including contractor and shared accounts (R-007, R-014) | Focused / tailored to the 10 statements on authorized users, removal, review, and shared credentials. Statements on account types, groups, and personnel transfer do not fit a one-person business |
| AC-3 | File sharing of carrier packets (R-008) | Basic / file suite |
| CP-9 | Independent copies and the TMS recovery point (R-001, R-010; 49 CFR 371.3(b)) | Basic / TMS and files |
| SA-9 | Vendor oversight, including the AI feature (R-012; Fla. Stat. 501.171(6)) | Focused / all 9 outside services |
| IR-6 | Incident reporting and notice contacts (R-013; shipper 72-hour notice) | Basic |
| RA-3 | Risk assessment (P01) | Basic |

Payment change verification and carrier identity checks (R-002, R-004) are procedures, not system settings. They were walked through in the self-review and become test items in the 2027 assessment, once POL-01 6.2 and 6.3 have been in use for a year.

## 2. Methods and objects
- **Examine:** user and administrator lists and security pages in each SaaS service, the file sharing report from P04, vendor terms, the TMS vendor's service terms, railroad portal user IDs, P01 and P05.
- **Test (2026-08-13):** sign-ins to the email suite, TMS, accounting SaaS, and load board from a new browser; sign-in attempt with each administrator account listed in the email admin console; creation of a test file share to see the default setting.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT consultant challenged each answer against what was on screen.

## 3. Rules of engagement
- No testing while loads were in transit without a phone at hand; tests ran after 6 p.m.
- No carrier or shipper data copied off the services; screenshots were cropped to settings only.
- The IT consultant worked only in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 12 |
| Other than satisfied | 23 |
| **Total** | **35** |

**Fully other than satisfied:** IA-2(1), IA-2(2), IR-6, AC-3.
**Partly satisfied:** RA-3 (6 of 8: the assessment exists; no review cycle yet), CP-9 (3 of 6: the TMS vendor's system backups are sound; the business's own copies are missing), AC-2 (2 of 10: roles are right; accounts are never reviewed and one is shared), and SA-9 (1 of 6: only roles are defined).
No control was fully satisfied.

**New finding:** an IT consultant super administrator account on the email suite, created in 2021 and unused since 2022-02, still signed in with a password only (IA-02(01)). Anyone who guessed or found that password could have taken over every mailbox and file. The owner disabled it during the test on 2026-08-13. It went back into the risk register as R-014 and is tracked in POAM-001 and POAM-005. The open sharing default found in P04 was confirmed by test (AC-03).

The 8 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-008). The High items are POAM-001 (administrator MFA) and POAM-002 (MFA on the TMS, accounting, and load board), both due 2026-09-30.

## 5. Deliverables
`assessment-results.csv` (35 rows), `poam.csv` (8 items), and this memo. Accepted by the owner on 2026-09-08. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

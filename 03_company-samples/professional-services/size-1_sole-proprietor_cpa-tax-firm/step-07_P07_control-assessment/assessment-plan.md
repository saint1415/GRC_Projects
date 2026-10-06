# Security Assessment Plan and Results Memo: Cris Santos Company | Professional Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (CPA and tax preparation practice) |
| System assessed | Tax Practice Systems Profile (TPSP), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Professional, Scientific, and Technical Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The CPA-owner (self-assessment), assisted by the on-call IT consultant after the consultant signed a services agreement and the IRC 7216 notice on 2026-07-23. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant ran the tests with the owner and read the settings, but also supports the laptop and router |
| Assessment window | 2026-07-27 to 2026-07-31 (tests on 2026-07-29) |
| Also satisfies | Testing of key controls under 16 CFR 314.4(d)(1) (N54-R01) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 44 determination statements.** Controls were chosen because they support the High risk R-001 in P01 (email takeover), a High or Moderate Safeguards Rule gap in P03, or a customer control the tax software vendor's SOC 2 report depends on.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1), IA-2(2) | MFA on the tax software, mailbox, practice management, and portal (R-001; 314.4(c)(5)) | Basic / every account |
| AC-2 | Account management in the tax software; vendor's customer control (R-005; 314.4(c)(1)(i)) | Focused / 8 of 26 objectives that fit a one-person firm |
| SC-8 | Transmission of returns and documents (R-004; 314.4(c)(3)) | Basic / email, text, portal |
| CP-9 | Backups (R-012; 314.3(b)(2)) | Basic / tax software and suite |
| SA-9 | Service providers and the AI vendor (R-006, R-008; 314.4(f)) | Focused / all providers |
| AU-6 | Activity review (R-001; 314.4(c)(8)) | Basic |
| SI-3 | Malware defense on the only workstation (R-003) | Focused / laptop |
| IR-6 | Incident reporting (R-013; 314.4(j); Pub. 1345) | Basic |
| RA-3 | Risk assessment (314.4(b)) | Basic |

## 2. Methods and objects
- **Examine:** account security pages, the tax software user list and activity log, the email suite's sign-in history and mailbox rules, device encryption and antivirus status, the email sent folder and phone camera roll (counts only), the contracts folder, the tax software vendor's SOC 2 report, P01 and P05.
- **Test (2026-07-29):** sign-ins from a new browser to the tax software, mailbox, and practice management; the portal's client MFA setting; download of a standard antivirus test file; a check of the mailbox for forwarding rules, delegates, and connected apps; review of the remote-support tool's settings.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT consultant challenged each answer against what was on screen.

## 3. Rules of engagement
- No testing on client deadline days. No client data copied off the systems; screenshots were cropped to settings, and the sent folder and camera roll were counted, not opened.
- The IT consultant worked only under the 2026-07-23 agreement and notice, in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 21 |
| Other than satisfied | 23 |
| **Total** | **44** |

**Fully satisfied:** SI-3 (the built-in antivirus detected and quarantined the test file).
**Fully other than satisfied:** IA-2(1), IA-2(2), SC-8, AU-6, IR-6.
**Partly satisfied:** RA-3 (the assessment exists; no review cycle yet), CP-9 (tax software backups inherited; the suite and laptop are not backed up), SA-9 (only the tax software vendor is overseen), AC-2 (roles and authorizations are right; nothing else in the account lifecycle exists).

**New finding:** the 2025 contract preparer's tax software account was still enabled, 15 months after the engagement ended (AC-02f.[04]). The vendor's audit log shows no sign-in after 2025-04-14. The owner disabled it during the test on 2026-07-29. It went back into the risk register as R-005, because an unused account with access to every client return and the firm's EFIN is exactly what the vendor's SOC 2 report expects its customers to prevent. The mailbox check found no unknown forwarding rules, but only 30 days of sign-in history exist, so the March 2026 phishing near miss could not be checked.

The 9 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-009). Four more items carry High and Moderate gaps from P03 and P01 that no tested control covered: the AI assistant and IRC 7216 (POAM-010), training and the call-back rule (POAM-011), the single-person dependency (POAM-012), and retention (POAM-013). **13 items in total: 2 High, 10 Moderate, 1 Low.** The High items are POAM-001 (mailbox MFA, due 2026-09-15) and POAM-012 (continuation and recovery codes, due 2026-12-31).

## 5. Deliverables
`assessment-results.csv` (44 rows), `poam.csv` (13 items), and this memo. Accepted by the CPA-owner on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

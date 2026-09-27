# Security Assessment Plan and Results Memo: Cris Santos Company | Finance and Insurance | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (state-registered investment adviser) |
| System assessed | Advisory Practice Systems Profile (APSP), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Finance and Insurance |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-adviser (self-assessment), assisted by the on-call IT consultant under the services agreement signed 2026-07-10. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant ran the tests and read the settings but also supports the laptop |
| Assessment window | 2026-07-13 to 2026-07-17 (tests on 2026-07-15) |
| Also satisfies | FTC Safeguards Rule duty to regularly test or monitor key controls, 16 CFR 314.4(d)(1) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **9 controls, 33 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-003) or a High or Moderate gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1) | MFA on administrator accounts (R-002, R-003; 314.4(c)(5)) | Basic / all 5 administrator accounts |
| IA-2(2) | MFA on the custodian portal, which can move money (R-001) | Basic / both user accounts |
| AT-2(3) | Recognizing and reporting business email compromise (R-001; 314.3(b)(3)) | Focused / the 2026-06-18 near miss |
| SC-28(1) | Encryption of devices and the USB backup (R-004; 314.4(c)(3)) | Basic / laptop, phone, USB drive |
| CP-9 | Backups and records (R-008, R-011; Fla. Stat. 517.121) | Basic / email, files, USB copy |
| SA-9 | Service providers and the AI assistant (R-006, R-007; 314.4(f)) | Focused / all 10 vendors |
| AU-6 | Log and mailbox rule review (R-002; 314.4(c)(8)) | Basic |
| IR-6 | Incident reporting (R-010; Fla. Stat. 501.171(4)) | Basic |
| RA-3 | Risk assessment (314.4(b)) | Basic |

## 2. Methods and objects
- **Examine:** account security pages, mailbox rules and sign-in history, device and drive encryption status, the vendor contracts folder, the portfolio platform's SOC 2 report, the AI assistant's terms, training records, the near-miss email thread, P01 and P05.
- **Test (2026-07-15):** sign-ins from a new browser to all seven SaaS services; encryption status on each device and the USB drive; restore of 3 files from the USB drive; a search of mailbox rules and connected apps.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT consultant challenged each answer against what was on screen.

## 3. Rules of engagement
- No testing during market hours. No client data copied off the devices; screenshots were cropped to settings only.
- The IT consultant worked only in sessions the owner started and watched, under the 2026-07-10 services agreement.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 10 |
| Other than satisfied | 23 |
| **Total** | **33** |

**Fully satisfied:** IA-2(2) (the custodian portal and the financial planning software enforce MFA).
**Fully other than satisfied:** IA-2(1), SC-28(1), AU-6, AT-2(3), IR-6.
**Partly satisfied:** RA-3 (the assessment exists; no review cycle yet), CP-9 (vendor and custodian backups work; the owner's own backup does not meet the RPO), SA-9 (roles are defined; vendors are not overseen).

**New finding:** the email mailbox had a forwarding rule the owner did not recognize, sending messages containing "wire" to an outside address (AU-06a.). It was deleted during the session on 2026-07-15. The 30 days of sign-in history showed nothing unusual, so a past compromise could not be confirmed or ruled out. The owner logged it as a suspected incident and asked counsel whether any notice is needed (P08 section 7). This finding is also why R-002 has a Very High likelihood of adverse impact.

The 8 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-008). The High items are POAM-001 (MFA, due 2026-09-15) and POAM-002 (callback rule and training, due 2026-11-30, with the callback rule in use by 2026-09-30).

## 5. Deliverables
`assessment-results.csv` (33 rows), `poam.csv` (8 items), and this memo. Accepted by the owner-adviser on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

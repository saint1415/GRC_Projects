# Security Assessment Plan and Results Memo: Cris Santos Company | Financial Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent insurance agency) |
| System assessed | Agency Systems Profile (ASP), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Financial Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-agent (self-assessment), assisted by the on-call IT consultant under the services agreement signed 2026-07-27. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant ran the tests and read the settings but also supports the laptop and router |
| Assessment window | 2026-08-03 to 2026-08-07 (tests on 2026-08-05) |
| Also supports | The 16 CFR 314.4(d)(1) benchmark (test key safeguards) and the lead insurer's questionnaire |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **9 controls, 41 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-005) or a High or Moderate gap in P03.

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| IA-2(2) | MFA on every portal (R-001, R-006; G-029; Carrier DSA) | Basic | Every account in SYS-01 to SYS-05 |
| IA-2 | Unique identity on the premium trust account (R-005; G-015) | Focused | Online banking |
| IA-5 | Password and code handling (R-006, R-007; G-024) | Basic | Browser store, router, recovery settings |
| AU-6 | Mailbox and sign-in review (R-001; G-033) | Focused | Email and AMS |
| SC-8 | Document exchange with clients (R-003; G-027) | Basic | 30 days of email; phone messages |
| SA-9 | Vendors with client data (R-004, R-005; G-012, G-040, G-041) | Focused | All vendors in SYS-01 to SYS-08 plus the bookkeeper |
| CP-9 | Backups and records (R-013, R-014; G-017) | Basic | AMS, email, files |
| MP-6 | Disposal (R-012; G-014) | Basic | Retired laptop, printer-scanner, phone |
| RA-3 | Risk assessment (G-021 to G-023) | Basic | P01 |

## 2. Methods and objects
- **Examine:** account security pages for the AMS, email, insurer portals, rater, and bank; bank user settings; mailbox rules and forwarding settings; the browser password store (count only); router admin page; email retention settings; the contracts folder; the AMS SOC 2 report; P01 and P05.
- **Test (2026-08-05):** sign-ins from a new browser to every portal; a count of saved and reused passwords; a 30-day sample of sent and received email for attachments with Restricted data; a review of phone messages for ID photos; a boot of the retired laptop; the printer-scanner's stored-jobs menu.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT consultant challenged each answer against what was on screen. The bookkeeper was interviewed by phone about banking access.

## 3. Rules of engagement
- No testing during client appointments. No client data copied off any device; screenshots were cropped to settings, and the email sample was reviewed on screen without export.
- The IT consultant worked only under the 2026-07-27 agreement, in sessions the owner started and watched.
- No sign-in attempts against insurer or bank systems beyond the owner's own accounts.

## 4. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-08-03 | Plan agreed; examine documents |
| 2026-08-05 | Tests |
| 2026-08-07 | Findings written; POA&M drafted |
| 2026-09-14 | Accepted by the owner-agent |

Deliverables: `assessment-results.csv` (41 rows), `poam.csv` (9 items), and this memo.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 15 |
| Other than satisfied | 26 |
| **Total** | **41** |

**Fully other than satisfied:** IA-2(2), IA-2, AU-6, SC-8.
**Partly satisfied:** RA-3 (the assessment exists; no review cycle), IA-5 (devices protect stored credentials, but passwords are reused and the bank credential is shared), SA-9 (only the AMS vendor is overseen), CP-9 (AMS backups inherited; email and files unprotected beyond 30 days), MP-6 (one safe reuse; two devices awaiting disposal hold client data).
**No control was fully satisfied.**

**New findings from testing:** the retired laptop booted straight to the owner's old account with client files present (MP-06a.[01]); 9 client driver license photos were still in the phone's messages (SC-08); the browser held 23 saved agency passwords, 6 reused (IA-05c.). The printer-scanner is leased and goes back to the dealer on 2026-11-30, so POAM-008 is due before then.

Each of the 9 controls has one POA&M item in `poam.csv` (POAM-001 to POAM-009). The High items are POAM-001 (MFA), POAM-002 (shared banking identity), and POAM-003 (mailbox monitoring). Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

# Security Assessment Plan and Results Memo: Cris Santos Company | Emergency Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (unarmed private security patrol, licensed Class "B" agency) |
| System assessed | Patrol Business SaaS Stack (PBS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Emergency Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner (self-assessment), assisted by the on-call IT technician after the technician signed a confidentiality agreement on 2026-08-07. **Independence is limited**: the owner designed, operates, and assessed these controls. The technician helped run the tests and read the settings, but also supports the laptop and router |
| Assessment window | 2026-08-10 to 2026-08-14 (tests on 2026-08-12) |
| Also supports | Evidence of "reasonable measures" under Fla. Stat. 501.171(2); answers to client security questionnaires (P09) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 46 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-003), a High gap in P03 (G-009, G-019, G-031, G-033), or a duty with a deadline (client notice clauses).

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1) | MFA on the account that can read every client's codes (R-002) | Basic / patrol app admin, email, accounting |
| IA-5 | Reused and default passwords (R-002) | Focused / 6 of 10 statements |
| PE-3 | Client keys, cards, and codes (R-003, R-004; 493.6118(1)(e)) | Focused / 7 statements on access devices; facility statements not applicable to a home office |
| SC-28 | Code spreadsheet and camera card (R-003, R-006) | Basic / all storage locations |
| CP-9 | Backups (R-001; 493.6121(2) records) | Basic / patrol app and owner data |
| AC-2 | Client portal accounts (R-009) | Focused / 6 of 27 statements |
| AU-6 | Sign-in review (R-002, R-010) | Basic |
| SA-9 | Vendors, AI provider, backup agency (R-007, R-008) | Focused / all vendors |
| IR-6 | Client and breach notice (R-011; contract 2-hour clause) | Basic |
| SI-3 | Ransomware defense on the laptop (R-001) | Focused / laptop |

## 2. Methods and objects
- **Examine:** patrol app user list, security settings, AI settings, and audit screen; email and accounting security pages; device encryption and lock settings; the code spreadsheet, phone note, and text threads; the body-camera card and sharing links; the router admin page; the key ring, key log, and vehicle; the 7 client agreements; the patrol app vendor's SOC 2 report.
- **Test (2026-08-12):** sign-ins to the patrol app, email, and accounting SaaS from a new browser; password manager breach check on saved passwords; router admin sign-in with the label password; count of keys and cards against the key log; download of a standard antivirus test file.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- No testing during patrol hours. No client codes or personal information copied off the devices; screenshots were cropped to settings only, and the code spreadsheet was reviewed on screen by the owner alone.
- The IT technician worked only under the confidentiality agreement signed 2026-08-07, in sessions the owner started and watched. The technician did not see codes or keys.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 19 |
| Other than satisfied | 27 |
| **Total** | **46** |

**Fully satisfied:** SI-3 (the built-in antivirus detected and quarantined the test file).
**Fully other than satisfied:** IA-2(1), SC-28, AU-6, IR-6.
**Partly satisfied:** IA-5 (owner protects the MFA phone; reused and default passwords), PE-3 (key log kept and rekeying covered by contract; keys, cards, and codes poorly secured), CP-9 (patrol app backups inherited; owner data not backed up), AC-2 (accounts named and site-limited; 3 stale and never reviewed), SA-9 (vendor SOC 2 shows strong controls; no vendor list or oversight).

**New findings from testing:** the router admin page accepted the default password from its label (IA-05e., changed the same day); the patrol app admin password was found in a public breach list (IA-05c., changed the same day); a browser extension with permission to read all sites, installed by a family member on the shared laptop account, was removed; and one access fob in the ring had no key log entry (PE-03f.; the client confirmed it was issued in 2025 and the log was corrected).

The 9 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-009). The High items are POAM-001 (MFA, due 2026-09-15), POAM-002 (keys and codes, due 2026-10-31), and POAM-003 (data at rest, due 2026-09-30).

## 5. Deliverables
`assessment-results.csv` (46 rows), `poam.csv` (9 items), and this memo. Accepted by the owner on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

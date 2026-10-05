# Security Assessment Plan and Results Memo: Cris Santos Company | Utilities | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent utility engineering consultant) |
| System assessed | Core Business Systems (CBS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Utilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-engineer (self-assessment), assisted by the on-call IT technician, who signed an NDA on 2026-07-17. **Independence is limited**: the owner designed, operates, and assessed these controls. The technician ran the tests and read the settings but also supports the laptop |
| Assessment window | 2026-07-20 to 2026-07-24 (SaaS mapping 2026-07-22; tests 2026-07-23) |
| Also supports | Client A's annual security questionnaire and the evidence behind P03 (SSA-A and VAA-B rows) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 30 determination statements.** Each control backs a High or Moderate risk in P01 or a client term with a gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-5 | Saved and reused passwords, SMS codes (R-001, R-003; G-023) | Focused / every business and client account |
| AC-6 | Administrator account on the laptop that connects to Client B relays (R-002; VAA-B (1)) | Basic / laptop |
| IA-2(1), IA-2(2) | MFA on the suite, accounting SaaS, and client accounts (R-001, R-008; SSA-A (8)) | Basic / all accounts |
| AC-3 | File shares that exposed Client A BCSI (R-004; G-007, G-010) | Focused / every share in the suite |
| SC-28 | Encryption of BCSI and CEII at rest (R-006; SSA-A (8); CEII NDA) | Basic / laptop, phone, CEII archive |
| SI-3 | Malware defense on the laptop that becomes a Transient Cyber Asset (R-002; VAA-B (1)) | Basic / laptop |
| MP-7 | USB drives carrying settings files (R-007; VAA-B (2)) | Basic / all 3 drives |
| AU-6 | Sign-in and sharing review (R-001; SSA-A (5)) | Basic / suite logs |
| IR-6 | 24-hour client notices (R-013; SSA-A (5), VAA-B (5)) | Basic |

## 2. Methods and objects
- **Examine:** suite admin console, sharing report, and activity log; accounting SaaS security page; laptop account, encryption, and antivirus settings; phone settings; browser password store; router admin page; USB drive contents; Client B checklists and session approvals; Client A notices; P01, P03, P05.
- **Test (2026-07-23):** sign-ins to the suite, accounting SaaS, and Client A portal from a new browser; access to every client folder from an outside test account; a standard antivirus test file; encryption status on each device.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- **No connection to any client system** during the assessment. The Client B gateway was not used; its MFA was examined from Client B's 2026 session approvals. The Client A portal test was a sign-in to the owner's own account only.
- The IT technician never opened client folders or the CEII archive. Screenshots were cropped to settings only.
- Any exposure found was fixed the same day and logged, and the client was told within 24 hours (the drafter share on 2026-07-21, reported 2026-07-22; the Client B link share on 2026-07-23, reported the same day).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 15 |
| Other than satisfied | 15 |
| **Total** | **30** |

**Fully satisfied:** IA-2(2) (every in-boundary account holding client information asks for a second factor), SC-28 (laptop, phone, and CEII archive encrypted), and SI-3 (the test file was detected and quarantined).
**Fully other than satisfied:** AC-3, AC-6, IA-2(1), AU-6, and IR-6.
**Partly satisfied:** IA-5 (4 of 10 statements satisfied; strength of SMS, saved passwords, and the default router password failed) and MP-7 (1 of 2).

**What the test changed on the day:** the open "anyone with the link" share on a Client B settings folder was turned off during the AC-3 test on 2026-07-23 and reported to Client B. The browser-saved Client B gateway password (IA-05g.) is the finding that most directly touches a client's OT network, because it would let a laptop thief or malware start the MFA push in P08.

The 7 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-007). The High items are POAM-001 (authenticators) and POAM-002 (least privilege and the dedicated field laptop).

## 5. Deliverables
`assessment-results.csv` (30 rows), `poam.csv` (7 items), and this memo. Accepted by the owner-engineer on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside review at least every second year; Client A's security reviewer is the most likely candidate.

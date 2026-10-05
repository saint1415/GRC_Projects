# Security Assessment Plan and Results Memo: Cris Santos Company | Energy | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (pipeline integrity engineering consultant) |
| System assessed | Core Business SaaS Stack (CBSS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Energy |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The engineer-owner (self-assessment), assisted by the on-call IT support contractor under an NDA signed 2026-08-07. **Independence is limited**: the owner designed, operates, and assessed these controls. The contractor ran the tests with the owner and challenged the answers but has no other role in the business |
| Assessment window | 2026-08-10 to 2026-08-14 (tests and walkthrough on 2026-08-13) |
| Also supports | Client A supplier questionnaire (addendum s.11); evidence for the 49 CFR Part 1520 rows in P03 |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 43 determination statements.** Controls were chosen because they support a High risk in P01 (R-001, R-003, R-004, R-005), an SSI duty in 49 CFR 1520.9, or a Client A addendum term with a gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| MP-4 | Secure storage of SSI and media (R-003, R-004; 1520.9(a)(1)) | Focused / all media and paper SSI |
| MP-3 | SSI marking (1520.9(a)(4), 1520.9(b), 1520.13) | Focused / both SSI records and derived drafts |
| SC-28 | Encryption at rest (R-004; addendum s.3) | Basic / laptop, phone, USB drive |
| IA-2(1) | MFA on administrator accounts (R-005; 501.171(2)) | Basic / suite and accounting SaaS |
| CP-9 | Backups (R-001; addendum s.13) | Basic / suite and local files |
| SI-3 | Ransomware defense on the laptop (R-001) | Focused / laptop |
| SA-9 | Services and subcontractors (R-006, R-007; addendum s.4 and s.5) | Focused / all services and both subcontractors |
| SI-12 | Retention and destruction (R-009; addendum s.7; 1520.19(b)) | Basic |
| IR-6 | Incident reporting (R-008; addendum s.6; 1520.9(c)) | Basic |
| RA-3 | Risk assessment (addendum s.11) | Basic |

IA-2(2) was left out to stay within 10 controls. Its gap (AI trial account and license portal without MFA) is recorded in P02 and P03 G-016 and tracked as POAM-002.

## 2. Methods and objects
- **Examine:** suite sharing settings and the 180-day activity log, account security pages, device encryption status, the SSI folder and printout, the USB drive, the fire safe and desk, the AI tool terms, subcontractor NDAs, the suite provider's SOC 2 report, the Client A addendum, P01 and P05.
- **Test (2026-08-13):** sign-ins to the suite and accounting SaaS from a new browser; mounting the USB drive on a second computer; restoring a deleted test file from suite version history; downloading a standard antivirus test file; listing who could reach the Client A folder.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT support contractor challenged each answer against what was on screen.

## 3. Rules of engagement
- The IT support contractor never opened or viewed the SSI records. The owner checked SSI markings and storage alone; the contractor saw only folder names and permission settings.
- No client data was copied off the laptop. Screenshots were cropped to settings only. The USB drive test used a file listing, not file contents.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 19 |
| Other than satisfied | 24 |
| **Total** | **43** |

**Fully satisfied:** SI-3 (built-in antivirus detected and quarantined the test file).
**Fully other than satisfied:** MP-4, SC-28, IA-2(1), IR-6.
**Partly satisfied:** RA-3 (assessment exists; no review cycle yet), MP-3 (original marked; drawing and draft not), CP-9 (provider backup works; local backup weak), SA-9 (only the suite provider is overseen), SI-12 (deliverables handled well; old source data kept).

**New findings during testing:**
- The GIS subcontractor's folder share reached the SSI files (MP-4, SA-9). The owner removed it on 2026-08-13. The 180-day activity log shows the folder listing was opened but neither SSI file was opened or downloaded. Client A was told on 2026-08-14 and agreed no release to an unauthorized person was shown, so no TSA report under 1520.9(c) was triggered. P01 R-003 and POAM-004 track the remaining steps.
- The USB backup drive opened on a second computer with no password (SC-28). It holds client data from 4 projects and a copy of the SSI plan excerpt (POAM-003).

Each of the 9 controls with weaknesses has one POA&M item in `poam.csv`, plus POAM-002 for the IA-2(2) gap found in P02 and P03, for 10 items (POAM-001 to POAM-010). The High items are POAM-001 (accounting MFA) and POAM-003 (backup drive encryption), due 2026-09-15, and POAM-004 (SSI storage), due 2026-09-30.

## 5. Deliverables
`assessment-results.csv` (43 rows), `poam.csv` (10 items), and this memo. Accepted by the engineer-owner on 2026-09-11. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

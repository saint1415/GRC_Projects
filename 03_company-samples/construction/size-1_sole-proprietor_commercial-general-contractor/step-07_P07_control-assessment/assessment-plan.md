# Security Assessment Plan and Results Memo: Cris Santos Company | Construction | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (commercial and institutional building general contractor) |
| System assessed | Project Management and Payment Application System (PMPAS), per the system security plan (P02) |
| Tier / Vertical | Sole Proprietorship / Construction |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner (self-assessment), assisted by the on-call IT technician. **Independence is limited**: the owner designed, runs, and assessed these controls. The technician ran the tests with the owner and read the settings, but also set up the laptop and router |
| Assessment window | 2026-07-20 to 2026-07-22 (tests on 2026-07-21) |
| Relation to CMMC | This is a security control assessment against SP 800-53A. It is **not** the CMMC Level 1 self-assessment, which must use the NIST SP 800-171A (June 2018) objectives and is scheduled for November 2026 (P03 G-021) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 41 determination statements.** Controls were chosen because they carry the top risks in P01 (R-001, R-002, R-006, R-009) or a FAR 52.204-21 or 52.204-25 gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1), IA-2(2) | MFA on the payment path (R-001; 52.204-21(b)(1)(vi)) | Basic / all SaaS accounts |
| IA-5 | Shared and default passwords (R-004, R-006; 52.204-21(b)(1)(vi)) | Focused / all accounts and the router |
| AC-20 | FCI on external systems (R-009; 52.204-21(b)(1)(iii)) | Basic / AI tool, photo cloud, bookkeeper |
| SC-7 | Home network boundary (R-006; 52.204-21(b)(1)(x)-(xi)) | Focused / router and connected devices |
| SC-28 | Device encryption (R-011) | Basic / laptop and phone |
| SI-3 | Malicious code (52.204-21(b)(1)(xiii)-(xv)) | Focused / laptop |
| CP-9 | Backups (R-012) | Basic / SaaS and local data |
| IR-6 | Incident reporting (R-014; 52.204-25(d)) | Basic |
| SR-5 | Section 889 purchase check (R-007; 52.204-25(b)) | Basic |

## 2. Methods and objects
- **Examine:** SaaS security and user settings, router administration pages, device encryption and antivirus status, the AI tool's upload history and terms, the bookkeeper engagement letter, the subcontract form, the Section 889 inquiry notes, and the project management vendor's SOC 2 report.
- **Test (2026-07-21):** sign-ins to SYS-01, SYS-02, and SYS-03 from a new browser; download of a standard antivirus test file; encryption status on each device; sign-in to the router with the manufacturer's default password; an external check of whether the router's remote administration port answered from the internet.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- No test touched the bank portal or a live payment.
- No client or federal documents were copied off the systems; screenshots were cropped to settings only.
- The IT technician worked under the written engagement signed 2026-07-13, in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 19 |
| Other than satisfied | 22 |
| **Total** | **41** |

**Fully satisfied:** SC-28 (laptop encryption verified) and SI-3 (the test file was detected and quarantined).
**Fully other than satisfied:** IA-2(1), IA-2(2), AC-20, IR-6.
**Partly satisfied:** IA-5 (3 of 10), SC-7 (1 of 6), CP-9 (4 of 6), SR-5 (2 of 3).

**New finding:** the home router accepted the manufacturer's **default administrator password**, and its remote administration page answered from the internet (IA-05e., SC-07a.[02]). Anyone who found it could have changed the router's settings and sent the owner's traffic to look-alike sign-in pages. The owner changed the password and turned off remote administration during the test on 2026-07-21. This went back into the risk register as R-006 and the P03 gap G-006, and POAM-003 and POAM-005 track the remaining steps (firmware, a separate work network).

The 8 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-008). The High items are POAM-001 (MFA on SYS-01 and SYS-02, due 2026-10-31) and POAM-003 (passwords, due 2026-09-30).

**CMMC reading.** These results confirm the P03 headline: FAR 52.204-21(b)(1)(iii), (vi), and (x) are not met today. Under CMMC Level 1 a POA&M does not count; every one of these must be fixed, not planned, before the November self-assessment.

## 5. Deliverables
`assessment-results.csv` (41 rows), `poam.csv` (8 items), and this memo. Accepted by the owner on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reader before each CMMC self-assessment.

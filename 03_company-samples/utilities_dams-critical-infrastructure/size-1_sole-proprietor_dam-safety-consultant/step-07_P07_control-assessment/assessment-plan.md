# Security Assessment Plan and Results Memo: Cris Santos Company | Dams | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent dam safety engineering consultant) |
| System assessed | Core Business SaaS Stack (CBSS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Dams |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-engineer (self-assessment), assisted by the on-call IT technician under the NDA signed 2026-07-14. **Independence is limited**: the owner designed, operates, and assessed these controls. The technician helped run the tests and read the settings but also supports the laptop. No client staff took part |
| Assessment window | 2026-07-20 to 2026-07-24 (home office walkthrough 2026-07-21; tests 2026-07-23) |
| Also supports | The evidence Client A may ask for under CSCA-A, and the CEII "secure place" duty (18 CFR 388.113(h)(2)) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 37 determination statements.** Controls were chosen because they support the High risks in P01 (R-001 gateway credentials, R-005 unencrypted backup), a High or Moderate gap in P03, or a client term the owner must be able to prove.

| Control | Why selected | Depth / coverage |
|---|---|---|
| AC-17 | Client A gateway path (R-001; CSCA-A (3); P03 G-010) | Focused / all 3 sessions in 2026 |
| AC-6(2) | Administrator account for daily work (R-001, R-013) | Basic / laptop |
| IA-2(2) | MFA on the accounting SaaS and Client B platform (R-003; GRS-B (2)) | Basic / all accounts without MFA |
| SC-28 | Encryption of devices, CEII container, and backup drive (R-005; 388.113(h)(2)) | Basic / 5 objects |
| CP-9 | Backups and the first restore test (R-006; 12.35(a)) | Focused / laptop and backup drive |
| MP-4 | Storage of the backup drive and paper (R-005, R-010) | Basic / home office |
| IR-6 | 24-hour client notices and the FERC CEII report (R-009) | Basic |
| SA-9 | Vendors and helpers holding client data (R-004, R-007, R-011) | Focused / all vendors and the field assistant |
| AU-6 | Own record of gateway sessions and sign-ins (CSCA-A (4)) | Basic |
| SI-3 | Malware defense on the laptop that reaches Client A (R-001) | Focused / laptop |

## 2. Methods and objects
- **Examine:** CSCA-A and GRS-B, Client A's gateway enablement emails and session list, laptop accounts and browser password store, account security pages, device and drive encryption status, suite sync and sharing settings, the AI tool account and terms, phone photo cloud settings, the suite provider's SOC 2 report, the home office and locked cabinet.
- **Test (2026-07-23):** sign-ins to the accounting SaaS and Client B platform from a new browser; encryption status on each device and the USB drive; a restore of one 2026-06 project folder from the USB drive; download of a standard antivirus test file; a check of which laptop accounts exist.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- No test touched any client system. The gateway was not opened during the assessment; evidence came from Client A's own emails and session list.
- No client data or CEII was copied off the laptop. Screenshots were cropped to settings only. The IT technician did not open client folders or the CEII container.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 14 |
| Other than satisfied | 23 |
| **Total** | **37** |

**Fully satisfied:** SI-3 (the built-in antivirus detected and quarantined the test file).
**Fully other than satisfied:** AC-6(2), IA-2(2), SC-28, IR-6, AU-6.
**Partly satisfied:** AC-17 (Client A's side holds; the owner's device, network, and credential store do not), CP-9 (documents are versioned; model files and the CEII archive are not reliably backed up), MP-4 (paper is locked away; the drive is not), SA-9 (roles are defined; vendors are not reviewed).

**New finding:** the first restore test from the USB drive found 2 of 41 model files empty (CP-09d.[02]). The backup had been copying them wrongly for an unknown time. Together with the unencrypted drive, this means the business's only second copy of its CEII was both exposed and incomplete.

**What SI-3 does not cover.** The antivirus passed every test, but R-001 stays High: information-stealing malware is designed to slip past signature checks, and the damage comes from the administrator account and the browser password store (AC-6(2), AC-17), not from the antivirus.

The 9 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-009). The High items are POAM-001 (gateway path), POAM-002 (administrator account), and POAM-004 (backup drive encryption), all due 2026-09-30.

## 5. Deliverables
`assessment-results.csv` (37 rows), `poam.csv` (9 items), and this memo. Accepted by the owner-engineer on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year. Client A may also ask to see the POA&M items tied to CSCA-A (POAM-001, POAM-007, POAM-008, POAM-009).

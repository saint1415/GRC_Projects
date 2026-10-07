# Security Assessment Plan and Results Memo: Cris Santos Company | Manufacturing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated CNC machine shop) |
| System assessed | Shop Business Systems (SBS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Manufacturing (NAICS 332710) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-machinist (self-assessment), assisted by the on-call IT technician after the technician signed an NDA on 2026-08-07. **Independence is limited**: the owner designed, runs, and assessed these controls. The technician helped run the tests and read the settings, but also supports the laptop and router |
| Assessment window | 2026-08-10 to 2026-08-14 (tests on 2026-08-12) |
| Relationship to CMMC | This is **not** the CMMC Level 1 self-assessment. It uses SP 800-53A objectives to find gaps early. The Level 1 self-assessment must use the SP 800-171A objectives (32 CFR 170.15(c)(1)) and is scheduled after the POA&M items tied to FAR requirements are closed (target 2026-11-30) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 46 determination statements.** Controls were chosen because they support a High risk in P01 (R-001, R-003, R-006) or carry a FAR 52.204-21 requirement with a gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| SC-7 | Flat network and VMC share (R-001, R-005; FAR (b)(1)(i), (x)) | Focused / router, laptop share, Wi-Fi |
| CP-9 | Ransomware recovery (R-001; OEM record retention) | Focused / Jobs folder, CAM settings, records |
| SI-7 | Released OEM programs (R-006; OEM SQA change control) | Focused / 10 OEM programs in the VMC |
| AC-20 | AI assistant and processors (R-004, R-008; FAR (b)(1)(iii)) | Basic / all external services |
| IA-2(1) | MFA on administrator accounts (R-002) | Basic / suite and accounting |
| AC-17 | Remote-support tool (R-007) | Basic / laptop |
| PE-8 | Visitors (R-013; FAR (b)(1)(ix)) | Basic / bay |
| MP-6 | Retired laptop and sticks (R-010; FAR (b)(1)(vii)) | Basic / all media |
| AC-22 | Website and social media (R-013; FAR (b)(1)(iv)) | Basic / website and social page |
| SI-3 | Ransomware defense and USB sticks (R-001; FAR (b)(1)(xiii)-(xv)) | Focused / laptop |

## 2. Methods and objects
- **Examine:** account security and sharing settings, router admin pages, remote-support tool settings, antivirus status, laptop integrity and encryption settings, the website gallery, sent email, AI chat history, the drawer of old media, and P01 and P05.
- **Test (2026-08-12):** sign-ins from a new browser; an external port check; opening the VMC share from a phone on the shop Wi-Fi; restoring a deleted program from file versions; a standard antivirus test file by download and by USB stick; comparing 10 OEM programs in VMC memory with the Jobs folder copies.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- No testing while a machine was cutting. No customer drawing copied off shop systems; screenshots cropped to settings only.
- The IT technician worked only under the NDA signed 2026-08-07, in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 20 |
| Other than satisfied | 26 |
| **Total** | **46** |

**Fully satisfied:** SI-3 (the built-in antivirus caught the test file on download and on the USB stick).
**Fully other than satisfied:** IA-2(1), PE-8, MP-6.
**Partly satisfied:** SC-7 (inbound blocked; nothing inside separated), CP-9 (provider protects versions; no copy the laptop cannot overwrite), SI-7 (laptop integrity checks work; released programs unprotected), AC-20, AC-17, AC-22.

**New findings:**
1. **The VMC share was open to any device on the Wi-Fi** with no password (SC-07a.[04]). A share password is due by 2026-09-15 (POAM-001 milestone).
2. **The router admin password was the factory default** (SC-07c.). Changed during the test on 2026-08-12.
3. **2 of 10 OEM programs in VMC memory did not match the Jobs folder copy** (SI-07a.[03]): feed-rate and offset edits made at the controller and never recorded. The parts made with them passed inspection, but the SQA requires approval of process changes. The owner reviews both with the OEM quality contact by 2026-09-15 (POAM-003).
4. **Unattended remote access was on** (AC-17a.[02]); turned off during the test.

The 9 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-009). The High items are POAM-001 (network), POAM-002 (backup), POAM-003 (released programs), and POAM-006 (external systems).

**CMMC consequence.** POAM-001, POAM-005, POAM-006, POAM-007, POAM-008, and POAM-009 each carry a FAR 52.204-21 requirement. Level 1 allows no POA&M, so all six must be closed, and re-tested, before the owner affirms in SPRS.

## 5. Deliverables
`assessment-results.csv` (46 rows), `poam.csv` (9 items), and this memo. Accepted by the owner-machinist on 2026-09-04. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

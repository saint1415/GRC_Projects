# Security Assessment Plan and Results Memo: Cris Santos Company | Public Administration | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent GovTech consultant) |
| System assessed | Consulting Delivery Environment (CDE), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Public Administration |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-consultant (self-assessment), assisted by the on-call IT technician under the NDA signed 2026-08-07. **Independence is limited**: the owner designed, operates, and assessed these controls. The technician ran the tests and read the settings but is not screened for CJI and did not see any; the CJI search results were read by the owner alone |
| Assessment window | 2026-08-24 to 2026-08-26 |
| Also serves | CA-2 for the county contract's SP 800-53 Moderate clause, and evidence for the sheriff's LASO that the owner's security program operates (Security Addendum sec. 3.01) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 39 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002), a High or Moderate gap in P03, or a duty the sheriff or county contract names.

| Control | Why selected | Depth / coverage |
|---|---|---|
| AC-6 | Daily administrator use (R-001, R-002; P03 G-006 High) | Focused / laptop |
| IA-2(1), IA-2(2) | MFA on every account (R-002, R-011) | Basic / all SaaS and agency accounts |
| SC-28 | Encryption of every place agency data sits (R-004) | Basic / laptop, phone, USB drive |
| CM-12 | Where agency data actually lives (R-003; P03 G-051 High) | Focused / laptop, sync folder, recycle bin, USB drive |
| MP-6 | Deletion of county extracts (R-003; county contract) | Basic |
| CP-9 | Backups (R-010) | Basic / USB drive and cloud versions |
| SA-9 | Providers that hold agency data (R-005) | Focused / all five SaaS providers |
| IR-6 | Agency reporting clocks (R-012; CJIS IR-6) | Basic |
| AT-2 | Training, including the CJIS course (CJ-03) | Basic |

## 2. Methods and objects
- **Examine:** device and tenant settings, account lists, the USB drive and backup job, the provider list and terms, the productivity suite SOC 2 report, the three agency contracts, the CJIS training certificate, the incident log, and P01, P03, and P05.
- **Test (2026-08-24 to 2026-08-26):** sign-ins from a new browser to every SaaS service and agency system; a test installer run from the daily account; encryption status of each device and the USB drive; a keyword and file-pattern search for agency data (booking number and driver license number patterns, agency names) across the laptop, sync folder, cloud recycle bin, and USB drive; a restore of one project folder from the USB drive.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- Tests ran outside agency working hours and never inside an agency system beyond a normal sign-in.
- No agency data was copied during testing; search results were recorded as file paths and counts only.
- If a test found CJI, the owner would stop, report it to the sheriff's LASO within 1 hour (CJISSECPOL v6.1 IR-6), and keep the IT technician away from it. That happened on 2026-08-25.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 13 |
| Other than satisfied | 26 |
| **Total** | **39** |

**Fully other than satisfied:** AC-6 (daily administrator account), IA-2(1) (laptop administrator account has a password only), IA-2(2) (website builder MFA off; city 311 has none), and SC-28 (unencrypted USB drive).
**Partly satisfied:** AT-2 (the CJIS course meets initial and yearly training, but nothing covers post-incident training or reminders), CM-12, CP-9, IR-6 (the owner met the agency clocks in practice, but nothing was written), MP-6, and SA-9 (only the productivity suite was reviewed).

**New finding (CM-12a.[01]).** At 10:40 on 2026-08-25 the search found a spreadsheet with CHRI fields (names, dates of birth, booking numbers, charges) for 140 people on the laptop and in the cloud sync folder. The owner had copied report test output out of the sheriff's virtual desktop on 2026-05-14, which the desktop's clipboard and drive mapping allowed. The owner:
1. stopped the test and kept the IT technician off that screen;
2. called the sheriff's LASO at 11:15 (35 minutes after discovery, inside the CJIS 1-hour rule) and followed up by email;
3. deleted the file from the laptop, the sync folder, and the cloud recycle bin, and confirmed the USB drive did not hold it.

The sheriff disabled clipboard and drive mapping for contractor desktops on 2026-08-26. The LASO accepted deletion with full-disk encryption as the remediation on 2026-08-27 and handles any report to the CJIS Systems Officer. The finding went back into the risk register as **R-015** (High) and into the gap analysis as CJ-05. The fields are not personal information under Fla. Stat. 501.171(1)(g), so no 501.171 notice applies.

Each of the 10 controls has one POA&M item in `poam.csv` (POAM-001 to POAM-010): 3 High (POAM-001 USB encryption, POAM-003 data location and CJI, POAM-004 daily administrator account) and 7 Moderate.

## 5. Deliverables
`assessment-results.csv` (39 rows), `poam.csv` (10 items), and this memo. Accepted by the owner-consultant on 2026-09-15. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year; the results and the R-015 fix are also shared with the sheriff's LASO.

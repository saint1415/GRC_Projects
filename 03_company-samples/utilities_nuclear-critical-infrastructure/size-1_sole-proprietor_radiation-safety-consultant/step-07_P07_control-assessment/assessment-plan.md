# Security Assessment Plan and Results Memo: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent radiation safety consultant) |
| System assessed | Core Business SaaS Stack (CBSS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Nuclear Reactors, Materials, and Waste |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-consultant (self-assessment), assisted by the on-call IT technician under an NDA signed 2026-07-14. **Independence is limited**: the owner designed, operates, and assessed these controls. The IT technician ran the tests and read the settings but also supports the laptops. Client A's supplier questionnaire answers are taken from these results, so the owner may not mark anything better than the evidence shows |
| Assessment window | 2026-07-20 to 2026-07-24 (link test 2026-07-21; device and sign-in tests 2026-07-23) |
| Also used for | Client A's annual supplier security questionnaire; the CSIA-B (4) notice to Client B on 2026-07-22 |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 34 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002), the attempted-pivot risk to Client A (R-004), or a Not met client term in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1), IA-2(2) | MFA on the suite and every SaaS account (R-003, R-011; CSR-A (4)) | Basic / all 5 accounts |
| AC-3 | Sharing of Client B security information (R-002; CSIA-B (1)-(2)) | Focused / every external link |
| MP-7 | The USB drive path to Client A (R-004; CSR-A (2)) | Focused / the one drive |
| SC-28 | Encryption of devices and media holding client data (CSR-A (6); CSIA-B (2)) | Basic / 4 devices |
| CP-9 | Survey data and report backup (R-006) | Basic |
| SI-2 | Unsupported field laptop (R-005) | Focused / 3 devices and the router |
| SA-9 | AI and SaaS services used with client data (R-002, R-009; CSIA-B (3)) | Focused / 5 services |
| IR-6 | Client notice clocks (R-013; CSR-A (5); CSIA-B (4)) | Basic |
| MP-6 | Return and destruction of client information (R-007; CSR-A (8)) | Basic |

AC-6(5) (daily administrator account, P03 G-009) was not tested separately; the owner confirmed it in the self-review and it is carried as POAM-010 from the gap analysis.

## 2. Methods and objects
- **Examine:** suite security and sharing settings, account security pages, device encryption and update status, the USB drive contents, Client A kiosk slips and training records, vendor terms, the suite provider's SOC 2 report, P01 and P05.
- **Test:** private-browser test of every external link in the suite's sharing report (2026-07-21, repeated 2026-07-23); sign-ins to each service from a new browser (2026-07-23); encryption status on each device and the drive; field laptop OS support status; router firmware and administrator password check.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- No client folder was opened by the IT technician. The owner ran every step that touched client information; the technician watched settings screens only.
- Nothing was tested on Client A or Client B systems beyond the owner's own sign-in. No scanning of any client network.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 13 |
| Other than satisfied | 21 |
| **Total** | **34** |

**Fully satisfied:** IA-2(1) (the suite administrator account requires a second factor).
**Fully other than satisfied:** IA-2(2), AC-3, SC-28, IR-6, MP-6.
**Partly satisfied:** MP-7 (no unknown drives, but one personal drive is used everywhere), CP-9 (provider backups, but no field data backup and one account holds every copy), SI-2 (main devices and router current; field laptop unsupported), SA-9 (suite provider reviewed; nothing else).

**New findings:** the router administrator password was still the default printed on the label (changed during the session on 2026-07-23; P01 R-012). MFA is available but off on the calibration-tracking SaaS (also found in P04).

The 9 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-009); POAM-010 (AC-6(5)) comes from P03 G-009. The High items are POAM-002 (Client B security information) and POAM-010 (administrator account and saved portal password).

## 5. Deliverables
`assessment-results.csv` (34 rows), `poam.csv` (10 items), and this memo. Accepted by the owner-consultant on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

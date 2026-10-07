# Security Assessment Plan and Results Memo: Cris Santos Company | Mining, Quarrying, and Oil and Gas Extraction | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated oilfield services contractor) |
| System assessed | Field Service Business Systems (FSBS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Mining, Quarrying, and Oil and Gas Extraction |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-operator (self-assessment), assisted by the on-call IT technician. **Independence is limited**: the owner designed, operates, and assessed these controls. The technician ran the tests with the owner and read the settings, but also supports the laptop. Customer A's questionnaire review is the only outside check this year |
| Assessment window | 2026-07-20 to 2026-07-24 (tests on 2026-07-23) |
| Also supports | Customer A annual security questionnaire (due 2026-09-30); CSF 2.0 ID.IM-01 in the voluntary benchmark (P03) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 49 determination statements.** Controls were chosen because they support a High risk in P01 (R-001, R-002, R-003, R-008) or a Customer A security schedule item with a gap in P03. They focus on what the owner carries into customer OT: credentials, the laptop account, removable media, backups of control programs, and change records.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1), IA-2(2) | MFA on every account (R-002, R-013; PR.AA-03) | Basic / all owner accounts (email, accounting, dynamometer service, laptop administrator) and the 2 customer paths |
| AC-6(2) | Administrator account used for everything (R-001; PR.AA-05) | Basic / laptop |
| IA-5 | Password spreadsheet and default passwords (R-004; MSA-A (1)) | Focused / spreadsheet, router, and a sample of 6 customer field devices |
| CA-3 | Customer connections and the Customer B shared login (R-003; MSA-A (2)) | Focused / all 4 MSAs |
| CP-9 | Backups of customer programs (R-007; PR.DS-11) | Basic / synced folder and laptop |
| CM-3 | Logic and setpoint change approval (R-006; MSA-A (4)) | Focused / 23 Customer A changes in 12 months |
| MP-7 | USB drives used at well sites (R-005) | Basic / all 3 drives |
| SI-3 | Malware defense on the laptop (R-001, R-005) | Focused / laptop |
| IR-6 | Incident reporting, including the 24-hour Customer A notice (R-014; MSA-A (3)) | Basic |

## 2. Methods and objects
- **Examine:** SaaS security and sign-in pages, laptop account and encryption settings, the password spreadsheet (on screen only), remote client settings, router settings, settings on 6 customer field devices during routine Customer A and B site visits (with each customer's permission), the 4 MSAs and Customer A's security schedule, Customer A approval emails, the USB drives, and the provider SOC 2 report.
- **Test (2026-07-23):** sign-ins from a new browser to each SaaS account; a software install attempt from the daily account; a restore of one program file from the file version history; download of a standard antivirus test file and a copy of it to a USB drive.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- No test touched a customer controller's logic or setpoints. Field device settings were only viewed, during routine visits, with the customer's permission.
- No customer data was copied off the laptop; screenshots were cropped to settings only. The password spreadsheet was viewed, not copied.
- The IT technician worked only in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 15 |
| Other than satisfied | 34 |
| **Total** | **49** |

**Fully satisfied:** SI-3 (8 of 8; the built-in antivirus caught the test file on download and when copied from a USB drive).
**Fully other than satisfied:** IA-2(1), IA-2(2), AC-6(2), and IR-6.
**Partly satisfied:** IA-5 (2 of 10; devices are encrypted, but credentials are not protected), CA-3 (1 of 8; Customer A terms only), CP-9 (2 of 6; the provider protects stored versions, but there is no offline copy), CM-3 (1 of 10; the 4 email-approved changes matched what was loaded, but 19 of 23 had phone approval only), and MP-7 (1 of 2).

**New finding:** the Customer B remote-desktop client on the laptop had the shared password saved, so anyone using the laptop's administrator session could connect to Customer B's SCADA operator workstation without typing it (IA-05g.). The owner removed the saved password during the session on 2026-07-23 and wrote to Customer B on 2026-07-24 asking for named accounts and MFA. P01 R-003 and POAM-004 track the rest.

The 9 controls with weaknesses map to 8 POA&M items in `poam.csv` (POAM-001 to POAM-008; IA-2(1) and IA-2(2) share POAM-001). Six are High: POAM-001 (MFA), POAM-002 (administrator account), POAM-003 (passwords), POAM-004 (customer connection terms), POAM-005 (backups), and POAM-008 (incident reporting).

## 5. Deliverables
`assessment-results.csv` (49 rows), `poam.csv` (8 items), and this memo. Accepted by the owner-operator on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year, and the POA&M summary goes to Customer A with the questionnaire answers.

# Security Assessment Plan and Results Memo: Cris Santos Company | Food and Agriculture | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (custom-exempt meat processing shop) |
| System assessed | Shop Production and Cold-Chain Monitoring System (SPCM), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Food and Agriculture |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-operator (self-assessment), assisted by the on-call IT technician. **Independence is limited**: the owner designed, operates, and assessed these controls. The technician ran the tests and read the settings but also supports the laptop and router |
| Assessment window | 2026-07-27 to 2026-07-31 (tests on 2026-07-29, a day with no product in the smokehouse) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **9 controls, 50 determination statements.** Controls were chosen because they support a High risk in P01 (R-001, R-002) or a binding records duty with a gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1) | MFA on every administrator account (R-002) | Basic / every SaaS account (the owner holds only administrator accounts) |
| IA-5 | Shared password, browser storage, and device defaults (R-001, R-002) | Focused / all accounts and 3 devices |
| CP-9 | Backups of the custom records and cook programs (R-004; 9 CFR 303.1(b)(3), 320.3(a)) | Basic / all shop data |
| SI-3 | Ransomware defense on the laptop (R-001) | Focused / laptop |
| AU-6 | Review of the cold-chain activity log (R-002) | Basic |
| SC-7 | Flat shop network (R-006) | Focused / router and Wi-Fi |
| SA-9 | Vendors, including the AI chatbot (R-011, R-012) | Basic / all 9 vendors |
| IR-6 | Incident reporting (R-013; Fla. Stat. 501.171) | Basic |
| RA-3 | Risk assessment | Basic |

**Not tested this cycle:** CP-2. The cold-chain alerting actions it covers (offline notice, battery backup, second contact) are not in place yet and are tracked in P01 R-003. CP-2 is the first control for the July 2027 assessment, with a test of a simulated gateway outage.

## 2. Methods and objects
- **Examine:** account security pages, the laptop browser's password store, router settings and connected-device list, smokehouse panel and app settings, the cold-chain activity log and alert settings, file account settings, vendor terms, the cold-chain vendor's SOC 2 report, P01 and P05.
- **Test (2026-07-29):** sign-ins to each SaaS account from a new browser; sign-in to the router admin page and the smokehouse panel with their factory defaults; reachability of the router and smokehouse controller from a phone on the shop Wi-Fi; a port check from outside; download of a standard antivirus test file.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- No testing while product was in the smokehouse or while the walk-ins were being loaded. The cold-chain alert settings were viewed but not changed during the test.
- No customer records were copied off the devices; screenshots were cropped to settings only.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 24 |
| Other than satisfied | 26 |
| **Total** | **50** |

**Fully satisfied:** SI-3 (the built-in antivirus detected and quarantined the test file).
**Fully other than satisfied:** IA-2(1), AU-6, IR-6.
**Partly satisfied:** RA-3 (the assessment exists; no review cycle yet), IA-5 (devices protect stored secrets, but passwords are shared, stored in the browser, and defaults were found), CP-9 (vendor backups inherited; the shop's own data not backed up), SC-7 (inbound traffic blocked, but one flat network), SA-9 (only the cold-chain vendor is overseen).

**New findings during testing (2026-07-29):**
1. The router admin page and the smokehouse controller panel accepted their **factory default** credentials (IA-05e.). The owner changed both the same day.
2. A phone on the shop Wi-Fi could reach the router admin page and the smokehouse controller (SC-07a.[04]). Customers are given this Wi-Fi password at pickup.
3. The smokehouse app allowed **remote program editing**. Not a determination statement in this set, but recorded under P01 R-002; the owner turned it off on 2026-08-03.

The 8 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-008). The High items are POAM-001 (MFA) and POAM-002 (passwords), both due 2026-09-15, before the busy season.

## 5. Deliverables
`assessment-results.csv` (50 rows), `poam.csv` (8 items), and this memo. Accepted by the owner-operator on 2026-08-31. Because independence is limited, POL-01 4.4 requires the IT technician to review the evidence at least every second year.

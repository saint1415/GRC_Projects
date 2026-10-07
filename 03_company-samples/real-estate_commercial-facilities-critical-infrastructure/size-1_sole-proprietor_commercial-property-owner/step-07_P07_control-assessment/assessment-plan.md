# Security Assessment Plan and Results Memo: Cris Santos Company | Commercial Facilities | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operator of one mixed-use commercial building) |
| System assessed | Property Systems Profile (PSP), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Commercial Facilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner (self-assessment), assisted by the on-call IT consultant. **Independence is limited**: the owner set up, runs, and assessed these controls. The consultant ran the network tests and read the settings, but also set up the router in 2023 |
| Assessment window | 2026-07-20 to 2026-07-24 (building walkthrough 2026-07-21; tests 2026-07-23) |
| Supports | CISA CPG 2.0 goal 2.C (independent validation, partly) and "reasonable measures" under Fla. Stat. 501.171(2) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 52 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-004), a High or Moderate CPG gap in P03, or the P08 scenario. For AC-2, a focused set of 9 of its 26 objectives was assessed (account types, managers, authorized users, approval, disabling, departure notice, authorization, review, and shared authenticators), because the other objectives assume groups, roles, and staff that a one-person business does not have.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1) | MFA on the building portals (R-002; CPG 3.F) | Basic / all 5 admin portals |
| IA-2 | Shared thermostat login (R-007; CPG 3.C) | Basic / all portals |
| IA-5 | Router default password, reuse, browser-saved passwords (R-001; CPG 3.A, 3.B) | Focused / all objectives |
| AC-2 | Credentials and installer accounts (R-003, R-006; CPG 3.D) | Focused / 9 objectives, all 58 credentials |
| AC-3 | Public folder link to guarantor files (R-004; Fla. Stat. 501.171(2)) | Basic / file account |
| SC-7 | Flat network with lobby Wi-Fi (R-005; CPG 3.I) | Focused / router and lobby Wi-Fi |
| CP-9 | Backups and configuration export (R-011; CPG 3.O) | Basic |
| SA-9 | Contractors and vendors (R-003; CPG 1.D, 1.E) | Focused / 4 contractors, 6 vendors |
| AU-6 | Log review (CPG 3.Q) | Basic |
| SI-3 | Ransomware defense on the laptop (R-001; CPG 4.A) | Focused / laptop |

## 2. Methods and objects
- **Examine:** security and user settings in the access control, video, thermostat, property management, and email portals; the SYS-01 credential list; router settings; the laptop's browser password report and antivirus status; file sharing settings; the contracts folder; the access control vendor's SOC 2 report; P01 and P05.
- **Test (2026-07-23):** sign-ins to all five portals from a new browser; opening the lease application folder link from a signed-out private browser window; signing in to the router with the factory password from its label; an external port check of the building's public address; a network scan from a phone joined to the free lobby Wi-Fi; download of a standard antivirus test file.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT consultant challenged each answer against what was on screen. The HVAC contractor was asked by phone how its technicians sign in.

## 3. Rules of engagement
- Tests ran outside business hours. No door was unlocked or schedule changed during testing, and the lobby Wi-Fi scan only listed devices; nothing was probed further.
- No guarantor data was copied. Screenshots were cropped to settings only.
- Tenants were asked on 2026-07-22 to confirm their credential lists; the replies are evidence for AC-2.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 20 |
| Other than satisfied | 32 |
| **Total** | **52** |

**Fully satisfied:** SI-3 (built-in antivirus detected and quarantined the test file).
**Fully other than satisfied:** IA-2(1), AC-3, AU-6.
**Partly satisfied:** IA-2, IA-5, AC-2, SC-7, CP-9 (vendor-held backups satisfied; the owner's own data and configuration not backed up), SA-9.

**Key test results:**
- The access control, video, and thermostat portals accepted a password alone, including the installer's two accounts (IA-02(01)).
- The router accepted its factory password (IA-05e.).
- A phone on the free lobby Wi-Fi could see every camera, door controller, and thermostat (SC-07a.[04], b.).
- The guarantor folder opened from a signed-out browser (AC-03). The owner removed the link on 2026-08-05, once the CPA's named share was set up.
- 7 of 58 credentials belonged to people who had left; the owner disabled them on 2026-07-24 (AC-02f.[04]).

The 9 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-009): 3 High (MFA, authenticator management, the public link) and 6 Moderate.

## 5. Deliverables
`assessment-results.csv` (52 rows), `poam.csv` (9 items), and this memo. Accepted by the owner on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

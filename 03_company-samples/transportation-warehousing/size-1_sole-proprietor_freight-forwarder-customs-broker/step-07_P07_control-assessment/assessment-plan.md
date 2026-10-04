# Security Assessment Plan and Results Memo: Cris Santos Company | Transportation and Warehousing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (freight forwarder and customs broker) |
| System assessed | Core Brokerage SaaS Stack (CBSS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Transportation and Warehousing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner (self-assessment), assisted by the on-call IT consultant. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant ran the tests and read the settings but also supports the laptop and network |
| Assessment window | 2026-08-17 to 2026-08-21 (tests on 2026-08-20) |
| Criteria | P02 control statements and POL-01 (adopted 2026-09-14 from the draft used during testing) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 37 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-003) or a High gap in P03 (G-008, G-040).

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2, IA-2(1), IA-2(2) | Account identity and MFA on every service (R-001, R-006) | Basic / all 4 SaaS and bank accounts |
| IA-5 | Passwords and defaults (R-001, R-008, R-015) | Focused / all accounts and the router |
| AT-2(3) | Payment redirection and phishing (R-002; 111.29(a)) | Basic |
| CP-9 | Records backup (R-003; 163.5(b)(2)(vi); 111.25(b)) | Focused / customs software and archive |
| SC-28 | Encryption of client records at rest (Fla. Stat. 501.171) | Basic / laptop, phone, vendors |
| IR-6 | Incident reporting, including the 72-hour CBP notice (R-004; 111.21(b)) | Basic |
| SA-9 | Vendors and client authorization (R-007; 111.24) | Focused / 6 services and 2 contractors that see client records |
| MP-6 | Disposal of old devices (R-012; Fla. Stat. 501.171(8)) | Basic / 2019 laptop and paper |

## 2. Methods and objects
- **Examine:** account and security pages of each service, the phone's mail app settings, password history, the router admin page, device encryption status, vendor contracts and client terms, the customs software vendor's SOC 2 report, training certificates, P01 and P05.
- **Test (2026-08-20):** sign-ins to each service from a new browser and through the phone mail app; administrator sign-ins; the router admin page with the label password; restore of one archive file from version history; encryption status on each device; a check of the 2019 laptop in the closet.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT consultant challenged each answer against what was on screen.

## 3. Rules of engagement
- No testing during filing deadlines (tests ran after 6 p.m.). No client data copied off the devices; screenshots were cropped to settings only.
- The IT consultant worked only in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 12 |
| Other than satisfied | 25 |
| **Total** | **37** |

**Fully satisfied:** IA-2(1) (every administrator sign-in asked for a second factor) and SC-28 (laptop, phone, and vendors encrypt stored data).
**Fully other than satisfied:** IA-2, IA-2(2), and IR-6.
**Partly satisfied:** IA-5 (3 of 10), AT-2(3) (1 of 4), CP-9 (4 of 6: the vendor side passes, the owner's archive fails), SA-9 (1 of 6), MP-6 (1 of 4).

**New findings fed back to P01 and P04:**
1. **Default router password (IA-05e.).** The home router's admin password was still the one printed on its label. Added to R-008 and the P04 map; fixed under POAM-003.
2. **The former bookkeeper still knows a working password (IA-05i.).** The accounting SaaS password history shows no change since 2024. Added to R-006; fixed under POAM-003 and POAM-007.
3. **The email MFA bypass was confirmed by test (IA-02(02)).** The phone mail app read new mail with no second factor. This is the root of R-001 and the first item in POAM-001.

The 8 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-008). The High items are POAM-001 (email MFA bypass, due 2026-09-30) and POAM-002 (independent archive backup, due 2026-10-31).

## 5. Deliverables
`assessment-results.csv` (37 rows), `poam.csv` (8 items), and this memo. Accepted by the owner on 2026-09-14. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

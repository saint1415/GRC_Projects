# Security Assessment Plan and Results Memo: Cris Santos Company | Critical Manufacturing | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated industrial equipment repair service) |
| System assessed | Field Service Business Systems (FSBS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Critical Manufacturing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-technician (self-assessment), assisted by the on-call IT consultant after the consultant signed the owner's NDA on 2026-08-20. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant helped run the tests and read the settings but is also the person who supports the laptop |
| Assessment window | 2026-08-24 to 2026-08-28 (tests on 2026-08-26 at the home office and 2026-08-27 at Customer B) |
| Also supports | Customer A supplier security questionnaire; P03 gap ratings |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 51 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-003) or a Customer A exhibit term with a gap in P03.

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-17 | Router at Customer B (R-003); exhibit S2 (G-037) | Focused | Router and Customer A gateway use |
| IA-2(1) | MFA on administrator accounts (R-003, R-006; G-017) | Basic | Suite, accounting SaaS, and router portal administrator accounts |
| CP-9 | Library backup (R-001; G-023) | Focused | Library and business records |
| SI-3 | Ransomware and malware defense (R-001, R-002) | Basic | Laptop and virtual machine |
| MP-7 | USB sticks into plant equipment (R-002; exhibit S3, G-038) | Focused | All 8 sticks |
| SI-7 | Firmware and program integrity (R-004; exhibit S5, G-040) | Focused | 2026 firmware loads; library |
| SC-7 | Home network and virtual machine bridging (R-009, R-012; G-027) | Basic | Laptop, home network, router |
| IA-5 | Customer machine passwords (R-005; G-016) | Basic | SaaS passwords, spreadsheet, router |
| IR-6 | Customer A 24-hour notice (R-013; exhibit S4, G-039) | Basic | Procedure and contacts |
| SA-9 | Suppliers and the AI trial (R-007; exhibit S1, G-036) | Basic | All 4 SaaS suppliers |

## 2. Methods and objects
- **Examine:** SaaS security, sharing, and user settings; laptop account, firewall, encryption, and virtual machine settings; antivirus status; the field kit; firmware load records; the contract file; supplier terms; the productivity suite provider's SOC 2 report; P01 and P05.
- **Test:**
  - 2026-08-26 (home office): sign-ins to the suite, accounting SaaS, and router portal from a new browser; download of a standard antivirus test file; test restore of one machine folder (40 files) from version history; check of which network the virtual machine reached.
  - 2026-08-27 (Customer B, with its maintenance supervisor present): router local admin page and portal session settings. The factory default password was accepted and was changed on the spot.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT consultant challenged each answer against what was on screen.

## 3. Rules of engagement
- No test touched a customer controller, plant network, or substation system. At Customer B only the owner's router was examined, with the maintenance supervisor present; the oven PLC and HMI were not accessed.
- No customer program or password was copied off the devices; screenshots were cropped to settings only.
- The IT consultant worked only under the NDA signed 2026-08-20, in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 19 |
| Other than satisfied | 32 |
| **Total** | **51** |

**Fully other than satisfied:** AC-17 (4 of 4), IA-2(1), IR-6 (2 of 2).
**Mostly satisfied:** SI-3 (7 of 8; only the virtual machine lacks protection).
**Partly satisfied:** CP-9 (1 of 6), MP-7 (1 of 2), SI-7 (2 of 6), SC-7 (1 of 6), IA-5 (5 of 10), SA-9 (2 of 6).

**Findings found or confirmed by test:**
- The router at Customer B accepted its **factory default local admin password** (AC-17a.[02], IA-05e.). Changed on 2026-08-27. With Customer B's agreement, the router has been powered off since 2026-09-03 except for sessions Customer B approves by phone.
- A full restore of the library from version history is **not workable**: restore went one file at a time (CP-09d.[03]), so the 4-hour RTO in P05 cannot be met today.
- The legacy virtual machine **reached the home network and the internet** through its bridged adapter (SC-07a.[04]).
- The antivirus **detected and quarantined** the test file (SI-03a.[02]).

The 10 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-010): 4 High, 5 Moderate, 1 Low. The High items are POAM-001 (router, due 2026-12-31), POAM-002 (MFA, due 2026-09-30), POAM-003 (offline backups, due 2026-10-31), and POAM-004 (USB sticks and scanning, due 2026-10-31).

## 5. Schedule and deliverables
`assessment-results.csv` (51 rows), `poam.csv` (10 items), and this memo. Accepted by the owner-technician on 2026-09-11. Next assessment August 2027. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year; the owner will also offer Customer A a walkthrough of the POA&M as part of its supplier review.

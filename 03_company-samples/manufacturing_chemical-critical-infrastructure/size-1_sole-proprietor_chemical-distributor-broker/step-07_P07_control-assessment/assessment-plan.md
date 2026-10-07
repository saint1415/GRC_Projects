# Security Assessment Plan and Results Memo: Cris Santos Company | Chemical | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (specialty chemical distributor, broker) |
| System assessed | Brokerage Core SaaS Stack (BCSS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Chemical |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner (self-assessment), assisted by the on-call IT technician. **Independence is limited**: the owner designed, operates, and assessed these controls. The technician ran the sign-in and device tests and read the settings, but also supports the laptop |
| Assessment window | 2026-09-08 to 2026-09-11 (tests on 2026-09-10) |
| Also supports | The annual HSP-01 review (49 CFR 172.802(c)) and the P09 self-attestation |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 41 determination statements.** Controls were chosen because they support the Very High and High risks in P01 (R-001, R-002, R-004) or a High or Moderate gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1), IA-2(2) | MFA on the accounts that release loads and move money (R-001, R-002; P03 G-023, G-032) | Basic / every account (12 sign-in tests) |
| AC-6(2) | Daily administrator use on a shared laptop (R-009) | Basic / laptop |
| AT-2(3) | Social engineering is how threats reach this business (R-001, R-003; G-016) | Basic |
| AT-3 | HMR role-based training (R-004; G-014 to G-019) | Focused |
| SA-9 | Vendors, including the ERI provider and the AI assistant (R-006, R-012; G-011) | Focused / all vendors |
| CP-9 | Backup of required records (R-007; G-013) | Basic / suite and local data |
| AU-6 | Review of sign-ins and forwarding rules (R-001; G-032) | Basic |
| IR-6 | Incident reporting (R-003; G-033, G-035) | Basic |
| RA-3 | Risk assessment, also the HSP-01 assessment (G-021) | Basic |

## 2. Methods and objects
- **Examine:** email, accounting, bank, and portal security pages; the laptop's account settings; the 2022 training certificate and course outline; the email suite SOC 2 report; the ERI product list; the AI assistant's data settings; P01 and P05.
- **Test (2026-09-10):** sign-ins from a new browser to the email suite, accounting SaaS, bank, and all 9 partner portals; a software install from the laptop's daily account; a restore of a BOL deleted in 2025; a scan of the email account for forwarding rules.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- Tests ran outside business hours, with no load in transit, so no pickup authorization could be disturbed.
- No customer, supplier, or driver data was copied off the systems. Screenshots were cropped to settings only.
- The IT technician worked in sessions the owner started and watched, and signed a confidentiality letter on 2026-09-08.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 13 |
| Other than satisfied | 28 |
| **Total** | **41** |

**Mostly satisfied:** RA-3 (6 of 8; the assessment exists but had no review cycle) and CP-9 (4 of 6; provider backups are inherited, but the owner's own records have no backup).
**Fully other than satisfied:** IA-2(1), IA-2(2), AC-6(2), AT-2(3), AU-6, IR-6.
**Partly satisfied:** AT-3 (2 of 9; initial training was done, recurrent training lapsed), SA-9 (1 of 6).

**New findings during testing:**
1. **An unknown forwarding rule** in the email account sent copies of incoming mail to a former personal address (AU-06a.). The owner set it up years ago and forgot it. It was removed on 2026-09-10. It shows why the monthly review in POL-01 7.6 matters: an attacker's rule would look the same.
2. **A BOL deleted in 2025 could not be restored** (CP-09a.), so the two-year retention in 172.201(e) depends on nobody deleting anything.
3. The ERI provider gap found in P03 was confirmed against the provider's product list (SA-09a.[01]) and fixed on 2026-09-14.

All 10 controls have weaknesses, and each has one POA&M item in `poam.csv` (POAM-001 to POAM-010). The High items are POAM-001 (email MFA, due 2026-10-15), POAM-002 (MFA on the other accounts, 2026-10-31), and POAM-003 (HMR training, 2026-11-30). By risk level: 3 High, 6 Moderate, 1 Low.

## 5. Deliverables
`assessment-results.csv` (41 rows), `poam.csv` (10 items), and this memo. Accepted by the owner on 2026-10-05. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year. The hazmat training provider will review the HSP-01 controls during the in-depth security training in November 2026.

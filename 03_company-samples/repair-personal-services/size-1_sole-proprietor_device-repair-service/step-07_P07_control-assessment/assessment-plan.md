# Security Assessment Plan and Results Memo: Cris Santos Company | Other Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (electronics and device repair service) |
| System assessed | Service Ticketing and Point-of-Sale System (STPS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Other Services (except Public Administration) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-technician (self-assessment), assisted by the independent security consultant under a confidentiality agreement. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant ran the tests with the owner and challenged the self-review answers, which is the only outside check |
| Assessment window | 2026-07-20 to 2026-07-27 (tests on Monday 2026-07-27, when the shop is closed) |
| Also supports | CSF 2.0 ID.IM-01 (improvements from evaluations); PCI DSS SAQ P2PE preparation |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 41 determination statements.** Controls were chosen because they support the two High risks in P01 (R-001 ticketing account takeover, R-002 customer data on the bench), a High gap in P03, or the shop's one strong inherited control (P2PE), which was tested to confirm it.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1) | MFA on the accounts that hold customer data or money (R-001; G-055) | Basic / all 6 SaaS accounts |
| AC-2, IA-2 | Shared SYS-01 login and contractor access (R-001, R-004; G-053, G-057) | Focused / SYS-01 |
| SI-12 | Passcodes, passwords, and card numbers in notes; retention (R-001, R-006; G-037, G-038) | Focused / SYS-01 notes, bench, paper |
| SC-28 | Customer data at rest on the bench (R-002; G-061) | Basic / all 5 devices and 2 drives |
| MP-6 | Sanitization of drop-off devices and drives (R-005; G-115) | Focused / drop-off bin and drives |
| SC-7 | Flat shop network (R-003; G-071) | Basic / router and Wi-Fi |
| SA-9 | Contractors and vendors (R-004, R-009; G-026) | Basic / all vendors and contractors |
| SC-8 | P2PE and TLS (inherited strength) | Basic |
| RA-3 | Risk assessment (CSF ID.RA) | Basic |

## 2. Methods and objects
- **Examine:** SYS-01 users, roles, sessions, activity log, and a search of ticket notes; account security pages; device encryption and lock settings; router settings and connected-device list; bench PC software and folders; the transfer drives; the drop-off bin; the contract folder; the ticketing vendor's SOC 2 report; P01 and P05.
- **Test (2026-07-27):** sign-ins from a new browser to each SaaS account; encryption status on each device; an external port check from a phone hotspot; a ping from a customer device on the bench to the counter tablet; power-on of 9 drop-off devices; a look at the transfer drives' folders.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the consultant challenged each answer against what was on screen.

## 3. Rules of engagement
- Tests only on a closed day. No customer content was opened: folder and file names were counted, never opened; drop-off devices were powered on only to the lock or home screen.
- The consultant never received a copy of customer data; screenshots were cropped to settings only.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 12 |
| Other than satisfied | 29 |
| **Total** | **41** |

**Fully satisfied:** SC-8 (P2PE and TLS confirmed).
**Fully other than satisfied:** IA-2, IA-2(1), SC-28, MP-6.
**Partly satisfied:** RA-3 (analysis done; no review cycle yet), AC-2 (owner is the account manager; everything else fails), SI-12 (no exports; retention fails), SC-7 (perimeter blocks inbound; no internal separation), SA-9 (duties for the ticketing vendor documented; no other oversight).

**New findings from testing:**
1. The SYS-01 account was still signed in on the fill-in technician's personal phone, last active 2026-06-13, six weeks after the cover period ended (AC-02f.[04]). The owner ended the session during the test and recorded it in POAM-002.
2. 4 of the 9 devices in the drop-off bin had not been reset, and 1 powered on to a home screen with photos (MP-06a.[01]). The owner reset it on the spot and put the bin behind the counter until the POL-01 8.7 procedure is running.
3. The transfer drives still held earlier customers' folders, so each new transfer customer's data sat next to other customers' data (MP-06a.[03]).
4. A customer device on the bench could reach the counter tablet and the bench PC over the shop Wi-Fi (SC-07a.[04]).

The 9 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-009). The High items are POAM-001 (MFA, due 2026-09-15), POAM-002 (shared account, 2026-09-30), POAM-003 (retention and note purge, 2026-10-31), and POAM-004 (bench encryption, 2026-10-31).

## 5. Deliverables
`assessment-results.csv` (41 rows), `poam.csv` (9 items), and this memo. Accepted by the owner-technician on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

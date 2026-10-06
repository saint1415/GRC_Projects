# Security Assessment Plan and Results Memo: Cris Santos Company | Accommodation and Food Services | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (six-room bed-and-breakfast inn) |
| System assessed | Inn Business Systems Profile (IBSP), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Accommodation and Food Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-innkeeper (self-assessment), assisted by the on-call IT consultant under a confidentiality agreement signed 2026-07-17. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant helped run the tests and read the settings but also supports the laptop and router |
| Assessment window | 2026-07-20 to 2026-07-24 (tests on 2026-07-23) |
| Also supports | PCI DSS v4.0.1 evidence for the 2026 SAQs (N72-R01); "reasonable measures" under Fla. Stat. 501.171(2) (N72-R04) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 47 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-004) or a High or Moderate PCI DSS gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1) | MFA on the accounts that reach card and guest data (R-001, R-004; Req 8.4) | Basic / all five SaaS accounts |
| IA-5 | Passwords and door codes (R-001, R-005; Req 8.3, 2.2) | Focused / laptop, router, locks |
| SC-28 | Data at rest on the laptop and in email (R-007; Req 3.5) | Basic / laptop, phone, email |
| SI-12 | Stored card data and ID photos (R-002, R-008; Req 3.2, 3.3.1) | Focused / paper, email, phone |
| CM-6 | Router and lock settings (R-006; Req 1.3, 2.2) | Basic / router and lock app |
| SA-9 | Providers and their accounts (R-003, R-013; Req 12.8) | Focused / all providers |
| SI-3 | Malware defense on the laptop (R-001; Req 5.2) | Focused / laptop |
| CP-9 | Backups (R-015) | Basic / SaaS and laptop |
| AU-6 | Log review (R-004; Req 10.4) | Basic / four logs |
| IR-6 | Incident reporting (R-014; Req 12.10) | Basic |

## 2. Methods and objects
- **Examine:** account security pages, user lists, the browser password list, device encryption and lock settings, router and lock app settings, antivirus status, the vendor folder (AOCs, SOC 2 report), the sub-merchant agreement, the desk drawer, a mailbox search, and P01 and P05.
- **Test (2026-07-23):** sign-ins to each SaaS account from a new browser; a sign-in to the router administrator page with the label password; a review of every account in the lock app; download of a standard antivirus test file; encryption status on each device.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT consultant challenged each answer against what was on screen.

## 3. Rules of engagement
- Tests run between 10:00 and 14:00, after checkouts and before arrivals. No guest data copied off the devices; screenshots were cropped to settings only. Card numbers found in email were counted, not opened in full.
- The IT consultant worked only in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 17 |
| Other than satisfied | 30 |
| **Total** | **47** |

**Fully satisfied:** SI-3 (built-in antivirus detected and quarantined the test file).
**Fully other than satisfied:** IA-2(1), SC-28, CM-6, AU-6, IR-6.
**Partly satisfied:** IA-5 (door codes are random; passwords are reused, saved in the browser, and default on the router), SI-12 (the register meets Florida law; card data and ID photos are kept with no limit), SA-9 (customer responsibilities are known; no oversight), CP-9 (vendor backups inherited; laptop files not backed up).

**New findings (fed back into P01):**
1. The lock installer's administrator account in the lock app was still active from the 2022 installation (SA-09a.[03]). The owner disabled it during the session on 2026-07-23. Added to P01 R-005; POAM-006 tracks the account review rule.
2. The router's internet-side remote management was turned on (CM-06b.), so anyone on the internet could reach a login page protected only by the default password. The consultant turned it off the same day; the rest of the router checklist is POAM-005. Added to P01 R-006.

The 9 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-009). The High items are POAM-001 (MFA), POAM-002 (passwords), POAM-003 (encryption), and POAM-004 (stored card data and ID photos), due between 2026-09-15 and 2026-10-31.

## 5. Deliverables
`assessment-results.csv` (47 rows), `poam.csv` (9 items), and this memo. Accepted by the owner-innkeeper on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

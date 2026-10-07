# Security Assessment Plan and Results Memo: Cris Santos Company | Real Estate | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (residential real estate brokerage) |
| System assessed | Transaction Management and Closing Communications System (TMCC), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Real Estate and Rental and Leasing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The broker-owner (self-assessment), assisted by the on-call IT technician under a confidentiality agreement signed 2026-08-14. **Independence is limited**: the owner designed, operates, and assessed these controls. The technician ran the tests and read the settings but also supports the laptop and router |
| Assessment window | 2026-08-17 to 2026-08-21 (tests on 2026-08-20) |
| Also supports | "Regularly test or otherwise monitor" in the 16 CFR 314.4(d)(1) benchmark, and evidence of reasonable measures under Fla. Stat. 501.171(2) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 33 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-004) or a High or Moderate gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2 | One identity per person (R-004; P03 G-024) | Basic / all user lists |
| IA-2(1), IA-2(2) | MFA on email, platform, banking, and the other accounts (R-001; G-029) | Basic / every account |
| AU-6 | Detecting a mailbox takeover (R-001; G-033) | Basic / email and platform logs |
| AT-2(3) | Recognizing fake wire instructions and sign-in pages (R-001, R-002; G-036) | Basic / owner and coordinator |
| SA-9 | Contractors and vendors with client data (R-007; G-006, G-038) | Focused / all contractors and vendors |
| CP-9 | Recovering mail, files, and the escrow ledger (R-014) | Basic |
| MP-6 | Disposal of devices and paper (G-007) | Basic |
| SC-28 | Encryption of the laptop and phone (R-005) | Basic / both devices |
| SI-8 | The email provider's spam and phishing filtering (R-002) | Basic |

## 2. Methods and objects
- **Examine:** user lists and security pages for email, the platform, e-signature, accounting, and banking; the email admin console (sign-in history, rules, alert settings); device encryption status; the contracts folder; the platform vendor's SOC 2 report; P01 and P05.
- **Test (2026-08-20):** sign-ins from a new browser to every account; a check of who can send as the owner; encryption status on both devices; a test spam message and a test phishing link sent from an outside account; a search for external forwarding rules (none found).
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen. The coordinator was asked by phone how they sign in and whom they would tell about a suspicious email.

## 3. Rules of engagement
- No testing on a closing day. No client data copied off any system; screenshots were cropped to settings only.
- The IT technician worked only under the agreement signed 2026-08-14, in sessions the owner started and watched.
- No test message imitated a title company, a lender, or a client.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 13 |
| Other than satisfied | 20 |
| **Total** | **33** |

**Fully satisfied:** SC-28 (both devices encrypted) and SI-8 (the provider caught and quarantined the test messages).
**Fully other than satisfied:** IA-2, IA-2(1), IA-2(2), AU-6, and AT-2(3).
**Partly satisfied:** SA-9 (roles are set, but contractors have no written security terms), CP-9 (vendor backups inherited; no independent backup of mail, files, or the escrow ledger), and MP-6 (paper is shredded; no device wipe method).

**What the tests showed about business email compromise.** Every control between an attacker and the owner's mailbox was weak or missing: a shared identity, relayable text codes, no alerts, and no training. The one strong control, spam filtering, does not help against a look-alike domain or a mailbox that is already taken over. **Observation:** the brokerage domain has no DMARC policy, so receivers do not reject mail forged in the owner's name (P01 R-002).

The 8 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-008). The High items are POAM-001 (shared identity), POAM-002 and POAM-003 (MFA), all due 2026-09-30, and POAM-004 (monitoring), due 2026-10-31.

## 5. Deliverables
`assessment-results.csv` (33 rows), `poam.csv` (8 items), and this memo. Accepted by the broker-owner on 2026-09-15. Because independence is limited, POL-01 4.5 requires the IT technician to check the settings independently at least every second year.

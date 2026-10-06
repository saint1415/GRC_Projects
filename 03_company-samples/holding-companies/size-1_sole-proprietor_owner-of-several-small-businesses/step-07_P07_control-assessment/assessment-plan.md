# Security Assessment Plan and Results Memo: Cris Santos Company | Management of Companies and Enterprises | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (the owner's management business for three wholly owned LLCs) |
| System assessed | Shared Back-Office Platform (SBP), per the system profile (P02), including the owner's administrator access to the three LLC systems |
| Tier / Vertical | Sole Proprietorship / Management of Companies and Enterprises |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-manager (self-assessment), assisted by the on-call IT technician under a confidentiality and security agreement signed 2026-07-24. **Independence is limited**: the owner designed, operates, and assessed these controls. The technician ran the tests and read the settings but also supports the devices |
| Assessment window | 2026-07-27 to 2026-07-31 (tests on 2026-07-30) |
| Also supports | The "reasonable measures" duty in Fla. Stat. 501.171(2) for each LLC and for the sole proprietorship as their third-party agent |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **9 controls, 56 determination statements.** Controls were chosen because they support the High risks in P01 (R-001 email takeover, R-002 payment redirection through account misuse) or a High gap in P03 (PR.AA-01, PR.AA-03, PR.AA-05, PR.DS-11, RS.CO-02).

| Control | Why selected | Depth / coverage |
|---|---|---|
| AC-2 | Stale and shared accounts across the LLCs (R-004; PR.AA-05) | Focused / all seven services and the POS |
| IA-2(1) | MFA on the administrator accounts that reach all four entities (R-001; PR.AA-03) | Basic / all seven services and the bank |
| IA-2(2) | MFA on staff accounts (R-005) | Basic / 3 staff accounts |
| IA-5 | Reused, default, and shared credentials (R-007, R-015) | Focused / all credentials |
| SC-28 | Unencrypted Storage desktop (R-005) | Basic / 4 devices |
| CP-9 | No backup of the shared mailbox and files (R-008; PR.DS-11) | Basic / suite and LLC systems |
| SA-9 | Bookkeeper and vendors without terms (R-011; GV.SC-05) | Focused / 7 vendors and 3 contractors |
| AU-6 | No review of sign-ins or mailbox rules (R-001; DE.CM-03) | Basic |
| IR-6 | No reporting duty or notice list for four covered entities (R-012; RS.CO-02) | Basic |

## 2. Methods and objects
- **Examine:** user lists, roles, and security settings in all seven SaaS services and the bank; the suite file listing and retention settings; device encryption and sign-in settings; router and gate controller settings; the agreements folder; the accounting service's SOC 2 report; P01 and P05.
- **Test (2026-07-30):** administrator and staff sign-ins from a new browser for every service; a sign-in attempt on the gate controller with the installer's default password; a check of the browser password store for reuse; encryption status on each device; disabling the former storage assistant's account.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen. The Storage manager and the Laundry attendants were asked two questions each (whom they would call about a suspicious email; whether they share a PIN).

## 3. Rules of engagement
- Tests ran outside Storage office hours and at the laundromat's quiet time. No tenant or applicant data was copied; screenshots were cropped to settings only.
- The IT technician worked only under the agreement signed 2026-07-24, in sessions the owner started and watched.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 14 |
| Other than satisfied | 42 |
| **Total** | **56** |

| Control | Statements | Satisfied | Other than satisfied |
|---|---|---|---|
| AC-2 | 26 | 7 | 19 |
| IA-2(1) | 1 | 0 | 1 |
| IA-2(2) | 1 | 0 | 1 |
| IA-5 | 10 | 3 | 7 |
| SC-28 | 1 | 0 | 1 |
| CP-9 | 6 | 3 | 3 |
| SA-9 | 6 | 1 | 5 |
| AU-6 | 3 | 0 | 3 |
| IR-6 | 2 | 0 | 2 |

**Fully other than satisfied:** IA-2(1), IA-2(2), SC-28, AU-6, IR-6.
**Partly satisfied:** AC-2 (the owner is the single, known account manager; nothing is defined, removed, or reviewed), IA-5 (vendor password rules work; the owner's own credential habits do not), CP-9 (vendor platform backups are sound; the owner's data has no independent copy), SA-9 (roles defined; no requirements or monitoring).

**What the tests showed for a holding business.** Every failure sat in the shared layer or in a habit the owner repeats across all three LLCs: the same text-message MFA, the same reused password, the same lack of removal steps. No LLC was better or worse because of its own vendor. Fixing the shared layer once fixes all three.

**New findings during the assessment:**
- The former storage assistant's account (left 2026-01-16) was still enabled in the storage system (AC-02f.[04]). The owner disabled it during the test on 2026-07-30.
- The gate controller accepted the installer's default administrator password (IA-05e.).
- The bookkeeper's accountant user also held the company administrator role in all four company files (SA-09a.[03]). The owner removed that role on 2026-08-12; reducing the accountant role itself is POAM-004.

The 9 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-009). The High item is POAM-001 (administrator MFA), due 2026-09-30.

## 5. Deliverables
`assessment-results.csv` (56 rows), `poam.csv` (9 items), and this memo. Accepted by the owner-manager on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.

# Security Assessment Plan and Results Memo: Cris Santos Company | Defense Industrial Base | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (engineering subcontractor handling CUI drawings) |
| System assessed | Engineering Office Systems (EOS), per the SSP (P02) |
| Tier / Vertical | Sole Proprietorship / Defense Industrial Base |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) for the 10 SP 800-53 controls below. The full SP 800-171 Rev. 2 self-assessment against SP 800-171A, required for the CMMC Level 2 (Self) entry (32 CFR 170.16(c)(1)), is scheduled for January 2027 (POAM-019) |
| Assessor(s) and independence | The owner (self-assessment), with the on-call IT consultant running tests on site on 2026-08-05 and the CMMC consultant reviewing the results by video. **Independence is limited**: the owner designed, operates, and assessed these controls. The IT consultant also supports the laptop. The CMMC consultant is the only reviewer with no role in operating the controls |
| Assessment window | 2026-08-03 to 2026-08-07 (tests on 2026-08-05) |
| Also satisfies | SP 800-171 3.12.1 (periodic assessment) for the requirements traced to these controls |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 41 determination statements.** Controls were chosen because they support the High and Very High risks in P01 or a high-value SP 800-171 requirement with a gap in P03, including requirements that may not be on a POA&M (3.1.20, 3.10.3, 3.10.4).

| Control | Why selected | SP 800-171 link | Depth / coverage |
|---|---|---|---|
| SA-9 | CUI in a non-FedRAMP cloud; AI chatbot (R-002, R-007) | 3.1.20; DFARS 252.204-7012(b)(2)(ii)(D) | Focused / all 5 SaaS services |
| IA-5 | Passwords and default credentials (R-001, R-015) | 3.5.7; 3.5.10 | Focused / all accounts and the router |
| AC-6(2) | Daily administrator use (R-011) | 3.1.6 | Basic / laptop |
| SC-7 | Shared home network (R-008) | 3.13.1 | Focused / router, laptop, printer |
| SC-13 | FIPS-validated cryptography | 3.13.11 | Basic / laptop, backup drive |
| SC-28(1) | Encryption at rest (R-005) | 3.13.16; 3.8.9 | Basic / laptop, backup drive |
| CP-9 | Backups (R-011; BIA RPO 8 h) | 3.8.9 | Basic / laptop and cloud |
| AU-6 | Log review (R-001) | 3.3.5 | Basic |
| IR-6 | DoD reporting in 72 hours (R-006) | 3.6.2; DFARS 252.204-7012(c) | Basic |
| PE-8 | Visitor records for the home office (R-012) | 3.10.4 | Basic |

## 2. Methods and objects
- **Examine:** SaaS security and audit pages, SYS-01 service terms and the FedRAMP Marketplace listing search, laptop account list and policy settings, encryption status, backup drive contents, router settings, the password spreadsheet (existence only, not its contents), P01, P02, P05.
- **Test (2026-08-05, with the IT consultant on site):** sign-in to the router administrator page with the factory default password; whether a household tablet can reach the printer; whether the backup drive opens without a password; the laptop FIPS policy setting; a one-folder restore from the backup; an attempt to open DIBNet; the laptop administrators group membership.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the CMMC consultant challenged each answer against the screenshots.

## 3. Rules of engagement
- No CUI was shown to either consultant. Screenshots were cropped to settings; file lists were shown by count, not by name.
- The IT consultant worked on site with the owner present, and every change made during testing was entered in the change log.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 11 |
| Other than satisfied | 30 |
| **Total** | **41** |

**Partly satisfied:** SA-9 (privacy terms only), IA-5 (identity proofing, initial content, device protection of the authenticator, no group accounts), SC-7 (inbound blocking, no public components, and the managed internet interface), CP-9 (backups are made and restorable).
**Fully other than satisfied:** AC-6(2), SC-13, SC-28(1), AU-6, IR-6, PE-8.

**New finding:** the router administrator password was still the factory default printed on the router's label (IA-05e.). It was changed during the session on 2026-08-05. It is added to the risk register as R-015 and tracked in POAM-002. The IT consultant's unused setup administrator account was confirmed and disabled the same day (AC-06(02); POAM-003). The household tablet test showed the printer's job list was readable from any home device (SC-07a.[04]).

**POA&M.** Each of the 10 controls has one POA&M item (POAM-001 to POAM-010). POAM-011 to POAM-019 carry the remaining P03 gaps, so every one of the 78 SP 800-171 requirements not fully met is on the POA&M, as 32 CFR 170.24(c)(2)(i)(B)(6) requires. Of the 19 items, 1 is Very High (POAM-019, the SPRS score and CMMC status), 17 are High, and 1 is Moderate. A POA&M does not make a requirement met, and the items for 3.1.20, 3.1.22, 3.10.3, 3.10.4, 3.10.5, and 3.12.4 must be closed before any Conditional status (32 CFR 170.21(a)(2)(iii)).

## 5. Deliverables
`assessment-results.csv` (41 rows), `poam.csv` (19 items), and this memo. Accepted by the owner on 2026-08-31. Because independence is limited, POL-01 4.5 requires the CMMC consultant's review before every SPRS entry or affirmation.

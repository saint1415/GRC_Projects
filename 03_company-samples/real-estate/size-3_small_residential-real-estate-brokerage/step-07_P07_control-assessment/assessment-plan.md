# Security Assessment Plan and Summary: Cris Santos Company | Real Estate | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (residential real estate brokerage with property management and an in-house Closing Services division) |
| System assessed | Transaction Management and Closing Communications System (TMCC), per the SSP (P02) |
| Tier / Vertical | Small / Real Estate and Rental and Leasing |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor, not involved in operating or designing the controls. Escorted by the IT Manager |
| Assessment window | 2026-08-24 to 2026-08-28 (office walkthroughs 2026-08-25) |
| Also satisfies | FTC Safeguards Rule 16 CFR 314.4(d)(1) (regularly test or monitor the effectiveness of key controls) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 141 determination statements.** Controls were chosen because they defend against the three High risks in P01 (diverted closing funds and unrecoverable data), or because they map to Safeguards Rule elements rated Not met or Partially met in P03.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| IA-2, IA-2(2), CM-6 | Contractor agents without MFA; legacy protocols (314.4(c)(5)); R-001, R-018 | Focused | Focused (contractor and employee test accounts) |
| AC-4, AU-6, SI-4 | No monitoring of mailbox rules or sign-ins (314.4(c)(8)); R-001, R-003 | Focused | Focused |
| AC-5, AT-3 | Wire approval and verification of payoffs and changed instructions (Fla. Stat. 626.8473(4); r. 61J2-14.010(1)); R-002, R-033 | Focused | Focused (all three escrow accounts) |
| AC-2, AC-6, PS-7 | Contractor account lifecycle and office-wide visibility (314.4(c)(1)); R-007 | Focused | Focused (sample of 12 departures) |
| AT-2, IR-4, IR-6 | Training and incident capability (314.4(e), (h)); the undocumented March 2026 near miss | Basic | Focused |
| CP-4, CP-9 | Backup isolation and restore (314.4(h)); R-006 (High) | Focused | Focused |
| RA-3, RA-5 | Risk assessment and vulnerability management (314.4(b), (d)(2)) | Basic | Basic |
| SA-9 | Service provider oversight (314.4(f)); R-013 | Basic | Focused (6 key contracts) |
| SC-8, SC-28, PE-3 | Encryption (314.4(c)(3)) and physical protection of paper and the storage device; R-011, R-012, R-016 | Basic | Focused (both offices) |

## 2. Methods and objects
- **Examine:** identity provider and productivity suite exports, mailbox rule export, bank approval settings for the three escrow accounts, backup reports, six key contracts, the independent contractor agreement, training roster, the P01 risk register, and walkthrough notes.
- **Interview:** COO, IT Manager, Controller, Closing Services Manager and 3 closers, both Sales Managers, the MSP lead technician, 8 employees, and 6 contractor agents (reporting awareness and wire instruction handling).
- **Test:**
  - sign-in tests with a contractor test account (password only, then a legacy mail client);
  - least-privilege test: what a contractor account can open in the transaction platform;
  - a simulated external forwarding rule and an out-of-country test sign-in, to see whether any alert fires;
  - a TLS scan of the portal and SaaS endpoints, and a header review of 20 outbound closing packages;
  - a review of every mailbox's inbox rules.

## 3. Rules of engagement
- No test touched live wires, bank sessions, or client funds. Bank settings were examined from exports and screenshots taken by the Controller.
- Test accounts were created for the assessment and removed on 2026-08-28.
- No customer information left company systems. Screenshots were redacted.
- The assessor stopped and notified the IT Manager on finding any active exposure. This happened once (below).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 32 |
| Other than satisfied | 109 |
| **Total** | **141** |

**Fully other than satisfied (no statement satisfied):** IA-2(2), AC-4, AC-5, AC-6, AT-3, AU-6, CP-4, IR-4, IR-6, PS-7, RA-5, SA-9, SC-8, SC-28, SI-4. For these, no process or technology met the objective at assessment time. IR-4 and IR-6 improved on 2026-09-21, when POL-03 and the P08 runbook were approved, but the capability has not yet been exercised.
**Largely satisfied:** RA-3 (the 2026 risk assessment; only the review cycle was missing), AC-2 provisioning and authorization (14 of 26 statements), PE-3 entry control and visitor escort.

**New finding: five contractor mailboxes auto-forwarding to personal webmail.** The inbox rule review on 2026-08-26 found five contractor agents' mailboxes forwarding all mail, including wire instructions and closing documents, to personal webmail accounts (AC-4). The assessor notified the IT Manager the same day. The rules were not known before testing. The finding was added to the risk register as R-032 and to POAM-006; the IT Manager is reviewing what was forwarded to decide whether a notification event occurred (P08 section 6).

**What the tests showed about the main threat.** A password alone opened a contractor mailbox and the transaction platform; a legacy mail client bypassed MFA settings entirely; a new forwarding rule and a foreign sign-in raised no alert; and 2 of 3 closers said they would call the phone number printed in a payoff letter. Together these are the conditions for the business email compromise scenario in P08.

All 22 controls have weaknesses and each has a POA&M item in `poam.csv` (POAM-001 to POAM-022). Six more items (POAM-023 to POAM-028) carry gaps from P03 that the assessed controls did not cover. The High items are POAM-001 to POAM-004 and POAM-028.

| POA&M risk level | Items |
|---|---|
| High | 5 |
| Moderate | 21 |
| Low | 2 |
| **Total** | **28** |

## 5. Deliverables
`assessment-results.csv` (141 rows), `poam.csv` (28 items), this plan and summary. The results were accepted by the COO on 2026-09-21.

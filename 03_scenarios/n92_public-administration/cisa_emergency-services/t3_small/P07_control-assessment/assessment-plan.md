# Security Assessment Plan and Summary: Cris Santos Company | Emergency Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensed private ambulance service) |
| System assessed | Dispatch and Patient Care Platform (DPCP), per the SSP (P02) |
| Tier / Vertical | Small / Emergency Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in operating or designing the controls. Escorted by the IT Manager |
| Assessment window | 2026-08-10 to 2026-08-14 (walkthrough of headquarters, Station 2, and two ambulances on 2026-08-12) |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8) (C-EMERGENCY-R04) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **22 controls, 163 determination statements.** Controls were chosen because they support the High and Very High risks in P01 (dispatch continuity, backups, remote access, detection), cover the Required HIPAA implementation specifications with gaps in P03, or address emergency-services concerns (CAD attribution, alternate dispatch site, vehicle devices).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-6, IA-2, IA-2(1), IA-5 | Access control gaps (P03 164.308(a)(3)-(4), 164.312(a), (d)); shared CAD logins; R-005, R-006, R-022 | Focused | Focused |
| AT-2 | Training gap (164.308(a)(5)); R-011, R-024 | Basic | Focused |
| AU-6, AU-9 | No log review (164.308(a)(1)(ii)(D)); CAD time edits (R-028) | Basic | Basic |
| CP-2, CP-4, CP-7, CP-9 | Contingency gaps (164.308(a)(7)); R-001 (Very High), R-002 and R-009 (High) | Focused | Focused |
| IR-4, IR-6 | No incident capability (164.308(a)(6)) | Focused | Basic |
| RA-3, RA-5 | Risk analysis and vulnerability management | Focused | Basic |
| SA-9 | Missing BAAs (164.308(b)); R-012, R-013, R-021 (High) | Focused | Focused |
| SC-7, SC-28 | Boundary and encryption (164.312(a)(2)(iv), (e)) | Basic | Focused |
| SI-2, SI-3, CM-6 | Patching, malware, and configuration; R-001, R-004, R-032 | Focused | Focused |

## 2. Methods and objects
- **Examine:** identity provider, ePCR, and CAD user exports; backup and patch reports; database and vault settings; BAAs and contracts, including the AI triage order form; training roster; the 2023 payer questionnaire and the 2026 risk register; the manual dispatch binder; walkthrough notes.
- **Interview:** COO, IT Manager, MSP lead technician, Communications Center Supervisor, Privacy Officer, HR Manager, Operations Manager, and 10 randomly selected staff (4 crew members, 4 dispatchers, 2 billing staff) on incident reporting.
- **Test:**
  - console and MDC sign-in tests, and a CAD administrator sign-in
  - local admin password comparison on 8 workstations
  - credential and exposure check on vehicle routers, with the MSP present and the unit out of service
  - an antivirus test alert on the CAD server to check alert routing
  - an internal network reachability test from the crew lounge Wi-Fi
  - an edit-history test on 5 CAD incidents

## 3. Rules of engagement
- **No testing that could disrupt dispatch.** No tests ran on live dispatch consoles during calls. Router tests used one ambulance at a time, out of service, with a spare unit covering. The Communications Center Supervisor could stop any test at once.
- No ePHI was copied off-site. Screenshots were redacted.
- The assessor stopped and notified the IT Manager on finding any critical exposure. **This happened once** (see below).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 45 |
| Other than satisfied | 118 |

**Fully other than satisfied (11 controls):** AC-6, IA-2, IA-2(1), AU-6, AU-9, CP-2, CP-4, CP-7, IR-6, RA-5, SC-28. For these, no plan, process, or technology met any determination statement.
**Largely satisfied:** AC-2 (account creation and authorization) and RA-3 (now that the 2026 analysis exists).
**Half satisfied:** CP-9 (backup frequency and confidentiality are fine; isolation and immutability are not) and SC-7 (external boundary rules are fine; internal separation is not).

**Critical new finding (2026-08-12):** 3 of 9 vehicle routers exposed web administration to the internet with the manufacturer default password (IA-05e.). This was not known before testing. The assessor stopped and notified the IT Manager, who disabled remote administration and changed the passwords on 2026-08-14. It was added to the risk register as R-007 (High) and to POAM-012.

All 22 controls have POA&M items in `poam.csv`. The 6 High items are POAM-002, POAM-004, POAM-005, POAM-006, POAM-012, and POAM-014.

## 5. Deliverables
`assessment-results.csv` (163 rows), `poam.csv` (22 items), this plan and summary. The results were accepted by the COO on 2026-09-04.

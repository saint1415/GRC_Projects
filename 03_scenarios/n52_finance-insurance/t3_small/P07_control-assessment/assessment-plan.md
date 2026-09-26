# Security Assessment Plan and Summary: Cris Santos Company | Finance and Insurance | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Bank, N.A. (community commercial bank) |
| System assessed | Wire and Digital Banking Platform (WDBP), per the SSP (P02), plus the bank-managed access controls of the core banking system (SYS-01) and the program-level controls the WDBP inherits from the bank |
| Tier / Vertical | Small / Finance and Insurance |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | IT audit team of the outsourced internal audit firm (a CPA firm). Not involved in operating or designing the controls. Escorted by the IT Manager (ISO) |
| Assessment window | 2026-08-03 to 2026-08-07 (walkthrough of the main office, the wire room, and two branches on 2026-08-05) |
| Also satisfies | Testing of key controls under the Interagency Guidelines, 12 CFR 30 App. B III.C.3 (N52-R02), and input to the annual board report (III.F) |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **21 controls, 153 determination statements.** Controls were chosen because they support the five High risks in P01, cover the Guidelines provisions with High or Moderate gaps in P03, or support the notification rule duties of 12 CFR Part 53.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-6, PS-4 | No core access reviews; super users unreviewed (P03 G-012; III.C.1.a); R-005 | Focused | Focused (full 12-month separation list) |
| AC-5 | Approvers maintain templates (P03 G-017; III.C.1.e); R-019 (High) | Focused | Focused |
| IA-2, IA-2(1), IA-5, IA-8 | Customer MFA optional (P03 G-004); R-002 (High), R-029 | Focused | Focused |
| AT-2 | Callbacks skipped; no BEC training (P03 G-013, G-021); R-001 (High), R-026 | Focused | Focused (25 branch wires, all 6 branches) |
| AU-6, SI-4 | No log review; no beneficiary change alerts (P03 G-018); R-009, R-027 | Focused | Focused |
| CM-3 | Wire limits changed by email (P03 G-016) | Basic | Focused (10 changes) |
| CP-4, CP-9 | Alternate wire procedure untested; backups not isolated (P03 G-020); R-004 (High), R-010 | Focused | Focused |
| IR-4, IR-6, IR-8 | No 36-hour OCC notice step (P03 G-039 to G-042); R-006 | Focused | Basic |
| PM-9, RA-3 | No board risk appetite (P03 G-007, G-009); R-008 | Basic | Basic |
| RA-5 | No routine scanning (P03 G-022); R-021 | Basic | Basic |
| SA-9 | SOC reports not reviewed (P03 G-026); R-007, R-032 | Focused | Focused (4 critical providers) |

## 2. Methods and objects
- **Examine:** identity provider, admin console, wire platform, and core user exports; the HR separation list for the last 12 months; wire platform role matrix and audit trail; a sample of 25 branch-originated wires (callback evidence); 10 admin console limit changes; backup job reports and vault settings; contracts and vendor files for 4 critical providers; the 2023 incident response plan; the 2025 risk assessment; board minutes; training roster and content.
- **Interview:** President and CEO, COO, ISO, Deposit Operations Manager, Treasury Management Officer, BSA/AML Officer, HR Director, all six Branch Managers, and 12 randomly selected branch staff (incident and fraud reporting awareness).
- **Test:**
  - comparison of the core user list with the HR separation list (found 4 enabled accounts of former employees)
  - self-approval attempt in the wire platform's test mode (blocked)
  - administrator sign-in with a hardware key, and password-only sign-in (refused)
  - a password-only business test user adding a new wire beneficiary (succeeded, no second factor asked)
  - a test call to the help desk requesting a customer password reset
  - a limit change on a test customer to check alerting (no alert)
  - deletion of a test backup by a production administrator (succeeded)

## 3. Rules of engagement
- No live wires or customer transactions were created. All payment and online banking tests used the providers' test environments or bank test customers, with the Deposit Operations Manager present.
- No customer information was copied off-site. Screenshots were redacted.
- The assessor stopped and notified the ISO on finding any critical exposure. The 4 enabled accounts of former employees were reported the same day and disabled on 2026-08-07.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 71 |
| Other than satisfied | 82 |
| **Total** | **153** |

Other than satisfied statements by risk level: 10 High, 50 Moderate, 22 Low.

**Fully other than satisfied (7):** AC-5, AC-6, AU-6, CP-4, IA-8, IR-6, PM-9. No working process or technical setting existed for these.
**Fully satisfied (2):** IA-2 (unique workforce identification) and IA-2(1) (hardware-key MFA for administrators).
**Largely satisfied:** IR-4 detection, containment, and recovery by the MSSP and IT; CP-9 backup creation and encryption; PS-4 exit steps.

**New finding:** 4 enabled core banking accounts belonged to employees who left the bank 2 to 11 months earlier (AC-02f.[04], PS-04a.). This was not known before testing. The accounts were disabled on 2026-08-07, the risk register was updated (R-005, 2026-08-07), and the fix is tracked in POAM-001 and POAM-013. Core activity logs for the 4 accounts after each separation date were requested from the core processor; the core processor's report showed no sign-ins.

**Most important result:** the controls that stop fraudulent wires exist on paper but are not enforced. The callback standard is skipped at 2 branches (AT-2), password-only customers can add beneficiaries (IA-8), approvers can edit templates (AC-5), and nobody is alerted to beneficiary or limit changes (SI-4). All four are High.

All 19 controls with weaknesses have POA&M items in `poam.csv`: 5 High (POAM-002, POAM-005, POAM-006, POAM-007, POAM-011), 13 Moderate, and 1 Low.

## 5. Deliverables
`assessment-results.csv` (153 rows), `poam.csv` (19 items), and this plan and summary. The Audit and Risk Committee reviewed the results on 2026-08-27, and the President and CEO accepted them on 2026-08-31.

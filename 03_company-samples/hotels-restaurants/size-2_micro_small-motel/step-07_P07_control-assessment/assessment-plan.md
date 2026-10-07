# Security Assessment Plan and Summary: Cris Santos Company | Accommodation and Food Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 38-unit roadside motel) |
| System assessed | Motel Property Management and Point-of-Sale System (MPPS), per the SSP (P02) |
| Tier / Vertical | Micro / Accommodation and Food Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent security consultant with payment card experience, under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Not a QSA; this is not a PCI DSS assessment. Accompanied by the Assistant Manager; MSP lead technician on site for tests |
| Assessment window | 2026-08-03 to 2026-08-05 (on site 2026-08-04) |
| Also supports | The 2026 PCI DSS self-assessment (evidence for requirement groups 7, 8, 9, 11, and 12) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **14 controls, 93 determination statements.** Controls were chosen because they support the four High risks in P01 (lock vendor remote access, stored card forms, the lock database, and emergency pricing, where only the vendor-governance part is a control here), cover High PCI DSS gaps in P03, or test what the MSP does for the motel.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2 | Shared logins and stale accounts (P01 R-006, R-007; P03 8.2) | Focused | Comprehensive (every account in the PMS, suite, gateway portal, lock system, and Windows) |
| AC-6 | Full card number display for all front office users (R-005; P03 3.4, 7.2) | Focused | Comprehensive |
| AC-17, IA-2(1) | Lock vendor remote tool; MFA on administrator logins (R-001; P03 8.4) | Focused | Focused (lock tool, MSP tool, firewall, gateway portal, backup console) |
| SC-7 | Flat office network (R-008; P03 1.3) | Focused | Focused (scan from the front desk PC; guest-room test) |
| SI-3, RA-5 | Malware protection and scanning on the PC where card numbers are keyed (R-001, R-002; P03 5, 11.3) | Basic | Focused (front desk PC test; after-hours alert test) |
| AU-6 | No log review (R-005; P03 10.4) | Basic | Basic |
| AT-2, IR-6 | No training; no reporting rule (R-016, R-017; P03 12.6, 12.10) | Basic | Focused (5 of 7 employees interviewed) |
| CP-9 | Backups that check-in depends on (R-009, R-012) | Focused | Comprehensive (job selection list reviewed line by line) |
| MP-4 | Paper card forms (R-004; P03 9.4) | Focused | Comprehensive (binder count) |
| SA-9 | Provider oversight (R-020; P03 12.8) | Focused | Comprehensive (all 8 providers that touch card data or administer systems) |
| CM-8 | Terminal list and inventory (R-019; P03 9.5, 12.5) | Basic | Comprehensive (walkthrough device count) |

## 2. Methods and objects
- **Examine:** user and permission lists for the PMS, suite, gateway portal, and lock system; the HR roster; firewall rule export; backup job report and selection list; MSP contract and monthly reports; antivirus console export; PMS vendor and gateway AOCs; P2PE Instruction Manual; the crew billing binder; P01 risk register.
- **Interview:** Owner-Manager, Assistant Manager, 5 of 7 employees (training, reporting, and caller handling), and the MSP lead technician.
- **Test:**
  - user lists compared against the HR roster in the PMS, suite, gateway portal, and lock system
  - a test front office PMS account attempting to display a full virtual card number
  - sign-in attempts to the firewall management page, gateway portal, and backup console without a second factor (with the MSP present)
  - a connection request through the lock vendor's remote tool (with the lock vendor on the phone)
  - a network scan from the front desk PC and a reachability test from a guest room
  - a harmless industry-standard antivirus test file on the front desk PC, and an after-hours test alert to check routing
  - a device walkthrough count, including terminal serial numbers

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-07-27 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2, RA-5 | Yes, 2026-07-31 |
| Antivirus console export (all devices) | SI-3 | Yes, 2026-07-31 |
| Firewall rule export and log settings | SC-7, AU-6 | Yes, 2026-07-31 |
| Backup job report, selection list, and retention settings | CP-9 | Yes, 2026-08-03 |
| Record of any restore test | CP-9 | No record exists (confirmed by the MSP) |
| Device encryption report | SC-28 | Yes, 2026-07-31 |
| Technician list and evidence of MFA on the remote management platform | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-013 |
| MSP security questionnaire | SA-9 | Not received by fieldwork end; follow-up in POAM-013 |

## 3. Rules of engagement
- No testing that could disrupt guests or payments. On-site tests ran between 10:00 and 14:00 on 2026-08-04, after checkout and before arrivals. The terminals were inspected but not opened or changed.
- No card data or guest personal information left the motel. Screenshots were redacted before they went into the evidence folder; the binder was counted, not copied.
- The assessor would stop and tell the Owner-Manager at once about any critical exposure. The lock tool finding and the binder were reported the same day, and both had first fixes by 2026-08-05.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 19 |
| Other than satisfied | 74 |
| **Total** | **93** |

**Fully other than satisfied (8 of 14 controls):** AC-6, AC-17, IA-2(1), RA-5, AU-6, AT-2, SA-9, IR-6. No process or technology met the objective. That is expected for a motel that had no written security program before July 2026.
**Largely satisfied:** SI-3 (detection and quarantine work; after-hours alerting does not) and SC-7 at the boundary (inbound traffic blocked, guest Wi-Fi properly separated; the office network inside is flat).

**New findings from testing:**
1. 2 former employees (left 2026-03 and 2026-05) still had active PMS accounts (AC-02f.[04]). Their activity logs showed no sign-ins after their last day. Disabled on 2026-08-04. Added to the risk register as R-006.
2. The backup job excluded the lock software's database folder (CP-09b.). The MSP added it on 2026-08-12. R-009 raised.
3. The lock vendor's tool accepted a connection request with no prompt at the motel (AC-17b.). Set to manual start on 2026-08-05. POAM-003.
4. The binder held 410 forms, about 160 with security codes (MP-04b.). Moved to a locked drawer on 2026-08-05. POAM-002.
5. Two of five staff interviewed said they would give a password to a caller from "PMS support" (AT-02b.). POAM-011.

All 14 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-001, POAM-002, POAM-003, and POAM-010: shared and stale accounts, stored card forms, vendor remote access, and the lock database backup.

## 5. Deliverables
`assessment-results.csv` (93 rows), `poam.csv` (14 items: 4 High, 10 Moderate), and this plan and summary. The Owner-Manager accepted the results on 2026-08-31.

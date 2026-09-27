# Security Assessment Plan and Summary: Cris Santos Company | Other Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (electronics and device repair service) |
| System assessed | Service Ticketing and Point-of-Sale Platform (STPP), per the SSP (P02) |
| Tier / Vertical | Small / Other Services (except Public Administration) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor, not involved in operating or designing the controls. Escorted by the IT Manager; store visits with each Store Manager |
| Assessment window | 2026-08-10 to 2026-08-14 (store and Depot visits 2026-08-11 and 2026-08-12) |
| Also supports | NIST CSF 2.0 ID.IM-01; evidence for the 2026 SAQ P2PE and the Manufacturer A program audit |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **23 controls, 158 determination statements.** Controls were chosen because they address the four High risks in P01, the High gaps in P03, the SAQ P2PE requirements with gaps, or the Manufacturer A program terms.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-3, AC-6, MP-7, PS-6 | Technician and staff access to customer data and devices (R-001, R-002; P03 G-057, G-063, G-016) | Focused | Focused (3 benches, 6 technicians) |
| AC-2, IA-2, IA-2(1), IA-5 | Shared logins, former employees, default passwords (R-003, R-009, R-015) | Focused | Focused (all sites) |
| SI-12, SC-28 | Retention and encryption of recovered data and passcodes (R-006) | Focused | Focused |
| CP-2, CP-4, CP-9 | Backups and recovery (R-014, High) | Focused | Basic |
| MP-6 | Sanitization of recycling devices (R-007; Fla. Stat. 501.171(8)) | Focused | Focused (bins at 2 stores) |
| CM-8 | Inventory and payment terminal list (PCI DSS 9.5.1.1) | Basic | Focused |
| IR-6, IR-8 | No incident capability (R-016, R-025) | Basic | Basic |
| AT-2, AU-6 | Training and log review | Basic | Basic |
| RA-5, SC-7, SI-3 | Scanning, flat networks, bench PC malware protection (R-008, R-018, R-019) | Basic | Focused |
| SA-9 | Vendor terms for AI vendors, recycler, and courier (R-011) | Focused | Focused |

## 2. Methods and objects
- **Examine:** identity provider and SYS-01 user and role exports, the SYS-01 field search results, backup and patch reports, contracts and the processor AOC, training records, HR files, recycler certificates, the lab storage listing, and the draft POL-03 and P08.
- **Interview:** General Manager, IT Manager, Operations Manager, Controller, Data Recovery Lead, HR and Payroll Specialist, all 4 Store Managers, 6 technicians, and 8 randomly selected staff (incident reporting awareness).
- **Test:**
  - sign-in as a counter user to see which ticket fields are visible
  - sign-in tests on counter tablets, bench PCs, and the Manufacturer A portal at Store B
  - local password comparison on 6 bench PCs
  - sign-in to the lab storage console with the vendor default credentials, with the Data Recovery Lead's approval and after hours
  - USB storage insertion at 3 benches
  - a network reachability scan from a bench PC at Store A
  - 3 devices pulled from a recycling bin and powered on to check for data (no content was opened beyond the lock screen or setup screen)
  - a count of payment terminals against the processor's list

## 3. Rules of engagement
- No customer device content was opened or copied. Tests on customer devices stopped at the lock screen or setup screen.
- No customer data left the company. Screenshots were redacted.
- The assessor stopped and notified the IT Manager on finding any critical exposure. One was found (the lab storage default password) and reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 46 |
| Other than satisfied | 112 |

**Fully other than satisfied:** AC-3, AC-6, AU-6, CP-2, CP-4, IA-2, IR-6, MP-7, PS-6, RA-5, SC-28, SI-12. No rule, process, or technology existed for these.
**Largely satisfied:** IA-2(1) (administrator MFA), IR-8 (the draft plan's content), SC-7 at the external boundary, SI-3 on office PCs, and AC-2 account creation and approval.

**What the tests showed about customer data:**
- A counter user account could read passcodes and account passwords on any ticket (AC-03).
- A technician opened a customer's photo library to test a screen repair, which the test checklist would not require (AC-06).
- One of three phones taken from a recycling bin still held the previous owner's data (MP-06a.[01]).
- Unencrypted USB drives mounted on every bench PC tested (MP-07a.).

**New finding:** the lab storage array's web console accepted the vendor default administrator password and was reachable from the store networks over the VPN (IA-05e., SC-07a.[04]). This was not known before testing. It was added to the risk register as R-031 and to POAM-009. The password was changed and the console restricted to the IT Manager's workstation on 2026-08-31.

All 22 controls with weaknesses have POA&M items in `poam.csv`. IA-2(1) had none. The High items are POAM-001 to POAM-005.

## 5. Deliverables
`assessment-results.csv` (158 rows), `poam.csv` (22 items), and this plan and summary. The results were accepted by the General Manager on 2026-09-04.

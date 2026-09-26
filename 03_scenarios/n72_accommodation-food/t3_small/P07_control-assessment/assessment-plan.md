# Security Assessment Plan and Summary: Cris Santos Company | Accommodation and Food Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent 140-room beachfront hotel) |
| System assessed | Property Management and Point-of-Sale Platform (PMPS), per the SSP (P02) |
| Tier / Vertical | Small / Accommodation and Food Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in operating or designing the controls, and not the hotel's MSP. Escorted by the IT Manager |
| Assessment window | 2026-08-03 to 2026-08-07 (hotel walkthrough and after-hours tests 2026-08-05) |
| Also supports | Evidence for the 2026 PCI DSS SAQ D (MID-1) and SAQ P2PE (MID-2). This is **not** a PCI DSS assessment by a QSA |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **23 controls, 156 determination statements.** Controls were chosen because they support the five High risks in P01, cover the High PCI DSS gaps in P03, or test practices named in *FTC v. Wyndham* (default passwords, network separation, vendor access, monitoring).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, AC-6, IA-2, IA-2(1), IA-5 | PMS account and card-display gaps (P03 rows 7.2, 8.2, 8.4); R-004, R-009 | Focused | Focused |
| AC-17 | Vendor remote access (P03 row 8.4); R-005 (High) | Focused | Focused |
| SC-7 | Flat network (P03 row 1.3); R-003 | Focused | Focused |
| SC-8, SC-28, MP-4, SI-12 | Stored card data in email and paper; retention (P03 rows 3.2, 3.5, 4.2, 9.4; G-078); R-002 (High), R-020 | Focused | Comprehensive (both shared mailboxes, full binder) |
| SI-2, SI-3, CM-6, CM-8 | Unsupported lock server, malware, configuration, inventory (P03 rows 2.2, 5.2, 6.3, 12.5); R-001, R-006 | Focused | Focused |
| RA-5 | No scans; ASV scans needed for SAQ D (P03 row 11.3) | Basic | Basic |
| AU-6 | No log review (P03 row 10.4); R-026 | Basic | Basic |
| IR-6, IR-8 | No incident capability (P03 row 12.10); R-025 | Focused | Basic |
| CP-9 | Backups and recovery; R-017 | Focused | Focused |
| AT-2 | No training since 2021 (P03 row 12.6); R-019 | Basic | Focused |
| SA-9 | Service provider management (P03 row 12.8); R-022 | Focused | Comprehensive (9 providers) |
| PE-3 | Server room and back office access (P03 row 9.2) | Basic | Focused |

## 2. Methods and objects
- **Examine:** identity provider and PMS user and permission exports, firewall rule export, patch and anti-malware reports, backup reports, vendor contracts and AOC files, the 2025 SAQs, training records, the front desk card-form binder, and a search of the reservations and sales mailboxes.
- **Interview:** General Manager, Controller, IT Manager, MSP lead technician, Front Office Manager, Chief Engineer, HR Manager, and 8 randomly selected staff (incident reporting and phishing awareness).
- **Test:**
  - sign-in tests on front desk PCs and the PMS, including a front desk agent account display test for full card numbers
  - an MFA test on an administrator account
  - a network scan from a back office PC to see what it can reach
  - a default-credential test on the lock server, approved by the lock vendor and run after midnight with the Chief Engineer present
  - a test file for anti-malware detection and alert routing
  - a single-file restore from the cloud backup vault
  - a TLS scan of external services

## 3. Rules of engagement
- No testing that could lock guests out of rooms. The lock server test ran after midnight with the Chief Engineer present and emergency key cards ready.
- No card data was copied, photographed, or removed. Mailbox search results were counted, not exported. The binder was counted in place.
- The assessor would stop and notify the IT Manager on finding any critical exposure. The lock server default password was reported to the IT Manager the same night (2026-08-05).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 40 |
| Other than satisfied | 116 |

**Fully other than satisfied:** AC-6, AC-17, AT-2, AU-6, CM-6, IA-2(1), IR-6, IR-8, RA-5, SA-9, SC-8, SC-28, SI-12. For these, no plan, process, or technology existed at fieldwork.
**Partly satisfied (satisfied statements shown):** PE-3 building access through the hotel lock system (6 of 12), SI-3 detection and quarantine on PCs (5 of 8), CP-9 backup execution and encryption (3 of 6), and IA-2 unique identity-provider accounts (1 of 2).

**New finding:** the lock server still uses the lock vendor's default administrator password (IA-05e.). It was not known before testing. It was added to the risk register as R-007 and to POAM-005, and the password is scheduled to be changed by 2026-09-15. This is the same kind of weakness the FTC alleged in *Wyndham* (default user IDs and passwords on hotel servers).

All 23 controls have at least one weakness and a POA&M item in `poam.csv`: 13 High, 9 Moderate, and 1 Low. The High items are POAM-001 to POAM-013.

## 5. Deliverables
`assessment-results.csv` (156 rows), `poam.csv` (23 items), this plan and summary. The results were accepted by the General Manager on 2026-08-31.

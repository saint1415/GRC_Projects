# Security Assessment Plan and Summary: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (radioactive and hazardous waste processor) |
| System assessed | Business Operations and Records Platform (BORP), per the SSP (P02), including the PACS server, NVR, and cameras while they sit on the business network |
| Tier / Vertical | Small / Nuclear Reactors, Materials, and Waste |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in operating or designing the controls. Escorted by the IT Manager; the RSO attended the Part 37 information tests |
| Assessment window | 2026-08-03 to 2026-08-07 |
| Also supports | The 2026 Part 37 security program review (10 CFR 37.55) for its electronic systems and information protection scope |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **20 controls, 141 determination statements.** Controls were chosen because they support the five High risks in P01, the High gaps in P03, or the Part 37 information and records duties (37.31, 37.43(d), 37.49(c), 37.101).

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-3, AC-6, MP-4 | Part 37 security-related information and background files (P03 G-018, G-031 to G-036); R-004, R-010 | Focused | Focused |
| AC-2, PS-4, IA-5, IA-2(1) | Account and badge removal (37.23(e)(5)); shared and default credentials; R-009, R-023 | Focused | Focused |
| AC-17, SA-9 | MSP and vendor access; vendor oversight; R-006, R-016, R-022 | Focused | Basic |
| SC-7, CM-8 | Segmentation of security systems and OT from the business network (37.49(c)); R-002, R-003 | Focused | Comprehensive (full VLAN scan) |
| CP-9, CP-4 | Records protection against loss (37.101); R-007 | Focused | Focused |
| SI-4, AU-6 | Detection and log review; R-001 | Focused | Basic |
| SI-2, RA-5 | Patching and firmware of security devices; R-014 | Basic | Focused |
| IR-4, IR-6 | Incident handling and Part 37 event reporting (37.57); R-019, R-020 | Focused | Basic |
| AT-2 | Awareness and phishing; R-001, R-026 | Basic | Focused |

## 2. Methods and objects
- **Examine:**
  - identity provider and SaaS exports
  - SYS-01 folder permission export
  - backup and patch reports
  - firewall rules and switch VLAN export
  - historian network settings
  - contracts (MSP, waste tracking, security system vendor, predictive maintenance vendor)
  - training roster
  - Part 37 procedures SEC-05 and TR-06
  - HR termination records
  - PACS badge report
- **Interview:** General Manager, IT Manager, RSO, HR Manager, Operations Manager, Maintenance and Controls Supervisor, the MSP lead technician, and 8 randomly selected staff (incident reporting awareness).
- **Test:**
  - sign-in to SYS-01 as a customer service test user, then an attempt to open the Radiation Safety folder
  - network scan of the business VLAN to compare with the inventory
  - default-credential test on business-VLAN devices, with the security system vendor's approval, outside operating hours, with the RSO present and the alarm company informed
  - dry-run deletion attempt against the backup vault with an administrator role (stopped at the confirmation prompt)
  - administrator sign-in with a hardware key
  - EDR alert routing test with the MSP

## 3. Rules of engagement
- No testing on the plant OT network, radiation monitors, or the vault IDS panel. These are outside the boundary, and active scanning can disrupt PLCs (SP 800-82 Rev. 3, Appendix E.2.3).
- No change to any security system setting during testing. The alarm company was told before the camera credential test so that no alarm would be misread.
- Part 37 security-related information seen during tests was not copied or photographed. The finding records only file names and permission counts.
- The assessor stopped and notified the IT Manager and RSO on finding any exposure that could weaken vault protection. One such item was found (default camera passwords), and the RSO applied a compensating measure the same day: an extra camera check at each shift walk-down.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 53 |
| Other than satisfied | 88 |

**Fully other than satisfied:** AC-3, AC-6, AU-6, CP-4, IR-6, and RA-5. No process or technology existed for these.
**Largely satisfied:** IA-2(1) (hardware-key MFA for administrators), AC-2 account creation and authorization, IA-5 password strength, and CP-9 backup frequency and encryption.

**Key finding (AC-03).** A customer service test account opened the Part 37 security plan and the approved-individuals list. This is the single most important result, because it is a direct gap against 10 CFR 37.43(d)(1) and (3).

**New finding:** 5 IP cameras on the business network accept the manufacturer's default admin password (IA-05e.). This was not known before testing. It was added to the risk register as R-031 and to POAM-009. The passwords are scheduled to be changed by 2026-09-15.

All 19 controls with weaknesses have POA&M items in `poam.csv`. The High items are POAM-001 to POAM-005.

## 5. Deliverables
`assessment-results.csv` (141 rows), `poam.csv` (19 items), and this plan and summary. The results were accepted by the General Manager on 2026-08-31. The RSO will include the Part 37-related findings in the 2026 security program review (37.55), due 2026-10-31.

# Security Assessment Plan and Summary: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (radiation safety consulting practice) |
| System assessed | Practice Business Platform (PBP), per the SSP (P02) |
| Tier / Vertical | Micro / Nuclear Reactors, Materials, and Waste |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent cybersecurity consultant under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager; MSP lead technician on call; the owner present for every test that opened client folders |
| Assessment window | 2026-08-24 to 2026-08-26 (on site 2026-08-25) |
| Criteria | P02 control statements; POL-02, POL-03, POL-04 (the assessor used the final drafts of 2026-08-21, approved unchanged on 2026-09-15); Part 37 client contract terms |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **14 controls, 85 determination statements.** Controls were chosen because they support the three High risks in P01 (client security information, media carried into reactor plants, MSP compromise), cover the High and Moderate Part 37 gaps in P03, or test what the MSP does on the practice's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Departed Health Physicist kept SYS-02 access; clients told late (P01 R-005; P03 G-015) | Focused | Comprehensive (all accounts in the suite, SYS-02, SYS-03, backup console, firewall) |
| AC-3, AC-21 | Client security information open to all staff and shared by public links (R-001, R-004, R-006; G-010, G-013, G-019) | Focused | Comprehensive (all 6 Part 37 folders) |
| IA-2(1) | MFA on administrator access, including MSP-held logins (R-013; G-036) | Focused | Focused |
| AT-2, IR-6 | No training; no reporting rule; client clocks (R-007, R-014; G-020, G-038) | Basic | Focused (5 of 7 staff interviewed) |
| CP-9, CP-4 | Backups untested, not immutable; no SYS-02 export (R-010, R-015; G-040) | Focused | Focused |
| MP-7 | USB drives carried to reactor plants (R-003; G-021) | Focused | Comprehensive (all drives in use and the shared field kit) |
| SC-28 | Unencrypted lab workstations and drives (R-011; G-039) | Basic | Focused (7 devices checked) |
| SI-2 | Lab workstations excluded from patching (R-009; G-041) | Focused | Focused (2 laptops, both lab workstations, firewall) |
| SA-9 | No supplier terms or oversight (R-013, R-016; G-029, G-030) | Basic | Comprehensive (MSP, backup subcontractor, SYS-02 vendor) |
| RA-3 | First risk assessment (G-034) | Basic | Basic |

## 2. Methods and objects
- **Examine:** suite, SYS-02, SYS-03, backup console, and firewall user lists; suite permission, sharing, and audit log reports; tenant sharing settings; client approval letters and contracts; departure records; MSP contract; SYS-02 terms and SOC 2 report; P01 risk register; training records; the MSP evidence listed below.
- **Interview:** owner, Office Manager, Part 37 services lead, field services lead, Calibration Laboratory Technician, 5 of 7 staff (training and incident reporting), and the MSP lead technician.
- **Test:**
  - user lists compared with the staff roster in every system
  - with the owner present, a sign-in as the Project Coordinator to check which Part 37 folders open (the assessor did not open any document)
  - sign-in attempts to the firewall management page, the backup console, and SYS-02 administrator accounts without a second factor (with the MSP present)
  - encryption status on 2 laptops, both lab workstations, and 3 USB drives
  - patch status on 2 laptops and both lab workstations; review of the firewall rule export
  - inspection of every USB drive in use and in the shared field kit

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-08-17 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-08-21 |
| Antivirus console export (all devices) | P02 SI-3 statement | Yes, 2026-08-21 |
| Device encryption report | SC-28 | Yes, 2026-08-21 |
| Backup job report (July 2026), retention settings, console user list | CP-9 | Yes, 2026-08-24 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Firewall rule export and firmware record | SI-2, AC-17 | Yes, 2026-08-21 |
| Technician list and evidence of MFA on the remote management platform | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-013 |
| Name of the backup subcontractor and its security terms | SA-9 | Name received; terms not received; follow-up in POAM-013 |

## 3. Rules of engagement
- **No client security information left the practice and the assessor read none.** The folder test confirmed only which folders opened; screenshots showed folder names redacted to client codes. The owner, who is approved by all 6 clients, sat with the assessor for the test.
- No testing that could disrupt calibration work. Lab workstation checks ran after the calibration queue closed on 2026-08-25. Nothing on the lab workstations was changed.
- The assessor would stop and tell the Office Manager at once about any critical exposure. The firewall port forward was reported, and removed by the MSP, the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 21 |
| Other than satisfied | 64 |
| **Total** | **85** |

**Fully other than satisfied:** AC-3, IA-2(1), AT-2, CP-4, IR-6, MP-7, SC-28. No process or technology met the objective.
**Largely satisfied:** RA-3 (6 of 8; the 2026 risk assessment meets every objective except review and update, which have not happened yet).
**Partly satisfied:** AC-2 (5 of 26; accounts are created properly but never reviewed, and departures are missed), CP-9 (3 of 6; nightly backups run, but versions are not immutable or long enough), SI-2 (3 of 10; laptop patching works, lab workstations are excluded), PS-4 (2 of 5), AC-21 (1 of 2), SA-9 (1 of 6).

**New findings from testing:**
1. An inbound remote desktop port forward on the office firewall, opened in 2024 for the gamma spectroscopy vendor, still reached lab workstation 2, which runs an unsupported operating system (SI-02a.[03]). The MSP removed it on 2026-08-25. Added to the risk register as R-023 and to POAM-012.
2. Two unlabeled USB drives in the shared field kit had no identifiable owner; one held outage survey templates (MP-07b.). They were withdrawn on 2026-08-26 for wiping. POAM-010.
3. The Project Coordinator's account opened all 6 clients' Part 37 folders (AC-03). This confirms the P03 finding by test. POAM-002.
4. The firewall management page accepted the shared MSP login with a password only (IA-02(01)). POAM-005.

All 14 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-002 (client folders), POAM-005 (MFA on MSP-held logins), POAM-007 (backups), and POAM-010 (media at client sites): the same themes as the High risks in P01.

## 5. Deliverables
`assessment-results.csv` (85 rows), `poam.csv` (14 items: 4 High, 9 Moderate, 1 Low), and this plan and summary. The owner accepted the results on 2026-09-15.

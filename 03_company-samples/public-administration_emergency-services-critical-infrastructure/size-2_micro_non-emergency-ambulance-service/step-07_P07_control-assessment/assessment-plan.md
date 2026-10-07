# Security Assessment Plan and Summary: Cris Santos Company | Emergency Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensed BLS ambulance service, non-emergency transport only) |
| System assessed | Transport Operations Platform (TOP), per the SSP (P02) |
| Tier / Vertical | Micro / Emergency Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent HIPAA security consultant with EMS experience, under a fixed-fee engagement. Did not take part in the risk analysis (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager; MSP lead technician on call |
| Assessment window | 2026-08-17 to 2026-08-19 (on site 2026-08-18) |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8) (C-EMERGENCY-R04) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **14 controls, 87 determination statements.** Controls were chosen because they support the three High risks in P01 (ransomware with a dispatch outage, platform credential theft, MSP compromise), cover Required HIPAA specifications with gaps in P03, or test what the MSP does on the company's behalf. The contingency plan itself (CP-2) was not assessed because it does not exist yet; it is tracked in P01 and P03 and will be assessed in 2027. Its testing (CP-4) was assessed because the gap there is what matters for dispatch.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Former EMT accounts active for months (P01 R-006; P03 164.308(a)(3)(ii)(C)) | Focused | Comprehensive (all staff and 23 facility portal accounts) |
| IA-2, IA-2(1) | Shared dispatch login; no MFA on the platform (164.312(a)(2)(i), (d)); R-002, R-007 | Focused | Comprehensive (platform, suite, backup console, firewall) |
| AC-11 | Dispatch desktop never locks (164.310(c)) | Basic | Focused (4 devices tested) |
| AT-2 | Training only at hire (164.308(a)(5)); R-015 | Basic | Focused (4 of 7 staff interviewed) |
| AU-6 | No log review (164.308(a)(1)(ii)(D)); R-002, R-022 | Basic | Basic |
| CM-7, CM-8 | Unknown devices and software at the edges (164.310(d)(2)(iii)); R-018 | Focused | Comprehensive (office and both ambulances) |
| CP-4, CP-9 | Backups never tested; manual dispatch never practiced (164.308(a)(7)(ii)(A), (D)); R-005, R-008 | Focused | Focused |
| SA-9 | Missing BAA, unreviewed AI terms, no vendor oversight (164.308(b)); R-003, R-004, R-013 | Focused | Comprehensive (all 6 vendors that handle ePHI or administer systems) |
| SC-28 | Unencrypted desktops (164.312(a)(2)(iv)); R-011 | Basic | Focused (4 devices tested) |
| SI-3 | MSP antivirus and after-hours alerting; R-001, R-016 | Focused | Focused (test file; after-hours alert) |

## 2. Methods and objects
- **Examine:** platform, suite, and phone user lists; facility portal user list; platform role list, security settings, access report, and export log; BAA folder; MSP contract; billing contract; AI feature terms; video sign-in sheet; the MSP evidence listed below.
- **Interview:** the Owner, the Office Manager, the Scheduler-Dispatcher, 2 EMTs, and the MSP lead technician.
- **Test:**
  - user lists compared with the staff roster and with facility contacts
  - sign-in at the dispatch desktop and the on-call phone (shared account)
  - sign-in attempts to the backup console and firewall management login without a second factor (with the MSP present)
  - idle lock on 4 devices
  - encryption status on 2 desktops, the laptop, and 1 tablet
  - an industry-standard harmless antivirus test file on the Office Manager desktop, and an after-hours test alert at 6:30 p.m.
  - installed software review on the dispatch desktop
  - walkthrough of the office and both ambulances for devices

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-08-10 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 (context) | Yes, 2026-08-14 |
| Antivirus console export (all computers) | SI-3 | Yes, 2026-08-14 |
| Device encryption report and MDM compliance report | SC-28, AC-11 | Yes, 2026-08-14 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-17 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Device lists (remote management and MDM) and installed software report | CM-8, CM-7 | Yes, 2026-08-14 |
| Firewall rule export | CM-7 | Yes, 2026-08-14 |
| Technician list with access to the company, and MFA on the remote management platform | SA-9 | Not received by fieldwork end; follow-up in POAM-011 |
| Subcontractor list and confirmation of the backup vendor BAA | SA-9 (164.314(a)(2)(iii)) | Not received by fieldwork end; follow-up in POAM-011 |

## 3. Rules of engagement
- No testing that could disrupt dispatch. On-site tests ran between 10:00 a.m. and 2:00 p.m. on 2026-08-18, with the Owner covering dispatch from the owner laptop. The dispatch desktop was examined but not changed during the visit.
- No ePHI left the office. Screenshots were redacted before they went into the evidence folder.
- The assessor would stop and tell the Office Manager at once about any critical exposure. The remote desktop tool on the dispatch desktop was reported the same day, and the MSP removed it the next morning.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 23 |
| Other than satisfied | 64 |
| **Total** | **87** |

**Fully other than satisfied:** IA-2, IA-2(1), AU-6, CP-4, SC-28. No process or technology met the objective.
**Largely satisfied:** SI-3 (detection, updates, scans, and quarantine work; after-hours alerting and false-positive handling do not) and CP-9 (backups run and are encrypted; they are not protected from deletion and have never been restored).

**New findings from testing:**
1. A free remote desktop tool, installed in 2025 by a former scheduler for after-hours access, ran on the dispatch desktop outside MSP management with a reused password (CM-07a., CM-07b.[04], CM-07b.[05]). The MSP removed it on 2026-08-19. The tool's own log showed no unknown sessions in the 90 days it kept. Added to the risk register as R-023 and to POAM-014.
2. 4 of 23 facility portal accounts belonged to discharge planners who had left those facilities (AC-02d.01, AC-02j.). The Office Manager disabled them on 2026-08-19.
3. The export log showed 3 full trip-list exports in July 2026 that nobody at the company could explain at first. They were traced to the billing company's month-end reconciliation, which shows why the log needs a weekly look (AU-06a.; POAM-007).
4. The backup console and firewall management login accept a password alone (IA-02(01); POAM-003).

All 14 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-003, POAM-009, POAM-010, and POAM-013: MFA, backups, restore and dispatch testing, and malware detection, the same sign-in and recovery theme as P01.

## 5. Deliverables
`assessment-results.csv` (87 rows), `poam.csv` (14 items), and this plan and summary. The Owner accepted the results on 2026-09-04.

**Independence note.** At this size the Office Manager both runs the controls and oversees their remediation. The independent assessor's results, the MSP's monthly report, and the Owner's monthly POA&M review are the checks on that overlap.

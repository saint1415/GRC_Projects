# Security Assessment Plan and Summary: Cris Santos Company | Transportation Systems | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (short line freight railroad) |
| System assessed | Train Dispatch and Operations Back Office (TDOB), per the SSP (P02) |
| Tier / Vertical | Micro / Transportation Systems |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent cybersecurity consultant with rail operations experience, under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager; MSP lead technician on call |
| Assessment window | 2026-08-04 to 2026-08-06 (on site 2026-08-05) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **12 controls, 84 determination statements.** Controls were chosen because they support the three High risks in P01 (ransomware, paper dispatch, MSP compromise), cover the binding TSA duties with gaps in P03 (cyber reporting and SSI), or test what the MSP does on the railroad's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2 | Shared crew login; former Conductor's access (P01 R-003; P03 G-035) | Focused | Comprehensive (all accounts in SYS-01, suite, telematics, payroll) |
| AC-3 | SSI open to every account (P03 G-012; R-008) | Basic | Focused |
| IA-2(1) | MFA on administrator access, including MSP-held logins (P03 G-036; R-004) | Focused | Comprehensive (every administrator login) |
| AT-2, IR-6 | No cyber training; the TSA 24-hour report missed (P03 G-007, G-008, G-038; R-006, R-015) | Basic | Focused (5 of 7 employees interviewed) |
| AU-6 | No log review (P03 G-046) | Basic | Basic |
| CP-4, CP-9 | Backups never tested; paper dispatch never drilled (P03 G-040, G-049, G-050; R-002, R-005) | Focused | Focused |
| SC-7 | Flat network around the dispatch desktop (P03 G-042; R-001) | Focused | Focused |
| SI-2, SI-3 | Unsupported dispatch desktop; MSP patching and antivirus (R-001, R-007) | Focused | Focused (3 desktops; alert routing test) |
| SA-9 | No vendor oversight (P03 G-030, G-031; R-004, R-020) | Focused | Comprehensive (all 7 vendors that hold company data or run company systems) |

## 2. Methods and objects
- **Examine:** SYS-01, suite, telematics, and payroll user lists; SYS-01 role list; shared-drive permission report; MSP contract; vendor terms; TSA report log; 2025 mailbox compromise notes; hazmat training records; the MSP evidence listed below.
- **Interview:** Owner and General Manager, Office Manager, Roadmaster, Conductor, Locomotive Engineer, and the MSP lead technician.
- **Test:**
  - user lists compared against the employee roster in SYS-01, the suite, the telematics portal, and payroll
  - sign-in attempts without a second factor to the backup console, firewall management page, and telematics portal (with the MSP present)
  - a sign-in with the crew login to confirm it cannot issue an authority (in a SYS-01 training area, not live dispatch)
  - reachability of the dispatch desktop from the shop desktop
  - patch and operating system status on the 3 desktops
  - an industry-standard harmless antivirus test file on the shop desktop, and an after-hours test alert to check routing

### MSP evidence requested
The MSP operates most technical controls, so evidence came from it. Requested on 2026-07-28 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) and patch policy | SI-2 | Yes, 2026-08-03 |
| Antivirus console export (all devices) | SI-3 | Yes, 2026-08-03 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-04 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP) |
| Firewall rule export and firmware record | SC-7, SI-2 | Yes, 2026-08-03 |
| Technician list with access to the railroad, and MFA on the remote management platform | AC-17, SA-9 | Not received by fieldwork end; follow-up in POAM-009 |
| Written approval for excluding the dispatch desktop from upgrades | SI-2 | None exists (the MSP acted on the radio vendor's request) |

## 3. Rules of engagement
- No testing that could affect train movements. Tests near the dispatch desk ran after the day's interchange turn had returned on 2026-08-05. The dispatch desktop was checked but not changed.
- No SSI or employee records left the building. Screenshots were redacted before they went into the evidence folder.
- The assessor would stop and tell the General Manager at once about any critical exposure. The telematics portal's shared installation password was reported the same day and changed on 2026-08-06.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 22 |
| Other than satisfied | 62 |
| **Total** | **84** |

**Fully other than satisfied:** AC-3, IA-2(1), AT-2, IR-6, AU-6, CP-4. No process or technology met the objective.
**Largely satisfied:** SI-3 (detection and quarantine work; after-hours alerting and false-positive handling do not).

**New findings from testing:**
1. The telematics portal (SYS-07) uses one shared administrator login with the password set at installation in 2024 and no MFA (IA-02(01)). Added to the risk register as R-017 and to POAM-002.
2. The after-hours test alert sent at 18:10 on 2026-08-05 was not seen until 08:20 the next day (SI-03c.02[02]). Interviews also showed the radio console software was quarantined once in 2026-04 and dispatch used handhelds for 2 hours (SI-03d.). POAM-005.
3. The shop desktop could reach the dispatch desktop's file sharing (SC-07a.[04]). POAM-010.
4. The MSP excluded the dispatch desktop from operating system upgrades without written company approval (SI-02d.). POAM-011.

All 12 controls have at least one weakness and a POA&M item in `poam.csv` (12 items: 4 High, 8 Moderate). The High items are POAM-003, POAM-004, POAM-005, and POAM-006: backups, recovery testing, malware detection, and the TSA report, the same themes as P01 and P03.

## 5. Deliverables
`assessment-results.csv` (84 rows), `poam.csv` (12 items), and this plan and summary. The Owner and General Manager accepted the results on 2026-08-31.

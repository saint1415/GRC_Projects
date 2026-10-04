# Security Assessment Plan and Summary: Cris Santos Company | Food and Agriculture | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (USDA-inspected sausage and smoked meats plant) |
| System assessed | Plant Production and Cold-Chain Monitoring System (PPCM), per the SSP (P02) |
| Tier / Vertical | Micro / Food and Agriculture |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor and independence | Independent consultant with food plant OT experience, under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Office Manager; the Maintenance and Sanitation Technician for plant equipment; MSP lead technician on call |
| Assessment window | 2026-08-10 to 2026-08-12 (on site 2026-08-11; plant equipment checked after the production shift) |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 106 determination statements.** Controls were chosen because they support the High risks in P01 (ransomware across the flat network, cook cycle changes through vendor access, unnoticed cold storage failures), cover the FSIS record gaps in P03, or test what the MSP and vendors do on the company's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2 | Shared logins and a March 2026 leaver (P01 R-007; P03 416.16(a), 417.5(b)) | Focused | Comprehensive (every account in the suite, records app, accounting, cold-chain dashboard, labeling PC, and smokehouse portal) |
| AC-17 | Always-on vendor connections to plant machines (P01 R-002, R-003) | Focused | Comprehensive (both vendor paths and the MSP agent) |
| IA-2, IA-2(1) | Attributable CCP entries (417.5(b)); MFA on administrator and vendor logins (P01 R-012) | Focused | Focused (15 lots of records; 4 privileged logins) |
| AT-2 | No training (P01 R-001, R-008, R-015) | Basic | Focused (5 of 7 employees interviewed) |
| AU-9 | Integrity of electronic CCP and SSOP records (417.5(d); 416.16(b); P01 R-005) | Focused | Focused (records app, cook-log exports, controller log) |
| CM-8 | No inventory of plant equipment (P03 benchmark ID.AM-01) | Basic | Comprehensive (network scan) |
| CP-2, CP-4, CP-9 | No contingency plan or tests; machine settings not backed up (417.2(c)(4); P01 R-004, R-006) | Focused | Focused |
| SA-9 | No vendor terms or oversight (P01 R-012, R-017, R-018) | Basic | Comprehensive (every vendor that runs a system or reaches a machine) |
| SC-7 | One flat network (P01 R-001, R-010) | Focused | Comprehensive (network scan and reachability tests) |
| SI-3 | MSP antivirus and alerting (P01 R-001) | Focused | Focused (labeling PC test; after-hours alert test) |

## 2. Methods and objects
- **Examine:** user lists for every service; the staff roster and the March 2026 leaver record; the MSP contract and scope document; vendor terms for the smokehouse, packager, records app, cold-chain service, and AI camera; the records app administrator settings and edit history; the cook-log export folder; the firewall rule export; the draft BIA, SSP, and policies; the MSP evidence listed below.
- **Interview:** the owner, the Office Manager, the Production Supervisor, the Maintenance and Sanitation Technician, 5 of 7 employees (training and reporting), and the MSP lead technician.
- **Test:**
  - user lists compared against the staff roster in every service
  - sign-in attempts to the firewall, backup console, records app administrator, and smokehouse portal without a second factor (with the MSP present)
  - a network scan from the office desktop and reachability tests to plant equipment
  - a test edit on a copy of a cook-log export to see whether the change is detectable
  - an industry-standard harmless antivirus test file on the labeling PC, and an after-hours test alert at 18:30 to check routing

### MSP evidence requested
The MSP operates the PC and network controls, so evidence came from it. Requested on 2026-08-03 with a one-week deadline:

| Item | Supports | Received |
|---|---|---|
| Monthly patch report (July 2026) | SI-2 context | Yes, 2026-08-06 |
| Antivirus console export (all PCs) | SI-3 | Yes, 2026-08-06 |
| Backup job report (July 2026) and retention settings | CP-9 | Yes, 2026-08-07 |
| Record of any restore test | CP-4 | No record exists (confirmed by the MSP on 2026-08-07) |
| Firewall rule export and log settings | SC-7 | Yes, 2026-08-06 |
| Device list | CM-8 | Yes, 2026-08-06 (3 PCs only) |
| Technician list with access, and MFA on the remote management platform | AC-17, SA-9 | Received 2026-08-12, the last day of fieldwork; follow-up in POAM-011 |

**Equipment vendor evidence.** The smokehouse manufacturer provided its portal session log for July 2026 on request (6 sessions). The packaging vendor did not answer a request for its remote access practices before fieldwork ended (POAM-002).

## 3. Rules of engagement
- No testing that could affect product or production. Plant equipment was checked after the production shift on 2026-08-11, with the smokehouse empty and the lines stopped. No machine setting was changed by the assessor.
- The network scan used a slow, safe profile agreed with the Maintenance and Sanitation Technician; the stuffer HMI and smokehouse controller were checked by reachability only, not scanned for vulnerabilities.
- No personal or Restricted information left the plant. Screenshots were redacted.
- The assessor would stop and tell the owner at once about any critical exposure. The default password on the smokehouse controller and the six unrequested portal sessions were reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 19 |
| Other than satisfied | 87 |
| **Total** | **106** |

**Fully other than satisfied:** AC-17, IA-2, IA-2(1), AT-2, AU-9, CP-2, CP-4. No process or technology met the objective.
**Largely satisfied:** SI-3 (detection and quarantine work; alerts are not seen after hours). **Half satisfied:** CP-9 (office backups run and are encrypted; machine settings are not backed up and the backups can be deleted).

**New findings from testing:**
1. The smokehouse controller's web interface accepted the manufacturer default administrator password from the office desktop. Changed the same day; the July cook logs were checked against the handheld readings and showed no unexplained changes. Added to the risk register as R-023 (closed) and to POAM-014 (check the other devices).
2. The smokehouse portal log showed 6 manufacturer sessions in July 2026 that nobody at the plant requested. The manufacturer said they were routine remote diagnostics. Both vendor paths were set to supervised, on-request sessions on 2026-08-12 (AC-17b.; POAM-002).
3. The network scan found 17 devices; the MSP's inventory lists 3 (CM-08a.01; POAM-007).
4. A test edit to a copy of a cook-log export left no trace (AU-09a.; POAM-006).

All 13 controls have at least one weakness and a POA&M item in `poam.csv`, plus POAM-014 for the default password found during testing (IA-5, outside the 13 selected controls). The High items are POAM-002, POAM-006, POAM-008, POAM-009, POAM-010, POAM-012, and POAM-014: vendor access, records integrity, contingency and backups, and network separation, the same themes as P01.

## 5. Deliverables
`assessment-results.csv` (106 rows), `poam.csv` (14 items: 7 High, 7 Moderate), and this plan and summary. The owner accepted the results on 2026-08-31.

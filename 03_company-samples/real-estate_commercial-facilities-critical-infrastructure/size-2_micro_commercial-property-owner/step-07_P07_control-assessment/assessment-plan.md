# Security Assessment Plan and Summary: Cris Santos Company | Commercial Facilities | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial office and retail property owner-operator) |
| System assessed | Building Automation and Access Control System (BAACS), per the SSP (P02) |
| Tier / Vertical | Micro / Commercial Facilities |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content); OT test limits from NIST SP 800-82 Rev. 3 |
| Assessor and independence | Independent security consultant with building systems experience, under a fixed-fee engagement. Did not take part in the risk assessment (P01) or the gap analysis (P03) and operates no control. Accompanied by the Property Manager; the Building Engineer and the MSP lead technician on hand for tests |
| Assessment window | 2026-08-10 to 2026-08-12 (on site at both properties 2026-08-11) |
| Criteria | The draft SSP (2026-07-31), draft POL-02 to POL-04 (approved 2026-08-31 without changes to the tested rules), and CPG 2.0 |

## 1. Scope and controls selected
Micro tier scope: 10-15 controls. **13 controls, 103 determination statements.** Controls were chosen because they support the four High risks in P01 (contractor remote access, unrecoverable BAS, flat network, platform administrator takeover), cover High and Moderate CPG gaps in P03, or test what the MSP and the controls contractor do on the company's behalf.

| Control | Why selected | Depth | Coverage |
|---|---|---|---|
| AC-2 | Shared BAS, contractor, and integrator accounts; slow departures (P01 R-005, R-008; CPG 3.C, 3.D) | Focused | Comprehensive (every account in the platform, suite, BAS workstation, remote-desktop tool, and backup console) |
| PE-2 | Building credentials never reviewed (R-006; CPG 3.D) | Focused | Focused (sample of 25 of 342 credentials) |
| IA-2(1) | No MFA on administrator access (R-005; CPG 3.F) | Focused | Comprehensive (all three administrator paths) |
| IA-5 | Shared and default passwords (R-008; CPG 3.A, 3.B) | Focused | Focused (BAS workstation, supervisory controller, both property routers) |
| MA-4 | Always-on contractor remote access (R-001; CPG 1.E) | Focused | Comprehensive |
| SC-7 | Flat network (R-003; CPG 3.I, 3.S) | Focused | Focused (one scan per property) |
| CM-8 | No device inventory (CPG 2.A) | Basic | Focused (engineering room, network closets, camera locations) |
| SI-2 | BAS workstation excluded from patching (R-009; CPG 2.B) | Focused | Focused (3 office computers and the BAS workstation) |
| CP-9, CP-4 | Backups untested (R-002; CPG 3.O, 6.A) | Focused | Focused |
| SA-9 | No contractor security terms (R-010, R-011; CPG 1.D, 1.E) | Basic | Comprehensive (MSP, controls contractor, security integrator, janitorial contractor, platform vendor) |
| AT-2 | New-hire video only (R-003, R-007; CPG 3.J) | Basic | Focused (5 of 7 staff interviewed) |
| AU-6 | No log review (R-021; CPG 3.Q) | Basic | Basic |

## 2. Methods and objects
- **Examine:** platform administrator and credential reports; suite user export and security settings; BAS workstation accounts; remote-desktop tool settings and connection history; backup job report and settings; MSP contract, patch policy, and monthly report; contractor agreements; draft SSP and policies; training sign-in sheet.
- **Interview:** Managing Member, Property Manager, Building Engineer, Tenant Services and Leasing Coordinator, 5 of 7 staff on training, the MSP lead technician, and the controls contractor's technician (by phone).
- **Test:**
  - user lists in every system compared with the staff and contractor roster
  - sign-in attempts without a second factor to the platform administrator portal, the remote-desktop service, and the backup console (with the account owners present)
  - a sign-in to the supervisory controller and each property router with the manufacturer's published default credentials (with the Building Engineer present, read-only; no setting changed)
  - a discovery scan from an office laptop at Property A and from the building device network at Property B
  - update history on 3 office computers and the BAS workstation
  - 25 credentials traced to request forms

### MSP and contractor evidence requested
Most technical controls are run by the MSP or the controls contractor, so evidence came from them. Requested on 2026-08-03 with a one-week deadline:

| Item | From | Supports | Received |
|---|---|---|---|
| Monthly patch report (July 2026) and patch policy | MSP | SI-2 | Yes, 2026-08-06 |
| Antivirus console export | MSP | SI-3 (context for SI-2) | Yes, 2026-08-06 |
| Backup job report (July 2026), retention, and console access settings | MSP | CP-9 | Yes, 2026-08-07 |
| Record of any restore test | MSP | CP-4 | No record exists (confirmed by the MSP 2026-08-07) |
| Firewall rule export | MSP | SC-7 | Yes, 2026-08-06 |
| Technician list with access, and MFA on the MSP's own platform | MSP | SA-9 | Not received by fieldwork end; follow-up in POAM-009 |
| Copies of controller programs and the supervisory controller database | Controls contractor | CP-9 | Not received; the contractor offered them for a fee, now in POAM-007 |
| Names of technicians who use the shared remote-desktop account | Controls contractor | AC-2, MA-4 | Yes, 2026-08-10 (4 technicians, 1 of whom left the contractor in 2025) |

## 3. Rules of engagement
- No test that could disturb building operation. Scans used a slow discovery profile and avoided BACnet write commands; nothing on a controller was changed. The on-site tests ran from 10:00 to 14:00 on 2026-08-11 with the Building Engineer present.
- No personal information left the company. Screenshots of credential lists were redacted before they went into the evidence folder.
- The assessor would stop and tell the Property Manager at once about any critical exposure. The two default passwords were reported the same day.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 23 |
| Other than satisfied | 80 |
| **Total** | **103** |

**Fully other than satisfied:** IA-2(1), CP-4, AU-6. No process or technology met the objective.
**Largely satisfied:** none. The best results were SI-2 (4 of 10: the MSP's patching of office computers works; the BAS workstation and firmware are outside it) and MA-4's documentation and session end (2 of 8).

**New findings from testing:**
1. The supervisory controller's web interface accepted the manufacturer's default administrator password (IA-05e.). Anyone on the Property A network could change setpoints and schedules. Added to the risk register as R-022 and to POAM-011.
2. The Property B ISP router accepted its factory default administrator password, and UPnP was on (IA-05e.; SC-07c.). The Property Manager changed the password and turned UPnP off with the MSP on 2026-08-12. Added as R-024; POAM-004 and POAM-011.
3. One of the 4 technicians who know the shared contractor remote-desktop password left the controls contractor in 2025, and the password was never changed (IA-05i.; MA-04c.). The connection history showed no sessions outside scheduled service visits in the last 30 days, which is all the history the tool keeps. POAM-001 and POAM-003.

All 13 controls have at least one weakness and a POA&M item in `poam.csv`. The High items are POAM-002, POAM-003, POAM-004, POAM-007, and POAM-008: MFA, contractor remote access, segmentation, and backups, the same themes as the High risks in P01.

## 5. Deliverables
`assessment-results.csv` (103 rows), `poam.csv` (13 items), and this plan and summary. The Managing Member accepted the results on 2026-08-31.

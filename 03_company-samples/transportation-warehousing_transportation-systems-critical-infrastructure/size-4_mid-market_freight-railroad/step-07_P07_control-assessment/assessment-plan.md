# Security Assessment Plan and Summary: Cris Santos Company | Transportation Systems | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Class II regional freight railroad, north and central Florida) |
| System assessed | Train Dispatch and PTC Operations Platform (TDPO): SYS-01, SYS-02, SYS-03, and the TDPO parts of SYS-04, SYS-05, SYS-07, SYS-08, and SYS-09, per the SSP (P02) |
| Tier / Vertical | Mid-Market / Transportation Systems |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Co-sourced internal audit firm (engagement lead, 2 IT auditors, 1 OT specialist), reporting to the board audit committee. The firm does not design or operate any assessed control. The Cybersecurity Manager coordinated access but did not select samples or rate findings. Field tests were run with a signal maintainer and the Chief Dispatcher on duty present, as the rules of engagement require |
| Assessment window | 2026-08-03 to 2026-08-21 (primary NOC and HQ data center 2026-08-11; backup NOC and Jacksonville Terminal Yard 2026-08-12; tower sites, control points, and detectors 2026-08-13) |
| Also satisfies | Annual internal IT audit; assessments in the TSA Cybersecurity Assessment Plan for the current plan year (SD 1580/82-2022-01E III.F.2.a and d) |
| Handling | Assessment results on Critical Cyber Systems are SSI (SD 1580/82-2022-01E IV.B.2; 49 CFR part 1520). The company's real report carries the 1520.13 marking and sits in the restricted SSI library. This sample omits the marking because the company is fictional |
| Results accepted | Chief Operating Officer, 2026-09-15; presented to the audit committee the same day |

## 1. Scope and controls selected
Mid-Market tier scope: 25-40 controls. **34 controls, 252 determination statements.** Controls were selected because they:
- address the Very High and High risks in the risk register (P01);
- test the directive measures with gaps in the gap analysis (P03), so the results also count toward the CAP's one-third minimum;
- support inherited-control reliance and SOC 2 readiness for the shared dispatch service (P09).

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| AC-2, PS-4 | Account lifecycle; SD III.C.4; R-024, R-025 | Focused | Focused (samples of 25) |
| AC-5, AC-6, IA-2 | Separation of duties, least privilege, shared logins; SD III.C.3, III.C.4.a; R-051 (High) | Comprehensive | Comprehensive (all 64 privileged accounts) |
| IA-2(1), IA-5 | MFA and authenticators; SD III.C.1, III.C.2, III.C.4.b; R-006, R-018, R-023 (High) | Focused | Focused (25 accounts; 20 field devices) |
| AC-17, MA-4, CA-3 | Vendor remote access and interconnections; SD III.B.1.b, III.C.2; R-007 (High), R-017 | Comprehensive | Comprehensive (all vendor paths) |
| AC-4, SC-7 | Zone boundaries; SD III.B; R-001 (Very High), R-004 (High) | Focused | Focused (data center, both NOCs, 6 of 38 tower sites) |
| AU-2, AU-6, AU-11, SI-4 | Logging and monitoring; SD III.D.2, III.D.3; R-019, R-020, R-034 | Focused | Focused |
| SI-3 | Malicious code protection; SD III.D.1.d, III.D.2.c | Basic | Focused (5 endpoints) |
| RA-5, SI-2 | Vulnerability and patch management; SD III.E; R-008, R-009 (High) | Focused | Comprehensive (46 of 46 findings) |
| CM-3, CM-8 | Change control and inventory; SD IV.C.2.a; R-048, R-035 | Focused | Focused |
| CP-2, CP-4, CP-9, CP-10 | Contingency and recovery; SD 1580-21-01E II.D.1.b; R-001 and R-003 (Very High), R-005, R-028 | Comprehensive | Comprehensive |
| IR-3, IR-4, IR-6, IR-8, AT-3 | Incident capability and reporting; SD 1580-21-01E II.C, II.D; R-011, R-049 | Focused | Focused (12 of 31 events) |
| CA-2 | Assessment program; SD III.F.2; R-010 (High) | Focused | Comprehensive |
| SA-9 | External services; SD II.A.2, II.A.3; R-014, R-034 | Focused | Comprehensive (8 Tier 1 vendors) |
| MP-4, PE-3 | SSI media and physical access to NOCs and field housings; 1520.9; 236.3; R-026, R-036 | Basic | Focused (both NOCs, 6 tower sites, 8 signal locations) |

**Not selected this year, with reasons:** CP-9 enhancements, SC-8, SC-12, and SC-13 (PTC message protection is inherited from the host's certified system and was reviewed in P03 G-094); AT-2 and PE-2 (tested in the 2025 internal audit with no findings); SR controls (waiting for STD-03; scheduled for the 2027 CAP year).

## 2. Sampling approach
Samples followed the co-sourced firm's attribute sampling table. For a control operating many times a year at moderate risk, the sample is 25 items; for weekly or monthly controls, 5 to 10 items; for High-risk controls with small populations, the whole population. The assessors chose samples at random from populations extracted in their presence.

| Population | Size | Sample | Controls |
|---|---|---|---|
| Terminations (2025-07-01 to 2026-06-30) | 96 | 25 | AC-2, PS-4 |
| Transfers (same period) | 41 | 25 | AC-2 |
| New CAD/CTC, BOS, and TMS accounts | 74 | 25 | AC-2 |
| Privileged accounts (IT, cloud, CAD/CTC, BOS) | 64 | 25 for the MFA test; all 64 for the rights review | IA-2(1), AC-6 |
| Shared accounts | 11 (9 field maintainer, 2 dispatcher) | All 11 | AC-2, IA-5 |
| Field devices (detector modems and crossing monitors) | 140 | 20 (default-credential test) | IA-5 |
| PAM vendor sessions (CAD/CTC and PTC vendors) | 212 | 25 | MA-4 |
| Changes to CAD/CTC, BOS, and field controllers (2026 H1) | 140 | 25 (including 12 field changes) | CM-3 |
| Critical and high vulnerability findings (Q1-Q2 2026) | 46 | 46 | RA-5, SI-2 |
| Backup job days (July 2026) | 31 | 31 | CP-9 |
| Security events in the incident log (last 12 months) | 31 | 12 | IR-4, IR-6 |
| Tier 1 vendors | 8 | 8 | SA-9 |
| Staff for reporting and role training interviews (dispatchers, chief dispatchers, maintainers) | about 140 | 15 | IR-6, AT-3 |
| Tower sites / signal locations for walkthroughs | 38 / 150 | 6 / 8 (including the 6 hub towers' 2 busiest) | CM-8, PE-3, SC-7, AC-17 |

## 3. Methods and objects
- **Examine:**
  - the 2023 policies and the 2026 drafts; the SSP draft; the CIP and CAP (inside the SSI library)
  - directory, identity provider, PAM, CAD/CTC, BOS, TMS, and MDM exports
  - firewall rule exports, the external connection list, field network diagrams, and the OT inventory
  - backup, patch, scan, KEV review, EDR, and SIEM reports
  - change tickets and change advisory board minutes
  - Tier 1 vendor contracts and SOC 2 reports
  - the incident log, the CISA report, the 2025-10 tabletop report, and the contingency plan
  - badge reports and key logs
- **Interview:**
  - vCISO, Cybersecurity Manager, Director of IT, the OT security engineer, and both GRC analysts
  - Director of Network Operations, 2 chief dispatchers, and 6 dispatchers
  - Director of Signals and Communications and 5 signal maintainers
  - PTC Program Manager; Director of Safety, Security, and Hazmat; HR Director
  - the MSSP service lead
- **Test:**
  - MFA sign-in tests on 25 privileged accounts
  - reachability tests from a detector modem segment and a tower router at 3 tower sites
  - default-credential tests on 20 detector modems and crossing monitors (after hours, vendor present)
  - comparison of 6 field controller configurations against the last recorded change
  - EDR test files on 5 endpoints, including 2 dispatch consoles in the vendor's test mode
  - a simulated impossible-travel sign-in to test MSSP escalation
  - a 2-hour passive capture at 1 hub tower
  - a restore of one file share folder from the backup account

## 4. Rules of engagement
- **Safety first.** No test touched vital signal logic, onboard PTC apparatus, or a production CAD/CTC server during train movements. Field tests ran only inside a work window the Chief Dispatcher on duty granted, with a signal maintainer present, and stopped at once if any CTC indication changed. Dispatch console EDR tests used the CAD/CTC vendor's test mode on standby consoles.
- **No SSI left company control.** CIP and CAP content was examined in the restricted SSI library. Workpapers that describe vulnerabilities are stored in the firm's encrypted workpaper system under a need-to-know record (POL-04 4.2).
- **Stop-and-notify rule:** any critical exposure is reported to the Cybersecurity Manager and the vCISO the same day. **Used twice:**
  - On 2026-08-13 the passive capture at the hub tower found an unlisted device. It was a detector vendor cellular router installed in 2024 without a change record. The company disabled its inbound access on 2026-08-14 and added it to POAM-004.
  - On 2026-08-13 the default-credential test succeeded on 4 of 20 field devices. The company changed those 4 passwords the same week and opened the full sweep under POAM-003.

## 5. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 169 |
| Other than satisfied | 83 |
| **Total** | **252** |

Other than satisfied statements by risk: 5 Very High, 56 High, 22 Moderate.

| Control | Satisfied | Other than satisfied | Highest risk | POA&M |
|---|---|---|---|---|
| AC-2 | 21 | 5 | High | POAM-001, POAM-002, POAM-003 |
| AC-4 | 0 | 1 | High | POAM-005 |
| AC-5 | 1 | 1 | High | POAM-002 |
| AC-6 | 0 | 1 | High | POAM-002 |
| AC-17 | 2 | 2 | High | POAM-004 |
| AT-3 | 6 | 3 | High | POAM-012 |
| AU-2 | 2 | 4 | High | POAM-006 |
| AU-6 | 2 | 1 | High | POAM-006 |
| AU-11 | 0 | 1 | High | POAM-006 |
| CA-2 | 9 | 2 | High | POAM-017 |
| CA-3 | 5 | 3 | High | POAM-004, POAM-014 |
| CM-3 | 8 | 2 | Moderate | POAM-009 |
| CM-8 | 2 | 4 | Moderate | POAM-008 |
| CP-2 | 18 | 6 | High | POAM-010 |
| CP-4 | 2 | 3 | Very High | POAM-011 |
| CP-9 | 6 | 0 | n/a | n/a |
| CP-10 | 0 | 2 | Very High | POAM-011 |
| IA-2 | 1 | 1 | High | POAM-002 |
| IA-2(1) | 1 | 0 | n/a | n/a |
| IA-5 | 7 | 3 | High | POAM-003 |
| IR-3 | 0 | 1 | High | POAM-012 |
| IR-4 | 10 | 3 | High | POAM-012 |
| IR-6 | 1 | 1 | Moderate | POAM-013 |
| IR-8 | 13 | 4 | High | POAM-012, POAM-013 |
| MA-4 | 3 | 5 | High | POAM-004 |
| MP-4 | 4 | 1 | Moderate | POAM-016 |
| PE-3 | 9 | 3 | Moderate | POAM-015 |
| PS-4 | 3 | 2 | High | POAM-001, POAM-003 |
| RA-5 | 7 | 2 | High | POAM-007 |
| SA-9 | 2 | 4 | Moderate | POAM-014 |
| SC-7 | 2 | 4 | High | POAM-004, POAM-005, POAM-006 |
| SI-2 | 7 | 3 | High | POAM-007 |
| SI-3 | 8 | 0 | n/a | n/a |
| SI-4 | 7 | 5 | High | POAM-006 |

**Fully satisfied (3 controls):** CP-9 (write-once, isolated, scanned backups on 31 of 31 days), IA-2(1) (MFA on 25 of 25 privileged accounts), and SI-3 (EDR blocked 5 of 5 test files within 4 minutes). These confirm the strengths listed in the scenario facts.

**Fully other than satisfied (5 controls):** AC-4, AC-6, AU-11, CP-10, and IR-3. Each has only 1 or 2 statements, so one finding fails the whole control.

**Themes:**
1. **The data center is defended; the field is not.** Every boundary, monitoring, and access control that works at the HQ data center and the NOCs (AC-4, SC-7, SI-4, AC-17) fails the same statement in the field backhaul and at the tower sites.
2. **Recovery is unproven.** Backups are excellent (CP-9), but nothing shows CAD/CTC or the BOS can be restored from them within the RTO (CP-4, CP-10), and the plan does not cover a cyber compromise (CP-2).
3. **Shared and vendor credentials** (AC-2, IA-5, MA-4) are the most likely way in, and the stop-and-notify findings came from them.
4. **The program is behind its own plan** (CA-2): the one-third CAP minimum and the architecture review.

**CAP credit.** These 34 controls test 41 CIP measures. With them, the current plan year (starting 2026-06-20) reaches 41% of CIP measures assessed, above the one-third minimum (P03 G-044).

**POA&M:** 31 controls had at least one Other than satisfied statement. They map to 17 POA&M items (POAM-001 to POAM-017), because related controls share an item. Six more items come from other sources: the gap analysis (POAM-018 CIP amendments and TSA notice, POAM-019 RSSM outage-mode drill, POAM-020 TSA training timing), the AI assessment (POAM-021), the SOC 2 readiness assessment (POAM-022), and the risk register (POAM-023 phishing-resistant MFA and administrator accounts). The total is 23 items: 1 Very High, 11 High, 10 Moderate, and 1 Low. Every item funded in the FY2027 security plan (P01 section 4) maps to one of them. See `poam.csv`.

## 6. Schedule and deliverables
| Date | Activity |
|---|---|
| 2026-07-27 | Plan, rules of engagement, and sample requests issued; plan approved by the Chief Operating Officer |
| 2026-08-03 to 2026-08-07 | Document examination and interviews |
| 2026-08-10 to 2026-08-14 | NOC and data center walkthroughs (2026-08-11 and 2026-08-12), field visit (2026-08-13), and technical tests |
| 2026-08-17 to 2026-08-21 | Analysis, draft findings, management responses |
| 2026-09-15 | Results and POA&M accepted by the COO and presented to the audit committee |

Deliverables: this plan and summary; `assessment-results.csv` (252 rows); `poam.csv` (23 items). Results feed the CAP annual report due in 2027-06.

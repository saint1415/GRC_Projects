# Security Assessment Plan and Summary: Cris Santos Company Holdings | Healthcare and Public Health | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the Hospital Clinical Information System (P02 SSP), and samples of Hospital System, Health Plan, and College controls |
| Tier / Vertical | Multi-Sector / Healthcare and Public Health (focus division: Hospital System) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8), for both covered entities and for corporate as business associate; testing of key controls for the College under 16 CFR 314.4(d)(1) |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in the Hospital System and the Health Plan come from the same corporate providers. Testing them twice would waste effort and produce two slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, with samples drawn from every division that inherits them (for example, the joiner-mover-leaver sample took events from all three divisions, and the student account extract came from the EHR).
2. **The HCIS's** own and hybrid controls were assessed because it is the SSP system and carries the group's top risk (GR-01).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

The College was sampled on its Safeguards Rule elements (risk assessment, MFA, incident response, training) because it is outside most common controls (scenario gap 5). This is its first independent test since the 2023 acquisition.

## 2. Controls selected
**37 control assessments** (32 distinct controls; AT-2, CP-9, IA-2(1), IR-8, and SC-7 were assessed in two scopes), **259 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1), IA-5 | 44 | Access for every division; GR-05, GR-08; scenario gap 4 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1; Group HR) | PS-4, AT-2 | 15 | Terminations and training for 43,000 group-identity users and about 4,500 trainees a year | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-03, GR-12; scenario gap 8 | Focused / Comprehensive |
| Common control (SYS-G3 data centers and cloud) | CP-9, SC-7, SC-8, SC-28, CM-6 | 20 | GR-01; immutable backups and data center zones | Focused / Focused |
| HCIS (SSP system) | AC-3, AU-6, CP-2, CP-4, CP-10, SI-2, CM-8 | 51 | HS-001, HS-002, HS-015 (High and Moderate); scenario gaps 1 and 2 | Comprehensive / Focused (3 of 9 hospitals visited) |
| Division sample: Hospital System | MA-4, PS-7, SC-7 | 19 | HS-005, HS-006, HS-007; scenario gaps 3 and 4 | Focused / Focused (all 140 vendor connections; 22 school agreements) |
| Division sample: Health Plan | AC-21, PT-3, SA-9, CP-9 | 20 | HP-002, HP-003, HP-007; scenario gap 7 | Focused / Focused |
| Division sample: College | RA-3, IA-2(1), IR-8, AT-2 | 36 | ED-001, ED-002, ED-006; scenario gap 5 | Focused / Focused |
| **Total** | **37** | **259** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, the EHR user extract, SIEM data sources and sensor maps, data center zone diagrams and firewall rules, backup and vault settings, the HCIS contingency plan, the unified emergency plan, downtime test logs, patch and inventory reports, vendor connection inventories, affiliation agreements, the intercompany data sharing addendum, the College's 2022 risk assessment and IR plan, and the 2025 compliance audit report.
- **Interview:** group identity, SOC, infrastructure, and network directors; the HCIS system owner; the Hospital System security and compliance lead and Privacy Officer; the system emergency management director; clinical engineering at 3 hospitals; the Health Plan Privacy Officer and security lead; the College IT director and financial aid director.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations;
  - an extract of all active EHR student accounts compared with school rotation calendars (412 active after rotations ended);
  - a hardware-key administrator sign-in, and a College SIS administrator sign-in (no second factor requested);
  - an east-west reachability test from an HCIS application server to Health Plan and College zones (with change approval);
  - restores of 3 file sets from the vault;
  - a TLS scan of 80 endpoints;
  - role tests in the EHR under 6 roles at 3 hospitals;
  - a review of all 140 device vendor connections.

## 4. Rules of engagement
- No testing that could affect patient care, devices in use, claims payment, or students' coursework. Network tests ran in maintenance windows with clinical engineering present; no scanning of devices connected to patients.
- No PHI or student records left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. One was reported the same day: plain-text interface passwords in configuration files (IA-5), now in POAM-002 with a 2026-10-31 milestone.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 108 | 25 | 133 |
| HCIS (SSP system) | 39 | 12 | 51 |
| Division sample: Hospital System | 10 | 9 | 19 |
| Division sample: Health Plan | 15 | 5 | 20 |
| Division sample: College | 26 | 10 | 36 |
| **Total** | **198** | **61** | **259** |

**Common controls are mostly strong.** 108 of 133 common statements were satisfied. Privileged access (AC-6(5), IA-2(1)), unique identification (IA-2), terminations (PS-4), backups (CP-9), and encryption (SC-8, SC-28) had no findings. The common findings are about **students and trainees** (AC-2, AC-2(3), AT-2), **service account credentials** (IA-5), **monitoring and scanning coverage** of device networks, vendor sessions, and the College (SI-4, RA-5), **separation inside the data centers** (SC-7), and **incident handling across divisions** (IR-3, IR-4, IR-6, IR-8), which is scenario gap 8.

**The HCIS is resilient to a site loss but not to ransomware.** Role-based access and privacy monitoring were sound (AC-3, AU-6). But the contingency plan, testing, and recovery controls (CP-2, CP-4, CP-10) show that recovery after a compromise of both data centers is unplanned and untested (scenario gap 1), and downtime workstations at 3 hospitals were not tested (gap 2). Ancillary patching (SI-2) and the inventory of interfaced devices (CM-8) also fell short.

**Division samples:**
- *Hospital System:* the 37 device vendor connections outside PAM caused 5 of 8 MA-4 statements to fail (approval, monitoring, strong authentication, and ending sessions and connections; High); device networks at 4 hospitals are not separated (SC-7); outside schools are not bound to report student changes (PS-7).
- *Health Plan:* no protocol or documented purpose for the hospital ADT feed (AC-21, PT-3, gap 7); vendor monitoring once a year (SA-9); claims recovery runbooks on the claims share (CP-9).
- *College:* MFA missing for SIS administrators (IA-2(1), High); the risk assessment and IR plan date from 2022 (RA-3, IR-8); training lacks phishing exercises (AT-2).

**Controls fully other than satisfied** (every statement failed): IR-3 (common), CP-10 (HCIS), and IA-2(1) (College). IR-3 and IA-2(1) each have one determination statement; CP-10 has two.

28 of the 37 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **25 items**: 22 from this assessment and 3 from the P03 gap analysis (POAM-023 emergency plan, POAM-024 sepsis model, POAM-025 College board report). By risk: 5 High (POAM-012 recovery after ransomware, POAM-013 device vendor access, POAM-020 College MFA, POAM-023 emergency plan, POAM-024 sepsis model), 16 Moderate, and 4 Low. Status: 19 In progress, 6 Open. Each item names the related P01 risks.

**Back into the risk register.** The plain-text interface passwords found during testing were added to P01 as part of HS-019 and rated with the other service account findings.

## 7. Deliverables and acceptance
`assessment-results.csv` (259 rows, with an `assessment_scope` column), `poam.csv` (25 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-15. Division presidents accepted their division findings the same week. The College results also go into the Qualified Individual's first written annual report (POAM-025).

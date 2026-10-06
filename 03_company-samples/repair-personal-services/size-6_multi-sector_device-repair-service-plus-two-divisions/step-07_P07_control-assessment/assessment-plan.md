# Security Assessment Plan and Summary: Cris Santos Company Holdings | Other Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the STPP (P02 SSP system), and samples of Device Repair, Electronics Retail, and IT Support controls |
| Tier / Vertical | Multi-Sector / Other Services (except Public Administration) (focus division: Device Repair) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`; long statements truncated) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only. The QSA and the SOC 2 service auditor were not involved; their examinations are separate |
| Assessment window | 2026-07-01 to 2026-08-31 |
| Also supports | IT Support's HIPAA evaluation, 45 CFR 164.308(a)(8); both merchants' preparation for their ROCs; IT Support's SOC 2 readiness (P09) |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three).
2. **The STPP's** system-specific controls were assessed because it is the SSP system and carries the group's credential exposure (GR-05) and bench access risk (GR-01).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Device Repair was sampled most heavily, on the bench and depot controls behind scenario gaps 2, 4, 5, and 10, because its supplement has drifted and its depots and labs have no documented inheritance (gap 9).

## 2. Controls selected
**43 control assessments** (36 distinct controls; AC-6, AU-6, CP-9, IA-2(1), SA-9, SC-7, and SI-7 were assessed in two scopes), **252 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1), IA-5 | 44 | Every division's access control; GR-01, GR-08 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1; Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-06, GR-19; scenario gap 8 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-8, SC-12, SC-28 | 16 | GR-07; immutable backups and hub network | Focused / Focused |
| STPP (SSP system) | AC-3, AC-6, AU-6, SI-12, CP-4, PT-3, CM-8 | 26 | GR-05, DR-001, DR-002 (High); scenario gaps 1 and 2 | Comprehensive / Comprehensive |
| Division sample: Device Repair | MP-6, MP-7, CM-7, SA-9, AU-12, SI-7, PS-6, PL-1 | 48 | DR-002, DR-005 (High); gaps 4, 5, 10 | Focused / Focused (24 stores, 12 in-store counters, 5 depots, 2 labs) |
| Division sample: Electronics Retail | SC-7, SI-7, AU-6, SI-2 | 25 | ER-001, ER-002 (High); gap 3 | Focused / Focused (10 stores) |
| Division sample: IT Support Services | AC-6, IA-2(1), CM-3, SA-9, CP-9 | 24 | IT-001, IT-002 (High); gaps 6 and 7 | Focused / Focused |
| **Total** | **43** | **252** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, SIEM data sources and rules, landing-zone policies, backup and immutability settings, STPP roles and retention settings, bench images and tool inventories, the 2019 sanitization standard and certificates, vendor terms, the RMM role export and script history, division supplements and procedures, the notification matrix.
- **Interview:** group identity, SOC, and cloud platform directors; the STPP product owner; division security and compliance leads; the Device Repair chief operating officer and depot managers; store and counter technicians; the Group General Counsel; the IT Support managed services director.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations;
  - test searches under 4 STPP store roles for passcode patterns in notes;
  - simulated USB copies on 6 bench workstations (with SOC approval, using synthetic data);
  - a forensic check of 40 sanitized trade-in devices at 2 depots;
  - restores of 3 STPP database snapshots from the provider B vault;
  - a retest of in-store counter network reachability at 3 retail stores;
  - a TLS scan of 60 endpoints and an external exposure scan of the landing zones;
  - a review of RMM sign-in paths, including local accounts.

## 4. Rules of engagement
- No testing on customer devices in custody. Bench tests used group test devices and synthetic data.
- No testing that could affect store payments or managed customers' endpoints. RMM testing was read-only.
- No customer data left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. One was escalated the same day: the two local RMM administrator accounts without MFA (POAM-004). They were disabled on 2026-08-20 pending removal.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 114 | 15 | 129 |
| STPP (SSP system) | 16 | 10 | 26 |
| Division sample: Device Repair | 33 | 15 | 48 |
| Division sample: Electronics Retail | 21 | 4 | 25 |
| Division sample: IT Support Services | 19 | 5 | 24 |
| **Total** | **203** | **49** | **252** |

**Common controls are strong.** 114 of 129 common statements were satisfied. Privileged access (AC-6(5)), MFA for privileged accounts (IA-2(1)), terminations (PS-4), training (AT-2), cloud protection (CP-9, SC-7, SC-8, SC-12, SC-28), and inactive account handling (AC-2(3)) had no findings. The common findings are about **shared bench logins at in-store counters** (AC-2, IA-2), **partner interface secrets** (IA-5), **bench telemetry** (SI-4), **bench scanning and patching** (RA-5), and **cross-division incident handling and notification** (IR-3, IR-4, IR-6, IR-8), which is scenario gap 8.

**The STPP is where the credential risk is.** AC-3 and AC-6 were fully other than satisfied. Test searches under all 4 store roles returned passcodes from other stores in the region, and nothing records what technicians open on customer devices (scenario gaps 1 and 2).

**Division samples:**
- *Device Repair:* USB allowed and no session records on store benches (MP-7, AU-12), local administrator rights and no allow-listing (CM-7), no tool vendor terms or update integrity checks (SA-9, SI-7), sanitization on the superseded SP 800-88 Rev. 1 without per-device records for drop-offs (MP-6), unsigned access agreements at in-store counters (PS-6), and a drifted supplement (PL-1). The forensic check found no recoverable data on 40 sanitized trade-ins; the finding is about the standard and the records, not a known failure.
- *Electronics Retail:* counter bench networks reach lanes at 112 stores and the traffic is not monitored (SC-7), and checkout script integrity checks miss the tag container while alerts are reviewed weekly (SI-7). Lane patching (SI-2) and log review (AU-6) had no findings.
- *IT Support:* 14 standing RMM global administrators (AC-6), two local RMM administrator accounts without MFA (IA-2(1)), multi-customer scripts and AI agent actions outside configuration control (CM-3), and no subcontractor agreement with the AI agent's model provider (SA-9). Managed backup (CP-9) had no findings.

**Controls fully other than satisfied** (every statement failed): IR-3 (common), AC-3 and AC-6 (STPP), and AC-6 and IA-2(1) (IT Support). Each has only one determination statement.

30 of the 43 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **26 items**: 24 from this assessment (several also trace to P03 gaps), POAM-013 from the P02 SSP (inheritance for depots and labs), and POAM-022 from the P03 gap analysis (card data outside the P2PE terminals). By risk: 8 High (POAM-002, POAM-003, POAM-004, POAM-005, POAM-007, POAM-008, POAM-009, POAM-023) and 18 Moderate. Status: 23 In progress, 3 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (252 rows, with an `assessment_scope` column), `poam.csv` (26 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-10. Division presidents accepted their division findings the same week.

# Security Assessment Plan and Summary: Cris Santos Company Holdings | Mining, Quarrying, and Oil and Gas Extraction | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the FSPA (P02 SSP system), and samples of Crude Oil Production (Mid-Continent legacy SCADA), Power Generation, and Crude Logistics controls |
| Tier / Vertical | Multi-Sector / Mining, Quarrying, and Oil and Gas Extraction (focus division: Crude Oil Production) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`); OT test practices from NIST SP 800-82 Rev. 3 |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. An OT specialist firm supported the field tests under internal audit's direction. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28. OT tests at Plant P2 during a planned outage on 2026-08-11 and at Permian field sites on 2026-08-13 |

## 1. Approach: assess common controls once, then sample divisions
Most IT safeguards in all three divisions come from the same corporate providers, so testing them three times would waste effort and produce three slightly different answers. Therefore:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the termination sample took events from all three).
2. **The FSPA's** system-specific and hybrid controls were assessed because it is the SSP system and sits where the top group risks land (GR-01, GR-02).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Crude Logistics was sampled most heavily (CA-2, PL-1, and four operational controls) because its inheritance is undocumented (scenario gap 6) and its supplement has drifted (gap 9). Power Generation was sampled on the new CIP-003-9 obligations (gap 3); its NERC program is also audited by its Regional Entities.

## 2. Controls selected
**36 control assessments** (32 distinct controls; AC-17 was assessed in three scopes, and CP-9 and CP-4 in two), **242 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1) | AC-2, AC-6(5), IA-2(1), AC-17, PS-4 | 37 | Every division's access and the jump servers; GR-02, GR-08 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR) | AT-2 | 10 | Awareness for 45,000 users | Focused / Focused |
| Common control (SYS-G2) | SI-4, RA-5, IR-4, IR-6, IR-8, IR-3 | 54 | Detection, response, and notices for all divisions; GR-03, GR-04, GR-13; scenario gap 7 | Focused / Comprehensive |
| Common control (SYS-G3) | CP-9, SC-7, SC-8 | 13 | Backups and the OT DMZ boundary; GR-01, GR-03 | Focused / Focused |
| FSPA (P02 SSP system) | AC-4, CM-3, CM-8, CP-4, IA-3, IA-5, SI-7, CM-7(5), AU-6 | 45 | SSP system; PD-003, PD-006, PD-007, PD-009, PD-014; Permian field test 2026-08-13 | Comprehensive / Focused (6 Permian well pads, 3 field areas) |
| Division sample: Crude Oil Production (Mid-Continent SYS-P5) | AC-17, SR-6, CP-9 | 11 | PD-001, PD-002 (High); scenario gap 2 | Focused / Focused (2 field offices) |
| Division sample: Power Generation | AC-17, MA-3, PE-3 | 20 | PG-001 (High); CIP-003-9 Sections 2, 5, 6; scenario gap 3; P2 outage test 2026-08-11 | Focused / Focused (P2, P3, and the GCC) |
| Division sample: Crude Logistics | CP-4, CM-4, AT-3, CA-2, PL-1, RA-3 | 52 | ML-002 (High), ML-003, ML-004, ML-007, ML-012, ML-013; scenario gaps 4, 5, 6, 9 | Focused / Comprehensive (heaviest sample, because inheritance is undocumented) |
| **Total** | **36** | **242** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, jump server and OT DMZ firewall rules, SIEM data sources and OT sensor coverage, vulnerability and KEV reports, the IR plan and notification matrix, backup and vault settings, OT change records, the OT inventory, the CIP-003-9 evidence binder, control room procedures and training records, the hazmat security plan, and division supplements.
- **Interview:** group identity, SOC, and cloud platform directors; the Group OT Security Director; the Production Vice President of Operations Technology and the Mid-Continent operations manager; the Power Generation NERC Compliance Manager; the Pipeline Control Center Manager and Fleet Safety Director; the Group General Counsel.
- **Test:**
  - a route test from a corporate virtual desktop to the shared jump servers;
  - a write test with the SYS-G6 historian service account against a test broker (with SOC approval);
  - login attempts with vendor default credentials on modems and controllers at 6 Permian well pads (2026-08-13);
  - sensor discovery compared with the OT inventory in 3 Permian field areas;
  - an application allowlisting execution test on IOC and Florida HMIs;
  - a restore of 2 SCADA server images and 1 SYS-M3 database from the provider B vault, and an attempted restore of a SYS-P5 HMI image;
  - a badge walk test at Plant P2 during its planned outage (2026-08-11) and at the GCC.

## 4. Rules of engagement
- **No active testing of live control.** No scans, logins, or configuration changes on devices that were controlling a process. Field credential tests were made only on devices the shift lead had placed in local or manual mode, with an automation technician present. Plant tests ran only during the P2 planned outage.
- The control room shift lead could stop any test at any time. None was stopped.
- No royalty owner or employee personal data left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. The default credentials found on 2026-08-13 were reported the same day; the three devices were changed on 2026-09-15 after the shift lead scheduled the work.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common control (SYS-G1) | 33 | 4 | 37 |
| Common control (Group HR) | 10 | 0 | 10 |
| Common control (SYS-G2) | 46 | 8 | 54 |
| Common control (SYS-G3) | 12 | 1 | 13 |
| FSPA (P02 SSP system) | 32 | 13 | 45 |
| Division sample: Crude Oil Production (Mid-Continent SYS-P5) | 4 | 7 | 11 |
| Division sample: Power Generation | 17 | 3 | 20 |
| Division sample: Crude Logistics | 40 | 12 | 52 |
| **Total** | **194** | **48** | **242** |

**Common controls are mostly strong.** 101 of 114 common statements were satisfied. Privileged access (AC-6(5), IA-2(1)), terminations (PS-4), awareness training (AT-2), backups (CP-9), and WAN encryption (SC-8) had no findings. The common findings are about **the shared paths into OT** (AC-2, AC-17, SC-7: the jump servers and the historian connector), **patching** (RA-5), **OT monitoring coverage** (SI-4), and **cross-division incident consistency and notification** (IR-3, IR-4, IR-6, IR-8; scenario gap 7).

**The FSPA:** the historian connector can write into the OT DMZ (AC-4); default credentials on field devices (IA-5) and unauthenticated radio links (IA-3); field logic changes without prior review and a model that changed setpoints without change control (CM-3); an incomplete OT inventory (CM-8) and program comparison (SI-7); no allowlisting on Florida HMIs (CM-7(5)); and untested field device restore (CP-4).

**Division samples:**
- *Crude Oil Production (Mid-Continent):* every AC-17 statement failed for the integrator path, the integrator was never assessed (SR-6), and the attempted restore of a SYS-P5 HMI image failed (CP-9).
- *Power Generation:* Plant P3 vendor access does not meet CIP-003-9 Section 6.3 (AC-17), and OEM laptop reviews are not recorded (MA-3). Physical security (PE-3) passed.
- *Crude Logistics:* the backup PCC test is overdue (CP-4), point-to-point and change analysis gaps (CM-4), training gaps for controllers and hazmat staff (AT-3), undocumented inheritance (CA-2), the 2023 supplement (PL-1), and a security plan risk assessment without cyber threats (RA-3).

**Controls fully other than satisfied** (every statement failed): IR-3 (Common control), AC-4 (FSPA), IA-3 (FSPA), AC-17 (Crude Oil Production), SR-6 (Crude Oil Production).

29 of the 36 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **27 items**: 24 from this assessment and 3 from the P03 gap analysis alone (POAM-022, POAM-023, POAM-025). By risk: 7 High (POAM-001, 002, 004, 012, 013, 015, 021), 18 Moderate, and 2 Low. Status: 17 In progress and 10 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (242 rows, with an `assessment_scope` column), `poam.csv` (27 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-17. Division presidents accepted their division findings the same week.

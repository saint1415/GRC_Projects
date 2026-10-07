# Security Assessment Plan and Summary: Cris Santos Company Holdings | Energy | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, Group HR), the Pipeline SCADA and Gas Control System (PSGCS, the P02 SSP system), and samples of Gathering and Production and Integrity Services controls |
| Tier / Vertical | Multi-Sector / Energy (focus division: Gas Transmission) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only. The Integrity Services OT Assessment Practice did not take part (POL-01 4.9) |
| Assessment window | 2026-07-06 to 2026-08-28. OT tests at Compressor Station 27 during a planned outage on 2026-08-12 and at Arkoma field sites on 2026-08-19 |
| Also supports | The Gas Transmission TSA Cybersecurity Assessment Plan (SD 02G III.G): results are recorded as evidence for 21 of its 96 measures. It does not replace the separate architecture design review (III.G.2.b) |

## 1. Approach: assess common controls once, then sample divisions
Most IT safeguards in all three divisions come from the same corporate providers, so:
1. **Common controls** marked "Yes (common control, assessed once)" in the P02 common control catalog were assessed **once**, with samples drawn from every division (the joiner-mover-leaver sample took events from all three divisions and corporate).
2. **The PSGCS** was assessed comprehensively on the controls marked "Yes (PSGCS scope)" in the catalog plus two system-specific controls (CM-3 and SA-22), because it is the SSP system, a TSA Critical Cyber System, and the center of GR-01, GR-03, and GR-06.
3. **Division samples** covered controls each division operates itself, chosen from its High risks and P03 gaps. Division findings are reported to that division, not averaged into the group.

Gathering and Production was sampled on governance (CA-2, PL-1) because its inheritance is undocumented (scenario gap 7) and its supplement has drifted (gap 10), and on the Arkoma assets (gap 4). Integrity Services was sampled on SSI handling (gap 2).

## 2. Controls selected
**36 control assessments** (32 distinct controls; AC-17, CA-2, IA-5, and SA-22 were assessed in two scopes), **262 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity and OT remote access gateway) | AC-2, AC-17, IA-2, IA-2(1), AC-6(5), PS-4 | 39 | Every division's access control; GR-02; scenario gap 3 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR) | AT-2 | 10 | Training for 45,000 users; SD 02G III.D.1.a | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-05, GR-15; scenario gaps 3 and 8 | Focused / Comprehensive |
| Common control (SYS-G3 cloud, network, and data centers) | CP-9, SC-28, CM-6 | 13 | Immutable backups and cloud guardrails; GR-16 | Focused / Focused |
| PSGCS (Gas Transmission) | IA-5, CA-2, CM-3, AT-3, SI-2, SA-22, AU-11, CP-2, CP-4, SC-7 | 88 | P02 SSP system; GR-01, GR-03, GR-06; TSA plan measures; scenario gaps 1, 5, 6 | Comprehensive / Comprehensive |
| Division sample: Gathering and Production | CA-2, PL-1, IA-5, AC-17, SA-22 | 44 | GP-001, GP-006, GP-008, GP-011; scenario gaps 4, 7, 10 | Focused / Focused (Haynesville and 2 Arkoma field offices) |
| Division sample: Integrity Services | AC-3, MP-3, MP-6, AC-6, SA-9 | 14 | ES-001, ES-002, ES-003, ES-009; scenario gap 2 | Focused / Focused (5 designated-client SSI sets) |
| **Total** | **36** | **262** | | |

## 3. Methods and objects
- **Examine:** identity governance, PAM, and gateway configuration; SIEM sources, OT sensor coverage, and baselines; backup and immutability settings; the TSA plans and tracker (SSI, reviewed on site and cited by section only); control room change records and point-to-point records; controller training content; division supplements; client deliverables and SSI sets; vendor files.
- **Interview:** group identity, SOC, OT security, and cloud directors; the Director of Pipeline Cybersecurity; the Director of Gas Control and 6 controllers; the SCADA Engineering Manager; the Vice President of Field Operations Technology and 8 field staff; the Integrity Services Client Security Officer and OT Assessment Practice Leader; the Group General Counsel.
- **Test:**
  - a joiner-mover-leaver sample of 60 events and 25 terminations across divisions;
  - administrator sign-in with a hardware key and federation checks on 40 applications;
  - a passive detection test at Compressor Station 27 during the 2026-08-12 planned outage (a scripted connection from the regional DMZ to the station network, which the SOC detected in 6 minutes);
  - a check of the unit control panel password at Compressor Station 27 against the plan schedule;
  - a passive credential check of field devices at two Arkoma sites on 2026-08-19 (default administrator passwords found on 5 devices);
  - restores of 2 cloud workloads from the provider B vault;
  - permission tests on 5 designated-client SSI sets and a review of 6 assessment toolkits.

## 4. Rules of engagement
- No active scanning or testing on live OT. OT tests ran only during the planned outage at Compressor Station 27 and with the Director of Gas Control's approval; field checks at Arkoma were read-only, with the field supervisor present.
- Controllers had authority to stop any test at any time. None was stopped.
- SSI was reviewed on site and not copied into workpapers; findings cite plan sections only.
- The assessor would stop and notify the Group CISO and the Director of Pipeline Cybersecurity on any critical exposure. The Arkoma default passwords were reported the same day and changed by 2026-09-10.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 105 | 11 | 116 |
| PSGCS (Gas Transmission) | 71 | 17 | 88 |
| Division sample: Gathering and Production | 32 | 12 | 44 |
| Division sample: Integrity Services | 9 | 5 | 14 |
| **Total** | **217** | **45** | **262** |

**Common controls are strong.** 105 of 116 common statements were satisfied. Identity authentication (IA-2, IA-2(1), AC-6(5)), terminations (PS-4), training (AT-2), vulnerability scanning (RA-5), and cloud protection (CP-9, SC-28, CM-6) had no findings. The common findings are about **the shared OT access path** (AC-17, AC-2; scenario gap 3), **OT monitoring coverage** (SI-4), and **cross-division incident handling and notification** (IR-3, IR-4, IR-6, IR-8; scenario gap 8).

**The PSGCS** satisfied 71 of 88 statements. Every PSGCS control had at least one finding, but most are narrow: TSA plan discipline (IA-5 panel passwords, CA-2 review interval; gap 5), the corporate IT seam (SC-7, CP-2, CP-4; gap 1), control room records and analytics change control (CM-3, AT-3; gaps 6 and 9), and patching and log retention (SI-2, SA-22, AU-11).

**Division samples:**
- *Gathering and Production:* 12 of 44 statements failed. Inheritance never documented or assessed (CA-2), a 2023 supplement that conflicts with group policy (PL-1), and the Arkoma assets: default device passwords, an always-on vendor connection, and unsupported systems (IA-5, AC-17, SA-22).
- *Integrity Services:* 5 of 14 statements failed. SSI without need-to-know or marking (AC-3, MP-3), toolkits reissued with earlier clients' captures (MP-6), standing access to the Transmission historian replica (AC-6), and annual-only subservice reviews (SA-9).

**Controls fully other than satisfied** (every statement failed): IR-3 (Common control, 1 statement), SA-22 (PSGCS, 2 statements), AU-11 (PSGCS, 1 statement), SA-22 (Gathering and Production, 2 statements), AC-3 (Integrity Services, 1 statement), AC-6 (Integrity Services, 1 statement).

27 of the 36 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **26 items**: 23 from this assessment and 3 from the P03 gap analyses (POAM-023, POAM-024, POAM-025). By risk: 12 High (POAM-001, POAM-003, POAM-006, POAM-007, POAM-008, POAM-009, POAM-014, POAM-015, POAM-019, POAM-020, POAM-023, POAM-026) and 14 Moderate. Status: 24 In progress, 2 Open. Each item names the related P01 risks in `related_risk_ids`. POAM-026 also closes the P03 control room change management gap (G-104).

## 7. Deliverables and acceptance
`assessment-results.csv` (262 rows, with an `assessment_scope` column), `poam.csv` (26 items), and this plan and summary. Results were presented to the board risk committee on 2026-09-22 and accepted by the Group CISO and the Group Chief Risk Officer the same day. Division presidents accepted their division findings the same week.

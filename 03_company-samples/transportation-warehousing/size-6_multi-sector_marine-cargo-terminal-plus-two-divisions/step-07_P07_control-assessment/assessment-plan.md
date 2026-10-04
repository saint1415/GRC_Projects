# Security Assessment Plan and Summary: Cris Santos Company Holdings | Transportation and Warehousing | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1 to SYS-G4, group HR), the Terminal Operations Platform (P02 SSP), and samples of Marine Terminals (Gulf terminals), Freight Trading and Port Real Estate controls |
| Tier / Vertical | Multi-Sector / Transportation and Warehousing (focus division: Marine Terminals) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. It has no regular cybersecurity duties at any terminal, so its results can support the Cybersecurity Plan audits (33 CFR 101.630(f)(4)). Division leads and the Division CySO acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28; OT tests at T5 on the night of 2026-08-12, with no vessel at berth |
| Also supports | Each terminal's Cybersecurity Assessment (101.650(e)(1)); the Freight Trading CMMC Level 1 re-assessment (32 CFR 170.15); the board's oversight for Reg S-K Item 106 |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took 75 events from all three).
2. **The Terminal Operations Platform's** system-specific controls were assessed because it is the SSP system, carries the affiliate data risk (GR-02) and sits next to OT at six regulated facilities.
3. **Division samples** covered controls each division operates itself, chosen from its High risks and P03 gaps. Division findings are reported to that division, not averaged into the group:
   - *Marine Terminals:* the Gulf terminals (T7 to T9), sampled at T8, because they sit outside the standard design (scenario gap 2).
   - *Freight Trading:* the CMMC Level 1 scope and DoD reporting (gap 4).
   - *Port Real Estate:* governance and integrator access, because its inheritance is undocumented (gap 6) and its supplement has drifted (P06).

## 2. Controls selected
**44 control assessments** (36 distinct controls; AC-3, AC-17, CA-2, CP-9, IA-5, IR-6 and SC-7 were assessed in more than one scope), **269 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2(1), IA-2(2), IA-5 | 43 | Every division's access control; GR-02, GR-10 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR) | PS-4, AT-2 | 15 | Terminations; Subpart F training for all personnel including longshore workers | Focused / Focused (4 hiring halls) |
| Common control (SYS-G2 SOC) | SI-4, IR-4, IR-6, IR-8, RA-5, AU-6 | 56 | GR-01, GR-03, GR-11; scenario gaps 2, 5 and 7 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-12, SC-28 | 15 | GR-01; immutable backups and guardrails | Focused / Focused |
| Common control (SYS-G4 integration hub) | SC-8, CA-3 | 9 | GR-01, GR-16; the hub is the P08 starting point | Focused / Comprehensive (all partner connections) |
| Terminal Operations Platform | AC-3, AC-6, AC-17, CM-4, CM-7, CM-8, CP-4, SI-2, IA-5, MP-7, AT-3 | 56 | GR-02 and gap 1; GR-09 and gap 8; Subpart F measures at T1 to T6 | Comprehensive / Focused (T2 and T5 on site) |
| Division sample: Marine Terminals (Gulf terminals) | SC-7, CP-9, AU-9, AC-17, IR-3 | 19 | MT-002 (Very High), MT-003, MT-004, MT-005 | Focused / Focused (T8 on site; T7 and T9 by document) |
| Division sample: Freight Trading | CA-2, AC-3, MP-6, IR-6 | 18 | FT-001, FT-002 (High); gap 4 | Focused / Focused (6 of 38 yards) |
| Division sample: Port Real Estate | CA-2, AC-17, PL-1, SA-9 | 38 | RE-001 (High); gaps 5 and 6 | Focused / Focused (all 49 sites by scan) |
| **Total** | **44** | **269** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, SIEM data sources and rules, landing-zone and hub configuration, backup and immutability settings, the TOS role matrix, change records, OT inventories, contingency and drill records, the CMMC scope and SPRS record, integrator contracts, division standards.
- **Interview:** the group identity, SOC, cloud and integration directors; the director of terminal systems; the Division CySO and FSOs at T2, T5 and T8; the director of engineering; hiring hall dispatch staff; the federal contracts compliance manager; the director of building technology.
- **Test:**
  - a joiner-mover-leaver sample of 75 events across divisions, and 25 terminations;
  - a hardware-key administrator sign-in and federation checks on 52 applications;
  - test queries under 5 TOS roles, including group logistics, using a test account;
  - a restore of a SYS-T1 database copy and a SYS-G4 configuration from the provider B vault;
  - a TLS scan of 45 partner endpoints and an external exposure scan of the landing zones and of 49 Port Real Estate sites;
  - a simulated vendor modem session to a T8 crane HMI, with SOC approval, to test detection;
  - night tests at T5 on 2026-08-12: credential and USB port checks on gate devices and ASC maintenance HMIs.

## 4. Rules of engagement
- No testing that could move equipment or affect a vessel operation. OT tests at T5 ran with no vessel at berth, the ASC block in maintenance mode and the T5 FSO and engineering lead present. At T8 the simulated session connected to an HMI in a crane parked for maintenance.
- No customer cargo data left group systems; test queries used a test account and results were destroyed after counting.
- SSI (network details, Plan drafts) stayed in the SSI library; this summary gives counts only.
- The assessor would stop and notify the Group CISO and the Division CySO of any critical exposure. One was reported on 2026-08-12 (the default passwords at T5); it was fixed by 2026-09-22.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls (SYS-G1 to SYS-G4, group HR) | 121 | 17 | 138 |
| Terminal Operations Platform | 44 | 12 | 56 |
| Division sample: Marine Terminals (Gulf terminals) | 10 | 9 | 19 |
| Division sample: Freight Trading | 13 | 5 | 18 |
| Division sample: Port Real Estate | 30 | 8 | 38 |
| **Total** | **218** | **51** | **269** |

The 51 statements other than satisfied carry these risk levels: 23 High, 26 Moderate and 2 Low.

**Common controls are strong.** 121 of 138 common statements were satisfied. Privileged access (AC-6(5)), MFA (IA-2(1), IA-2(2)), inactive account handling (AC-2(3)), terminations (PS-4), activity review (AU-6) and every cloud control tested (CP-9, SC-7, SC-12, SC-28) had no findings. The common findings are about **coverage, not design**: service accounts and cross-division certification (AC-2, IA-5), longshore training (AT-2), monitoring that stops at the Gulf terminals and the building systems (SI-4, RA-5), cross-division incident consistency and notification (IR-4, IR-6, IR-8; scenario gap 7), and the integration hub's shared routes and FTP partners (SC-8, CA-3).

**The Terminal Operations Platform** is sound at the infrastructure layer (remote access through the jump host, AC-17, had no findings) but has two High problems inside the application and at its edge:
- The group logistics role (AC-3, AC-6): a Freight Trading test user retrieved competing importers' cargo data (scenario gap 1).
- The unreviewed change that let SYS-T5 sequence ASCs at T5 (CM-4; gap 8).

It also has Subpart F gaps at T1 to T6: OT training (AT-3), OT inventory and allowlisting (CM-8, CM-7), OT KEVs (SI-2), the untested T5 restore (CP-4), and the new finding below.

**New finding (fed back to P01).** The night test at T5 found **default vendor passwords on 2 OCR portal controllers and 4 ASC maintenance HMIs**, and open USB ports on the same HMIs (IA-5, MP-7). This became P01 risk MT-024 and POAM-006 and POAM-020.

**Division samples:**
- *Marine Terminals, Gulf terminals:* flat networks with unmonitored IT-OT traffic (SC-7), local-only backups (CP-9), deletable local logs (AU-9), always-on vendor modems (AC-17) and no cyber drills (IR-3). 9 of 19 statements failed; these are the Very High risk MT-002.
- *Freight Trading:* the Level 1 scope omitted SYS-F2 (CA-2), CUI sat in general systems (AC-3), scale PCs were disposed of without records (MP-6), and there is no DFARS reporting procedure (IR-6).
- *Port Real Estate:* no inheritance documentation (CA-2), internet-exposed integrator access (AC-17), a 2023 supplement that conflicts with group policy (PL-1) and integrator contracts without security terms (SA-9).

**Controls fully other than satisfied** (every statement failed): SC-8 (SYS-G4), AC-3 and AC-6 (Terminal Operations Platform), AU-9 and IR-3 (Gulf terminals), and AC-3 (Freight Trading). Each has one or two determination statements.

33 of the 44 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **27 items**: 23 from this assessment (POAM-001 to POAM-023) and 4 from the P03 gap analyses (POAM-024 to POAM-027). By risk: 15 High and 12 Moderate. Status: 22 In progress and 5 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (269 rows, with an `assessment_scope` column), `poam.csv` (27 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-15. Division presidents accepted their division findings the same week. The Division CySO will use the Marine Terminals results in each terminal's Cybersecurity Assessment.

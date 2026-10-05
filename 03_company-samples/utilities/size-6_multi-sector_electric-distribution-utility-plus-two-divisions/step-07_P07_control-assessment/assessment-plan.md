# Security Assessment Plan and Summary: Cris Santos Company Holdings | Utilities | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G4, group HR, learning, procurement, and governance), the Distribution Operations Platform (P02 SSP), and samples of Gas Production and Engineering Services controls |
| Tier / Vertical | Multi-Sector / Utilities (focus division: Electric Utility) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only. The SYS-G4 design was reviewed by an outside firm in 2026 because internal audit had advised on its rollout |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Relation to NERC CIP | The TCC's medium impact program is audited by SERC and tested quarterly by the Electric Utility's CIP internal controls team, so this assessment did not re-test it. CIP findings from the P03 gap analysis are carried in the same POA&M |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three, and the SYS-G4 session sample covered all three OT environments).
2. **The DOP's** system-specific controls were assessed because it is the SSP system and carries the group's High risk GR-02.
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Gas Production was sampled on governance controls (PL-1, CA-2) because its standards have drifted (scenario gap 6) and its inheritance is undocumented (gap 7). Engineering Services was sampled on client information and client notice controls (gaps 4 and 5).

## 2. Controls selected
**34 control assessments** (28 distinct controls; AC-2, AC-6, CA-2, CP-9, IR-6, and SC-7 were assessed in two scopes), **254 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 and SYS-G4 identities) | AC-2 | 26 | GR-01; every division's accounts | Focused / Comprehensive (all divisions sampled) |
| Common control (SYS-G4 OT remote access) | AC-17, AC-17(1), MA-4 | 14 | GR-01 (High); scenario gap 1 | Comprehensive / Comprehensive (3 OT environments) |
| Common control (SYS-G1 identity) | IA-2(1) | 1 | Administrator MFA for all divisions | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-4, IR-6 | 27 | GR-02, GR-03; scenario gaps 2 and 9 | Focused / Comprehensive |
| Common control (group governance) | IR-8 | 17 | GR-03; scenario gap 9 | Focused / Focused |
| Common control (Group HR and learning) | PS-3, PS-4, AT-2 | 18 | Personnel controls for 45,000 users | Focused / Focused |
| Common control (group procurement) | SA-9, SR-6 | 7 | GR-07; affiliate as vendor (gap 4) | Focused / Focused |
| DOP (P02 SSP) | AC-4, AC-6, SC-7, CM-8, CP-2, CP-4, CP-9, SA-22, AU-6 | 54 | GR-02 (High); EU-002, EU-003, EU-006; scenario gap 2 | Comprehensive / Focused (DCC and backup DCC; 3 distribution substations) |
| Division sample: Gas Production | PL-1, CA-2, AC-2, SC-7, CP-9 | 66 | GP-001, GP-003, GP-005, GP-006; gaps 6 and 7 | Focused / Focused (POC; 3 compressor stations) |
| Division sample: Engineering Services | AC-3, AC-6, IR-6, MA-3, PL-4, CA-2 | 24 | ES-001, ES-005, ES-006, ES-008; gaps 4, 5, and 7 | Focused / Focused (25 projects; 12 site connections) |
| **Total** | **34** | **254** | | |

## 3. Methods and objects
- **Examine:** identity governance and SYS-G4 entitlement exports, SYS-G4 session recordings, SIEM sources and use cases, IT/OT firewall rules, DOP inventory and contingency plan, backup architecture, division standards, project platform permissions, contracts and vendor files.
- **Interview:** Group OT security director; group identity and SOC directors; Electric Utility distribution operations director and OT engineering manager; DCC shift supervisors; Gas Production SCADA and automation manager; Engineering Services contracts director and security and compliance lead.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions and 25 terminations;
  - 40 sampled vendor maintenance sessions through SYS-G4, and a test session to a substation without a sensor;
  - a simulated network scan inside the DOP test network segment at the DCC (scheduled with the shift supervisor; no production switching affected);
  - a test connection from the corporate network to DOP hosts through the firewall;
  - a test of backup deletion rights with an OT administrator account in the test environment;
  - an external exposure scan of Gas Production modem addresses (approved by the division president);
  - access attempts to CEII and BCSI folders on 25 projects with a non-project engineer account.

## 4. Rules of engagement
- No testing that could affect grid operations, gas deliveries, or client systems. DOP tests ran in the test network or outside switching hours with the shift supervisor's approval. Substation and modem tests were passive or read-only.
- No BCSI, CEII, or personal information left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO and the affected shift supervisor on any critical exposure. One was found: the internet-reachable well pad modems (Gas Production SC-7). The division moved the 20 highest-producing pads to a private APN on 2026-08-21, before the report; the rest are in POAM-019.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 89 | 21 | 110 |
| DOP (P02 SSP) | 39 | 15 | 54 |
| Division sample: Gas Production | 52 | 14 | 66 |
| Division sample: Engineering Services | 18 | 6 | 24 |
| **Total** | **198** | **56** | **254** |

**Common controls are sound where they were designed for IT.** Administrator MFA (IA-2(1)) and personnel screening (PS-3) had no findings, and most statements for monitoring, incident handling, and training were satisfied. The common findings sit where a common service meets OT and affiliates: **SYS-G4 entitlements** (AC-2, AC-17, MA-4: standing access without per-session approval, scenario gap 1), **detection coverage** (AC-17(1), SI-4), **cross-division incident consistency and notification** (IR-4, IR-6, IR-8, gap 9), and the **affiliate treated as an insider** (SA-9, SR-6, gap 4).

**The DOP is where the operational risk is.** AC-4, AC-6, and SA-22 were fully other than satisfied. The scan inside the DCC test segment went undetected (SI-4), broad firewall rules and DMZ bypasses were confirmed (SC-7), and an OT administrator account could delete backups (CP-9). The contingency plan assumes the standby cluster survives (CP-2).

**Division samples:**
- *Gas Production:* a 2023 supplement never re-aligned (PL-1), inheritance never documented (CA-2), shared SCADA accounts (AC-2), internet-reachable modems (SC-7), and monthly offline backups (CP-9).
- *Engineering Services:* client CEII and BCSI folders open to project-wide groups, including the Electric Utility's TCC BCSI (AC-3, AC-6), no client notice register (IR-6), unevidenced laptop connections (MA-3), no AI rules in the division's rules of behavior (PL-4), and an incomplete SOC 2 scope (CA-2).

**Controls fully other than satisfied** (every statement failed): SR-6 (common), AC-4, AC-6, and SA-22 (DOP), and AC-3 and AC-6 (Engineering Services). Each has one or two determination statements.

32 of the 34 control assessments had at least one statement other than satisfied (only IA-2(1) and PS-3 were clean). All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **26 items**: 21 from this assessment, 4 from the P03 gap analysis (POAM-012 to POAM-015, the potential CIP noncompliances; POAM-013 and POAM-015 were also confirmed by P07 tests), and 1 from the P10 AI assessment (POAM-024). By risk: 9 High, 16 Moderate, and 1 Low. Status: 17 In progress, 9 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (254 rows, with an `assessment_scope` column), `poam.csv` (26 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-15. Division presidents accepted their division findings the same week; the CIP Senior Manager accepted the CIP-related items and approved the self-reports.

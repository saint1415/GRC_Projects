# Security Assessment Plan and Summary: Cris Santos Company Holdings | Chemical | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1 identity and the OT remote access gateway, SYS-G2 SOC and OT desk, SYS-G3 cloud and WAN, Group HR), the Plant C1 PCBMS (P02 SSP), and samples of Specialty Chemicals, Distribution, and Hazmat Transport controls |
| Tier / Vertical | Multi-Sector / Chemical (focus division: Specialty Chemicals) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`), with OT test cautions from NIST SP 800-82 Rev. 3 |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls, with a contracted OT test firm under its direction. Division security and compliance leads acted as liaisons only. The Terminal T1 work also counts toward the independence the USCG rule requires for future Plan audits (33 CFR 101.630(f)(4)) |
| Assessment window | 2026-07-06 to 2026-08-28. OT tests at Plant C1 on 2026-08-12 (planned turnaround), at Terminal T1 on 2026-08-19, and at two Hazmat Transport terminals on 2026-08-25 |
| Also supports | RBPS 8 benchmark audits (voluntary), the Terminal T1 Cybersecurity Assessment (33 CFR 101.650(e)(1)), and the RMP compliance audit cycle at Plant C1 (40 CFR 68.79; next due 2028-05-14) |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three, and gateway sessions were sampled at three plants and Terminal T1).
2. **The PCBMS** (Plant C1) system-specific controls were assessed because it is the SSP system and carries the top division risks (SC-001, SC-007).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps:
   - *Specialty Chemicals:* 2 of the 7 legacy plants (segmentation and backups) and the PHA program (Plant C1 and 2 Program 2 plants).
   - *Distribution:* Terminal T1 against the USCG rule, and the managed inventory service's vendor portal.
   - *Hazmat Transport:* governance controls, because its inheritance is undocumented (scenario gap 7) and its supplement has drifted (gap 10), plus ELD accounts at two terminals.

Division findings are reported to that division, not averaged into the group.

## 2. Controls selected
**42 control assessments** (34 distinct controls; RA-3, IA-5, and IA-2(1) were assessed in two scopes, CP-9 in three, and SC-7 in four), **281 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, IA-2(1), IA-5, AC-6(5) | 38 | Every division's access; GR-01 | Focused / Comprehensive (all divisions sampled) |
| Common control (SYS-G1 OT remote access gateway) | AC-17, AC-17(1), AC-17(4), MA-4 | 19 | GR-01 (High); scenario gap 1 | Comprehensive / Comprehensive (17 sites reviewed, 20 sessions sampled) |
| Common control (Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC and OT desk) | SI-4, IR-4, IR-6, IR-8, IR-3, RA-5 | 54 | GR-05, GR-07; scenario gap 8 | Focused / Comprehensive |
| Common control (SYS-G3 cloud and WAN) | CP-9, SC-7 | 12 | GR-03; immutable backups and guardrails | Focused / Focused |
| PCBMS (Plant C1, SSP system) | AC-3, AC-4, AC-6, CM-3, CM-4, CM-5, AU-6, CP-9, CP-4, SI-7, SC-7 | 47 | SC-001, SC-003, SC-007 (High); gaps 3 and 9 | Comprehensive / Comprehensive |
| Division sample: Specialty Chemicals | SC-7, CP-9, RA-3 | 20 | GR-05, SC-003; gaps 2 and 3 | Focused / Focused (2 of 7 legacy plants; 3 PHAs) |
| Division sample: Distribution | IA-5, AT-3, CM-8, SC-7, SA-9, IA-2(1) | 38 | DS-001, DS-006 (High); gaps 4 and 6 | Focused / Focused (Terminal T1; vendor portal) |
| Division sample: Hazmat Transport | IA-2, CA-2, PL-1, RA-3 | 38 | Gaps 5, 7, and 10 | Focused / Focused (2 of 28 terminals) |
| **Total** | **42** | **281** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration; gateway policies and session records; SIEM data sources and OT desk rules; OT DMZ firewall rules; DCS role matrix and event journal; MOC records and the recipe push log; PHAs and hazard reviews; backup and restore records; Terminal T1 inventory, network map, and training records; vendor contracts; the Hazmat Transport supplement and security plan.
- **Interview:** Group OT Security Director, group identity and SOC directors, the Plant C1 Plant Manager, Process Safety Manager, and Controls Engineering Manager, shift superintendents, the Terminal T1 Terminal Manager, FSO, and CySO, the managed inventory service director, the Hazmat Transport Vice President of Safety and Compliance, and the Group General Counsel.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, 25 terminations, and 6 integrator leavers;
  - a test gateway session to the Plant C1 jump host and a review of 20 integrator sessions at Plant C1, 2 other plants, and Terminal T1;
  - **Plant C1 (2026-08-12, during the turnaround, with the reactors shut down and chlorine cars isolated):** a scan of the OT DMZ from the business network, role tests on an operator station, a simulated engineering command watched by the OT desk, and a configuration restore on spare hardware;
  - **Terminal T1 (2026-08-19):** a credential check of OT devices, a passive capture on the rack segment, and a walkthrough;
  - **legacy plants (2026-07-21 and 2026-07-23):** passive capture only;
  - **Hazmat Transport terminals (2026-08-25):** ELD account review;
  - restores of 3 cloud workloads and the Plant C1 configuration copy from the provider B vault;
  - an administrator sign-in test on the telemetry vendor portal.

## 4. Rules of engagement
- **Safety first.** No active scanning or testing of controllers, SIS, PLCs, or HMIs on a running process. Active tests at Plant C1 ran only during the turnaround, with the Plant Manager's written approval and the process in a safe state. At Terminal T1 and the legacy plants, tests on OT networks were passive. The plant or terminal could stop any test at any time.
- No testing that could affect deliveries to water utility customers, vessel transfers, or loads in transit.
- SSI and legacy CVI stayed inside group systems; screenshots were redacted.
- The assessor would stop and notify the Group CISO and the site on any critical exposure. One was found: the default passwords at Terminal T1, reported on 2026-08-19 (changed 2026-09-10).

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 121 | 17 | 138 |
| PCBMS (Plant C1) | 36 | 11 | 47 |
| Division sample: Specialty Chemicals | 13 | 7 | 20 |
| Division sample: Distribution | 27 | 11 | 38 |
| Division sample: Hazmat Transport | 28 | 10 | 38 |
| **Total** | **225** | **56** | **281** |

**Common controls are strong, except the gateway.** 121 of 138 common statements were satisfied. Identity (IA-2(1), AC-6(5)), terminations and training (PS-4, AT-2), and cloud backups and boundaries (CP-9, SC-7) had no findings. The common findings concentrate in two places:
- **The OT remote access gateway** (AC-17, AC-17(1), AC-17(4), MA-4, and the related AC-2 and IA-5 statements on shared integrator accounts): no per-session site approval, recording at 9 of 17 sites, standing hub connections (scenario gap 1).
- **Incident consistency and notification** (IR-3, IR-4, IR-6, IR-8): the matrix has not been exercised (gap 8), and Hazmat Transport still uses its own severity scale (gap 10).
Monitoring at legacy plants (SI-4) and remediation speed (RA-5) were also other than satisfied.

**The PCBMS is well built but changes reach it by unguarded paths.** Access enforcement (AC-3), backups (CP-9), and the OT DMZ boundary (SC-7) were satisfied. AC-4 and AC-6 failed outright: the AI-001 write rule and broad engineering rights. CM-3, CM-4, and CM-5 failed on the paths that bypass MOC (gaps 3 and 9).

**Division samples:**
- *Specialty Chemicals:* the 2 sampled legacy plants have flat networks, always-on integrator tools, and weak backups (SC-7, CP-9; gap 2); the PHAs do not treat control system compromise as a cause (RA-3; gap 3).
- *Distribution:* Terminal T1 had default passwords, untrained contractors, an outdated inventory and map, and rack PLCs on the office segment (IA-5, AT-3, CM-8, SC-7; gap 4). The telemetry vendor portal has no MFA and no vendor oversight (SA-9, IA-2(1); gap 6).
- *Hazmat Transport:* shared ELD support accounts (IA-2), no assessment of inherited or technical controls (CA-2; gap 7), a drifted supplement (PL-1; gap 10), and a security plan risk assessment without cyber threats (RA-3; gap 5).

**Controls fully other than satisfied** (every statement failed): IR-3 (common), AC-4 and AC-6 (PCBMS), IA-2(1) (Distribution vendor portal), and IA-2 (Hazmat Transport). The first four have one determination statement each; IA-2 has two.

33 of the 42 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **27 items**: 22 from this assessment and 5 from the P03 gap analyses, the P02 SSP, and the P10 AI assessment (POAM-013, POAM-020, POAM-021, POAM-022, POAM-025). By risk: 9 High (POAM-001, POAM-003, POAM-004, POAM-005, POAM-006, POAM-010, POAM-011, POAM-019, POAM-021), 16 Moderate, and 2 Low. Status: 18 In progress, 9 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (281 rows, with an `assessment_scope` column), `poam.csv` (27 items), and this plan and summary. Results were presented to the board risk committee on 2026-09-17 and accepted by the Group CISO and the Group Chief Risk Officer. Division presidents accepted their division findings the same week. The Plant C1 Plant Manager, as RMP qualified person, accepted the PCBMS findings and the interim measures in P02 section 4.2.

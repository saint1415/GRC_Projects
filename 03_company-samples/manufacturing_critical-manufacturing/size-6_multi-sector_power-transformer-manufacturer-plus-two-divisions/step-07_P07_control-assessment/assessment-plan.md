# Security Assessment Plan and Summary: Cris Santos Company Holdings | Critical Manufacturing | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the Group ERP and Production Scheduling Platform (GEPS, the P02 SSP system), and samples of Transformer Manufacturing, Electric Utility, and Grid Engineering controls |
| Tier / Vertical | Multi-Sector / Critical Manufacturing (focus division: Transformer Manufacturing) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. The P8 OT tests were co-sourced with an outside OT assessment firm, because the Group OT security director wrote the group OT standard; group internal audit signed the results. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 (P8 OT tests in the maintenance window on 2026-08-22) |
| Also supports | CSF 2.0 ID.IM-01 (P03 G-066); evidence for the Grid Engineering SOC 2 period and the FMS readiness (P09). It does **not** replace the Electric Utility's CIP compliance monitoring, internal controls, or SERC audits |

## 1. Approach: assess common controls once, then sample divisions
All three divisions sign in through the same identity platform, are watched by the same SOC, and run their cloud workloads in the same landing zones. Testing those controls three times would waste effort and give three slightly different answers. So:
1. **Common controls** marked for 2026 in the P02 common control catalog (18 controls) were assessed **once**, across all divisions, with samples drawn from every division and from P8 (for example, the joiner-mover-leaver sample took events from all three divisions and the acquired plant).
2. **The GEPS** system-specific controls were assessed because it is the SSP system and carries two High group risks (GR-01, GR-02).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Six controls were assessed in more than one scope because the division runs its own version: SC-7 and CP-9 (group cloud, and P8), IR-6 (group SOC, the Electric Utility reporting desk, and Grid Engineering client notices), AC-3 (the utility's BCSI and Grid Engineering's client folders), CM-6 (cloud guardrails, and commissioning laptops), and SI-4(4) (GEPS hub traffic, and substation vendor access).

## 2. Controls selected
**44 control assessments** (37 distinct controls), **225 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2(1), IA-5 | 42 | Every division's access; GR-07 (P8 trust); GR-02 (hub accounts) | Focused / Comprehensive (all divisions and P8 sampled) |
| Common control (Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-01, GR-03, GR-12; scenario gap 7 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-8, SC-28, CM-6 | 20 | Immutable backups and landing-zone guardrails behind every division | Focused / Focused |
| GEPS | AC-4, AC-6, CA-3, CP-4, CP-10, AU-6, SI-4(4) | 24 | GR-02 (High); scenario gap 1 | Comprehensive / Comprehensive |
| Division sample: Transformer Manufacturing | SC-7, AC-17, CP-9, SA-22 (P8); SI-7, SC-12, SR-4, IR-6(3) (TMU product) | 30 | MF-001, MF-003, MF-005, MF-006 (High and Moderate); gaps 2 and 3 | Comprehensive at P8; Focused for the product |
| Division sample: Electric Utility | AC-3, PS-3, IR-6, SR-6, SI-4(4) | 11 | EU-001 (High), EU-003, EU-006, EU-008; gaps 4 and 5 | Focused / Focused (controls touching group services and affiliates only) |
| Division sample: Grid Engineering | AC-3, AU-11, CM-6, MP-7, IR-6, PL-1 | 29 | ES-001, ES-003 (High), ES-002, ES-007; gap 6 | Focused / Focused (20 projects, 40 laptops) |
| **Total** | **44** | **225** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, the GEPS service account register and integration hub configuration, interface and interconnection records, DR test reports, SIEM data sources and rules, IR plan v5, the draft notification matrix, landing-zone policies and backup settings, P8 firewall exports and network capture, firmware release records and the build server keystore, SBOMs, the PSIRT log, PRA attestations, the utility's reporting procedures and CIP-013-2 vendor files, project platform permissions and retention settings, laptop images and patch reports, and the 2023 Grid Engineering standards.
- **Interview:** the group identity, SOC, cloud platform, and ERP platform directors; the VP manufacturing operations; the Director of OT engineering and the P8 plant manager; the Chief product security officer; the Electric Utility NERC compliance director and system operations director; the Grid Engineering contracts director, project platform director, and chief operating officer.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions and P8, and 25 terminations;
  - a hardware-key administrator sign-in and federation checks on 40 applications;
  - restores of 3 cloud workloads from the immutable vault, and a TLS scan of 60 endpoints;
  - a read-only review of hub service account permissions against each plant MES;
  - at P8 on 2026-08-22: passive network capture, a firewall rule review, and identification of the cellular routers and the historian connector (no active scanning of controllers);
  - a check of 10 firmware releases against published hashes;
  - a review of 40 commissioning laptops against the hardened image.

## 4. Rules of engagement
- No testing that could affect plant processes, the TCC or substations, or customer systems. OT work at P8 was passive only, in the 2026-08-22 maintenance window, with the plant manager's approval and an operator present.
- No BCSI or CEII left its authorized location. The utility's NERC compliance director selected the BCSI samples and screenshots were redacted.
- The assessor would stop and notify the Group CISO, and for OT the plant manager, on any critical exposure or safety concern. None was found.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 113 | 18 | 131 |
| GEPS | 13 | 11 | 24 |
| Division sample: Transformer Manufacturing | 13 | 17 | 30 |
| Division sample: Electric Utility | 5 | 6 | 11 |
| Division sample: Grid Engineering | 19 | 10 | 29 |
| **Total** | **163** | **62** | **225** |

**Common controls are strong.** 113 of 131 common statements were satisfied. Cloud protection (CP-9, SC-7, SC-8, SC-28, CM-6), administrator controls (AC-6(5), IA-2(1)), terminations in SYS-G1 (PS-4), and training (AT-2) had no findings. The common findings cluster in three places:
- **Service accounts** (AC-2, IA-5): the GEPS team manages hub and batch accounts outside identity governance with old static keys.
- **The acquired plant P8** (AC-2, AC-2(3), RA-5, SI-4): the legacy domain still holds stale and unterminated accounts, P8 is outside regular scanning, and nothing monitors P8 or the DCC.
- **Cross-division incident handling** (IR-3, IR-4, IR-6, IR-8): one plan exists but it does not define contract or reliability reportable incidents, the matrix is not adopted, divisions still use different scales, and nothing has been exercised (scenario gap 7).

**The GEPS is where the group risk sits.** AC-4, AC-6, and CP-10 were fully other than satisfied: the hub reaches every plant with the same over-privileged accounts, and recovery of scheduling has never been shown (scenario gap 1).

**Division samples:**
- *Transformer Manufacturing:* P8 is flat, dual-homed, reachable through always-on OEM routers, and not backed up in a way that would support recovery (SC-7, AC-17, CP-9, SA-22). The TMU signing key is not in a hardware security module (SC-12), SBOMs are incomplete (SR-4), and two utility advisories were late (IR-6(3)). Firmware release hashes matched for all 10 sampled releases.
- *Electric Utility:* the TCC program held up. Findings are all at its edges: affiliate access to BCSI (AC-3) and the affiliate PRA attestation (PS-3), no CIP-013-2 assessment of the affiliates (SR-6), the DCC's DOE-417 procedure (IR-6), and vendor access detection at 36 low impact substations (SI-4(4)).
- *Grid Engineering:* client BCSI folders open to whole projects (AC-3), 90-day log retention (AU-11), uneven laptop hardening and personal USB media (CM-6, MP-7), no route for client notices (IR-6), and standards that drifted from group policy (PL-1).

**Controls fully other than satisfied** (every statement failed): IR-3 (common); AC-4, AC-6, and CP-10 (GEPS); SR-4 and IR-6(3) (Manufacturing); AC-3 and SR-6 (Electric Utility); AC-3 and AU-11 (Grid Engineering).

35 of the 44 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **27 items**: 24 from this assessment (22 of them also trace to a P03 gap row), 1 from the P03 gap analysis alone (POAM-016, CIP-012-2), and 2 from the P10 AI governance assessment (POAM-019 and POAM-021). By risk: 14 High and 13 Moderate. Status: 22 In progress and 5 Open. Each item names the related P01 risks.

The High items are the P8 items (POAM-007, POAM-008, POAM-020, POAM-023), the GEPS items (POAM-002, POAM-004), firmware signing (POAM-010), notification (POAM-005, POAM-012, POAM-026), the Electric Utility's substation detection and BCSI (POAM-015, POAM-024), and Grid Engineering's BCSI folders and laptops (POAM-013, POAM-025).

## 7. Deliverables and acceptance
`assessment-results.csv` (225 rows, with an `assessment_scope` column), `poam.csv` (27 items), and this plan and summary. Results were presented to the board risk committee on 2026-09-15 and accepted by the Group CISO and the Group Chief Risk Officer the same day. Division presidents accepted their division findings from 2026-09-14 to 2026-09-16. The Electric Utility's CIP Senior Manager received the utility findings and used them in the 2026-09-30 self-reports to SERC (P03).

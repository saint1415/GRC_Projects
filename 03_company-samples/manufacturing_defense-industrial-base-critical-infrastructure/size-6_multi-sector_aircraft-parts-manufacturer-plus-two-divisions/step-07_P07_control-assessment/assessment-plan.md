# Security Assessment Plan and Summary: Cris Santos Company Holdings | Defense Industrial Base | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR and export compliance, group supply chain), the GCEE (P02 SSP), and samples of Aircraft Parts, Engineering Services, and Defense Software controls |
| Tier / Vertical | Multi-Sector / Defense Industrial Base (focus division: Aircraft Parts) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit and risk committee and neither designs nor operates the controls. Division security and compliance leads and the Group CMMC program director acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also satisfies | SP 800-171 Rev. 2 requirement 3.12.1 (periodic assessment) for the Enterprise CUI Environment, as a readiness check before the voluntary C3PAO assessment (target window 2026-12-07 to 2026-12-18). It is not a CMMC assessment and does not produce a CMMC status |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and give three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three).
2. **The GCEE's** system-specific and hybrid controls were assessed because it is the SSP system and carries the top group risk (GR-01).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Sampling choices:
- **Aircraft Parts:** plants 2, 3, and 7, chosen to include one plant without USB device control (plant 3) and one with an outdated inventory (plant 7). Plant 9 was visited but is outside the planned Level 2 scope; its findings appear only where a common control covers it (RA-5, SC-13).
- **Engineering Services:** governance controls (PL-1, CA-2), because its supplement has drifted (gap 9) and its HPC inheritance is undocumented (gap 6), plus field controls (AC-19, AC-20) for customer sites (gap 5).
- **Defense Software:** change control and developer testing after the 2026-05 model change, tenant isolation, and the handling of the SYS-D4 3PAO findings (gap 4). The DoD edition's own authorization is assessed under its DoD package and is outside this plan.

**SP 800-53A versus SP 800-171A.** This assessment uses SP 800-53A determination statements for the SP 800-53 controls in the SSP. A C3PAO will use the SP 800-171A objectives for the 110 requirements; the P03 gap analysis already scores against those requirements, and each P07 finding is linked to the P03 rows it affects through the POA&M.

## 2. Controls selected
**48 control assessments** (44 distinct controls; AC-3, AC-20, CM-8, and CP-9 were assessed in two scopes), **266 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1), IA-2(2), IA-5 | 45 | Every division's access control; GR-01, GR-19 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR and export compliance) | PS-3, PS-4, AT-2, AT-2(2) | 20 | U.S.-person gating, terminations, training for 45,000 users; GR-08 | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, SI-4(4), AU-6, AU-11, IR-3, IR-4, IR-6, IR-8, RA-5 | 62 | GR-01, GR-02, GR-07; scenario gaps 8 and 10 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | SC-7, SC-8, SC-13, SC-28, CP-9, CM-6 | 22 | FIPS cryptography, boundary, backups | Focused / Focused |
| Common control (Group supply chain) | SR-3, SR-6 | 5 | GR-06; scenario gap 3 | Focused / Focused (30 suppliers) |
| GCEE | AC-3, AC-4, AC-20, CM-8, CM-11, CA-3, SA-9 | 28 | GR-01, GR-05; scenario gaps 4 and 6 | Comprehensive / Comprehensive |
| Division sample: Aircraft Parts | AU-12, MP-7, SI-2, CM-8, CP-9 | 27 | AP-002, AP-004, AP-005, AP-013; gaps 2 and 10 | Focused / Focused (plants 2, 3, 7) |
| Division sample: Engineering Services | AC-20, AC-19, PL-1, CA-2 | 35 | ES-002, ES-004, ES-010; gaps 5, 6, 9 | Focused / Focused (10 customer sites, 60 engineers) |
| Division sample: Defense Software | AC-3, CM-3, SA-11, CA-5 | 22 | DS-001, DS-002, DS-003; gap 4 | Focused / Focused |
| **Total** | **48** | **266** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, SIEM sources and rules, landing-zone guardrails, backup and immutability settings, PLM role matrices and export tags, flow and interconnection registers, external service register and CRMs, plant inventories and diagrams, division supplements, release records, the SYS-D4 3PAO report.
- **Interview:** group identity, SOC, and cloud platform directors; the GCEE platform engineering lead; the Group CMMC program director; division security and compliance leads; plant manufacturing engineering staff; the Engineering Services HPC manager and field operations director; the Defense Software chief data scientist and customer operations director; the Group export compliance director.
- **Test:**
  - a joiner-mover-leaver sample of 72 events across divisions, and 25 terminations;
  - hardware-key administrator sign-in and federation checks on 48 applications;
  - test queries under 8 PLM project roles, including a test account without the U.S.-person attribute;
  - a simulated 900-file download from a Program H test project (SOC approved) to test egress alerts;
  - restores of 3 PLM project vaults and 2 MES databases from the immutable vault;
  - a TLS scan of 70 endpoints, including plant VPNs, and an external exposure scan of both landing zones;
  - device control tests at transfer workstations at plants 2, 3, and 7;
  - cross-tenant access attempts in 2 SYS-D4 test tenants;
  - a field survey of 60 Engineering Services engineers.

## 4. Rules of engagement
- No testing that could affect production at the plants, test events, or platform customers. Tests used non-production projects and tenants; the download test used synthetic files in a test project inside the Program H enclave.
- No CUI left group systems. Screenshots were redacted, and assessors were U.S. persons with existing CUI access approvals.
- The assessor would stop and notify the Group CISO on any critical exposure. None was found.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 137 | 17 | 154 |
| GCEE | 16 | 12 | 28 |
| Division sample: Aircraft Parts | 20 | 7 | 27 |
| Division sample: Engineering Services | 29 | 6 | 35 |
| Division sample: Defense Software | 18 | 4 | 22 |
| **Total** | **220** | **46** | **266** |

**Common controls are strong.** 137 of 154 common statements were satisfied. Strong authentication (IA-2, IA-2(1), IA-2(2), AC-6(5)), U.S.-person screening and terminations (PS-3, PS-4), cloud protection (SC-7, SC-8, SC-28, CP-9, CM-6), log review and retention (AU-6, AU-11), and account disablement (AC-2(3)) had no findings. The common findings are about **service accounts** (AC-2, IA-5), **plant monitoring coverage** (SI-4), **outbound baselines for Program H** (SI-4(4)), **cross-division incident consistency and reporting** (IR-3, IR-4, IR-6, IR-8; scenario gap 8), **Plant 9** (RA-5, SC-13), **supplier verification** (SR-3, SR-6; gap 3), and one training content item (AT-2).

**The GCEE is where the cross-division risk shows.** AC-4 was fully other than satisfied: the daily Aircraft Parts export to SYS-D4 is not an approved flow, and a test file from the Program H space reached a general MES queue. SA-9 and AC-20 failed for the same SYS-D4 dependency (gap 4). CM-8 failed for the thick workstations at plants 4 and 7, CA-3 for the HPC and SYS-D4 exchanges, and CM-11 for CAD plug-ins. Project-based access with export tags (AC-3) passed every test, including the account without the U.S.-person attribute.

**Division samples:**
- *Aircraft Parts:* USB device control missing at plant 3 with unowned drives in use (MP-7, fully other than satisfied), plant 7 MES records without user identity (AU-12), late patching at plants 7 and 3 (SI-2), and an outdated plant 7 inventory (CM-8). MES backups and restores at plant 2 passed (CP-9).
- *Engineering Services:* customer systems and GFE not registered and CUI synced to laptops (AC-20), a drifted supplement (PL-1), and an assessment plan that left out the HPC cluster and test systems (CA-2). Field laptop controls passed (AC-19).
- *Defense Software:* the 2026-05 model change approved without data-use review or a documented decision (CM-3), no independent model validation (SA-11), and 3PAO findings tracked without milestones (CA-5). Tenant isolation tests passed (AC-3).

**Controls fully other than satisfied** (every statement failed): IR-3 (common), SR-6 (common), AC-4 (GCEE), and MP-7 (Aircraft Parts). IR-3, SR-6, and AC-4 each have one determination statement; MP-7 has two.

29 of the 48 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **26 items**: 20 from this assessment (several also trace to P03 rows) and 6 from the P03 gap analyses only (POAM-011, POAM-017, POAM-018, POAM-021, POAM-022, POAM-023). By risk: 6 High (POAM-003 plant USB control, POAM-006 SYS-D4 export, POAM-007 Plant 9, POAM-010 Engineering Services field CUI, POAM-015 SYS-D4 equivalency, POAM-016 Government-related data reuse), 17 Moderate, and 3 Low. Status: 21 In progress, 5 Open. Each item names the related P01 risks.

**CMMC note.** Before the C3PAO assessment, the POA&M must shrink to items that 32 CFR 170.21(a)(2) allows: 1-point requirements only, and never 3.1.20, 3.1.22, 3.12.4, 3.10.3, 3.10.4, or 3.10.5. POAM-003, POAM-004, POAM-005, POAM-006, POAM-009, and POAM-010 touch requirements that are not eligible and are therefore due by 2026-11-30.

## 7. Deliverables and acceptance
`assessment-results.csv` (266 rows, with an `assessment_scope` column), `poam.csv` (26 items), and this plan and summary. Results were presented to the board audit and risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-15. Division presidents accepted their division findings the same week.

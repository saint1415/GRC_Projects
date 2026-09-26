# Security Assessment Plan and Summary: Cris Santos Company Holdings | Health Care | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the Group Data Platform (P02 SSP), and samples of Care Delivery, Health Plan, and Health-Tech SaaS controls |
| Tier / Vertical | Multi-Sector / Health Care and Social Assistance (focus division: Care Delivery) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-01 to 2026-08-31 |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8), for both covered entities and for the SaaS and corporate as business associates |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three).
2. **The Group Data Platform's** system-specific controls were assessed because it is the SSP system and carries the top group risk (GR-01).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

The Health Plan was sampled on governance controls (PL-1, CA-2) because its inheritance is undocumented (scenario gap 6) and its standards have drifted (gap 2).

## 2. Controls selected
**39 control assessments** (36 distinct controls; AC-3, CP-9, and SA-9 were assessed in two scopes), **261 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1), IA-5 | 44 | Every division's access control; GR-07 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1; Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-02, GR-03, GR-12; scenario gap 5 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-8, SC-12, SC-28, CM-6 | 22 | GR-02; immutable backups and guardrails | Focused / Focused |
| Group Data Platform | AC-3, AC-4, AC-6, PT-3, CM-8, CP-4 | 20 | GR-01 (High); scenario gap 1 | Comprehensive / Comprehensive |
| Division sample: Care Delivery | AU-6, SI-2, CP-2, SA-9 | 43 | CD-001, CD-006, CD-007, CD-017; ASC plans (42 CFR 416.54) | Focused / Focused (4 regions, 3 of 14 ASCs) |
| Division sample: Health Plan | PL-1, CA-2, AU-11, CP-9 | 35 | Gaps 2 and 6; HP-003, HP-005 | Focused / Focused |
| Division sample: Health-Tech SaaS | SA-9, CM-3, CM-4, SA-11, AC-3 | 28 | HT-001, HT-003 (High); gap 4 | Focused / Focused |
| **Total** | **39** | **261** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, SIEM data sources and rules, landing-zone policies, backup and immutability settings, the GDP policy engine and catalog, contingency and emergency plans, division standards, change records and vendor files, BAAs and subcontractor agreements.
- **Interview:** group identity, SOC, and cloud platform directors; the group data platform director; division security and compliance leads; both covered entities' Privacy Officers; the Group General Counsel; the SaaS general manager and product lead; ASC administrators at 3 sites.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations;
  - a hardware-key administrator sign-in and federation checks on 40 applications;
  - a simulated bulk export from GDP storage (with SOC approval) to test egress detection;
  - test queries under 6 analyst roles to check purpose-based access;
  - restores of 3 GDP datasets from the immutable vault;
  - a TLS scan of 60 endpoints and an external exposure scan of the landing zones;
  - cross-tenant access attempts in SaaS test tenants.

## 4. Rules of engagement
- No testing that could affect patient care, claims payment, or SaaS customers. Tests ran in non-production tenants where possible; the GDP egress test used synthetic data.
- No PHI left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. None was found.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 122 | 13 | 135 |
| Group Data Platform | 12 | 8 | 20 |
| Division sample: Care Delivery | 37 | 6 | 43 |
| Division sample: Health Plan | 28 | 7 | 35 |
| Division sample: Health-Tech SaaS | 23 | 5 | 28 |
| **Total** | **222** | **39** | **261** |

**Common controls are strong.** 122 of 135 common statements were satisfied. Identity (IA-2, IA-2(1), AC-2(3), AC-6(5)), cloud protection (CP-9, SC-7, SC-8, SC-12, SC-28), training (AT-2), terminations (PS-4), and vulnerability management (RA-5) had no findings. The common findings are about **service accounts** (AC-2, IA-5), **monitoring coverage** (SI-4), and **cross-division incident consistency and notification** (IR-3, IR-4, IR-6, IR-8), which is scenario gap 5.

**The Group Data Platform is where the risk is.** AC-3, AC-4, and AC-6 were fully other than satisfied, and 3 of 6 PT-3 statements failed. Test queries under 2 of 6 analyst roles reached the other covered entity's tables (scenario gap 1).

**Division samples:**
- *Care Delivery:* late patching at legacy sites and unsupported devices (SI-2), contingency plans that assume short outages (CP-2), unmonitored imaging vendor tunnels (SA-9), and no activity review for the legacy EHR (AU-6).
- *Health Plan:* standards that conflict with group policy (PL-1, gap 2), inheritance never documented or confirmed (CA-2, gap 6), 90-day log retention (AU-11), and recovery documentation stored only on the claims share (CP-9).
- *Health-Tech SaaS:* the AI feature added a PHI subcontractor without privacy analysis, monitoring, or updated commitments (SA-9, CM-3, CM-4, gap 4), and no accuracy or prompt-injection testing (SA-11). Tenant isolation tests (AC-3) passed.

**Controls fully other than satisfied** (every statement failed): IR-3 (common), AC-3, AC-4, and AC-6 (Group Data Platform), and AU-11 (Health Plan). Each has only one determination statement.

26 of the 39 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **23 items**: 19 from this assessment and 4 from the P03 gap analyses (POAM-020 to POAM-023). By risk: 3 High (POAM-006 Group Data Platform access, POAM-018 SaaS AI feature commitments, POAM-021 UM model governance), 18 Moderate, and 2 Low. Status: 17 In progress, 6 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (261 rows, with an `assessment_scope` column), `poam.csv` (23 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-10. Division presidents accepted their division findings the same week.

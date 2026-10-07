# Security Assessment Plan and Summary: Cris Santos Company Holdings | Management of Companies and Enterprises | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SCSP identity component SYS-G1, SYS-G2, SYS-G3, Group HR), the Shared Corporate Services Platform (P02 SSP), and samples of Insurance and Health Care Services controls |
| Tier / Vertical | Multi-Sector / Management of Companies and Enterprises (focus: the holding company) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the audit committee and neither designs nor operates the controls. The Insurance information security officer and the Health Care Services HIPAA Security Officer acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also satisfies | The insurers' annual assessment of key controls (Model #668 sec. 4C(5), as enacted in Alabama, South Carolina, and Tennessee); Health Care Services' and the group health plan's HIPAA evaluation (45 CFR 164.308(a)(8)); evidence for SOX IT general controls testing (shared with the external auditor) |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in both divisions come from the holding company. Testing them once per division would waste effort and produce slightly different answers for the same control. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, with samples drawn from all three divisions (for example, the joiner-mover-leaver sample took events from every division, and the help desk test called all three division help desks).
2. **The SCSP's** system-specific controls were assessed because it is the SSP system and carries the group's payment and financial reporting integrity.
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Health Care Services was sampled more heavily (6 controls) because its acquired clinics sit outside the inheritance matrix and the risk analysis (scenario gap 8), so the group cannot assume common controls reach them.

## 2. Controls selected
**35 control assessments** (33 distinct controls; SA-9 and CP-9 were assessed in two scopes), **243 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SCSP identity component SYS-G1) | AC-2, AC-6, AC-6(5), IA-2(1), IA-5 | 39 | Every division's access; GR-01, GR-11; scenario gap 1 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-02, GR-07, GR-18; scenario gap 7 | Focused / Comprehensive |
| Common control (SYS-G3 cloud and network) | CP-9, SC-7, SC-8, SC-12, CM-6 | 21 | GR-02; immutable backups and guardrails | Focused / Focused |
| SCSP | AC-5, AC-6(7), AC-4, PT-3, CA-3, CP-4, SA-9 | 30 | GR-04, GR-05, GR-08, GR-09, GR-13; scenario gaps 1, 3, 4 | Comprehensive / Comprehensive |
| Division sample: Insurance | IA-8, IA-12, CP-2, SA-9 | 36 | INS-001 (High), INS-005, INS-007; P03 sec. 4F gaps | Focused / Focused |
| Division sample: Health Care Services | AC-3, AU-6, SI-2, CP-9, PL-1, CA-2 | 48 | HCS-001 and HCS-004 (High); scenario gaps 6 and 8 | Focused / Focused (8 of 50 acquired clinics visited) |
| **Total** | **35** | **243** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, help desk procedures and reset logs, ERP segregation-of-duties rules and superuser lists, integration route catalog, SIEM data sources and rules, landing-zone policies, backup and immutability settings, contingency plans, intercompany agreements, vendor report reviews, EHR role configuration, division supplements.
- **Interview:** Group identity director, Group SOC director, Group Controller, Group benefits director, SCSP platform director, Group General Counsel, the Insurance information security officer and claims leaders, the Health Care Services HIPAA officers, and clinic managers at 8 acquired clinics.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations;
  - hardware-key administrator sign-in for 10 administrators;
  - a cross-division reset by a division help desk test account, and social engineering test calls to 3 division help desks for a test identity (both approved by the Group CISO);
  - simulated suspicious sign-in and mass HCM export to test detection;
  - restores of 2 integration datasets and 1 claims database copy from the immutable vault;
  - a TLS scan of 80 endpoints and an external exposure scan of the landing zones;
  - review of 30 recorded bank-detail change calls in the insurance call center;
  - adjuster test account queries on 10 synthetic patients in the clinic EHR test environment.

## 4. Rules of engagement
- No testing that could affect claims payments, payroll, bank files, or patient care. Social engineering calls used a dedicated test identity with no access, and EHR queries used synthetic patients.
- No PHI, consumer nonpublic information, or MNPI left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. The successful help desk reset in the test was reported to the Group CISO the same day and triggered the interim procedure in POAM-001.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls (SYS-G1, Group HR, SYS-G2, SYS-G3) | 112 | 17 | 129 |
| SCSP | 16 | 14 | 30 |
| Division sample: Insurance | 26 | 10 | 36 |
| Division sample: Health Care Services | 37 | 11 | 48 |
| **Total** | **191** | **52** | **243** |

**Common controls are mostly strong.** 112 of 129 common statements were satisfied. Cloud and network protection (CP-9, SC-7, SC-8, SC-12, CM-6), terminations (PS-4), vulnerability management (RA-5), and administrator authentication (IA-2(1), AC-6(5)) had no findings. The common findings sit in two places:
- **Identity recovery and privilege** (AC-2, AC-6, IA-5): a division help desk test account reset a user in another division, and 2 of 3 social engineering test calls obtained an MFA reset (scenario gap 1).
- **Cross-division incident coordination** (IR-3, IR-4, IR-6, IR-8, SI-4): no cross-division exercise, an incomplete notification matrix, and no SIEM coverage of the acquired clinics' directory (gaps 7 and 8).

**The SCSP is where the integrity risk sits.** 14 of 30 statements failed: standing ERP superusers (AC-5, AC-6(7); gap 4), the benefits export (AC-4, PT-3; gap 3), the unapproved legacy directory trust (CA-3), the integration failover that missed its RTO (CP-4), and unmapped vendor complementary controls (SA-9).

**Division samples:**
- *Insurance:* bank-detail changes by phone verified only with knowledge questions (IA-8, all 30 sampled calls), surge adjusters not proofed (IA-12), no second site for workers' compensation (CP-2), and no oversight of the holding company as a service provider (SA-9; P03 sec. 4F).
- *Health Care Services:* the adjuster role opened non-work visits for all 10 synthetic patients (AC-3; gap 6), and the acquired clinics lack activity review, timely patching, frequent backups, current policy, and assessment coverage (AU-6, SI-2, CP-9, PL-1, CA-2; gap 8).

**Controls fully other than satisfied** (every statement failed): AC-6 and IR-3 (common), AC-6(7) and AC-4 (SCSP), IA-8 (Insurance), and AC-3 (Health Care Services). AC-6(7) has two determination statements; the others have one.

26 of the 35 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

**Finding returned to the risk register.** The successful cross-division reset in the test confirmed GR-01's High likelihood of initiation, which the risk register had rated from interviews alone, and the board risk committee approved its treatment plan on that evidence. The AC-6 and IA-5 findings feed POAM-001.

## 6. POA&M
`poam.csv` has **24 items**: 18 from this assessment alone, 5 that combine an assessment finding with a P03 gap (POAM-016, POAM-017, POAM-019, POAM-023, POAM-024), and 1 from the P03 gap analysis alone (POAM-022). By risk: 5 High (POAM-001 identity recovery and privilege, POAM-006 legacy directory trust, POAM-013 bank-detail change verification, POAM-017 adjuster EHR access, POAM-023 AI assistant), 18 Moderate, and 1 Low. Status: 15 In progress, 9 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (243 rows, with an `assessment_scope` column), `poam.csv` (24 items), and this plan and summary. Results were presented to the board risk committee on 2026-09-15 (with the SOX-related findings, POAM-003 and POAM-004, also reported to the audit committee) and accepted by the Group CISO and the Group Chief Risk Officer the same day. Division presidents accepted their division findings the same week.

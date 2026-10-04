# Security Assessment Plan and Summary: Cris Santos Company Holdings | Educational Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the college's Student Records and Learning Platform (P02 SSP), and samples of Higher Education, Education Software, and Student Health controls |
| Tier / Vertical | Multi-Sector / Educational Services (focus division: Higher Education) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also satisfies | The college's regular testing of key controls (16 CFR 314.4(d)(1)); Education Software's testing of children's information safeguards (16 CFR 312.8(b)(4)); Student Health's HIPAA evaluation (45 CFR 164.308(a)(8)) |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every federated division (for example, the joiner-mover-leaver sample took events from all three).
2. **The SRLP's** system-specific controls were assessed because it is the SSP system and carries the college's top risk on the warehouse (HE-002, GR-05).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Student Health was sampled on governance controls (CA-2, PL-1) because its inheritance is undocumented and its standards predate the acquisition (scenario gap 4), and on identity and backups because its legacy domain sits outside SYS-G1.

## 2. Controls selected
**38 control assessments** (34 distinct controls; AC-6, IA-2, IA-5, and CP-9 were assessed in two scopes), **236 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1), IA-5 | 44 | Every division's access control; GR-07, GR-14 | Focused / Comprehensive (all federated divisions sampled) |
| Common control (Group HR with SYS-G1; Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-03, GR-15; scenario gap 7 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-8, SC-12, CM-6 | 21 | GR-02; immutable backups and guardrails | Focused / Focused |
| SRLP (P02 system) | AC-3, AC-4, AC-6, PT-3, CM-8, CP-4 | 20 | HE-002 and GR-05 (High); scenario gap 2 | Comprehensive / Comprehensive |
| Division sample: Higher Education | SA-9, CA-8, SI-2, AU-6, IA-5 | 30 | HE-003, HE-005, HE-018; scenario gaps 3 and 8 | Focused / Focused (2 of 6 legacy campuses) |
| Division sample: Education Software | AC-6, SA-11, CM-4, SI-12 | 16 | ES-001, ES-003 (High); scenario gaps 1 and 6 | Focused / Focused |
| Division sample: Student Health | CA-2, PL-1, IA-2, CP-9 | 36 | SH-001, SH-004, SH-005; scenario gap 4 | Focused / Focused (6 of 96 clinics) |
| **Total** | **38** | **236** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, SIEM data sources and rules, landing-zone policies, backup and immutability settings, warehouse grants and catalog, the intercompany service agreement and vendor contracts, the support console role model, AI tutor release records, division standards, and contingency plans.
- **Interview:** group identity, SOC, cloud, and data platform directors; the College CISO; the university registrar; the executive director of financial aid; the Education Software support director, chief product officer, and privacy counsel; the Student Health security and compliance lead and Privacy Officer; clinic managers at 6 sites.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across federated divisions, and 25 terminations;
  - a hardware-key administrator sign-in and federation checks on 45 applications;
  - a simulated bulk export from warehouse object storage (with SOC approval, synthetic data) to test egress detection;
  - test queries under 6 warehouse analyst roles to check legitimate educational interest limits;
  - restores of 3 warehouse data sets from the immutable vault;
  - a TLS scan of 70 endpoints and an external exposure scan of the landing zones;
  - a read of a test tenant with a support account, and 30 support tickets traced to tenant reads;
  - local administrator password checks on 31 servers at 2 legacy campuses;
  - walk-throughs of sign-in practice at 6 clinics.

## 4. Rules of engagement
- No testing that could affect instruction, aid disbursement, clinical care, or software customers. Tests ran in test tenants where possible; the warehouse egress test used synthetic data.
- No student, patient, or customer data left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. The shared local administrator password on legacy campus servers was reported the same day and rotation started before the end of fieldwork.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 121 | 13 | 134 |
| SRLP (P02 system) | 11 | 9 | 20 |
| Division sample: Higher Education | 21 | 9 | 30 |
| Division sample: Education Software | 10 | 6 | 16 |
| Division sample: Student Health | 27 | 9 | 36 |
| **Total** | **190** | **46** | **236** |

**Common controls are strong.** 121 of 134 common statements were satisfied. Identity for people (IA-2, IA-2(1), AC-2(3), AC-6(5)), terminations (PS-4), training (AT-2), cloud protection (CP-9, SC-7, SC-8, SC-12, CM-6), and vulnerability management (RA-5) had no findings. The common findings are about **service accounts** (AC-2, IA-5), **monitoring coverage** for warehouse exports and the support console (SI-4), and **cross-division incident consistency and notification** (IR-3, IR-4, IR-6, IR-8), which is scenario gap 7.

**The SRLP is where the college's risk is.** AC-3, AC-4, and AC-6 were fully other than satisfied, and 3 of 6 PT-3 statements failed. Test queries under 4 of 6 analyst roles reached every student's records and the clinic utilization tables (scenario gap 2).

**Division samples:**
- *Higher Education:* no security requirements, oversight, or monitoring for the Campus Platform as a service provider (SA-9, gap 3); penetration test scope (CA-8); late patching at legacy campuses (SI-2); FAMS logs not reviewed (AU-6). **New finding:** one local administrator password shared by all 31 servers at the 2 sampled legacy campuses, unchanged since 2023 (IA-5). It was added to the risk register as HE-021.
- *Education Software:* standing cross-tenant support access, with 19 of 30 sampled reads lacking customer approval (AC-6, gap 1); the AI tutor launched without privacy impact analysis or safety testing (CM-4, SA-11, gap 6); retention of 212 former districts' data (SI-12).
- *Student Health:* inheritance undocumented (CA-2) and standards not reviewed since 2023 (PL-1), both gap 4; incomplete and untested file server backups (CP-9). **New finding:** shared front desk logins at 3 clinics on the legacy domain (IA-2).

**Controls fully other than satisfied** (every statement failed): IR-3 (common), AC-3, AC-4, and AC-6 (SRLP), CA-8 (Higher Education), and AC-6 (Education Software). Each has only one determination statement.

26 of the 38 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **24 items**: 19 from this assessment and 5 from the P03 gap analyses (POAM-020 to POAM-024). By risk: 6 High (POAM-001 support access, POAM-005 warehouse roles, POAM-006 clinic extract, POAM-009 intercompany service provider oversight, POAM-014 AI tutor governance, POAM-022 admissions scoring), 17 Moderate, and 1 Low. Status: 15 In progress, 9 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (236 rows, with an `assessment_scope` column), `poam.csv` (24 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-15. Division presidents accepted their division findings the same week. The College CISO will summarize the testing results in the 2026-10-20 report to the college board of trustees (314.4(i)(2)).

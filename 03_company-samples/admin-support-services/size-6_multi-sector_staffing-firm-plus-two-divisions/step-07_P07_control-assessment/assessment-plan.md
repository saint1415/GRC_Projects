# Security Assessment Plan and Summary: Cris Santos Company Holdings | Admin and Support Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the Group Workforce Platform (P02 SSP), and samples of Staffing, Consulting, and Home Health controls |
| Tier / Vertical | Multi-Sector / Administrative and Support and Waste Management and Remediation Services (focus division: Staffing) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-01 to 2026-08-31 |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8), for Home Health (covered entity) and for Consulting and corporate as business associates; the inspection and quality assurance evidence for the electronic I-9 program (8 CFR 274a.2(e)(1)(iii)) for the GWP sample; the annual self-assessment of the Federal Solutions enclave against FAR 52.204-21 |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three).
2. **The Group Workforce Platform's** system-specific and hybrid controls were assessed because it is the SSP system and carries the top group risks (GR-01, GR-05, GR-10).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Home Health was sampled most heavily (60 statements) on governance and resilience controls (PL-1, CA-2, CP-2) and endpoint protection (SI-3), because its inheritance is undocumented (scenario gap 6), its supplement has drifted (gap 3), and its tablets sit outside group endpoint management.

## 2. Controls selected
**39 control assessments** (36 distinct controls; SC-7, PS-4, and CP-9 were assessed in two scopes), **266 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1), IA-5 | 44 | Every division's access control; E-Verify accounts (gap 8); GR-07, GR-09 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1; Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 core employees | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-03, GR-12; scenario gap 5 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-8, SC-28, CM-6 | 20 | GR-02; immutable backups, tokenization, guardrails | Focused / Focused |
| Group Workforce Platform | AC-4, AC-6, IA-2(2), PT-3, AU-12, CP-4, SA-9, CM-12 | 30 | GR-01, GR-05, GR-10 (High); scenario gaps 1, 2, 4, 8 | Comprehensive / Comprehensive |
| Division sample: Staffing | CM-8, MP-6, AU-6, SC-7 | 19 | ST-006, ST-015; Disposal Rule (16 CFR 682.3) | Focused / Focused (6 branches, 4 on-site offices) |
| Division sample: Consulting | AC-20, PS-4, CP-9, SI-2 | 24 | CN-001 (High), CN-004; scenario gap 7; FAR 52.204-21 | Focused / Focused (10 engagements; the enclave) |
| Division sample: Home Health | PL-1, CA-2, SI-3, CP-2 | 60 | HH-002 (High), HH-006 to HH-008; gaps 3 and 6; 42 CFR 484.102 | Focused / Focused (3 agencies in 3 states) |
| **Total** | **39** | **266** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, the E-Verify user list, the secret inventory, SIEM data sources and rules, landing-zone policies, backup and immutability settings, tokenization settings, the visit-pay interface specification, the GWP processing register and data map, vendor files, contingency and emergency plans, division supplements, and client account records.
- **Interview:** group identity, SOC, cloud, and workforce platform directors; the group payroll director; the Group Chief Privacy Officer; the Staffing Vice President, Employment Compliance; the Consulting HIPAA compliance officer; engagement managers; the Home Health HIPAA Privacy and Security Officers; agency directors in 3 states.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations;
  - a hardware-key administrator sign-in and federation checks on every GWP staff application;
  - a simulated bulk export from the payroll engine and a scripted burst of 25 bank changes to one destination in a test tenant (with SOC approval);
  - test queries under 4 payroll roles for visit-pay records;
  - test reads of 5 archived Forms I-9 to check for audit records;
  - restores of 3 payroll engine tables from the provider B vault and of 2 enclave file shares;
  - a TLS scan of 70 endpoints and an external exposure scan of the landing zones;
  - kiosk network tests at 6 branches; 30 field tablets checked in 3 agencies.

## 4. Rules of engagement
- No testing that could affect a payroll run, a client go-live, or patient visits. Bank-change tests ran in a test tenant with synthetic workers.
- No personal information or PHI left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. None was found.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 118 | 15 | 133 |
| Group Workforce Platform | 17 | 13 | 30 |
| Division sample: Staffing | 16 | 3 | 19 |
| Division sample: Consulting | 20 | 4 | 24 |
| Division sample: Home Health | 50 | 10 | 60 |
| **Total** | **221** | **45** | **266** |

**Common controls are strong.** 118 of 133 common statements were satisfied. Identity assurance (IA-2, IA-2(1), AC-2(3), AC-6(5)), cloud protection (CP-9, SC-7, SC-8, SC-28, CM-6), training (AT-2), terminations (PS-4), and vulnerability management (RA-5) had no findings. The common findings are about **accounts outside identity governance** (AC-2, IA-5: E-Verify users and integration service accounts), **monitoring coverage** (SI-4), and **cross-division incident consistency and notification** (IR-3, IR-4, IR-6, IR-8), which is scenario gap 5.

**The Group Workforce Platform is where the risk is.** AC-4, AC-6, and IA-2(2) were fully other than satisfied: visit-pay records carry patient identifiers into payroll, every payroll role tested could see them, and an SMS code both signs associates in and approves bank changes. A scripted burst of 25 bank changes to one account raised no alert (SI-4). Half of the PT-3 statements failed, and the I-9 archive produced no audit records for test reads (AU-12).

**Division samples:**
- *Staffing:* kiosks reached staff devices at 2 of 6 sampled branches (SC-7), uninventoried time clocks (CM-8), and unreviewed VMS tenant logs (AU-6). Media disposal (MP-6) passed.
- *Consulting:* client-issued accounts are not inventoried (AC-20, both statements failed) and are not removed promptly at roll-off (PS-4); enclave patching ran late (SI-2). Enclave backups (CP-9) passed.
- *Home Health:* a supplement that predates group policy (PL-1), no inheritance documentation (CA-2), EDR on 72% of tablets with detections not reaching the SOC (SI-3), and a contingency plan built for short outages (CP-2).

**Controls fully other than satisfied** (every statement failed): IR-3 (common), and AC-4, AC-6, and IA-2(2) (GWP). Each has only one determination statement.

25 of the 39 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **28 items**: 23 from this assessment and 5 from the P03 gap analyses (POAM-024 to POAM-028). By risk: 6 High (POAM-006 visit-pay patient data, POAM-008 self-service authentication, POAM-017 client-issued accounts, POAM-024 intercompany BAA scope, POAM-025 AI hiring duties from 2027-01-01, POAM-026 Consulting subcontractor BAAs), 21 Moderate, and 1 Low. Status: 21 In progress, 7 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (266 rows, with an `assessment_scope` column), `poam.csv` (28 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-10. Division presidents accepted their division findings the same week.

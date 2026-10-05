# Security Assessment Plan and Summary: Cris Santos Company Holdings | Construction | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1 to SYS-G5 and group HR), the Project Delivery and Payment Platform (PDPP, the P02 SSP system), a pre-assessment of the CUI enclave (SYS-G6), and samples of Construction, Property, and A&E controls |
| Tier / Vertical | Multi-Sector / Construction (focus division: Commercial Construction) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls it assessed. Division security and compliance leads and the Director of Federal Contracts Compliance acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also supports | The CMMC Level 1 annual affirmation for the PDPP scope (32 CFR 170.15, 170.22) and the independent pre-assessment of the enclave before a Level 2 (C3PAO) assessment. The enclave's requirement-by-requirement scoring against NIST SP 800-171A is in P03 (`gap-analysis-cui-enclave.csv`); this plan tests the related SP 800-53 controls |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and give three slightly different answers. So:
1. **Common controls** marked "assessed in P07" in the P02 common control catalog (21 controls) were assessed **once**, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three divisions and corporate, including craft workers).
2. **The PDPP's** system-specific and hybrid controls were assessed because it is the SSP system, the CMMC Level 1 scope, and the system behind two High group risks (GR-01 CUI outside the enclave, GR-02 payment fraud).
3. **The CUI enclave** was pre-assessed on the controls behind its open SP 800-171 R2 requirements, so the group knows what blocks a Level 2 (C3PAO) assessment (GR-03).
4. **Division samples** covered controls each division runs itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Property was sampled on governance controls (CA-2, PL-1) because its inheritance is undocumented and its supplement has drifted (scenario gap 4), and on building systems because they are outside group monitoring.

## 2. Controls selected
**54 control assessments** (44 distinct controls; 9 controls were assessed in more than one scope: AC-2(3), AC-4, AC-5, CM-8, CP-9, IA-5 (three scopes), SC-7, SI-10, and SR-5), **305 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2(1), IA-5 | 42 | Every division's access control; FAR 52.204-21(b)(1)(i), (v), (vi) | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1) | AT-2, PS-4 | 15 | Training and terminations for 45,000 users, including craft workers | Focused / Focused |
| Common control (SYS-G2 SOC) | IR-3, IR-4, IR-6, IR-8, SI-4 | 45 | GR-04, GR-06, GR-14; scenario gap 7 | Focused / Comprehensive |
| Common control (SYS-G3 cloud and network) | CM-6, CP-9, SC-7, SC-8, SC-28 | 20 | GR-05, GR-15; immutable backups and guardrails | Focused / Focused |
| Common control (SYS-G4 payment factory) | AC-5, SI-7, SI-10 | 9 | GR-02 (High); scenario gap 3 | Focused / Focused |
| Common control (SYS-G5 email) | SI-8 | 5 | GR-02; PRP-003 | Focused / Focused |
| PDPP | AC-2(3), AC-4, AC-21, AU-6, CM-8, CM-12, CP-4, IA-8, SA-9, SI-10 | 36 | GR-01, GR-02 (High); CON-001, CON-005, CON-011; P03 G-001, G-018, G-020 | Comprehensive / Comprehensive |
| CUI enclave pre-assessment | AC-4, AT-3, AU-5, CM-7(5), MP-3, PE-17, PL-2, SC-13 | 43 | GR-03, AE-002 (High); the 9 open enclave requirements in P03 | Comprehensive / Comprehensive |
| Division sample: Construction | IA-5 (TSSI vault), PE-8, SR-5, SR-6 | 17 | CON-014, CON-015 (High), CON-009, CON-029; P03 G-009, G-026, G-030 | Focused / Focused (TSSI, 10 trailers, 25 awards) |
| Division sample: Property | AC-5, CA-2, CM-8, IA-5, MA-4, PL-1, SC-7 | 60 | PRP-001, PRP-005 (High), PRP-006, PRP-009, PRP-018; scenario gaps 3 and 4 | Focused / Focused (12 properties, 6 garages) |
| Division sample: A&E | AC-3, AC-20, CP-9, SR-5 | 13 | AE-006, AE-008, AE-009, AE-013; P03 AE-G10, AE-G15, AE-G19 | Focused / Focused |
| **Total** | **54** | **305** | | |

For the enclave's AT-3 the 6 security training statements were assessed (the enclave holds CUI, not personal information, so the role-based privacy training statements were not selected). For PL-2, the 23 statements on the security plan were assessed; the privacy plan statements were not selected for the same reason.

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, SIEM data sources and rules, landing-zone policies, backup and immutability settings, payment factory workflows, the PDPP tenant and integration configuration, the enclave SSP v2.3 and allowlist, the Property supplement and building system inventories, the TSSI vault configuration, subcontract award files, and A&E master specifications.
- **Interview:** group identity, SOC, cloud and network, and IT operations directors; the Group Treasurer; the PDPP system owner; the enclave operations manager; the Director of Federal Contracts Compliance; superintendents on 5 DoD projects; the Systems Integration Director; Property building operations and accounts payable staff; integrators at 4 properties; the A&E chief quality officer and digital services director.
- **Test:**
  - a joiner-mover-leaver sample of 75 events across divisions and 25 terminations;
  - a phishing-resistant administrator sign-in and MFA policy checks;
  - a test pay application with an altered remittance block in the PDPP test tenant;
  - a bank change without call-back evidence in the payment factory (rejected) and 20 sampled bank changes in Property accounts payable;
  - restores of 3 workloads from the provider B vault;
  - a TLS scan of 80 endpoints and an external exposure scan;
  - a simulated integrator remote session at one property (with SOC approval) to test detection;
  - a credential check of 60 building controllers at 3 properties, with the integrator present;
  - a physical check of cameras and recorders at 2 federally leased properties (2026-08-12);
  - visitor record checks at 10 jobsite trailers;
  - a content scan of the AI estimating assistant tenant and cross-tenant access attempts in 2 digital twin test tenants.

## 4. Rules of engagement
- No testing that could affect building life-safety interfaces, jobsite safety systems, client systems under the TSSI managed service, or live payments. Payment tests ran in test tenants; controller credential checks were read-only, with the integrator present.
- No CUI left the enclave during testing. Evidence about CUI files was recorded by file identifier, not content.
- The assessor would stop and notify the Group CISO on any critical exposure. Two findings were escalated the same day: the default controller credentials (2026-08-12) and the CUI-marked specification in the AI estimating assistant (2026-08-14), which was removed and reported under POL-03 4.4.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls (all six providers) | 126 | 10 | 136 |
| PDPP | 22 | 14 | 36 |
| CUI enclave pre-assessment | 29 | 14 | 43 |
| Division sample: Construction | 10 | 7 | 17 |
| Division sample: Property | 40 | 20 | 60 |
| Division sample: A&E | 10 | 3 | 13 |
| **Total** | **237** | **68** | **305** |

**Common controls are strong.** 126 of 136 common statements were satisfied. Identity (AC-2, AC-2(3), AC-6(5), IA-2(1)), terminations (PS-4), training (AT-2), cloud protection (CM-6, CP-9, SC-7, SC-8, SC-28), and the payment factory's bank-change controls (AC-5, SI-7, SI-10) had no findings. The common findings are about **cross-division incident handling and notification** (IR-3, IR-4, IR-6, IR-8; scenario gap 7), **monitoring coverage** for Property building systems and PDPP remittance edits (SI-4), **DMARC on property domains** (SI-8), and **6 old integration secrets** (IA-5).

**The PDPP is where the shared risks meet.** AC-4 (CUI uploads), AC-21 (sharing decisions), and SI-10 (remittance block) were fully other than satisfied. 3,800 external accounts from closed projects were still active (AC-2(3)), which also affects FAR 52.204-21(b)(1)(i) for the Level 1 scope.

**Enclave pre-assessment.** The findings line up with the P03 enclave table: the field release export (AC-4; 3.1.3 and 3.1.20), untrained field staff (AT-3; 3.2.2), blanket allowlist exceptions (CM-7(5); 3.4.8), an out-of-date SSP (PL-2; 3.12.4), one non-FIPS gateway component (SC-13; 3.13.11), and lower-risk items for logging failure alerts, plot marking, and trailers as alternate work sites.

**Division samples:**
- *Construction:* no CMMC status check before any of 25 sampled subcontract awards (SR-6); TSSI client credentials not partitioned or rotated (IA-5); private-label products not traced to the parent manufacturer (SR-5); and missing visitor records in 3 of 10 trailers (PE-8), a FAR 52.204-21 requirement that must be met before the January Level 1 affirmation.
- *Property:* inheritance never documented or assessed (CA-2, 4 statements); a 2024 supplement that conflicts with group policy (PL-1); flat building networks and integrator VPNs (SC-7, MA-4); default credentials on 14 controllers (IA-5); covered cameras at 2 federally leased properties not recorded in inventories (CM-8); and single-approver bank changes in accounts payable (AC-5).
- *A&E:* a CUI-marked specification in the AI estimating assistant (AC-20); digital twin system documentation not backed up (CP-9); and master specifications not screened for Section 889 (SR-5). Digital twin tenant isolation (AC-3) passed.

**Controls fully other than satisfied** (every statement failed): IR-3 (common), AC-4, AC-21, and SI-10 (PDPP), AC-4 (enclave), and SR-6 (Construction). Each has one or two determination statements.

38 of the 54 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **33 items**. 30 trace to findings in this assessment (most also to a P03 gap); 3 come from other sources: POAM-008 (external user MFA, from the P02 SSP and P01 CON-028; the IA-8 statement itself was satisfied), POAM-028 (PCI DSS for parking, from P03), and POAM-030 (CMMC affirmations and Level 2 readiness, from P03).

| Risk | Items | |
|---|---|---|
| High | 13 | POAM-006, POAM-009, POAM-011, POAM-014, POAM-015, POAM-016, POAM-020, POAM-022, POAM-023, POAM-025, POAM-030, POAM-031, POAM-032 |
| Moderate | 17 | |
| Low | 3 | POAM-012, POAM-017, POAM-027 |

Status: 26 In progress, 7 Open. Each item names the related P01 risks. Four enclave items (POAM-011, POAM-014, POAM-015, POAM-016) must close before even a Conditional Level 2 status is possible (P03 G-029), and POAM-001 and POAM-033 must close before the 2027-01-20 Level 1 affirmation.

## 7. Deliverables and acceptance
`assessment-results.csv` (305 rows, with an `assessment_scope` column), `poam.csv` (33 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-15. Division presidents accepted their division findings the same week. The CMMC Affirming Officials received the PDPP and enclave results for the counsel review of their affirmations (POAM-030).

# Security Assessment Plan and Summary: Cris Santos Company Holdings | Manufacturing | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the Device Engineering and Manufacturing System (DEMS, the P02 SSP system), and samples of Medical Devices, Distribution, and Testing controls |
| Tier / Vertical | Multi-Sector / Manufacturing (focus division: Medical Devices) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only. The Testing division was **not** used as an assessor, to avoid the independence question raised in P03 |
| Assessment window | 2026-07-06 to 2026-08-28 (DEMS plant and lab testing 2026-08-11 to 2026-08-14) |
| Also satisfies | HIPAA evaluation (45 CFR 164.308(a)(8)) for the DCC; the evidence base for Distribution's first FAR 52.204-21 self-assessment; an input to 524B(b)(2) process maintenance |

## 1. Approach: assess common controls once, then sample divisions
Most IT safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the termination sample took events from all three).
2. **DEMS** system-specific and hybrid controls were assessed because it is the SSP system and carries the top group risk (GR-01).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Distribution was sampled on governance and FAR-related controls (CA-2, PE-8, AC-3, MP-6, SI-3) because its inheritance is undocumented (scenario gap 3) and it needs evidence for a CMMC Level 1 self-assessment (gap 4). Testing was sampled on the information barrier (gap 5) and the acquired laboratories (gap 3).

## 2. Controls selected
**41 control assessments** (35 distinct controls; SC-7, CP-9, IA-2(1), AC-3, SC-28, and AU-6 were assessed in two scopes), **227 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2(1), IA-5 | 42 | Every division's access control; PLM guest accounts (gap 9) | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-4, IR-6, IR-8, RA-5 | 53 | GR-03, GR-04, GR-12; scenario gap 7 | Focused / Comprehensive |
| Common control (SYS-G3 cloud and network) | CP-9, SC-7, SC-8, SC-28, CM-6 | 20 | GR-03; immutable backups and guardrails | Focused / Focused |
| DEMS (SSP system) | SC-12, SC-7, IA-2, SR-3, CM-8, CP-9, CM-3, SI-7, AC-5, CA-8(1) | 45 | GR-01 (High); gaps 1, 2, 5, 9 | Comprehensive / Comprehensive (all 5 plants; lab units of each product) |
| Division sample: Medical Devices (DCC, PSIRT, fielded devices) | SI-2, SI-5, AU-6, RA-5(11) | 18 | MD-001, MD-011 (High); 524B(b)(1) | Focused / Focused |
| Division sample: Distribution | CA-2, PE-8, AC-3, MP-6, SI-3 | 27 | DS-003 (High), DS-007; gaps 3 and 4 | Focused / Focused (8 of 24 distribution centers) |
| Division sample: Testing | AC-4, IA-2(1), AC-3, SC-28, AU-6 | 7 | TS-001, TS-002 (High); gaps 3 and 5 | Focused / Focused (2 of 4 acquired laboratories) |
| **Total** | **41** | **227** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, SIEM data sources and rules, landing-zone policies, backup and immutability settings, HSM configuration and key ceremony records, SBOM repository and supplier agreements, plant change logs, the IR plan and PSIRT procedure, ERP roles and file share permissions, visitor logs, collaboration space membership.
- **Interview:** group identity, SOC, and cloud platform directors; the VP Engineering, VP Manufacturing Operations, and Chief Product Security Officer; the VP Quality and Regulatory Affairs; plant managers at Plants D and E; the Distribution security lead and federal contracts compliance director; the Testing division president and laboratory quality director; the Group General Counsel.
- **Test:**
  - a termination sample of 25 events across divisions and a joiner-mover-leaver sample of 60 events;
  - a hardware-key administrator sign-in test and a key custodian account review;
  - network scans at all 5 plants on 2026-08-13, including an attempt to reach MES servers from an office laptop;
  - a simulated suspicious MES login at Plant D to test SOC detection;
  - a walkthrough of the Plant D build server and the IX-3 key file (2026-08-12), without using the key;
  - secure boot and signature verification on lab units of IX-4, PM-7, and US-2;
  - a restore attempt of MES backups at Plant E and restores of 3 cloud datasets from the provider B vault;
  - a TLS scan of 70 endpoints and an external exposure scan of the landing zones;
  - a vulnerability report sent through the public CVD channel;
  - access attempts with 3 Testing client accounts and a membership export of collaboration spaces.

## 4. Rules of engagement
- No testing on production lines during a production run, on fielded devices, or on hospital networks. Device tests used lab units only.
- The IX-3 signing key was inspected in place and never copied or used. Findings about it were reported to the Group CISO the same day.
- No PHI, client data, or Federal contract information left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. The Plant D signing key and the Plants D and E network finding were escalated on 2026-08-12 and 2026-08-13; interim custody controls began within the week (POAM-003).

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 120 | 10 | 130 |
| DEMS (SSP system) | 32 | 13 | 45 |
| Division sample: Medical Devices | 17 | 1 | 18 |
| Division sample: Distribution | 21 | 6 | 27 |
| Division sample: Testing | 4 | 3 | 7 |
| **Total** | **194** | **33** | **227** |

**Common controls are strong.** 120 of 130 common statements were satisfied. Identity (AC-2(3), AC-6(5), IA-2(1), IA-5), cloud protection (CP-9, SC-7, SC-8, SC-28, CM-6), training (AT-2), terminations (PS-4), and vulnerability management (RA-5) had no findings. The common findings are about **guest accounts** (AC-2), **monitoring coverage of OT** (SI-4), and **cross-division incident consistency and notification** (IR-4, IR-6, IR-8), which is scenario gap 7.

**DEMS is where the risk is.** The release chain for current products is sound (SI-7 and AC-5 fully satisfied; HSM signing works). The findings are all about the **legacy and acquired parts**: the IX-3 signing key (SC-12, both statements), the flat networks and shared logins at Plants D and E (SC-7, IA-2), their on-site backups (CP-9), IX-3 changes outside the change board (CM-3), the missing IX-3 SBOM and stations (CM-8), supplier SBOM data (SR-3), and tester independence (CA-8(1)).

**Division samples:**
- *Medical Devices:* the PSIRT, advisories, DCC access reviews, and the CVD channel all worked (SI-5, AU-6, RA-5(11)). The one finding is IX-3 update adoption at 58% (SI-2).
- *Distribution:* inheritance never documented or confirmed (CA-2, gap 3), incomplete visitor records (PE-8), and Federal contract information in open file shares (AC-3, gap 4). Sanitization and malware protection (MP-6, SI-3) were satisfied, which helps the FAR self-assessment.
- *Testing:* the information barrier fails at the application layer (AC-4) and is not monitored (AU-6), and acquired laboratory administrators sign in without MFA (IA-2(1)). Per-client encryption of findings (SC-28) and client separation in the LIMS (AC-3) passed.

**Controls fully other than satisfied** (every statement failed): SC-12 and CA-8(1) (DEMS), AC-3 (Distribution), and AC-4 and IA-2(1) (Testing).

20 of the 41 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **23 items**: 16 from this assessment (POAM-001 to POAM-016), 6 from the P03 gap analyses (POAM-017, POAM-018, POAM-020 to POAM-023; POAM-021 also records the Distribution AC-3 finding), and 1 from the P10 AI assessment (POAM-019). By risk: 6 High (POAM-003 IX-3 signing key, POAM-005 Plants D and E networks, POAM-010 Testing information barrier, POAM-012 IX-3 update adoption, POAM-020 IX-3 end of support, POAM-021 CMMC Level 1), 16 Moderate, and 1 Low. Status: 20 In progress, 3 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (227 rows, with an `assessment_scope` column), `poam.csv` (23 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-15. Division presidents accepted their division findings the same week.

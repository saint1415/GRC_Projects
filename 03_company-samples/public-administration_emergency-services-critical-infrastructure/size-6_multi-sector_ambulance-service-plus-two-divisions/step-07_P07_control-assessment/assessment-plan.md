# Security Assessment Plan and Summary: Cris Santos Company Holdings | Emergency Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, Group HR), the Dispatch and Patient Care Platform (P02 SSP), and samples of Ambulance Services, Urgent Care, and BDS controls |
| Tier / Vertical | Multi-Sector / Emergency Services (focus division: Ambulance Services) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8), for both covered entities and for BDS and corporate as business associates |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three).
2. **The DPCP's** platform controls were assessed because it is the SSP system and carries the top group risks (GR-01, GR-02).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Ambulance Services was sampled on fleet device controls because its fleet systems sit outside group configuration management and its inheritance documentation leaves them out (scenario gap 4). Urgent Care was sampled on the acquired clinics and its supplement (gap 8). BDS was sampled on client data, vendors, and card data (gaps 5, 6, and 9).

## 2. Controls selected
**39 control assessments** (35 distinct controls; AC-2, AU-6, SA-9, and SC-28 were assessed in two scopes), **271 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1), IA-5 | 44 | Every division's access control; GR-05; gap 2 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1; Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-03, GR-12; gap 7 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-8, SC-28, CM-6 | 20 | GR-02; backups, segmentation, and guardrails | Focused / Focused |
| DPCP (P02 system) | AC-4, AC-17, CP-2, CP-4, CP-7, CP-10, AU-6, CM-8, SA-9 | 55 | GR-01, GR-02 (High); gaps 1, 3, and 6 | Comprehensive / Comprehensive (all 4 centers) |
| Division sample: Ambulance Services | CM-2, SI-2, IA-3, AC-19 | 20 | AMB-002, AMB-021; gap 4 | Focused / Focused (40 vehicles in 3 states) |
| Division sample: Urgent Care | AU-6, AC-2, PL-1 | 46 | UC-001, UC-008; gap 8 | Focused / Focused (3 of 46 acquired clinics) |
| Division sample: BDS | AC-21, SA-9, CA-3, SC-28 | 17 | BDS-004, BDS-005, BDS-008; gaps 5, 6, and 9 | Focused / Focused |
| **Total** | **39** | **271** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, CAD account lists, SIEM data sources, landing-zone and legacy account network configuration, backup settings, the DPCP contingency plan and the 4 center binders, drill reports, interface agreements, vendor files and BAAs, the Urgent Care supplement, and fleet configuration records.
- **Interview:** group identity, SOC, and cloud platform directors; the group dispatch and clinical platforms director; the BDS vice president of communications operations and 4 center supervisors; the Ambulance fleet technology director; division security and compliance leads; both covered entities' Privacy Officers; the Group General Counsel.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations;
  - a hardware-key administrator sign-in and federation checks on 44 applications;
  - an external exposure scan of the cellular addresses of all vehicle routers (2026-08-19);
  - router and MDC configuration review in 40 vehicles in 3 states;
  - a simulated connection from a file transfer server to a CAD server in the legacy account (with SOC approval);
  - a restore of the CAD database to a test copy from the provider B vault;
  - a TLS scan of 70 endpoints;
  - legacy account lists and 15 departures at 3 acquired clinics;
  - a sample of 200 recorded card payment calls.

## 4. Rules of engagement
- No testing that could affect live dispatch, patient care, or client agencies. Router checks were done on vehicles out of service; the legacy account test used a test port agreed with the SOC.
- No PHI or card data left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. **One was found:** on 2026-08-19 the exposure scan showed 41 vehicle routers with remote web administration open on the cellular interface and the factory default password. The Group CISO was told the same day, and the fleet technology team closed the exposure on all 41 by 2026-08-21. This finding went back into the risk register as AMB-002 (High).

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 112 | 21 | 133 |
| DPCP (P02 system) | 39 | 16 | 55 |
| Division sample: Ambulance Services | 14 | 6 | 20 |
| Division sample: Urgent Care | 40 | 6 | 46 |
| Division sample: BDS | 11 | 6 | 17 |
| **Total** | **216** | **55** | **271** |

**Common controls are strong for federated users and cloud workloads.** 112 of 133 common statements were satisfied. MFA for administrators (IA-2(1)), inactive account disabling (AC-2(3)), terminations (PS-4), training (AT-2), backups (CP-9), and encryption (SC-8, SC-28) had no findings. The common findings sit where systems escape group identity and the landing zone: **CAD vendor and vehicle accounts** (AC-2, AC-6(5), IA-2, IA-5), **the legacy account** (SC-7, CM-6, SI-4), **unscanned field and center devices** (RA-5), and **multi-party incident notification** (IR-3, IR-4, IR-6, IR-8), which is scenario gap 7.

**The DPCP is where the risk is.** AC-4 and all 4 CP-7 statements were other than satisfied: there is no alternate site for the CAD, and the CAD shares a flat subnet with billing servers. CP-2, CP-4, and CP-10 show the contingency plan stops at a few hours inside provider A (gap 1).

**Division samples:**
- *Ambulance Services:* no router or MDC configuration baseline (CM-2), shared tunnel key (IA-3), late console patches and an older MDC operating system (SI-2), and MDCs outside device management (AC-19).
- *Urgent Care:* the acquired clinics' legacy system is not reviewed (AU-6) and uses shared logins removed late (AC-2); the supplement has not been reviewed since 2024 (PL-1).
- *BDS:* card numbers in 9 of 200 payment recordings (SC-28), AI processing of client callers without client terms and no vendor PCI attestation (SA-9), and an unclear rule for the county premise notes (AC-21, CA-3).

**Controls fully other than satisfied** (every statement failed): AC-6(5) and IR-3 (common), AC-4 and CP-7 (DPCP), IA-3 (Ambulance Services), and SC-28 (BDS). All except CP-7 have only one determination statement.

32 of the 39 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **20 items**: 15 from this assessment alone and 5 that also trace to the P03 gap analyses (POAM-015 to POAM-019). By risk: 8 High (POAM-003 vendor access, POAM-010 vehicle routers, POAM-011 contingency plan, POAM-012 legacy account, POAM-013 CAD standby, POAM-016 acquired clinics, POAM-017 AI triage for client callers, POAM-018 card data) and 12 Moderate. Status: 17 In progress, 3 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (271 rows, with an `assessment_scope` column), `poam.csv` (20 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-16. Division presidents accepted their division findings the same week.

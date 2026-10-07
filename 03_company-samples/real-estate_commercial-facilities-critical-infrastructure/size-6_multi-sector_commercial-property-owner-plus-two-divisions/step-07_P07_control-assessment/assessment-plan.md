# Security Assessment Plan and Summary: Cris Santos Company Holdings | Commercial Facilities | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the BAACS (P02 SSP system), and samples of Commercial Property, Construction, and Hotels controls |
| Tier / Vertical | Multi-Sector / Commercial Facilities (focus division: Commercial Property) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. An OT specialist from the group's assessment firm supported site testing under internal audit's direction. Division security and compliance leads and the Group OT security lead acted as liaisons only |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also supports | CISA CPG 2.0 goal 2.C (independent validation); evidence for the Hotels Report on Compliance and the Construction CMMC reassessments (not a substitute for either) |

## 1. Approach: assess common controls once, then sample the BAACS and the divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three, including BTI technicians).
2. **The BAACS** was assessed on its system-specific and hybrid controls because it is the SSP system and carries the top group risks (GR-01 to GR-03). Site testing covered 12 properties and 6 hotels.
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Construction was sampled on supplier and federal-data controls (SA-9, AC-20) because the BTI unit services the BAACS (scenario gap 4) and because CUI handling is a binding contract duty.

## 2. Controls selected
**34 control assessments** (30 distinct controls; AC-2 and SC-7 were assessed in two scopes, SA-9 in three), **258 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, IA-2(1), AC-6(5), IA-5 | 38 | Every division's access; BTI technician identities; OT credentials (GR-02) | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR) | PS-4, AT-2 | 15 | Terminations and badge revocation; training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-4, IR-6, IR-8, AU-6 | 47 | GR-04, GR-09; scenario gaps 2 and 7 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, CM-6, SC-7 | 18 | Immutable backups, guardrails, hub boundary | Focused / Focused |
| BAACS (SSP system) | AC-17, MA-4, SC-7, CM-8, CP-10, AU-12, RA-5, CM-7 | 44 | GR-01, GR-03 (High); scenario gaps 1 to 3 | Comprehensive / Focused (12 properties, 6 hotels) |
| Division sample: Commercial Property | PE-2, SI-12, CP-2, SA-9 | 40 | CF-006, CF-008, CF-009, CF-016; P03 goals 3.D, 6.A | Focused / Focused |
| Division sample: Construction | AC-2, AC-20, SR-5, SA-9 | 38 | CN-001, CN-002, CN-012 (High and Moderate); P03 CN-G-001, CN-G-024 | Focused / Focused |
| Division sample: Hotels | CA-8, AC-3, SI-2, SA-9 | 18 | HO-001, HO-002 (High); P03 HO-G-003, HO-G-012 | Focused / Focused (6 hotels, 3 of the 14 acquired) |
| **Total** | **34** | **258** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, the group vault inventory, SIEM data sources and rules, landing-zone guardrails, backup and immutability settings, the OT asset inventory, site supervisor and firewall configurations, the BAACS contingency plan and site procedures, the intercompany services agreement, vendor files, retention settings, PCI segmentation and penetration test reports.
- **Interview:** group identity, SOC, cloud, and building technology directors; the Group OT security lead; 6 regional chief engineers and 6 hotel engineers; the BTI unit general manager and regional leads; the Commercial Property director of security operations; the Construction director of federal contracts compliance; the Hotels payment security lead; the Group General Counsel.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations with badge revocation;
  - credential tests on OT devices at 12 properties and 6 hotels (default passwords);
  - a survey of remote tools on all 311 site supervisors, and a test session through a legacy tool at a non-production test site;
  - reachability tests from building IT networks to OT devices at the sampled sites;
  - a simulated outbound relay connection from a test site supervisor, to test SOC detection;
  - a restore of one site supervisor from the group vault, and of the central supervisor;
  - an external exposure scan (2026-08-04) and a CUI discovery scan of SYS-D3, SYS-D5, and the estimating assistant workspace (2026-07-29);
  - a card display test in the legacy PMS at 3 hotels.

## 4. Rules of engagement
- **No testing that could affect building operations or guests.** No writes to live BAS points or door schedules. Reachability tests used read-only discovery during low-occupancy hours, with the chief engineer present and the RBOC watching. The legacy tool test ran on a test site supervisor, not a building.
- No card data, CUI, or badge holder data left group systems. Screenshots were redacted. The CUI found in SYS-D5 was reported to the Construction director of federal contracts compliance the same day and not copied.
- The assessor would stop and notify the Group CISO on any critical exposure. One was found: the 3 internet-exposed video recorders, reported on 2026-08-04 and closed on 2026-09-04 (POAM-012).

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 104 | 14 | 118 |
| BAACS (SSP system) | 25 | 19 | 44 |
| Division sample: Commercial Property | 32 | 8 | 40 |
| Division sample: Construction | 30 | 8 | 38 |
| Division sample: Hotels | 12 | 6 | 18 |
| **Total** | **203** | **55** | **258** |

**Common controls are strong.** 104 of 118 common statements were satisfied. Phishing-resistant MFA for administrators (IA-2(1)), PAM (AC-6(5)), terminations and badge revocation (PS-4), training (AT-2), log review (AU-6), immutable backups (CP-9), and the hub boundary (SC-7) had no findings. The common findings are about **people and credentials that sit at the edge of the group**: BTI technician identities (AC-2), OT device credentials (IA-5), OT monitoring coverage (SI-4), and cross-division incident handling and notification (IR-4, IR-6, IR-8). CM-6 had one finding: the legacy Construction account that hosts SYS-D5 was never recorded as a guardrail deviation.

**The BAACS is where the risk is.** 19 of 44 statements were other than satisfied:
- **Remote access** (AC-17, MA-4): legacy vendor tools at 47 sites with a shared account, no MFA, no approval, and no records.
- **Segmentation** (SC-7): at 8 of 12 sampled properties and 5 of 6 sampled hotels, a building IT device could reach site supervisors and door controllers.
- **Recovery** (CP-10): the test site could not be restored from the group vault because its programs exist only in the BTI repository.
- **Visibility** (CM-8, AU-12, RA-5): inventory gaps, site logging off, unsupported supervisors.
- **Exposure** (CM-7): management interfaces reachable from building IT, and 3 recorders reachable from the internet.

**Division samples:**
- *Commercial Property:* 9,400 stale tenant badges (PE-2), visitor ID scans kept indefinitely (SI-12), manual procedures at 7 of 12 sampled properties (CP-2), and a shared guard contractor login plus unreviewed analytics and optimization vendors (SA-9).
- *Construction:* CUI-marked drawings for 2 DoD client facilities in the BTI repository and FCI in the estimating assistant (AC-20), BTI tools outside group requirements under an agreement with no security terms (SA-9), 14 covered cameras at 2 acquired office properties (SR-5), and about 5,200 stale external project users (AC-2).
- *Hotels:* full card numbers shown to every front desk user in the legacy PMS (AC-3), segmentation failures not retested (CA-8), an unsupported legacy PMS (SI-2), and vendor remote access outside group PAM (SA-9).

**Controls fully other than satisfied** (every statement failed): CP-10 (BAACS, 2 statements), CA-8 and AC-3 (Hotels, 1 statement each).

27 of the 34 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **29 items**: 25 from this assessment and 4 from the P03 gap analyses (POAM-026 to POAM-029). By risk: 7 High (POAM-006 legacy remote tools, POAM-007 segmentation, POAM-009 recovery at scale, POAM-017 CUI outside the enclave, POAM-018 BTI tools and agreement, POAM-020 hotel segmentation testing, POAM-021 legacy PMS card display) and 22 Moderate. Status: 23 In progress, 6 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (258 rows, with an `assessment_scope` column), `poam.csv` (29 items), and this plan and summary. Results were presented to the board audit committee and the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-15. Division presidents accepted their division findings the same week.

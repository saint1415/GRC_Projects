# Security Assessment Plan and Summary: Cris Santos Company Holdings | Arts, Entertainment, and Recreation | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the TVOP (P02 SSP system), and samples of Live Venues, Hotels and Restaurants, and Ticketing and Streaming controls |
| Tier / Vertical | Multi-Sector / Arts, Entertainment, and Recreation (focus division: Live Venues) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only. The QSA's ROC work is separate and was used only as supporting evidence |
| Assessment window | 2026-07-01 to 2026-08-31 |
| Also supports | PCI DSS v4.0.1 Requirement 12.4 (compliance management) and the evidence for the 2026 Live Venues ROC and the hotels SAQ D (N71-R04, N72-R01); the assessment program the CCPA cybersecurity audit will build on (N51-R03) |

## 1. Approach: assess common controls once, then sample
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three).
2. **The TVOP's** system-specific controls were assessed because it is the SSP system and carries the top group risk (GR-01).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

Hotels and Restaurants was sampled most heavily (PL-1, CA-2, AC-2, SC-7) because its inheritance is undocumented (scenario gap 6), its standards have drifted (gap 7), and its SAQ D is due 2026-12-31.

## 2. Controls selected
**39 control assessments** (35 distinct controls; SC-7 was assessed in three scopes, and AC-2 and CP-4 in two), **275 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2, IA-2(1), IA-5 | 44 | Every division's access control; GR-07 | Focused / Comprehensive (all divisions sampled) |
| Common control (Group HR) | PS-4, AT-2 | 15 | Terminations and training for 45,000 users | Focused / Focused |
| Common control (SYS-G2 SOC) | SI-4, IR-3, IR-4, IR-6, IR-8, RA-5 | 54 | GR-02, GR-03, GR-12; scenario gap 5 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-8, SC-12, SC-28, CM-6 | 22 | GR-02; CDE account; keys and backups | Focused / Focused |
| TVOP | CM-8, SI-7, SC-18, CM-3, AC-22, SA-9, AU-6, PT-3 | 49 | GR-01 and GR-10 (High); scenario gaps 1 and 3 | Comprehensive / Comprehensive |
| Division sample: Live Venues | CP-4, SC-7 (acquired theaters), AC-17, SR-10 | 16 | LV-002 (High), LV-012; gap 2 | Focused / Focused (3 of 8 theaters; 4 integrated venues) |
| Division sample: Hotels and Restaurants | PL-1, CA-2, AC-2 (PMS), SC-7 (front desks) | 60 | Gaps 6 and 7; HO-001 (High), HO-004 | Focused / Focused (4 of 16 hotels) |
| Division sample: Ticketing and Streaming | SA-11, AC-6, CP-4 (TVOP failover) | 15 | TS-003, TS-007, TS-011; GR-04 | Focused / Focused |
| **Total** | **39** | **275** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, SIEM data sources and rules, landing-zone and CDE account policies, backup and key settings, the TVOP content security policy, script inventory, tag manager settings, data catalog and feed register, contingency test records, division standards, PMS user exports, and vendor files.
- **Interview:** group identity, SOC, and cloud platform directors; the General Manager Ticketing and Chief Technology Officer; the Group PCI program director; division security and compliance leads; the Group Chief Privacy Officer; the Group General Counsel; hotel general managers at 4 hotels.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, and 25 terminations;
  - a hardware-key administrator sign-in and federation checks on 52 applications;
  - a **test tag added to a test tenant's checkout page** (with SOC approval) to check whether inventory, tamper detection, and SOC alerting would catch it;
  - a checkout scan of every tenant's payment pages on 2026-07-21;
  - restores of 2 TVOP databases from the immutable vault;
  - a TLS scan of 70 endpoints and an external exposure scan;
  - offline scanner tests at 2 venues and network walks at 3 acquired theaters and 4 hotels;
  - a sample of 30 support impersonation sessions.

## 4. Rules of engagement
- No testing during on-sales or within 6 hours of doors at any venue. The checkout test used a test tenant with no real patrons and a harmless tag.
- No card data or patron data left group systems. Screenshots were redacted.
- The assessor would stop and notify the Group CISO on any critical exposure. One was reported: open management ports on consumer routers at 3 acquired theaters (2026-07-14), closed within 48 hours as an interim fix and tracked in POAM-018.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common control (SYS-G1) | 38 | 6 | 44 |
| Common control (Group HR) | 15 | 0 | 15 |
| Common control (SYS-G2) | 46 | 8 | 54 |
| Common control (SYS-G3) | 22 | 0 | 22 |
| **Common controls subtotal** | **121** | **14** | **135** |
| TVOP | 30 | 19 | 49 |
| Division sample: Live Venues | 10 | 6 | 16 |
| Division sample: Hotels and Restaurants | 49 | 11 | 60 |
| Division sample: Ticketing and Streaming | 12 | 3 | 15 |
| **Total** | **222** | **53** | **275** |

**Common controls are strong.** 121 of 135 common statements were satisfied. MFA (IA-2, IA-2(1)), PAM (AC-6(5)), terminations (PS-4), training (AT-2), vulnerability management (RA-5), and every cloud control (CP-9, SC-7, SC-8, SC-12, SC-28, CM-6) had no findings. The common findings are **seasonal accounts** (AC-2, AC-2(3)), **static integration keys** (IA-5), **monitoring coverage** (SI-4), and **incident response across divisions and clients** (IR-3, IR-4, IR-6, IR-8), which is scenario gap 5.

**The TVOP is where the risk is.** 19 of 49 statements were other than satisfied. The test tag on the test tenant's checkout page was **not inventoried, not detected by tamper detection, and not seen by the SOC** (CM-8, SC-18, SI-7, SI-4). Tenant tag changes are not change-controlled or reviewed (CM-3, AC-22, AU-6), the vendors whose code runs on checkout were never assessed (SA-9), and the training feed exceeds client agreements (PT-3).

**Division samples:**
- *Live Venues:* the acquired theaters' flat networks and consumer routers (SC-7, High), offline scanner tests at only 4 of 30 venues (CP-4), and persistent integrator tunnels (AC-17). P2PE device inspections at integrated venues (SR-10) were satisfied.
- *Hotels and Restaurants:* standards that conflict with group policy (PL-1, gap 7), inheritance never documented (CA-2, gap 6), PMS local accounts with stale, shared, and over-privileged access (AC-2), and front desk terminals on flat networks (SC-7).
- *Ticketing and Streaming:* pricing and bot module releases not tested for accessibility or accessible seating price rules (SA-11), and a standing support impersonation role (AC-6). TVOP failover tests (CP-4) were satisfied.

**Controls fully other than satisfied** (every statement failed): IR-3 (common) and AC-6 (Ticketing and Streaming). Each has only one determination statement.

25 of the 39 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **26 items**: 20 from this assessment and 6 from the P03 gap analyses and P10 (POAM-010 and POAM-022 to POAM-026). By risk: 5 High (POAM-006 payment page script inventory, POAM-007 tamper detection, POAM-018 acquired theaters, POAM-022 AI pricing and accessible seating, POAM-023 price displays), 20 Moderate, and 1 Low. Status: 16 In progress, 10 Open. Each item names the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (275 rows, with an `assessment_scope` column), `poam.csv` (26 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-15. Division presidents accepted their division findings the same week.

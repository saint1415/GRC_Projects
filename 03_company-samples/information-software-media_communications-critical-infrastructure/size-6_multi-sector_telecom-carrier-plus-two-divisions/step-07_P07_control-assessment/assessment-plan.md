# Security Assessment Plan and Summary: Cris Santos Company Holdings | Communications | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR and procurement), the OSS/BSS (P02 SSP system, including the shared service assurance platform), and samples of Telecom Carrier, Network Engineering Services, and Tower and Fiber Infrastructure controls |
| Tier / Vertical | Multi-Sector / Communications (focus division: Telecom Carrier) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads acted as liaisons only. Network element tests were run by internal audit's technical specialists with NOC supervision |
| Assessment window | 2026-07-06 to 2026-08-28 |
| Also supports | The CPNI "reasonable measures" duty (47 CFR 64.2010(a)); the evidence pack for the CPNI certifications due 2027-03-01 (POL-01 4.13); the Reg S-K Item 106 description of the program |

## 1. Approach: assess common controls once, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** in the P02 common control catalog were assessed **once**, across all divisions, with samples drawn from every division (for example, the joiner-mover-leaver sample took events from all three divisions and both outsourced contact center vendors).
2. **The OSS/BSS's** system-specific controls were assessed because it is the SSP system, it holds the largest CPNI stores, and its service assurance platform is shared by all three divisions (P01 GR-02).
3. **Division samples** covered controls each division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

The Tower division was sampled on governance controls (PL-1, CA-2) because its inheritance is undocumented (scenario gap 9) and its standards have drifted, and on its device fleet (CM-8, IA-5, CP-2) because lighting alarms are a safety function (gap 6).

## 2. Controls selected
**41 control assessments** (38 distinct controls; IA-5 was assessed in three scopes and CP-9 in two), **297 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2(1), IA-5, PS-4 | 47 | Every division's access control; GR-08, GR-12 | Focused / Comprehensive (all divisions and both vendors sampled) |
| Common control (SYS-G2 SOC) | SI-4, AU-6, IR-4, IR-6, IR-8, RA-5 | 56 | GR-01, GR-04, GR-09; scenario gaps 3 and 8 | Focused / Comprehensive |
| Common control (SYS-G3 cloud) | CP-9, SC-7, SC-28, CM-6 | 19 | GR-03; immutable backups and guardrails | Focused / Focused |
| Common control (group functions) | AT-2, SR-3 | 14 | Awareness for 47,000 users; GR-07 (gap 10) | Focused / Focused |
| OSS/BSS (P02 SSP system) | AC-3, AC-6, AC-21, IA-2, IA-8, SI-2, CP-4, AU-12, PT-3 | 31 | GR-01, GR-02 (High); scenario gaps 1 to 4 | Comprehensive / Comprehensive |
| Division sample: Telecom Carrier | AT-3, SA-9, CP-9, PL-2 | 33 | TC-007, TC-008, TC-012, TC-014; CPNI training; CALEA SSI policies | Focused / Focused (both acquired regions; 12 PL-2 statements applied to the SSI policies) |
| Division sample: Network Engineering Services | AC-17, IA-5, CA-3, MP-6, PE-8 | 29 | NE-001, NE-002 (gap 7); FAR 52.204-21(b)(1)(vii), (ix) | Focused / Focused (6 project offices) |
| Division sample: Tower and Fiber Infrastructure | CM-8, IA-5, CP-2, PL-1, CA-2 | 68 | TF-001, TF-002, TF-006; gaps 6 and 9 | Focused / Comprehensive (300 RMUs credential-tested; 120 sites field-checked) |
| **Total** | **41** | **297** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, SIEM sources and rules, landing-zone policies, backup and immutability settings, the service assurance tenant configuration, AAA configuration, contingency plans, CALEA SSI policies and FCC filing history, vendor contracts, intercompany agreements and the campaign register, project office disposal and visitor records, the RMU inventory, and Tower standards.
- **Interview:** group identity, SOC, cloud, and procurement directors; the Carrier OSS/BSS platform vice president, NOC director, CPNI compliance officer, and CALEA senior officer; the Engineering MNO general manager and federal contracts compliance manager; the Tower site operations director and Alarm Monitoring Center supervisors.
- **Test:**
  - a joiner-mover-leaver sample of 75 events, and 25 employee terminations;
  - a hardware-key administrator sign-in and login tests on 12 network elements;
  - test queries under 8 operator roles on the service assurance platform (including Engineering and Tower roles);
  - a simulated management plane login from an unapproved host (with SOC and NOC approval) to test detection;
  - restores of 3 OSS and BSS datasets and 5 network element configurations;
  - a test read of a CDR object to check audit logging;
  - credential tests on 300 sampled legacy RMUs (2026-08-19), with the Alarm Monitoring Center watching for any lighting effect;
  - portal, app, chatbot, and legacy billing portal authentication tests;
  - route tests from the SYS-E1 aggregation account toward the Carrier management plane.

## 4. Rules of engagement
- No testing that could affect calling, 911, broadband, customer networks, or tower lighting. Network element and RMU tests ran in maintenance windows with the NOC and the Alarm Monitoring Center on the bridge.
- No CPNI, intercept information, or FCI left group systems. Screenshots were redacted. Lawful-intercept systems were examined by document review and interview only.
- The assessor would stop and notify the Group CISO on any critical exposure. **One was found:** the RMU default password on 2026-08-19. Internal audit notified the Group CISO and the Tower site operations director the same day; passwords on all 212 units were changed by 2026-09-30 (POAM-022), and the finding went back into P01 as TF-014.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 118 | 18 | 136 |
| OSS/BSS (P02 SSP system) | 17 | 14 | 31 |
| Division sample: Telecom Carrier | 24 | 9 | 33 |
| Division sample: Network Engineering Services | 20 | 9 | 29 |
| Division sample: Tower and Fiber Infrastructure | 54 | 14 | 68 |
| **Total** | **233** | **64** | **297** |

**Common controls are strong.** 118 of 136 common statements were satisfied. Identity for IT systems (AC-2(3), AC-6(5), IA-2(1), PS-4), cloud protection (CP-9, SC-28, CM-6), and awareness (AT-2) had no findings. The common findings are about **outsourced agent leavers** (AC-2), **integration secrets** (IA-5), **coverage of non-IT device fleets** (SI-4, AU-6, RA-5), **cross-division incident coordination and notification** (IR-4, IR-6, IR-8; scenario gap 8), **one hub route** that lets Engineering reach the Carrier management plane (SC-7), and **supply chain screening** (SR-3; gap 10).

**The OSS/BSS is where the risk is.** AC-3, AC-6, AC-21, and IA-8 were fully other than satisfied. Test queries under the Engineering and Tower operator roles returned Carrier tickets with customer names, addresses, and call detail (gap 2). Shared accounts in the acquired regions (IA-2), unsupported SBCs (SI-2), the untested three-tenant failover (CP-4), missing CDR read logging (AU-12), and undocumented CPNI purposes (PT-3) complete the picture.

**Division samples:**
- *Telecom Carrier:* CPNI training gaps for outsourced agents and affiliates (AT-3), a vendor contract without incident notice terms (SA-9), single-server configuration backups in the acquired regions (CP-9), and stale CALEA SSI policies for 2 operating companies (PL-2, gap 5).
- *Network Engineering Services:* persistent tunnels the Carrier never authorized (AC-17, gap 7), shared gateway passwords (IA-5), no interconnection or tenant agreements (CA-3), and two project offices missing disposal and visitor records for FCI (MP-6, PE-8).
- *Tower and Fiber Infrastructure:* the RMU default password (IA-5), an inaccurate RMU inventory (CM-8), no lighting fallback in the contingency plan (CP-2, gap 6), drifted standards (PL-1, gap 9), and undocumented inheritance (CA-2).

**Controls fully other than satisfied** (every statement failed): AC-3, AC-6, AC-21, and IA-8, all in the OSS/BSS scope. AC-3, AC-6, and IA-8 have one determination statement each; AC-21 has two.

33 of the 41 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **30 items**: 27 from this assessment and 3 from the P03 gap analysis (POAM-028 to POAM-030). By risk: 10 High (POAM-003, POAM-006, POAM-008 to POAM-012, POAM-019, POAM-022, POAM-024) and 20 Moderate. Status: 25 In progress, 5 Open. Each item names its scope and the related P01 risks.

## 7. Deliverables and acceptance
`assessment-results.csv` (297 rows, with an `assessment_scope` column), `poam.csv` (30 items), and this plan and summary. Results were presented to the board risk committee and accepted by the Group CISO and the Group Chief Risk Officer on 2026-09-17. Division presidents accepted their division findings the same week.

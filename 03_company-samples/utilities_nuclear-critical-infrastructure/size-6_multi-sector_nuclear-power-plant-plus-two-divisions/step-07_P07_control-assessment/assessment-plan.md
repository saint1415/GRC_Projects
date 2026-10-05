# Security Assessment Plan and Summary: Cris Santos Company Holdings | Nuclear Reactors, Materials, and Waste | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Scope | Group common controls (SYS-G1, SYS-G2, SYS-G3, group HR), the Plant Business Network and Work Management System (PBN-WMS, the P02 system), and samples of Engineering and Radiation Services and Radioactive Waste Management controls |
| Tier / Vertical | Multi-Sector / Nuclear Reactors, Materials, and Waste (focus division: Nuclear Generation) |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor and independence | Group internal audit, which reports to the board audit committee and neither designs nor operates the controls. Division security and compliance leads and station IT managers acted as liaisons only |
| Assessment window | 2026-06-29 to 2026-08-28 (station fieldwork: Station A 2026-07-13 to 2026-07-17; Station B 2026-08-03 to 2026-08-07) |
| Not in scope | CDAs, the security network, the PMMD kiosks themselves, and SGI stand-alone systems (reviewed under 73.55(m) by Nuclear Oversight and inspected by the NRC); the NERC CIP environment (audited by the Regional Entity) |

## 1. Approach: assess common controls once, then the PBN-WMS, then sample divisions
Most safeguards in all three divisions come from the same corporate providers. Testing them three times would waste effort and produce three slightly different answers. So:
1. **Common controls** marked "assessed once" in the P02 common control catalog (21 controls) were assessed **once**, across all divisions, with samples drawn from every division. For example, the joiner-mover-leaver sample took events from all three divisions and included 40 cross-division outage accounts.
2. **The PBN-WMS** system-specific and hybrid controls were assessed because it is the SSP system, it is where staff and devices from all three divisions meet, and it is the network an attacker must cross to reach the CDAs (P01 GR-01, GR-02, GR-04).
3. **Division samples** covered controls each service division operates itself, chosen from its High risks and its P03 gaps. Division findings are reported to that division, not averaged into the group.

**The assessment stopped at the one-way devices.** Assessors did not connect to, scan, or test anything inside a CSP boundary. At the kiosk update server the test was a walkthrough of one release with the Station A CST, observed from the business side.

## 2. Controls selected
**42 control assessments** (36 distinct controls; AC-3, AU-6, IA-5, and SC-7 were assessed in more than one scope), **246 determination statements**.

| Scope | Controls | Statements | Why selected | Depth / coverage |
|---|---|---|---|---|
| Common control (SYS-G1 identity) | AC-2, AC-2(3), AC-6(5), IA-2(1), IA-2(2), IA-5 | 43 | Every division's access to station systems; GR-01; scenario gap 1 | Comprehensive / Comprehensive (all divisions sampled) |
| Common control (Group HR with SYS-G1) | PS-4, PS-5, AT-2 | 19 | Terminations, cross-division reassignments, training for 45,000 users | Focused / Comprehensive |
| Common control (SYS-G2 SOC) | SI-4, AU-6, IR-3, IR-4, IR-6, IR-8, RA-5 | 57 | GR-03, GR-05; scenario gap 8 | Focused / Comprehensive |
| Common control (SYS-G3 cloud and network) | CP-9, SC-7, SC-8, SC-28, CM-6 | 20 | GR-03; immutable backups and guardrails | Focused / Focused |
| PBN-WMS (P02 system) | AC-3, MP-3, AC-21, IA-3, CM-8, SI-7, SC-7, IA-5, CP-4, SA-22 | 41 | GR-01, GR-02, GR-04 (High); scenario gaps 1 to 3 | Comprehensive / Focused (Stations A and B; Station C by document review) |
| Division sample: Engineering and Radiation Services | AC-3, AU-6, IA-8, PS-3, MP-6, SA-9 | 18 | ER-003, ER-004 (High), ER-006, ER-012; scenario gaps 4 to 6 | Focused / Focused (2 of 4 SGI offices) |
| Division sample: Radioactive Waste Management | CA-2, PL-1, AC-17, SC-7, IA-5 | 48 | WM-001, WM-003 (High), WM-007, WM-011, WM-012; scenario gaps 7 and 9 | Focused / Focused (both facilities) |
| **Total** | **42** | **246** | | |

## 3. Methods and objects
- **Examine:** identity governance and PAM configuration, the outage schedule and intercompany service agreements, SIEM data sources and rules, landing-zone policies and backup settings, WMS role matrix and attachment metadata, station firewall and network access control configurations, kiosk update server configuration and vendor documentation, contingency plans and test records, division supplements, the Florida facility network diagram, and the group incident response plan and notification matrix.
- **Interview:** group identity, SOC, and cloud platform directors; the fleet IT director and station IT managers; the work management director; the fleet cyber security program manager and the Station A CST lead; the fleet security director; the SGI program manager; the contractor/vendor access authorization program manager; the dosimetry laboratory director; the Florida facility Radiation Safety Officer and the Radioactive Waste Management OT lead.
- **Test:**
  - a joiner-mover-leaver sample of 60 events across divisions, 25 terminations, and 40 cross-division outage accounts traced against assignment end dates;
  - WMS test queries under 5 user roles to check who can open CDA work packages;
  - a simulated bulk export of 2,000 CDA work packages from the WMS test copy (with SOC approval) to test detection;
  - connection of a division-managed laptop to the Station A business network (contractor port, coordinated with station IT);
  - a credential scan of 310 station multifunction printers and 140 servers, and of OT devices at both waste facilities;
  - a read test of engineering project shares with a project engineer account;
  - a sign-in test as a dosimetry customer administrator (test tenant);
  - restores of the WMS database and one division share from the immutable vault;
  - a TLS scan of 60 endpoints and an external exposure scan of the landing zones.

## 4. Rules of engagement
- No testing inside a CSP boundary, on the security network, on the NERC CIP environment, or on processing PLCs. No active scanning of the Florida vault security systems; their network placement was confirmed from configuration and diagrams.
- No test during a refueling outage window or a planned plant transient. Station tests were coordinated with the shift manager and the CST.
- No SGI, CSP information, or access authorization data left the systems that hold them. Screenshots were redacted; evidence that would itself be SGI (printer use logs in the security buildings) was reviewed in place with the fleet security director.
- The assessor would stop and notify the Group CISO and, for anything touching a CSP control, the fleet cyber security program manager. **One stop was called:** on 2026-08-05 the printer finding was reported the same day to the fleet security director, who entered it in the station CAP within 24 hours (73.77(b)(1)) and changed the passwords by 2026-09-04.

## 5. Results summary
| Scope | Satisfied | Other than satisfied | Total |
|---|---|---|---|
| Common controls | 124 | 15 | 139 |
| PBN-WMS | 28 | 13 | 41 |
| Division sample: Engineering and Radiation Services | 14 | 4 | 18 |
| Division sample: Radioactive Waste Management | 37 | 11 | 48 |
| **Total** | **203** | **43** | **246** |

**Common controls are strong.** 124 of 139 common statements were satisfied. MFA and privileged access (IA-2(1), IA-2(2), AC-6(5)), authenticator management (IA-5), cloud protection (CP-9, SC-7, SC-8, SC-28, CM-6), terminations (PS-4), training (AT-2), and vulnerability management (RA-5) had no findings. The common findings sit in two places:
- **Identity lifecycle for people who cross divisions** (AC-2, AC-2(3), PS-5; 7 statements): accounts have no expiry, are not disabled at assignment end, and are not reviewed on reassignment (scenario gap 1).
- **Detection and notification across divisions** (SI-4, AU-6, IR-3, IR-4, IR-6, IR-8; 8 statements): no detection of bulk reads of CDA information, no joint SOC and CST test, and a notification matrix that misses the 73.77(a)(2)(iii) trigger, CIP-008, Part 37, and contract clocks (scenario gap 8).

**The PBN-WMS is where the risk is.** 13 of 41 statements were other than satisfied:
- AC-3 and IA-3 failed outright: all 5 test roles opened CDA work packages, and a division laptop joined the Station A network with no device check.
- SI-7 (3 of 6) and SC-7 (1 of 6): the kiosk update path is unverified and sits on a flat server subnet.
- **IA-5 (1 of 10): 6 printers in the Station A and B security buildings had manufacturer default admin passwords and had been used to copy SGI.** This finding was not in the 2026 risk analysis. It became P01 NG-024 (High) and P03 G-043 (73.22(e), Not met).

**Division samples:**
- *Engineering and Radiation Services:* access authorization files readable by project teams and never reviewed (AC-3, AU-6), password-only customer administrators (IA-8), and an unsanitized scanner that copied SGI (MP-6). Screening (PS-3) and the background investigation vendor (SA-9) passed.
- *Radioactive Waste Management:* no inheritance documentation (CA-2), a 2024 supplement in conflict with group policy (PL-1), a shared vendor account for PLC remote access (AC-17), vault security systems on the business network (SC-7), and 2 HMIs on default passwords (IA-5).

**Controls fully other than satisfied** (every statement failed): IR-3 (common), AC-3 and IA-3 (PBN-WMS), and AC-3 and IA-8 (Engineering and Radiation Services). Each has only one determination statement.

28 of the 42 control assessments had at least one statement other than satisfied. All are in `poam.csv`.

## 6. POA&M
`poam.csv` has **25 items**: 20 from this assessment (POAM-001 to POAM-020) and 5 from the P03 gap analyses that this assessment did not test (POAM-021 to POAM-025). By risk: **9 High** (POAM-001, -002, -003, -004, -005, -010, -012, -018, -019) and **16 Moderate**. Status: 19 In progress, 6 Open. Each item names the related P01 risks and the P03 rows it closes.

**CSP-related items** (POAM-002, POAM-004, POAM-010, POAM-025) are also in the station CAP, which is the record of correction for the CSP. The POA&M tracks the business-side work.

## 7. Deliverables and acceptance
`assessment-results.csv` (246 rows, with an `assessment_scope` column), `poam.csv` (25 items), and this plan and summary. Results were presented to the board risk committee on 2026-09-17 and accepted by the Group CISO and the Group Chief Risk Officer. Division presidents and the Chief Nuclear Officer accepted their division findings the same week. The SSP authorization conditions (P02 section 4.2) are POAM-001 to POAM-005 and POAM-010.
